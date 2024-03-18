import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from action.utils import create_action
from .forms import ImageForm

# print(rf"sfs{5+4}")
# Createf your views here.
from .models import Image


@login_required
def create_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            Imagee = form.save(commit=False)
            user = request.user
            Imagee.user = user
            Imagee.save()
            create_action(request.user, 'Bookmarked an image', Imagee)
            messages.success(request, "Image saved successfully!")
            return redirect(Imagee.get_absolute_url())
    else:
        form = ImageForm(request.GET)

    return render(request, "images/image/create.html", context={
        'form': form,
        'section': 'images'

    })


@login_required
def show_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, "images/image/detail.html", {
        'section': 'images',
        'image': image
    })


@login_required
@require_POST
def like(request):
    if 'special_action' in request.POST:
        print("add user requested")
        print("Data",request.POST)
        return render(request, 'images/image/add_liked_user.html', {'user': request.user})
    else:
        image_id = request.POST.get('id')
        action = request.POST.get('action')
        if action and image_id:
            try:
                image = get_object_or_404(Image, id=image_id)
                if action == "like":
                    image.users_liked.add(request.user)
                    image.total_likes += 1
                    image.save()

                    create_action(request.user, 'Liked an image', image)
                    return JsonResponse({'status': "ok"})
                else:
                    image.users_liked.remove(request.user)
                    image.total_likes -= 1
                    image.save()
                    create_action(request.user, 'Disliked an image')
                    return JsonResponse({'status': "ok"})
            except Image.DoesNotExist:
                pass
        return JsonResponse({"status": "failed"})

@login_required
def add_images(request):
    image = Image.objects.get(id=int(request.GET['image']))
    return render(request,'images/image/add_liked_user.html',{'image':image})

@login_required
def show_images(request):  # infinit scroll pagination
    # request.is_secure()
    images = Image.objects.all()
    all_pages = Paginator(images, 8)
    requested_page_number = request.GET.get('page')
    if not requested_page_number:
        requested_page_number = 1
    images_only = request.GET.get('images_only') # if it is just about loading new images to the whole
    try:
        images = all_pages.page(requested_page_number)
    except PageNotAnInteger:
        images = all_pages.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse('')  # returns an empty page if AJAX is used
        images = all_pages.page(all_pages.num_pages)  # show the last page
    if images_only:
        return render(request, "images/image/pics_list.html", context={
            'section': "images",
            'images': images,
        })
    # print("amount pages",all_pages.num_pages)
    return render(request, "images/image/list.html", context={
        'section': "images",
        'images': images
    })
