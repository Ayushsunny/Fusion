# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-19 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Calendar',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_details', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('curriculum_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=20)),
                ('credits', models.IntegerField()),
                ('course_type', models.CharField(choices=[('Professional Core', 'Professional Core'), ('Professional Elective', 'Professional Elective'), ('Professional Lab', 'Professional Lab'), ('Engineering Science', 'Engineering Science'), ('Natural Science', 'Natural Science'), ('Humanities', 'Humanities'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('Management Science', 'Management Science')], max_length=25)),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('DESIGN', 'DESIGN'), ('Common', 'Common')], default='Common', max_length=10)),
                ('batch', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('optional', models.BooleanField(default=False)),
                ('floated', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
            options={
                'db_table': 'Curriculum',
            },
        ),
        migrations.CreateModel(
            name='Curriculum_Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_inst', models.BooleanField(default=False)),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
            ],
            options={
                'db_table': 'Curriculum_Instructor',
            },
        ),
        migrations.CreateModel(
            name='Exam_timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('exam_time_table', models.FileField(upload_to='Administrator/academic_information/')),
                ('batch', models.IntegerField(default='2016')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
            ],
            options={
                'db_table': 'Exam_Timetable',
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=4)),
                ('verify', models.BooleanField(default=False)),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
            ],
            options={
                'db_table': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_date', models.DateField()),
                ('holiday_name', models.CharField(max_length=40)),
                ('holiday_type', models.CharField(choices=[('restricted', 'restricted'), ('closed', 'closed'), ('vacation', 'vacation')], default='restricted', max_length=30)),
            ],
            options={
                'db_table': 'Holiday',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('agenda', models.TextField()),
                ('minutes_file', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='Spi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField()),
                ('spi', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'Spi',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globals.ExtraInfo')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('batch', models.IntegerField(default=2016)),
                ('cpi', models.FloatField(default=0)),
                ('category', models.CharField(choices=[('GEN', 'General'), ('SC', 'Scheduled Castes'), ('ST', 'Scheduled Tribes'), ('OBC', 'Other Backward Classes')], max_length=10)),
                ('father_name', models.CharField(default='', max_length=40)),
                ('mother_name', models.CharField(default='', max_length=40)),
                ('hall_no', models.IntegerField(default=1)),
                ('room_no', models.CharField(blank=True, max_length=10, null=True)),
                ('specialization', models.CharField(choices=[('Power and Control', 'Power and Control'), ('Microwave and Communication Engineering', 'Microwave and Communication Engineering'), ('Micro-nano Electronics', 'Micro-nano Electronics'), ('CAD/CAM', 'CAD/CAM'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('CSE', 'CSE'), ('Mechatronics', 'Mechatronics'), ('MDes', 'MDes'), ('None', 'None')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=False)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum_Instructor')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Student_attendance',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('time_table', models.FileField(upload_to='Administrator/academic_information/')),
                ('batch', models.IntegerField(default='2016')),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Des', 'B.Des'), ('M.Tech', 'M.Tech'), ('M.Des', 'M.Des'), ('PhD', 'PhD')], max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('DESIGN', 'DESIGN'), ('Common', 'Common')], default='Common', max_length=10)),
            ],
            options={
                'db_table': 'Timetable',
            },
        ),
        migrations.AddField(
            model_name='spi',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student'),
        ),
        migrations.AddField(
            model_name='grades',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student'),
        ),
        migrations.AddField(
            model_name='curriculum_instructor',
            name='instructor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo'),
        ),
        migrations.AlterUniqueTogether(
            name='spi',
            unique_together=set([('student_id', 'sem')]),
        ),
        migrations.AlterUniqueTogether(
            name='curriculum_instructor',
            unique_together=set([('curriculum_id', 'instructor_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='curriculum',
            unique_together=set([('course_code', 'batch', 'programme')]),
        ),
    ]
