from django.shortcuts import render, HttpResponseRedirect,redirect
from .forms import StudentRegistration
from .models import Registration
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

## SignUp Function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Create Successfully !!')
            fm.save()
    else:
        fm = SignUpForm() 
    return render(request, 'app/signup.html', {'form': fm})


## Login Function
def user_login(request):
    if request.method == "POST":
        fm = LoginForm(request = request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user =  authenticate(username = uname, password = upass)
            if user is not None:
                login(request, user)
                
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                    
                return redirect('/')
    else:
        fm = LoginForm()
    return render(request, 'app/userlogin.html', {'form': fm})

## Log Out Function

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


## Create and Show Function
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST, request.FILES)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            phone = fm.cleaned_data['phone']
            photo = fm.cleaned_data['photo']
            reg = Registration(name = name, phone = phone, photo = photo)
            if request.user.is_authenticated:
                reg.save()
            else:
                return HttpResponseRedirect('/login/')
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Registration.objects.all()
    return render(request, 'app/addandshow.html', {'form': fm, 'stu': stud})

## Update and Edit Function
def update_data(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Registration.objects.get(pk = id)
            fm = StudentRegistration(request.POST, request.FILES, instance = pi)
            image_path = pi.photo.path
            
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/')
        else:
            pi = Registration.objects.get(pk = id)
            fm = StudentRegistration(instance = pi)
        return render(request, 'app/updatestudent.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
## Delete Function
def delete_data(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Registration.objects.get(pk = id)
            pi.delete()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')


## Details Function
@login_required(login_url='/login')
def details_data(request, id):
    pi = Registration.objects.get(pk = id)
    return render(request, 'app/details.html', {'user': pi})