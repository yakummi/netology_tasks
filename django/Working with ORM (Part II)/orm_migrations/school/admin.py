from django.contrib import admin

from .models import Student, Teacher

class ConnectInline(admin.TabularInline):
    model = Student.teacher.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [ConnectInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [ConnectInline]
