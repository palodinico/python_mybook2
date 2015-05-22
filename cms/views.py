# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import BookForm, ImreppsionForm
from cms.models import Book, Impression

class BookList(ListView):
    '''書籍の一覧'''
    context_object_name = 'books'
    template_name = 'cms/book_list.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        books = Book.objects.all().order_by('id')
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

class ImpressionList(ListView):
    '''感想の一覧'''
    context_object_name = 'impressions'
    template_name = 'cms/impression_list.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])
        impressions = book.impressions.all().order_by('id')
        self.object_list = impressions
        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)

def impression_edit(request, book_id, impression_id=None):
    '''感想の編集'''
    book = get_object_or_404(Book, pk=book_id)
    if impression_id:
        impression = get_object_or_404(Impression, pk=impression_id)
    else:
        impression = Impression()

    if request.method == 'POST':
        form = ImreppsionForm(request.POST, instance=impression)
        if form.is_valid():
            impression = form.save(commit=False)
            impression.book = book
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:
        form = ImreppsionForm(instance=impression)
    return render_to_response('cms/impression_edit.html',
                              dict(form=form, book_id=book_id, impression_id=impression_id),
                              context_instance=RequestContext(request))

def impression_del(request, book_id, impression_id):
    '''感想の削除'''
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)

def publisher_list(request):
    '''出版社の一覧'''
    return HttpResponse(u'出版社の一覧')

def publisher_edit(request, publisher_id=None):
    '''出版社の編集'''
    return HttpResponse(u'出版社の編集')

def publisher_del(request, publisher_id):
    '''出版社の削除'''
    return HttpResponse(u'出版社の削除')