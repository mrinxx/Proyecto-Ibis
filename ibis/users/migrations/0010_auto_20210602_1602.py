# Generated by Django 3.2.3 on 2021-06-02 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_guardian_activated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom', models.CharField(choices=[('1E', '0-1 años'), ('2E', '1-2 años'), ('3E', '2-3 años'), ('4E', '3-4 años'), ('5E', '4-5 años'), ('6E', '5-6 años')], default='1E', max_length=2, unique=True)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='People',
        ),
        migrations.RemoveField(
            model_name='alumn',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='alumn',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cicle'),
        ),
    ]