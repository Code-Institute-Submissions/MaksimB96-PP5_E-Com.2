from django import form
from .models import Subscribers, NewsLetter 


class SubscribeForm(form.ModelForm):
    class Meta:
        model = Subscribers
        field = ['email',]


class SubscriberAdminNews(form.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'