from django.urls import path
from . import views

urlpatterns = [
    path('admin_news/', views.admin_news_form, name='admin_news'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]
