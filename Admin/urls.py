from django.urls import path
from .views import *
urlpatterns = [
    path("admin_login",Admin_login,name='Admin_login'),
    path("Adminpage",Admin_page,name='Admin_page'),
    path("logout",Admin_logout,name='Admin_logout'),
]