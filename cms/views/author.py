# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from cms.forms import AuthorForm
from cms.models import Author
from cms.views.base import BaseList, BaseEdit, BaseDelete

class AuthorList(BaseList):
    '''著者の一覧'''
    context_object_name = 'authors'
    template_name = 'cms/author_list.html'

    def refresh_object_list(self):
        return Author.objects.all().order_by('-update', 'id')

class AuthorEdit(BaseEdit):
    template_name = 'cms/author_edit.html'
    redirect_view = 'cms:author_list'
    object = Author
    form_object = AuthorForm

class AuthorDelete(BaseDelete):
    redirect_view = 'cms:author_list'
    object = Author