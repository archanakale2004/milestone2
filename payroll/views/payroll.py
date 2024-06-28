from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import User,auth


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_hr:
            return redirect('hrs')
        elif request.user.is_emp:
            return redirect('emps')


    return render(request, 'payroll/home.html')

def Logout(request):

    auth.logout(request)
    return render(request, 'payroll/home.html')
