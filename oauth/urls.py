from django.urls import path
from .endpoint import auth_views, views

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('author/', views.AuthorView.as_view({'get': 'list'})),
    path('author/<int:pk>/', views.AuthorView.as_view({'get': 'retrieve'})),
    
    path('google/', auth_views.google_auth),
    path('login/google/', auth_views.google_login)
]