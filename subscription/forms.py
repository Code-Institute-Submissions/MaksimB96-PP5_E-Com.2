from django import forms
from .models import Subscribers, NewsLetter


class SubscribeForm(forms.ModelForm):
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
        )

    class Meta:
        model = Subscribers
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class SubscriberAdminNews(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
