from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from attendance.forms import AttendanceForm, CourseForm, NumberOfClassesForm
from attendance.models import Course, AttendanceRecord

@login_required
def index(request):
    courses = Course.objects.filter(attendancerecord__user=request.user).distinct()
    return render(request, 'index.html', {'courses': courses})

@login_required
def submit_attendance(request):
    if request.method == 'POST':
        form = NumberOfClassesForm(request.POST)
        if form.is_valid():
            number_of_classes = int(form.cleaned_data['number_of_classes'])
            return redirect('attendance:fill_attendance', num_classes=number_of_classes)
    else:
        form = NumberOfClassesForm()
    return render(request, 'submit_attendance.html', {'form': form})

@login_required
def fill_attendance(request, num_classes):
    AttendanceFormSet = forms.modelformset_factory(AttendanceRecord, form=AttendanceForm, extra=num_classes)
    if request.method == 'POST':
        formset = AttendanceFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user  
                instance.save()
            return redirect('attendance:index')
    else:
        formset = AttendanceFormSet(queryset=AttendanceRecord.objects.none())
    return render(request, 'fill_attendance.html', {'formset': formset, 'num_classes': num_classes})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    records = course.attendancerecord_set.filter(user=request.user) 
    return render(request, 'course_detail.html', {'course': course, 'records': records})

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course successfully created!')
            return redirect('attendance:index')        
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})
