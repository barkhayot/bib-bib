import django_filters
from .models import Drive
from django import forms

class DriveSearchForm(django_filters.FilterSet):
    

    
    passengers = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Passengers',
        'class': 'form-control',
    }))

    class Meta:
        model = Drive
        fields = ['leaving_city', 'going_city', 'date']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(DriveSearchForm, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['leaving_city'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'e.g. Busan'})
            self.filters['going_city'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'e.g. Seoul'})
            self.filters['date'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'e.g. 2022-12-28'})


