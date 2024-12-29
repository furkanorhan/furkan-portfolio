from django.contrib import admin
from .models import Education, Experience, TechnicalSkill, Project

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'field', 'start_date', 'end_date')
    list_filter = ('degree', 'school')
    search_fields = ('school', 'degree', 'field')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date')
    list_filter = ('company',)
    search_fields = ('company', 'position')

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'skills')
    search_fields = ('category', 'skills')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'description') 