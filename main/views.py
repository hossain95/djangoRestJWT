from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Semester, Subject, Student, Teacher
from .serializers import SemesterSerializer, SubjectSerializer, StudentSerializer, TeacherSerializer

# Create your views here.


class SubjectView(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SemesterView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        semsters = Semester.objects.all()
        serializer = SemesterSerializer(semsters, many=True)
        return Response(serializer.data)


class StudentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def studentExisit(self, pk):
        try:
            return Student.objects.get(id=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.studentExisit(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.studentExisit(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        student = self.studentExisit(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
