
from django import forms
from .models import GuestbookEntry


class GuestbookForm(forms.ModelForm):

    class Meta:
        model = GuestbookEntry
        fields = ['name', 'message']

        labels = {
            'name': 'Your Name',
            'message': 'Your Message',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here',
                'rows': 4
            }),
        }
