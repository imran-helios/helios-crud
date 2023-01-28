from django.shortcuts import render
from .forms import StudentRegistration
from .models import Registration

# Create your views here.

## Create Function

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            phone = fm.cleaned_data['phone']
            reg = Registration(name = name, phone = phone)
            reg.save()
            fm = StudentRegistration()
    else:
     stud = Registration.objects.all()
     fm = StudentRegistration()
    return render(request, 'app/addandshow.html', {'form': fm, 'stu': stud})