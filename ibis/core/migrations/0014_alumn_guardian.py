# Generated by Django 3.2.3 on 2021-05-23 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210521_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('guardiancode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='legal-guardian')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=9)),
                ('privacity', models.CharField(blank=True, choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2)),
                ('terms', models.CharField(blank=True, choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2)),
                ('newsletter', models.CharField(blank=True, choices=[('no', 'no'), ('si', 'si')], default='no', max_length=2)),
                ('guardian_created_at', models.DateField(auto_now_add=True)),
                ('guardian_updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='guardians')),
                ('classroom', models.CharField(choices=[('1E', '0-1 años'), ('2E', '1-2 años'), ('3E', '2-3 años'), ('4E', '3-4 años'), ('5E', '4-5 años'), ('6E', '5-6 años')], default='1E', max_length=2)),
                ('alumn_created_at', models.DateField(auto_now_add=True)),
                ('alumn_updated_at', models.DateField(auto_now=True)),
                ('legal_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guardian')),
            ],
        ),
    ]
