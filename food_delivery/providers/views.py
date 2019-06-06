from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import *
from user_profiles.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
import math
from rest_framework import generics

from .serializers import *
  
# Create your views here. 
def food_providers(request): 
  
	if request.method == 'POST': 
		form = ResForm(request.POST, request.FILES) 
  
		if form.is_valid(): 
			form.save() 
			return render(request, 'success.html', {'id':'successfuly uploaded'}) 
	else: 
		form = ResForm() 
	return render(request, 'index.html', {'form' : form}) 
  
  
def success(request): 
	return HttpResponse('successfuly uploaded')

def all_res(request):
	queryset = Restaurants.objects.all()
	print(queryset)

	if request.method == 'POST': 
		form = ResForm(request.POST, request.FILES) 
  
		if form.is_valid(): 
			form.save() 
			return render(request, 'success.html', {'id':'successfuly uploaded'}) 
	else: 
		form = ResForm() 

	return render(request, 'index.html', {'qs':queryset, 'form':form})


def show_navigation(request):
	print(request.user)
	query = request.GET.get('query_name')
	forxy = Restaurants.objects.get(id=query)
	delivery_pts = Delivery_partners.objects.all()
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
		
		
		
		template = 'navigate.html'
		d1 = math.sqrt((profile.x-forxy.x)**2+(profile.y-forxy.y)**2)
		min1 = 99999999999
		d2 = 0
		for i in delivery_pts:
			x = math.sqrt((i.x-forxy.x)**2+(i.x-forxy.x)**2)
			print(x, i.name)
			if x<min1:
				min1 = x
				d2 = min1
				delivery_name =i.name
		total_distance = d1+d2

		context = {
			'profile': profile,
			'restaurant':forxy,
			'd':total_distance,
			'name':delivery_name
		}

		return render(request, template, context)
	else:
		return render(request, 'sign_up.html')

class ListResView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Restaurants.objects.all()
    serializer_class = ResSerializer

class ListDelView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Delivery_partners.objects.all()
    serializer_class = DelSerializer