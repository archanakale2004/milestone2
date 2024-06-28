from django.urls import include, path

from .views import payroll, emps, hrs

urlpatterns = [
    path('', payroll.home, name='home'),

    path('emps/', include(([

    ], 'payroll'), namespace='emps')),

    path('hrs/', include(([


    ], 'payroll'), namespace='hrs')),
]
