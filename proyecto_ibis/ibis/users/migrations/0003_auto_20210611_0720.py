# Generated by Django 3.2.4 on 2021-06-11 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_guardian_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumn',
            name='address',
        ),
        migrations.RemoveField(
            model_name='alumn',
            name='city',
        ),
    ]
