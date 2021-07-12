from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

from GoodData.models import Customer

class UserForm(UserCreationForm):
    
    class Meta:
        model = Customer
        fields = ['cus_ID', 'cus_PW', 'cus_name', 'cus_address', 'cus_RRN', 'cus_phone_number']
        
        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            if commit:
                user.save()
            return user