# Generated by Django 3.2.3 on 2021-05-31 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0007_guardian_floor_letter'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('job', models.CharField(choices=[('DR', 'Directiva'), ('TC', 'Profesorado'), ('PS', 'Psicología'), ('AS', 'Ayuda Sanitaria'), ('AI', 'Asistencia al infante'), ('TC', 'Técnico especialista'), ('PA', 'PAS')], default='TC', max_length=2)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='people')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('birth_date', models.DateField()),
                ('via_type', models.CharField(choices=[('CL', 'Calle'), ('AV', 'Avenida'), ('CJ', 'Callejón'), ('BL', 'Bulevar'), ('CA', 'Camino')], default='CL', max_length=2)),
                ('via_name', models.CharField(max_length=100)),
                ('via_number', models.IntegerField(default=0)),
                ('address_floor', models.IntegerField()),
                ('floor_letter', models.CharField(default='', max_length=9)),
                ('cp', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='teachers')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('image', models.ImageField(blank=True, upload_to='alumns')),
                ('classroom', models.CharField(choices=[('1E', '0-1 años'), ('2E', '1-2 años'), ('3E', '2-3 años'), ('4E', '3-4 años'), ('5E', '4-5 años'), ('6E', '5-6 años')], default='1E', max_length=2)),
                ('legal_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.guardian')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
