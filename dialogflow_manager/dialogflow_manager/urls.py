"""dialogflow_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from dlf_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),
    path('intents/', views.intents, name='intents'),
    path('entities/', views.entities, name='entities'),
    path('test/', views.test, name='test'),
    path('intents_sync/', views.intents_sync, name='intents_sync'),
    path('entities_sync/', views.entities_sync, name='entities_sync'),
    path('accounts/', include('django.contrib.auth.urls'))
]
