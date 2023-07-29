from django.db import models


# Create your models here.
class Dota_item_name(models.Model):
    name = models.CharField('Название', max_length=100)
    appearance_time = models.TimeField('Время появления')
    discription = models.TextField('Описание предмета')

    def __str__(self):
        return self.name

class ServisesInSupport(models.Model):
    name = models.CharField('Название', max_length=100)
    guid_server = models.CharField('Guid', max_length=100)
    appearance_time = models.DateField('Дата Принятия в поддержку')
    discription = models.TextField('Дополнительная информация, документация')
    ip_adreses = models.TextField('Айпи адреса серверов', default='')

    def __str__(self):
        return self.name

