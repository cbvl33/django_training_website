from django.db import models

# Create your models here.
class TeleSetting(models.Model):
    tg_token = models.CharField(max_length=255, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат Айди')
    tg_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
