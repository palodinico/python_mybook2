# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import AuthorForm
from cms.models import Author

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