from django.urls import path, reverse_lazy, reverse
from .views import login_user, dashboard_view, register_new_user,edit,user_details,users_list,follow
from django.contrib.auth.views import LoginView
import django.contrib.auth.views as auth_view
from django.urls import include
app_name = 'a_ccount'

urlpatterns = [
    path('login2/',login_user,name='login'),
    path('login/', LoginView.as_view(success_url=reverse_lazy("a_ccount:dashboard_view")), name='login_view'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout_view'),
    path("", dashboard_view, name='dashboard_view'),
    # path("password-change/",PasswordChangeView.as_view(),name="password_change"),
    # path("password-change/done/",PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('password-change/',
         auth_view.PasswordChangeView.as_view(success_url=reverse_lazy('a_ccount:password_change_done')),
         name='password_change'),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/',
         auth_view.PasswordResetView.as_view(success_url=reverse_lazy('a_ccount:password_reset_done')),
         name='password_reset_form'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password-reset/<uidb64>/<token>',
         auth_view.PasswordResetConfirmView.as_view(success_url=reverse_lazy('a_ccount:password_reset_complete')),
         name='pasword_reset_confirm'),
    path('password-reset/complete/', auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('register',register_new_user,name = 'register' ),
    path('edit/',edit,name= "edit_user"),
    path('users/',users_list,name="users"),
    path('users/<username>/',user_details,name="user_details"),
    path('follow/',follow,name="follow_view"),

]
