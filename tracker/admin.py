from django.contrib import admin
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'inn')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category_programm)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Programms)
class ProgrammsAdmin(admin.ModelAdmin):
    list_display = ('name',)
     

