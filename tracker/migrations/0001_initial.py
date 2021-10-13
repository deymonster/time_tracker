# Generated by Django 3.2.8 on 2021-10-12 11:46

from django.db import migrations, models
import django.db.models.deletion
import tracker.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_programm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Programms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_process', models.DateTimeField()),
                ('is_productive', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.category_programm')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование организации')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес организации')),
                ('inn', models.CharField(max_length=12, validators=[tracker.validators.inn_check])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.department')),
                ('positions', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.positions')),
            ],
        ),
    ]
