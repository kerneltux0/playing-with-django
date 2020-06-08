from django import forms
from .models import Testing

class TestForm(forms.ModelForm):
    class Meta:
        model = Testing
        fields = [
            'title',
            'info',
            'coolStuff'
        ]