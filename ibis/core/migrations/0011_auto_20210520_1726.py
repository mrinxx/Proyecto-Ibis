# Generated by Django 3.2.3 on 2021-05-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210520_1635'),
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
                ('teacher_created_at', models.DateField(auto_now_add=True)),
                ('teacher_updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_Description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_updated_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_media2',
            new_name='media2',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_media3',
            new_name='media3',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_media4',
            new_name='media4',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_media5',
            new_name='media5',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_media6',
            new_name='media6',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_subtitle',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='new',
            name='new_media1',
        ),
        migrations.AddField(
            model_name='new',
            name='media1',
            field=models.ImageField(default='', upload_to='news/images'),
            preserve_default=False,
        ),
    ]