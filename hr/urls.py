from os import name
from django.urls import path,include
from . import views
from hr.views import *
from student_register.views import *
urlpatterns = [
    path('hr',hrhome,name='hrhome'),
    path('register',register, name='register'),
    path('login', login, name='login'),
    path('logout',mylogout, name='logout'),
    # path('showData', student_list, name='showData')
    # path('checklogin', checklogin, name='checklogin'),
]