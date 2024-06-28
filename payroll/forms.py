from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from payroll.models import (Emp,Hr,
                                EmpLeaveApp ,User,AppStatus)


class HrSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_hr = True
        user.save()
        hr = Hr.objects.create(user=user)
        return user


class EmpSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_emp = True
        user.save()
        emp = Emp.objects.create(user=user)
        return user



class AppStatusForm(forms.ModelForm):
    class Meta:
        model = AppStatus

        fields = ('status',)

        widgets = {

            'status':forms.TextInput,

        }

class EmpLeaveAppForm(forms.ModelForm):
    class Meta:
        model = EmpLeaveApp

        fields = ('content', 'to_hr')

        widgets = {

            'content': forms.TextInput,

        }

