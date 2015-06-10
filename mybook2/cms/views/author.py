# -*- coding: utf-8 -*-
from cms.forms import AuthorForm
from cms.models import Author
from cms.views.base_list import BaseList
from cms.views.base_edit import BaseEdit
from cms.views.base_delete import BaseDelete

class AuthorList(BaseList):
    '''著者の一覧'''
    context_object_name = 'authors'
    template_name = 'cms/author_list.html'
    object = Author

class AuthorEdit(BaseEdit):
    '''著者の編集'''
    template_name = 'cms/author_edit.html'
    redirect_view = 'cms:author_list'
    object = Author
    form_object = AuthorForm

class AuthorDelete(BaseDelete):
    '''著者の削除'''
    redirect_view = 'cms:author_list'
    object = Author