# Generated by Django 3.2.3 on 2021-05-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_guardian_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='floor_letter',
            field=models.CharField(default='', max_length=9),
        ),
    ]