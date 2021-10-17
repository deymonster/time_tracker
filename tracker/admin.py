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

@admin.register(CategoryProgramm)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Programms)
class ProgrammsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
            'start_at', 'end_at', 'total_work', 'total_away',
            'productive_time', 'non_productive_time', 'user', 'get_programms',
             'settings'
            )
    def get_programms(self, obj):
        return "\n".join([p.name for p in obj.programms.all()])



@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'department', 'position', 'is_connected', 'time_refresh',
        'fired'
    )

    


     
@admin.register(Employe)
class EployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'surname', 'department', 
        'position', 'user'
    )
