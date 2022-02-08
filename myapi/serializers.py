from rest_framework import serializers
from student_register.models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields =['fullname','st_code','phone']

