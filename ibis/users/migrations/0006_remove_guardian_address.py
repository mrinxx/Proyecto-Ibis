# Generated by Django 3.2.3 on 2021-05-29 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210529_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='address',
        ),
    ]
