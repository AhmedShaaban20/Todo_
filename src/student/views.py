from django.shortcuts import render
from .models import Student,Course,City
from .serializers import StudentSerializer, CitySerializer, CourseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
# Create your views here.



class StudentListApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

