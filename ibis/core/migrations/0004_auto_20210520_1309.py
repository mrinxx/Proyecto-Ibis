# Generated by Django 3.2.3 on 2021-05-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210519_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='new_subtitle',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='new_title',
            field=models.CharField(max_length=100),
        ),
    ]