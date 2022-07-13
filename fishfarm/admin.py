from django.contrib import admin
from .models import ManageStaff,ManageDam,ManageFish,ManageCredit,ManageDepartment,ManageSales,ManageTimeline
# Register your models here.
admin.site.register(ManageStaff)
admin.site.register(ManageDam)
admin.site.register(ManageFish)
admin.site.register(ManageCredit)
admin.site.register(ManageDepartment)
admin.site.register(ManageSales)
admin.site.register(ManageTimeline)