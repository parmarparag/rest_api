from django.contrib import admin
from .models import Company,Employee

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'name','location','about','types','added_date','active']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['email','address','phone','position','company']