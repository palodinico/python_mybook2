# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import BookForm
from cms.models import Book
from cms.views.base import BaseList, BaseDelete

class BookList(BaseList):
    '''書籍の一覧'''
    context_object_name = 'books'
    template_name = 'cms/book_list.html'

    def refresh_object_list(self):
        return Book.objects.all().order_by('-update', 'id')

def book_edit(request, book_id=None):
    '''書籍の編集'''
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:
        form = BookForm(instance=book)

    return render_to_response('cms/book_edit.html',
                              dict(form=form, book_id=book_id),
                              context_instance=RequestContext(request))

class BookDelete(BaseDelete):
    redirect_view = 'cms:book_list'
    object = Book