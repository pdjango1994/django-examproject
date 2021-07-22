from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
@login_required
def java_exam_view(request):
    return render(request,'testapp/javaexam.html')

def python_exam_view(request):
    return render(request,'testapp/pythonexam.html')
def logout_view(request):
    return render(request,'testapp/logout.html')
def signup_view(request):
    form=SignUpForm()
    return render(request,'testapp/signup.html',{'form':form})
