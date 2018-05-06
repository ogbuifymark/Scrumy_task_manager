from django.forms import ModelForm
from .models import ScrumyUser,Task




class AddUser(ModelForm):

    class Meta:
        model = ScrumyUser
        fields = ['user_name','email','name','role_id']


class AddTask(ModelForm):

    class Meta:
        model = Task
        fields = ['name','status']