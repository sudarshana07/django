from django.shortcuts import render, redirect

# Create your views here.
from .forms import StudentForm
from .models import Student, Management


def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'school/success.html')
    else:
        form = StudentForm()

    return render(request, 'school/index.html', {'form': form})


def studentMerit(request):
    merit_list = Student.objects.filter(student_marks__gt=88)[:10]
    #management = Management.objects.all()[:3]
    #testimonials = Testimonials.objects.all()[:3]
    return render(request, 'school/base.html', {'meritList': merit_list})

