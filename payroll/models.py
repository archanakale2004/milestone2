from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_emp = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)


class Emp(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    emp = models.ForeignKey(Emp,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username


   

class EmpLeaveApp(models.Model):

    user = models.ForeignKey(Emp,on_delete=models.CASCADE)
    to_hr = models.ForeignKey(Hr,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,null=True)


class AppStatus(models.Model):

    leaveApp = models.ForeignKey(EmpLeaveApp,on_delete=models.CASCADE)
    leaveApp = models.ForeignKey(EmpLeaveApp,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True)




