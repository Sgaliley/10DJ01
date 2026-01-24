from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News_post(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название новости')
    short_description  = models.TextField(max_length=200, null=True, blank=True, verbose_name='Краткое описание новости')
    text = models.TextField(verbose_name='Новость')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Автор')
    
    def __str__(self):
        return '{}'.format(self.title)
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name='Новость'
        verbose_name_plural='Новости'