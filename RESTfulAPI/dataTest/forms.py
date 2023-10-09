from django import forms
from .models import Users

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'address', 'phone_number', 'job_position', 'age', 'image']