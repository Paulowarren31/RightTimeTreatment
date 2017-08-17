# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm, ProfileForm

# Create your views here.
def index(request):
  return render(request, 'index.html')


