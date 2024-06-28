from django.contrib import admin
from payroll.models import ( Emp,User,
    Hr,EmpLeaveApp )

# Register your models here.

class TeachAdmin(admin.ModelAdmin):

    class Meta:
        model = Hr

admin.site.register(Hr,TeachAdmin)

class StudAdmin(admin.ModelAdmin):

    class Meta:
        model = Emp

admin.site.register(Emp,StudAdmin)

class StLeaveAppAdmin(admin.ModelAdmin):

    class Meta:
        model = EmpLeaveApp

admin.site.register(EmpLeaveApp,StLeaveAppAdmin)




