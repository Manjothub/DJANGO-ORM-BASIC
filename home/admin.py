from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','mobile','email','teacher_name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','teacher_name']
