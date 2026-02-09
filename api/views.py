from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
# Create your views here.


def studentsView(request):
    # Manuel Serializing
    students = Student.objects.all()
    students_list = list(students.values()) # passing value of students as n number of dictionaries inside a list.
    return JsonResponse(students_list,safe=False)