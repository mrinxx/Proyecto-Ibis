# Generated by Django 3.2.3 on 2021-06-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210606_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=400)),
                ('resource_created_at', models.DateField(auto_now_add=True)),
                ('resource_updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
