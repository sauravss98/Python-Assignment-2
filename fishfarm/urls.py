from django.urls import path
from .views import *

urlpatterns=[
    path('dam',DamView,name='dam'),
    path('damentry',ShowViewDam,name='damentry'),
    path('edit/<int:id>',EditViewDam),
    path('update/<int:id>',UpdateViewDam),
    path('delete/<int:id>',DestroyViewDam),
]
