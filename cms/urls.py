# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    # 書籍
    url(r'^book/$', views.BookList.as_view(), name="book_list"),
    url(r'^book/add/$', views.book_edit, name="book_add"),
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name="book_mod"),
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name="book_del"),

    #感想
    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),
    url(r'^impression/add/(?P<book_id>\d+)/$', views.impression_edit, name='impression_add'),
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),

    #出版社
    url(r'^publisher/$', views.PublisherList.as_view(), name='publisher_list'),
    url(r'^publisher/add/$', views.publisher_edit, name='publisher_add'),
    url(r'^publisher/mod/(?P<publisher_id>\d+)/$', views.publisher_edit, name='publisher_mod'),
    url(r'^publisher/del/(?P<publisher_id>\d+)/$', views.publisher_del, name='publisher_del'),

    #著者
    url(r'^author/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^author/add/$', views.author_edit, name='author_add'),
    url(r'^author/mod/(?P<author_id>\d+)/$', views.author_edit, name='author_mod'),
    url(r'^author/del/(?P<author_id>\d+)/$', views.author_del, name='author_del'),

)
