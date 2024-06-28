from django.forms.formsets import formset_factory
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import hr_required
from ..forms import HrSignUpForm,AppStatusForm
from ..models import  User,Hr,EmpLeaveApp,Emp


class HrSignUpView(CreateView):
    model = User
    form_class = HrSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hr'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('hrs')

#def TeachLeaveApp(request):

#    form = EmpLeaveAppForm(request.POST)

 #   if form.is_valid():
  #      form.save()

  #  context = {'form':form}

   # return render(request,'empApp.html',context)


def ShowApp(request): # It will show all application send from emps
    
    hr = Hr.objects.filter(user=request.user).first()
    app = EmpLeaveApp.objects.filter(to_hr = hr).all()
    app1 = EmpLeaveApp.objects.filter(to_hr = hr).all()
    
    app2 = EmpLeaveApp.objects.filter(id=request.POST.get('answer')).all()

    for items in app2:

        items.status = request.POST.get('status')
        items.save()

    context = { 'app':app }

    return render(request,'ShowApp.html',context)


def Tpage(request):

    context = locals()

    return render(request,'tpage.html',context)







