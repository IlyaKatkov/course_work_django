from django.db import models
from client.models import Client

NULLABLE = {'blank': True, 'null': True }



class Periodicity(models.Model):
    vars = models.CharField(max_length=50, verbose_name='Вид периодичности')

    def __str__(self):
        return f'{vars}'

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'


class Mailing(models.Model):
    data_mailing = models.DateTimeField(verbose_name='Время рассылки')
    periodicity = models.ForeignKey(Periodicity, on_delete=models.CASCADE, verbose_name='Периодичность')
    user = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client id')
    status = models.CharField(max_length=30, verbose_name='Статус рассылки')


    def __str__(self):
        return f'{self.data_mailing}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
