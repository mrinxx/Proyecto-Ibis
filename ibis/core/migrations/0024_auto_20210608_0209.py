# Generated by Django 3.2.3 on 2021-06-08 00:09

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210608_0209'),
        ('core', '0023_resource'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'menu', 'verbose_name_plural': 'menus'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': 'resource', 'verbose_name_plural': 'resources'},
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'verbose_name': 'timetable', 'verbose_name_plural': 'timetables'},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='age',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='age',
        ),
        migrations.AddField(
            model_name='menu',
            name='cicle',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='users.cicle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timetable',
            name='cicle',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='users.cicle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(validators=[core.models.validate_date]),
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menus',
        ),
        migrations.AlterModelTable(
            name='resource',
            table='resources',
        ),
        migrations.AlterModelTable(
            name='timetable',
            table='timetables',
        ),
    ]
