# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import ImreppsionForm
from cms.models import Impression, Book

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