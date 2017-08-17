from django.forms import ModelForm
from .models import Patient
from django.contrib.auth.models import User


class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
  class Meta:
    model = Patient
    fields = ('name',)
