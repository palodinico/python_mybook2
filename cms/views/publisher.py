# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.list import ListView
from cms.forms import PublisherForm
from cms.models import Publisher

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