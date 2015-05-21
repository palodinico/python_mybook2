# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from cms.forms import BookForm
from cms.models import Book

def book_list(request):
    '''書籍の一覧'''
    books = Book.objects.all().order_by('id')
    return render_to_response('cms/book_list.html',
                              {'books':books},
                              context_instance=RequestContext(request))

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
    return HttpResponse(u'書籍の削除')


'''
#    return HttpResponse(u'書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render_to_response('cms/book_list.html',  # 使用するテンプレート
                              {'books': books},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト

'''