from django.contrib import admin
from companyapiapp.models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'type']
    search_fields = ['name']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'position', 'company']
    list_filter = ['company', 'position']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
