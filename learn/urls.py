from django.urls import path, include
from learn import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
]