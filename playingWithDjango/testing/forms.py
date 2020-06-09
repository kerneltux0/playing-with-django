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
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "something" in title:
            raise forms.ValidationError("Wrong question!")
        return title