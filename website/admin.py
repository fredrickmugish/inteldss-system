from django.contrib import admin
from .models import*

# Register your models here.
#admin.site.register(Organization)
#admin.site.register(Disruptor)
#admin.site.register(Team)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','title','university','image')
admin.site.register(Team,TeamAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')
admin.site.register(Organization,OrganizationAdmin)

class DisruptorAdmin(admin.ModelAdmin):
    list_display = ('category','affected_aspect')
admin.site.register(Disruptor,DisruptorAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('regNo','fName','sName','lName','academic_level','program','year')
admin.site.register(Student,StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empId','fName','sName','lName','department','orgName','professional')
admin.site.register(Employees,EmployeeAdmin)
