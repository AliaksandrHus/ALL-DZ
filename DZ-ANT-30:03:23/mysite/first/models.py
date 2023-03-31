from django.db import models


class Students(models.Model):

    name = models.TextField()
    sex = models.TextField()
    group_id = models.TextField()
    description = models.TextField()


class UserForm(models.Model):

    name = models.TextField()
    how = models.IntegerField()