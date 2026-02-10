from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


# Manuel Serializing
# def studentsView(request):
    # students = Student.objects.all()
    # students_list = list(students.values()) # passing value of students as n number of dictionaries inside a list.
    # return JsonResponse(students_list,safe=False)


# Fetching all data (GET) and POST form
@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serialzer = StudentSerializer(students,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
    


# Fetching single data
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)