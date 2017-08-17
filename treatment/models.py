# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

  
class Patient(models.Model):
  name = models.CharField(max_length=15)
  profile = models.ForeignKey(User, on_delete=models.CASCADE)

class Entry(models.Model):
  date = models.DateField()
  height = models.DecimalField(decimal_places=2, max_digits=5)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
