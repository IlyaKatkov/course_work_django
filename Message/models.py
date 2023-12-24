from django.db import models

NULLABLE = {'blank': True, 'null': True }



class Message(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
