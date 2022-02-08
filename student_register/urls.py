
from os import name
from django.urls import path,include
from . import views
from student_register.views import *
urlpatterns = [
    path('',views.student_form, name='student_insert'),
    path('list/', views.student_list, name='student_list'),
    path('<int:id>',views.student_form, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('Tracklist', Tracklist.as_view(), name='Tracklist')
]