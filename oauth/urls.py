from django.urls import path
from .endpoint import auth_views, views

urlpatterns = [
    path('google/', auth_views.google_auth),
    path('', auth_views.google_login)
]