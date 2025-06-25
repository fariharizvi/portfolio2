from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Student
from .forms import StudentForm

# Create your views here.

def homepage(request, id):
    xyz = Student.objects.all()
    context = {
        "data" : xyz, 
    }
    
    return render(request, 'myapp/index.html', context)

def aboutUs(request):
    return HttpResponse("My name is Fariha Rizvi.")


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # save to DB
            return redirect('success')  # or redirect
    else:
        form = StudentForm()
    
    return render(request, 'myapp/student_form.html', {'form': form})


def index(request):
    return render(request, 'myapp/index.html')


def success(request):
    return render(request, 'myapp/success.html')