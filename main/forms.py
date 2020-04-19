from django import forms
from main.models import Asset,Supplier
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

class AdditionForm(forms.ModelForm):
	user=forms.ModelChoiceField(
		widget=forms.HiddenInput,
		queryset=get_user_model().objects.all(),		
		#disabled=True,	

		)
	class Meta:
		model=Asset		
		fields=['user','asset_description','tag_number','asset_cost','serial_number','category','location','supplier']
		widgets={
			'asset_description':forms.Textarea(attrs={'col':.5,'rows':1}),
			'tag_number':forms.Textarea(attrs={'col':1,'rows':1}),
			'serial_number':forms.Textarea(attrs={'col':1,'rows':1}),

		}	


class SupplierForm(forms.ModelForm):	
		
	class Meta:
		model=Supplier
		fields=['supplier_name','supplier_location','supplier_Phonenumber','supplier_email','supplier_website']

