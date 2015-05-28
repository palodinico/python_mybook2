# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from cms.views.base_list import BaseList
from cms.views.base_edit import BaseEdit
from cms.views.base_delete import BaseDelete
from cms.forms import PublisherForm
from cms.models import Publisher

class PublisherList(BaseList):
    '''出版社の一覧'''
    context_object_name = 'publishers'
    template_name = 'cms/publisher_list.html'
    object = Publisher

class PublisherEdit(BaseEdit):
    '''出版社の編集'''
    template_name = 'cms/publisher_edit.html'
    redirect_view = 'cms:publisher_list'
    object = Publisher
    form_object = PublisherForm

class PublisherDelete(BaseDelete):
    '''出版社の削除'''
    redirect_view = 'cms:publisher_list'
    object = Publisher