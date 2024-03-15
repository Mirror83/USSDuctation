# Generated by Django 5.0.3 on 2024-03-15 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('reg_no', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('current_year', models.IntegerField()),
                ('current_semester', models.IntegerField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Unit_Info',
            fields=[
                ('unit_code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('unit_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'unit_info',
            },
        ),
        migrations.CreateModel(
            name='Student_Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('fee', models.FloatField()),
                ('date', models.DateField()),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
            options={
                'db_table': 'student_finance',
            },
        ),
        migrations.CreateModel(
            name='Student_Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=10)),
                ('reg_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('unit_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unit_info')),
            ],
            options={
                'db_table': 'student_units',
            },
        ),
    ]