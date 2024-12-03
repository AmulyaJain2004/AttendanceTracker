# Generated by Django 5.0.7 on 2024-08-05 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time_duration', models.CharField(help_text='Format: HH:MM-HH:MM (e.g., 14:45-15:45)', max_length=20)),
                ('attended', models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('cancelled', 'CANCELLED')], max_length=10)),
                ('comments', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.course')),
            ],
        ),
    ]
