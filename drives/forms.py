from django.forms import ModelForm
from django import forms
from .models import Drive

class PostDriveForm(forms.ModelForm):
    class Meta:
        model = Drive
        fields = ['leaving_city', 'going_city', 'date', 'leaving_time', 'coming_time', 'passengers',
                    'price', 'car', 'contact'] 

    def __init__(self, *args, **kwargs):
            super(PostDriveForm, self).__init__(*args, **kwargs)
            self.fields['leaving_city'].widget.attrs['placeholder']='e.g. Deagu'
            self.fields['going_city'].widget.attrs['placeholder']='e.g. Busan'
            self.fields['date'].widget.attrs['placeholder']='e.g. 2023-02-24'
            self.fields['leaving_time'].widget.attrs['placeholder']='e.g. 09:30'
            self.fields['coming_time'].widget.attrs['placeholder']='e.g. 16:30'
            self.fields['passengers'].widget.attrs['placeholder']='e.g. 1 person'
            self.fields['price'].widget.attrs['placeholder']='e.g. 200 Won'
            self.fields['car'].widget.attrs['placeholder']='e.g. Hyundai Sonata'
            self.fields['contact'].widget.attrs['placeholder']='e.g. +8210 XXXX XXXX'
            
            


            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'