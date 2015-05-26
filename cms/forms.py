# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Book, Impression, Publisher, Author

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

class PublisherForm(ModelForm):
    '''出版社のフォーム'''
    class Meta:
        model = Publisher
        fields = ('name',)

class AuthorForm(ModelForm):
    '''著者のフォーム'''
    class Meta:
        model = Author
        fields = ('family_name', 'first_name',)