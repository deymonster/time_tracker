from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeField, DurationField
from tracker.validators import validate_inn
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Positions(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование организации")
    address = models.CharField(max_length=100, verbose_name="Адрес организации")
    inn = models.CharField(max_length=12, validators=[validate_inn], verbose_name="ИНН")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="Отдел")
    positions = models.ForeignKey(Positions, on_delete=models.PROTECT,  verbose_name="Должности")

    def __str__(self):
        return self.name


class CategoryProgramm(models.Model):
    name = models.CharField(max_length=60, verbose_name="Категория программы")
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Programms(models.Model):
    name = models.CharField(max_length=100, verbose_name="Программа")
    #time_process = models.DurationField(verbose_name="Время")
    is_productive = models.BooleanField(default=False, verbose_name="Продуктивность")
    category = models.ForeignKey(CategoryProgramm, on_delete=PROTECT, verbose_name="Категория")

    

    def __str__(self):
        return self.name

class Employe(models.Model):
    name = models.CharField(max_length=60, verbose_name="Имя сотрудника")
    surname = models.CharField(max_length=60, verbose_name="Фамилия сотрудника")
    department = models.ForeignKey(Department, verbose_name="Отдел", on_delete=models.PROTECT)
    position = models.ForeignKey(Positions, on_delete=PROTECT,  verbose_name="Должность")
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Settings(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    is_connected = models.BooleanField(default=False)
    time_refresh = models.DurationField()
    fired = models.BooleanField(default=True)

    def __str__(self):
        return self.department.name

class Client(models.Model):
    start_at = DateTimeField()
    end_at = DateTimeField()
    total_work = DurationField()
    total_away = DurationField()
    productive_time = DurationField()
    non_productive_time = DurationField()
    user = models.ForeignKey(Employe, on_delete=PROTECT)
    programms = models.ManyToManyField(Programms)
    settings = models.ForeignKey(Settings, on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s' % (self.user.name, self.user.surname)


class Screenshot(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='screenshots/', verbose_name="Скриншот", blank=True)
    client = models.ForeignKey(Client, on_delete=PROTECT)


class CategorySites(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория сайтов")
    description = models.TextField(max_length=200, verbose_name="Описание") 


class Sites(models.Model):
    url = models.URLField()
    time_url = models.DurationField()
    category = models.ForeignKey(CategorySites, on_delete=PROTECT)
    is_productive = models.BooleanField(default=False)
    
