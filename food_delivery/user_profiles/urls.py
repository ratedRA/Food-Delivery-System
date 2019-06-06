from user_profiles.views import (
    sign_up,
    sign_in,
    profile_create,
    logout_view,
    all_res,
    ListUserView,
)
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView



urlpatterns = [

    path('signup/', sign_up, name='signup'),
    path('sign-in/', sign_in, name='signin'),
    path('logout/', logout_view, name='logout'),
    path('profile-create/', profile_create, name='profile-create'),
    path('', all_res, name='all-res'),
    path('all_user/', ListUserView.as_view(), name="ListUserView"),

]


