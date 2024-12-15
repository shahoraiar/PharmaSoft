from typing import Any
from django import forms
from apps.permission.models import Role
from apps.user.models import User

class UserAddForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    user_role = forms.ModelChoiceField(queryset=Role.objects.all())
    status = forms.CharField(required=False)
    password = forms.CharField(required=False)
    confirm_password = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['user_verification'] 
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password do not match.")
            
        cleaned_data['user_verification'] = User.UserVerification.NO
        
        return cleaned_data
    
    