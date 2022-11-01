from django.db import models

class Theme(models.Model):
    theme = models.CharField(max_length=100, verbose_name='Тема')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.theme



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    theme = models.ManyToManyField(Theme, through='Relations', through_fields=('article', 'theme'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Relations(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Главная тема')