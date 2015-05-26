# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import BookForm, ImreppsionForm, PublisherForm, AuthorForm
from cms.models import Book, Impression, Publisher, Author

class AuthorList(ListView):
    '''著者の一覧'''
    context_object_name = 'authors'
    template_name = 'cms/author_list.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        authors = Author.objects.all().order_by('-update', 'id')
        self.object_list = authors
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

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

def author_edit(request, author_id=None):
    '''著者の編集'''
    if author_id:
        author = get_object_or_404(Author, pk=author_id)
    else:
        author = Author()
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('cms:author_list')
    else:
        form = AuthorForm(instance=author)

    return render_to_response('cms/author_edit.html',
                              dict(form=form, author_id=author_id),
                              context_instance=RequestContext(request))

def author_del(request, author_id=None):
    '''著者の削除'''
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('cms:author_list')

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
        impressions = book.impressions.all().order_by('-update', 'id')
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

class PublisherList(ListView):
    '''出版社の一覧'''
    context_object_name = 'publishers'
    template_name = 'cms/publisher_list.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        publishers = Publisher.objects.all().order_by('-update', 'id')
        self.object_list = publishers
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

def publisher_edit(request, publisher_id=None):
    '''出版社の編集'''
    if publisher_id:
        publisher = get_object_or_404(Publisher, pk=publisher_id)
    else:
        publisher = Publisher()
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            return redirect('cms:publisher_list')
    else:
        form = PublisherForm(instance=publisher)

    return render_to_response('cms/publisher_edit.html',
                              dict(form=form, publisher_id=publisher_id),
                              context_instance=RequestContext(request))

def publisher_del(request, publisher_id):
    '''出版社の削除'''
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    publisher.delete()
    return redirect('cms:publisher_list')