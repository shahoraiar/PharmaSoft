from django import forms 
from apps.supplier.models import Supplier
from apps.user.models import User
from system.middleware.thread_local import _thread_local

class SupplierForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)
    email = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zip = forms.CharField(required=True)
    balance = forms.DecimalField(required=True)
    
    class Meta:
        model = Supplier
        fields = '__all__'
        exclude = ['status'] 
        
    def __init__(self, *args, **kwargs):
        # Extract the request object from kwargs
        self.request = kwargs.pop('request', None)
        super(SupplierForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        # Access the current user from thread-local storage
        user_instance = getattr(_thread_local, 'user', None)
        if user_instance:
            cleaned_data['admin_id'] = user_instance  # Set the User instance (not user ID)
        else:
            cleaned_data['admin_id'] = None

        return cleaned_data