from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_course/', views.create_course, name='create_course'),
    path('submit/', views.submit_attendance, name='submit_attendance'),
    path('fill_attendance/<int:num_classes>/', views.fill_attendance, name='fill_attendance'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]
