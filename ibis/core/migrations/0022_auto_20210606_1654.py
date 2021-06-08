# Generated by Django 3.2.3 on 2021-06-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_timetable_timetable_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='timetable_file',
        ),
        migrations.AlterField(
            model_name='menu',
            name='age',
            field=models.CharField(choices=[('1E', '0-1 años'), ('2E', '1-2 años'), ('3E', '2-3 años'), ('4E', '3-4 años'), ('5E', '4-5 años'), ('6E', '5-6 años')], default='1E', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='age',
            field=models.CharField(choices=[('1E', '0-1 años'), ('2E', '1-2 años'), ('3E', '2-3 años'), ('4E', '3-4 años'), ('5E', '4-5 años'), ('6E', '5-6 años')], default='1E', max_length=2, unique=True),
        ),
    ]