# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Patient, Entry

admin.site.register(Patient)
admin.site.register(Entry)

# Register your models here.
