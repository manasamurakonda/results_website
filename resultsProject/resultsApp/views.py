from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Student
def home(request):
    return render(request,'home.html')

def data(request):
    rollno = request.POST.get("rollno")
    student = get_object_or_404(Student, roll_number = rollno)
    return render(request,'output.html',{'student' : student})
    #return HttpResponse(rollno)