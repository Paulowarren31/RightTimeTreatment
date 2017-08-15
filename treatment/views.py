# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request, user_id):
  return render(request, 'base.html')

