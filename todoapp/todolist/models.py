from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Задание', max_length=300)
    description = models.TextField('Описание', null=True, blank=True)
    is_complete = models.BooleanField('Выполнено', default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['is_complete']

    def __str__(self):
        return self.title
