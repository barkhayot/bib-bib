from django.forms import ModelForm
from django import forms
from .models import Account, UserProfile

# User Register Form
class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegisterUserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
            'Passwords does not match !'
        )

    def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['placeholder']='Enter the Email'
            self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
            self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
            
            
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'


# Profile Edit Form
class ProfileForm(forms.ModelForm):

    
    class Meta:
        model = UserProfile
        fields = ['age', 'about', 'experience', 'over_drive', 'address_line', 'city', 'state',
                    'country', 'music', 'talking', 'smoking', 'pets']




    def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            self.fields['age'].widget.attrs['placeholder']='e.g. 28'
            self.fields['about'].widget.attrs['placeholder']='e.g. Software Developer from California'
            self.fields['experience'].widget.attrs['placeholder']='e.g. 7 years'
            self.fields['over_drive'].widget.attrs['placeholder']='e.g. 5'
            self.fields['address_line'].widget.attrs['placeholder']='Madison Square 223'
            self.fields['city'].widget.attrs['placeholder']='e.g. Queens'
            self.fields['state'].widget.attrs['placeholder']='e.g. New York'
            self.fields['country'].widget.attrs['placeholder']='e.g. USA'
            self.fields['music'].widget.attrs['placeholder']='music'
            self.fields['pets'].widget.attrs['placeholder']='pets'
            self.fields['smoking'].widget.attrs['placeholder']='pets'
            self.fields['talking'].widget.attrs['placeholder']='pets'


            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control' 



                   