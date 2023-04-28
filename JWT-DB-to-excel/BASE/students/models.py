from django.db import models


# - Grop model

class Group(models.Model):

    group_num = models.CharField(verbose_name='Группа', max_length=2)
    description = models.CharField(verbose_name='Описание', max_length=50)

    def __str__(self): return str(self.group_num)


# - Students model

class Student(models.Model):

    name = models.CharField(verbose_name='ФИО', max_length=50)
    age = models.IntegerField(verbose_name='Возраст')

    SEX = ((1, 'Ж'), (2, 'М'))
    sex = models.IntegerField(verbose_name='Sex', choices=SEX)

    in_group = models.ForeignKey(Group, on_delete=models.CASCADE, default='0', max_length=10)

    def __str__(self): return str(self.name)
