# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from cms.forms import AuthorForm
from cms.models import Author
from cms.views.base import BaseList, BaseDelete

class AuthorList(BaseList):
    '''著者の一覧'''
    context_object_name = 'authors'
    template_name = 'cms/author_list.html'

    def refresh_object_list(self):
        return Author.objects.all().order_by('-update', 'id')

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

class AuthorDelete(BaseDelete):
    redirect_view = 'cms:author_list'
    object = Author