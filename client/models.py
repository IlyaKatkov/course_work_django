from django.db import models

NULLABLE = {'blank': True, 'null': True }


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    lastname = models.CharField(max_length=20, verbose_name='Lastname')
    email = models.EmailField(max_length=50, verbose_name='Email')
    comment = models.CharField(max_length=500, verbose_name='Комментарий', **NULLABLE)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.lastname}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
