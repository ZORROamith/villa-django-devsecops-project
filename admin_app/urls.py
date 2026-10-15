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
    path('reqbuilder',views.reqbuilder),
    path('delete_builder/<int:id>',views.delete_builder,name="delete_builder"),
    path('approve_builder/<int:id>',views.approved_builder,name="approve_builder"),
    path('view_approved_builders',views.view_approved_builders),
    # path('admin_prop_view',views.admin_prop_view),
    # path('propdelete/<int:id>',views.propdelete,name="propdelete"),
    # path('propupdate/<int:id>',views.propupdate,name="propupdate"),
    # path('propupdate/propupdates/<int:id>',views.propupdates,name="propupdates"),
    # path('admin_book_view',views.admin_book_view),
    # path('userview',views.userview),
    # path('userdelete/<int:id>',views.userdelete,name="userdelete"),
    # path('admin_dashboard',views.admin_dashboard,name="admin_dashboard")
    
]
