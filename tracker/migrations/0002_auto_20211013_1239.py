# Generated by Django 3.2.8 on 2021-10-13 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория сайтов')),
                ('description', models.TextField(max_length=200, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('total_work', models.DurationField()),
                ('total_away', models.DurationField()),
                ('productive_time', models.DurationField()),
                ('non_productive_time', models.DurationField()),
            ],
        ),
        migrations.RemoveField(
            model_name='programms',
            name='time_process',
        ),
        migrations.AlterField(
            model_name='category_programm',
            name='description',
            field=models.TextField(blank=True, max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category_programm',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Категория программы'),
        ),
        migrations.AlterField(
            model_name='company',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(max_length=12, validators=[tracker.validators.validate_inn], verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='company',
            name='positions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.positions', verbose_name='Должности'),
        ),
        migrations.AlterField(
            model_name='programms',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.category_programm', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='programms',
            name='is_productive',
            field=models.BooleanField(default=False, verbose_name='Продуктивность'),
        ),
        migrations.AlterField(
            model_name='programms',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Программа'),
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('time_url', models.DurationField()),
                ('is_productive', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.category_sites')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_connected', models.BooleanField(default=False)),
                ('time_refresh', models.DurationField()),
                ('fired', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.positions')),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='screenshots/', verbose_name='Скриншот')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.client')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя сотрудника')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия сотрудника')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.department', verbose_name='Отдел')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.positions', verbose_name='Должность')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='programms',
            field=models.ManyToManyField(to='tracker.Programms'),
        ),
        migrations.AddField(
            model_name='client',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.settings'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.employe'),
        ),
    ]
