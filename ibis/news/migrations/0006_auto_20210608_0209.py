# Generated by Django 3.2.3 on 2021-06-08 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_new_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'new', 'verbose_name_plural': 'news'},
        ),
        migrations.AlterModelTable(
            name='new',
            table='news',
        ),
    ]
