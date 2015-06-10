from django.contrib import admin
from cms.models import Book, Publisher, Impression, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'publisher', 'page')
    list_display_links = ('id', 'name')
admin.site.register(Book, BookAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
admin.site.register(Publisher, PublisherAdmin)

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', 'comment')
admin.site.register(Impression, ImpressionAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'family_name', 'first_name')
    list_display_links = ('id', 'family_name')
admin.site.register(Author, AuthorAdmin)
