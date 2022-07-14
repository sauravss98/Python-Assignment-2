from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('dashboard',DashboardView,name='dashboard'),
    path('dam',DamView,name='dam'),
    path('damentry',ShowViewDam,name='damentry'),
    path('edit/<int:id>',EditViewDam),
    path('update/<int:id>',UpdateViewDam),
    path('delete/<int:id>',DestroyViewDam),
    path('staffadd',StaffView,name='staffadd'),
    path('staffshow',EditViewStaff,name='staffshow'),
    path('edit/<int:id>',EditViewStaff),
    path('update/<int:id>',UpdateViewStaff),
    path('delete/<int:id>',DestroyViewStaff),
]
