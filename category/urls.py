from django.urls import path
from .views import *
    
urlpatterns = [
    path("add_category",add_category,name='add_category'),
    path("Category",admin_category,name='admin_category'),
    path('SubCategory/<int:id>',admin_sub_category,name='sub_category'),
    path('add_sub_category',add_sub_category,name='add_sub_category'),

]