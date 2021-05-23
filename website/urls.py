"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from learn import views
from learn.views import SearchResultsView
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home, name='home'),
    path('account/', include('learn.urls')),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('javascript/', views.javascript, name='javascript'),
    path('system_design/', views.system_analysis, name='system_analysis'),
    path('system_design/design', views.design, name='design'),
    path('system_design/implimentation', views.implimentation, name='implimentation'),
]
