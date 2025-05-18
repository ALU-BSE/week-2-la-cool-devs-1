from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Book
from django.db.models import Count

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    list_filter = ('published_year',)
    search_fields = ('title', 'author')

admin.site.site_header = "📘 Engineer’s Library Admin"
admin.site.site_title = "Engineer’s Portal"
admin.site.index_title = "Book Dashboard"
