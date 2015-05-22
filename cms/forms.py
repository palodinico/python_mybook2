# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Book, Impression

class BookForm(ModelForm):
    '''書籍のフォーム'''
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'author', 'page',)

class ImreppsionForm(ModelForm):
    '''感想のフォーム'''
    class Meta:
        model = Impression
        fields = ('comment',)