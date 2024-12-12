
from django.urls import path
from .views import *

app_name = 'management'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('superuser_list/', superuser_list, name='superuser-list'),
    path('staff_list/', staff_list, name='staff-list'),
    path('create-superuser/', create_superuser, name='create_superuser'),
    path('signup/', signup, name='signup'),
    path('customer/', customer, name='customer'),
    path('product-view/', product_view, name='product_view')
]