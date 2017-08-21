# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm
from .models import Patient
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
  if request.user.is_authenticated():
    patients = list(request.user.patient_set.all())
    print patients
    
  return render(request, 'adduser.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
      pass
        # Return an 'invalid login' error message.


def create(request):
  #if request.method == "POST":
  #  form = UserForm(request.POST)
  #  if form.is_valid():
  #    new_user = User.objects.create_user(**form.cleaned_data)
  #    login(new_user)
  #    # redirect, or however you want to get to the main view
  #    return HttpResponseRedirect('adduser.html')
  form = UserForm() 
  return render(request, 'adduser.html', {'form': form}) 

def post_new(request):
  form = UserForm()
  print form
  return render(request, 'adduser.html', {'form': form})


def test(request):
  if request.method == 'POST':
    print request.POST

    username = request.POST.get('username')
    password = request.POST.get('password')
    name = request.POST.get('name')

    user = User.objects.create_user(username=username, password=password, email='kek@k.com')
    patient = Patient.objects.create(name=name, profile_id=user.pk)
    print 'it worked?'




