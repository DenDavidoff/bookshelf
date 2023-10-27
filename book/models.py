from django.db import models

# Create your models here.
        
class Authors(models.Model):
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    
    def __str__(self):
        return self.surname
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Books(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Краткое описание', max_length=255)
    text = models.TextField('Текст книги')
    img = models.FileField(upload_to='img/')
    author = models.ForeignKey(Authors, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'