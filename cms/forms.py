# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Book

class BookForm(ModelForm):
    '''書籍のフォーム'''
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'author', 'page',)