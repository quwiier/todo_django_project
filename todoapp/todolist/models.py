from django.db import models


# Create your models here.

class ToDo(models.Model):
    title = models.CharField('Задание', max_length=300)
    is_complete = models.BooleanField('Выполнено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title