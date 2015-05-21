from django.db import models

class Author(models.Model):
    '''著者'''
    name = models.CharField(u'著者', max_length=255)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    '''出版社'''
    name = models.CharField(u'出版社名', max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    '''書籍'''
    name = models.CharField(u'書籍名', max_length=255)
    page = models.IntegerField(u'ページ数', blank=True, default = 0)
    publisher = models.ForeignKey(Publisher, verbose_name=u'出版社', related_name='publishers', blank=True, default=None)
    author = models.ForeignKey(Author, verbose_name=u'著者', related_name='authors', blank=True, default=None)

    def __str__(self):
        return self.name

class Impression(models.Model):
    '''感想'''
    book = models.ForeignKey(Book, verbose_name=u'書籍', related_name='impressions')
    comment = models.TextField(u'コメント', blank=True)

    def __str__(self):
        return self.comment
