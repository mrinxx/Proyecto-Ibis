# Generated by Django 3.2.3 on 2021-05-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210520_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='new_media1',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
