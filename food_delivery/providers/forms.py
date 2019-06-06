from django import forms
from .models import Restaurants, Delivery_partners

class ResForm(forms.ModelForm): 
	class Meta: 
		model = Restaurants 
		fields = ['res_name', 'res_image', 'contact_no','content','x','y'] 
