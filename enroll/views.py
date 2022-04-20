from django.shortcuts import render
from . models import Student

# Create your views here.
def showdata(request):
    stud = Student.objects.all()
    return render(request,'showdata.html',{'stu':stud})
