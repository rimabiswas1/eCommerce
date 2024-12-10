
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('superuser_list/', superuser_list, name='superuser-list'),
    path('staff_list/', staff_list, name='staff-list')

]