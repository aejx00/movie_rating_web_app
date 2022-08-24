from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User
from django.db import models
from django import forms


class UserCreateForm(UserCreationForm):
    email = models.EmailField()
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                                      {'class': 'form-control'})
    
    
    def username_clean(self):  
            username = self.cleaned_data['username'].lower()  
            new = User.objects.filter(username = username)  
            if new.count():  
                raise ValidationError("User Already Exist")  
            return username  
  

    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  