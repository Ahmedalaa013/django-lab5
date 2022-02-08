from django.shortcuts import render
from django.http import HttpResponse
from student_register.models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework import permissions
# Create your views here.

def noster (request):
    students = Student.objects.all()
    request.session['students']= students[0].id
    return HttpResponse('no error')

class Studentlist(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]