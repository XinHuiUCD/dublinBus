from re import TEMPLATE
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages




# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates"),'
)



def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")   

def twitter(request):
    return render(request,"twitter.html")   




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


