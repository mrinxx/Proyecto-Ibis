# Generated by Django 3.2.3 on 2021-06-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210531_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='timetable_file',
            field=models.FileField(default='', upload_to='test'),
            preserve_default=False,
        ),
    ]