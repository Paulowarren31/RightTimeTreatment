from django.forms import ModelForm
from .models import Patient
from django.contrib.auth.models import User

class UserForm(ModelForm):
  class Meta:
    model = Patient
    fields = ['name', 'profile']
    def __init__(self, username, password, *args, **kwargs):
      print 'init'
      super(UserForm, self).__init__(*args, **kwargs)
      user = User.objects.create(username=username, password=password, email='kek@k.com')
      self.fields['profile'] = user
      print 'created user'

