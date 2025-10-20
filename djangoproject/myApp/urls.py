
from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_views, name='auth'),
    path('login/', views.auth_login, name='login'),

]
