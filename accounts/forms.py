from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


USER_CHOICES= [
    ('Customer', 'Customer'),
    ('Hotel', 'Hotel'),
   
    ]


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length = 20)
    last_name=forms.CharField(max_length = 20)
    User_type=forms.CharField(label='select your user type', widget=forms.Select(choices=USER_CHOICES),max_length = 20)
    
    


    class Meta:
        model= User
        fields =['username','email','password1','password2','first_name','last_name','User_type']
     
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Your email is not unique.')
        return email
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()


    class Meta:
        model= User
        fields =['email']

    


class ProfileUpadteForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['first_name','last_name']