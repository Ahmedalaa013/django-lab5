from django.urls import path,include
from .views import noster
from rest_framework import routers
from student_register.models import Student
from .views import Studentlist
router = routers.DefaultRouter()
router.register(r'student',Studentlist)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]