from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.views import View

from ..decorators import emp_required
from ..forms import EmpLeaveAppForm,EmpSignUpForm
from ..models import Hr,Emp, User, EmpLeaveApp


class EmpSignUpView(CreateView):
    model = User
    form_class = EmpSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'emp'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('emps')

def StLeaveApp(request):

    form = EmpLeaveAppForm(request.POST)
    
    emp = Emp.objects.filter(user=request.user).first()

    if form.is_valid():
        form.instance.user=emp
        form.save()

    context = {'form':form}

    return render(request,'empApp.html',context)

def StatusOfApp(request):

    emp = Emp.objects.filter(user=request.user).first()

    app = EmpLeaveApp.objects.filter(user=emp).all()

    context = { 'app':app }

    return render(request,'AppStatus.html',context)


def emppage(request):

    emp =Emp.objects.filter(user=request.user).first()

    app = EmpLeaveApp.objects.filter(user=emp).all()

    context = { 'app':app }

    return render(request,'emppage.html',context)
