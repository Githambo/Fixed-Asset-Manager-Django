from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
	form_class=UserCreationForm
	template_name='register.html'
	success_url='user:login'
