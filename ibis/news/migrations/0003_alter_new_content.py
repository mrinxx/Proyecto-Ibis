# Generated by Django 3.2.3 on 2021-05-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_new_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]
