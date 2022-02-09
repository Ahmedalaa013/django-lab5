from django.shortcuts import render
from django.http import HttpResponse
from student_register.models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def deletestudent (request,pk):
    student = Student.objects.get(pk=id)
    student.delete()
    return Response({'message': '{} student was deleted successfully!'.format(student.fullname)})


def noster (request):
    students = Student.objects.all()
    request.session['students']= students[0].id
    return HttpResponse('no error')

class Studentlist(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]