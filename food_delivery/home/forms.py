from django import forms
from providers.models import Restaurants

class ResForm(forms.ModelForm): 
	class Meta: 
        model = Restaurants 
        fields = ['res_name', 'res_image', 'contact_no', 'point','content','x','y'] 

