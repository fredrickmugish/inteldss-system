from django.contrib import admin
from .models import*
from .models import Document

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

class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('classrooms', 'library', 'laboratory', 'accomodation', 'playgrounds', 'online_resources','get_college','health_facilities')

    def get_college(self, obj):
        return obj.college.college if obj.college else None
    get_college.short_description = 'College'

admin.site.register(Facilities, FacilitiesAdmin)

class AcademicAdmin(admin.ModelAdmin):
    list_display = ('college', 'programs', 'enrollment_rate')
admin.site.register(Academic, AcademicAdmin)

class FinanceAdmin(admin.ModelAdmin):
    list_display = ('get_college','program','tuition_fee',)

    def get_college(self, obj):
        return obj.college.college if obj.college else None
    get_college.short_description = 'College'

admin.site.register(Finance, FinanceAdmin)

class AdministrativeAdmin(admin.ModelAdmin):
    list_display = ('policy',)
admin.site.register(Administrative, AdministrativeAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display = ('sport',)
admin.site.register(Social, SocialAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file')
    search_fields = ('title', 'description')
admin.site.register(Document, DocumentAdmin)