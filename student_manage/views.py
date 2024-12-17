from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentInfoForm

def list_student(request):
    students = Student.objects.all().values()

    return render (request,"crud/list_student.html",{"students":students})

def update_student(request,id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        form = StudentInfoForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        student = Student.objects.get(id=id)
        form = StudentInfoForm(instance=student)
    return render(request,"crud/update_student.html",{"form":form})


# Create your views here.
