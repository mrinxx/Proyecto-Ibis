# Generated by Django 3.2.3 on 2021-05-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('guardiancode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('guardianusername', models.CharField(max_length=9, unique=True)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='legal-guardian')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=9)),
                ('privacity', models.CharField(blank=True, choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2, null=True)),
                ('terms', models.CharField(blank=True, choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2, null=True)),
                ('newsletter', models.CharField(blank=True, choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2, null=True)),
                ('activated', models.CharField(choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2)),
                ('guardian_created_at', models.DateField(auto_now_add=True)),
                ('guardian_updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
