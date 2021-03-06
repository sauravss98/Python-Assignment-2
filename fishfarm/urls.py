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
    path('staffadd',StaffAdd,name='staffadd'),
    path('staffshow',StaffView,name='staffshow'),
    path('staffedit/<str:pk>',EditViewStaff,name="staffedit"),
    path('staffdelete/<str:pk>',DestroyViewStaff,name="staffdelete"),
    path('fishadd', FishAdd, name='fishadd'),
    path('fishshow', ViewFish, name='fishshow'),
    path('fishedit/<int:id>', EditViewFish),
    path('fishupdate/<int:id>', UpdateViewFish),
    path('fishdelete/<int:id>', DestroyViewFish),
    path('departmentadd', DepartmentAdd, name='departmentadd'),
    path('departmentshow', ViewDepartment, name='departmentshow'),
    path('departmentedit/<int:id>', EditViewDepartment),
    path('departmentupdate/<int:id>', UpdateViewDepartment),
    path('departmentdelete/<int:id>', DestroyViewDepartment),
    path('salesadd', SalesAdd, name='salesadd'),
    path('salesshow', ViewSales, name='salesshow'),
    path('salesedit/<int:id>', EditViewSales),
    path('salesupdate/<int:id>', UpdateViewSales),
    path('salesdelete/<int:id>', DestroyViewSales),
    path('creditadd', CreditAdd, name='creditadd'),
    path('creditshow', ViewCredit, name='creditshow'),
    path('creditedit/<int:id>', EditViewCredit),
    path('creditupdate/<int:id>', UpdateViewCredit),
    path('creditdelete/<int:id>', DestroyViewCredit),
]
