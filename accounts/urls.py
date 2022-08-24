from django.urls import path
from .views import *
    
urlpatterns = [
    path("login/",login_page,name='login'),
    path("signup/",signup,name='signup'),
    path("verify/",verify_code,name='verify'),
    path("logout/",logout_page,name='logout'),
]