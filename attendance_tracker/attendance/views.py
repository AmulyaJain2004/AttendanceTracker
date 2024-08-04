from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AttendanceForm, CourseForm, NumberOfClassesForm
from .models import Course, AttendanceRecord

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def submit_attendance(request):
    if request.method == 'POST':
        form = NumberOfClassesForm(request.POST)
        if form.is_valid():
            number_of_classes = int(form.cleaned_data['number_of_classes'])
            return redirect('attendance:fill_attendance', num_classes=number_of_classes)
    else:
        form = NumberOfClassesForm()
    return render(request, 'submit_attendance.html', {'form': form})

def fill_attendance(request, num_classes):
    AttendanceFormSet = forms.modelformset_factory(AttendanceRecord, form=AttendanceForm, extra=num_classes)
    if request.method == 'POST':
        formset = AttendanceFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('attendance:index')
    else:
        formset = AttendanceFormSet(queryset=AttendanceRecord.objects.none())
    return render(request, 'fill_attendance.html', {'formset': formset, 'num_classes': num_classes})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    records = course.attendancerecord_set.all()
    return render(request, 'course_detail.html', {'course': course, 'records': records})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            course = Course(
                name = name
            )
            course.save()
            messages.success(request, 'Course successfully created!')
            return redirect('attendance:index')        
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})
