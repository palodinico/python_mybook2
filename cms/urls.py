# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms.views import book, impression, publisher, author, index

urlpatterns = patterns('',
    #トップページ
    url(r'^$', index.Index.as_view(), name="index_page"),

    # 書籍
    url(r'^book/$', book.BookList.as_view(), name="book_list"),
    url(r'^book/add/$', book.book_edit, name="book_add"),
    url(r'^book/mod/(?P<book_id>\d+)/$', book.book_edit, name="book_mod"),
    url(r'^book/del/(?P<book_id>\d+)/$', book.book_del, name="book_del"),

    #感想
    url(r'^impression/(?P<book_id>\d+)/$', impression.ImpressionList.as_view(), name='impression_list'),
    url(r'^impression/add/(?P<book_id>\d+)/$', impression.impression_edit, name='impression_add'),
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', impression.impression_edit, name='impression_mod'),
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', impression.impression_del, name='impression_del'),

    #出版社
    url(r'^publisher/$', publisher.PublisherList.as_view(), name='publisher_list'),
    url(r'^publisher/add/$', publisher.publisher_edit, name='publisher_add'),
    url(r'^publisher/mod/(?P<publisher_id>\d+)/$', publisher.publisher_edit, name='publisher_mod'),
    url(r'^publisher/del/(?P<publisher_id>\d+)/$', publisher.publisher_del, name='publisher_del'),

    #著者
    url(r'^author/$', author.AuthorList.as_view(), name='author_list'),
    url(r'^author/add/$', author.author_edit, name='author_add'),
    url(r'^author/mod/(?P<author_id>\d+)/$', author.author_edit, name='author_mod'),
    url(r'^author/del/(?P<author_id>\d+)/$', author.author_del, name='author_del'),

)
