# Generated by Django 3.2.3 on 2021-05-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='new_media2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='new',
            name='new_media3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='new',
            name='new_media4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='new',
            name='new_media5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='new',
            name='new_media6',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]