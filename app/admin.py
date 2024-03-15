from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['reg_no', 'name', 'course',
                    'current_year', 'current_semester']
    search_fields = ['reg_no', 'name', 'course']
    list_filter = ['current_year', 'current_semester']


@admin.register(Unit_Info)
class UnitInfoAdmin(admin.ModelAdmin):
    list_display = ['unit_code', 'unit_name', 'year', 'semester', 'course']
    search_fields = ['unit_code', 'unit_name', 'course']
    list_filter = ['year', 'semester']


@admin.register(Student_Units)
class StudentUnitsAdmin(admin.ModelAdmin):
    list_display = ['reg_no', 'unit_code', 'result']
    search_fields = ['reg_no', 'unit_code']
    list_filter = ['result']


@admin.register(Student_Finance)
class StudentFinanceAdmin(admin.ModelAdmin):
    list_display = ['reg_no', 'balance', 'fee', 'date']
    search_fields = ['reg_no', 'balance', 'fee']
    list_filter = ['date']


@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ['course_name']
    search_fields = ['course_name']
    list_filter = ['course_name']