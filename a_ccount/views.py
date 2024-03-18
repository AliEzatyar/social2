from django.contrib.auth import authenticate, login, get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from action.models import Action
from action.utils import create_action
from .forms import LoginForm
from .forms import RegisterForm
from .models import Profile, Relation
from .forms import UserEditForm, ProfileEditForm
import django.contrib.messages as ms


# Create your views here.
# this was a simple view function, but is not used, instead default django's loginview()
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request, username=cleaned_data['username']
                                , password=cleaned_data['password'])  # this method returns a User
            if user is not None:
                if user.is_active:
                    login(request, user)  # VERY IMPORTANT, it creates a session of the user
                    return redirect(to="a_ccount:dashboard_view")
                else:
                    return HttpResponse('Disabled User')
            else:
                return HttpResponse('NO MATCHINGS')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', context={'form': form})


@login_required
def dashboard_view(request):
    # logged = request.user
    # taking out actions
    logged = get_user(request)
    actions = Action.objects.exclude(user_id=logged.id)
    # relations which this user created by following other users
    following_relations = Relation.objects.filter(From_id=request.user.id)
    # creating a list of user ids who are being followed by the logged user
    following_users = [rel[2] for rel in following_relations.values_list()]
    if following_users:
        actions.filter(user_id__in= following_users)
    actions = actions[:10]
    return render(request, 'account/dashboard.html', {"section": 'dashboard', 'loggedUser': logged,'actions':actions})


def register_new_user(request):
    if request.method == "POST":
        context = {}
        user_details_form = RegisterForm(request.POST)
        if user_details_form.is_valid():
            cd = user_details_form.cleaned_data
            new_user = user_details_form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            create_action(new_user, 'has created account')
            Profile.objects.create(user=new_user)
            context['user'] = new_user

            return render(request, 'account/register_done.html', context=context)
        return render(request, 'account/register.html', {'form': user_details_form})
    else:
        void_form = RegisterForm()
        return render(request, "account/register.html", context={'form': void_form})


@login_required  # this adds a user obejct to the request after the authenication of the user, so we can say request.use
# if user is previously logged in other things, again that user object is binded with request
def edit(request):
    context = {}
    if request.method == "POST":
        u_e_form = UserEditForm(instance=request.user, data=request.POST)
        # u_e_form = UserEditForm(data=request.POST)
        # if we don't give model instance of the moeldformoject as argument, the form is treated as if it is creating a
        # new instance of its related model---> for any model form it is the rule
        p_e_form = ProfileEditForm(instance=request.user.profile,
                                   data=request.POST,
                                   files=request.FILES
                                   )
        context['user_form'] = u_e_form
        context['profile_form'] = p_e_form
        if u_e_form.is_valid() and p_e_form.is_valid():
            u_e_form.save()  # saves in database and returns a ProfileObject
            p_e_form.save()  # saves in database and returns a ProfileObject
            context['changed'] = True
            context['user_form'] = u_e_form
            context['profile_form'] = p_e_form
            ms.success(request, "Profile edit was successful!")
        else:
            ms.error(request, "There was an error while modifying the profile")

    else:
        u_e_form = UserEditForm(instance=request.user)  #
        p_e_form = ProfileEditForm(instance=request.user.profile)
        context['user_form'] = u_e_form
        context['profile_form'] = p_e_form

    return render(request, 'account/edit.html', context=context)


@login_required
def users_list(request):
    user_model = get_user_model()
    users = user_model.objects.filter(is_active=True)
    return render(request, "account/users.html", {'section': 'People', 'users': users})


@login_required
def user_details(request, username):
    user = get_object_or_404(get_user_model(), username=username, is_active=True)
    return render(request, "account/user_details.html", {'section': "People", 'user': user})


@require_POST
@login_required
def follow(request):
    data = request.POST
    print("post-------------->", data)
    print(len(data['fd_user_id']), "lenth")
    fd_user_id = data['fd_user_id']
    user = request.user
    action = data['action']
    if fd_user_id and action:
        try:
            fd_user = get_object_or_404(User, id=fd_user_id)
            if action == "follow":
                r = Relation(From=user, To=fd_user)
                print("this user", fd_user, " is followed by ", user)
                r.save()
                create_action(user, 'is following', fd_user)
                return JsonResponse({"status": "ok"})
            else:
                try:
                    f = Relation.objects.get(From_id=user.id, To_id=fd_user_id).delete()
                    print("deleted relation", f)
                except:
                    pass
                return JsonResponse({"status": "ok"})
        except User.DoesNotExist:
            return JsonResponse({"status": "does_not_exist"})
    return JsonResponse({"status": "unknown error occured"})
