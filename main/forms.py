from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SimpleSignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. We will send you notifications here.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password help text and validators
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'
        self.fields['username'].help_text = None
        
        # Add Bootstrap classes
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
