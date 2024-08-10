from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def total_classes(self, user):
        return self.attendancerecord_set.filter(user=user).exclude(attended='cancelled').count()

    def attended_classes(self, user):
        return self.attendancerecord_set.filter(user=user, attended='yes').count()

    def attendance_percentage(self, user):
        total = self.total_classes(user)
        attended = self.attended_classes(user)
        if total > 0:
            return (attended / total) * 100
        return 0

class AttendanceRecord(models.Model):
    CHOICES = (
        ('yes', 'YES'),
        ('no', 'NO'),
        ('cancelled', 'CANCELLED'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_duration = models.CharField(max_length=20, help_text="Format: HH:MM-HH:MM (e.g., 14:45-15:45)")
    attended = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return f'{self.course.name} - {self.date} - {self.time_duration}'
