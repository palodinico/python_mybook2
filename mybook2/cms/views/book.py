# -*- coding: utf-8 -*-
from cms.forms import BookForm
from cms.models import Book
from cms.views.base_list import BaseList
from cms.views.base_edit import BaseEdit
from cms.views.base_delete import BaseDelete

class BookList(BaseList):
    '''書籍の一覧'''
    context_object_name = 'books'
    template_name = 'cms/book_list.html'
    object = Book

class BookEdit(BaseEdit):
    '''著者の編集'''
    template_name = 'cms/book_edit.html'
    redirect_view = 'cms:book_list'
    object = Book
    form_object = BookForm

class BookDelete(BaseDelete):
    redirect_view = 'cms:book_list'
    object = Book