from django.urls import path
from .views import user_settings


urlpatterns = [
    path('settings/', user_settings, name='user_settings'),
]