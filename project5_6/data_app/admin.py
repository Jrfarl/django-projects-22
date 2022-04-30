from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'major', 'academic_class')
    list_display_links = ('name', 'major')

admin.site.register(Student, StudentAdmin)