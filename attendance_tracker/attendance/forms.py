from django import forms
from .models import AttendanceRecord, Course

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['course', 'time_duration', 'attended']

class CourseForm(forms.Form):
    name = forms.CharField(max_length=200, label='Course')
    
    def save(self):
        data = self.cleaned_data
        course = Course.objects.create(title=data['name'])
        course.save()
        return course
    
class NumberOfClassesForm(forms.Form):
    number_of_classes = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 7)], label="How many classes did you attend today?")