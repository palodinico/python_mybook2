# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import BookForm
from cms.models import Book

class BookList(ListView):
    '''書籍の一覧'''
    context_object_name = 'books'
    template_name = 'cms/book_list.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        books = Book.objects.all().order_by('-update', 'id')
        self.object_list = books
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

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

def book_del(request, book_id=None):
    '''書籍の削除'''
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')