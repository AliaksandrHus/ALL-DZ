from django.db import models


# - Grop model

class Group(models.Model):

    grop_num = models.CharField(verbose_name='Группа', max_length=2)
    description = models.CharField(verbose_name='Описание', max_length=50)

    def __str__(self): return str(self.grop_num)


# - Students model

class Student(models.Model):

    name = models.CharField(verbose_name='ФИО', max_length=50)
    age = models.IntegerField(verbose_name='Возраст')

    SEX = ((1, 'Ж'), (2, 'М'))
    sex = models.IntegerField(verbose_name='Sex', choices=SEX)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, default='0')

    def __str__(self): return str(self.name)


