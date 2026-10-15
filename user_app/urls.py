"""
URL configuration for villaproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name="index"),
   path('home',views.home,name="home"),

   path('user_register',views.user_register),
   path('login',views.login,name="login"),
   path('user_prop_view',views.user_prop_view),
   
   path('visit_date/<int:id>',views.visit_date,name="visit_date"),
   path('bookvisit/<int:id>',views.bookvisit,name="bookvisit"),
   path('user_book_view',views.user_book_view),

   path('userprofile',views.userprofile),
   path('logout',views.logout)
]
