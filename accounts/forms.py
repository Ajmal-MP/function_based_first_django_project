from django import forms
from .models import Account

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)
    
    class Meta:
        model=Account
        fields=['first_name','last_name','email','mobile','password','confirm_password']

        def clean(self):
            cleaned_data = super(UserRegisterForm,self).clean()
            password     = cleaned_data.get('password')
            confirm_password=cleaned_data.get('confirm_password')

            if password != confirm_password:
                raise forms.ValidationError("Password does not match")