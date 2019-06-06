from django.contrib.auth.models import User
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
# Same App importing
from .forms import SignUpForm, ProfileForm
from .models import Profile
from providers.models import *
# Posts App importing
# from posts.models import Post
from rest_framework import generics

from .serializers import *


def sign_up(request):
    """Complex Signup View"""
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['repassword']
        user = User.objects.filter(username=username)
        if password == confirm_password:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            # If User is Authenticated, then allow Login and go to Profile Create
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile-create')

    template = 'sign_up.html'
    return render(request, template)


def sign_in(request):
    """Sign In view"""
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    queryset = Restaurants.objects.all()
    return redirect('/providers')


def profile_create(request):
    """Creating profile is Mandatory"""
    name = request.user.first_name + ' ' + request.user.last_name
    initial_data = {
        "user_name": name,
        "email": request.user.email
    }

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            # Save to Database
            profile.save()
            return redirect('/providers')

    context = {
        'form': ProfileForm(initial=initial_data),
        }

    template = 'profile_create.html'
    return render(request, template, context)

def logout_view(request):
    logout(request)

    return redirect('/providers')

def all_res(request):
	queryset = Restaurants.objects.all()
	print(queryset)

	return render(request, 'index.html', {'qs':queryset})

class ListUserView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Profile.objects.all()
    serializer_class = UserSerializer