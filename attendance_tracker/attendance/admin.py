from django.contrib import admin
from .models import Course, AttendanceRecord

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_classes', 'attended_classes', 'attendance_percentage')

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('course', 'date', 'time_duration', 'attended')
    list_filter = ('course', 'date', 'attended')
