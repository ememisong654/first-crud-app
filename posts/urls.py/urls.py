from django.urls import path
from .views import HomePageView

urlspattern = [
    path('',HomePageView.as_view(), name='home'),
]