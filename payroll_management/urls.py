from django.urls import include, path
from django.contrib import admin
from payroll.views import payroll, emps, hrs
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payroll.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', payroll.SignUpView.as_view(), name='signup'),
    path('accounts/signup/emp/', emps.EmpSignUpView.as_view(), name='emp_signup'),
    path('accounts/signup/hr/', hrs.HrSignUpView.as_view(), name='hr_signup'),
    path('emps',emps.emppage ,name='emps'),
    path('hrs',hrs.Tpage ,name='hrs'),
    path('logout',payroll.Logout ,name='logout'),
    path('sleaveApp',emps.StLeaveApp,name='sleaveApp'),
    path('Showapp',hrs.ShowApp,name='Showapp'),
    path('ShowTResp',emps.StatusOfApp,name='ShowTResp'),


]
