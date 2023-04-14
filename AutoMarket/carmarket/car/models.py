from django.db import models
from django.utils.safestring import mark_safe
from django.contrib import admin


class Cars(models.Model):

    manufacturer = models.TextField('Производитель')
    years_of_production = models.TextField('Годы производства')
    body_type = models.TextField('Тип кузова')
    platform = models.TextField('Платформа')
    layout = models.TextField('Компоновка')
    description = models.TextField('Описание')
    link = models.URLField('Ссылка на википедию')

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.platform

    def get_absolute_url(self):
        return f'/news/{self.id}'


