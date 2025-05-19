from django.contrib import admin
from .models import Book

admin.site.site_header = "📘 The Engineer’s Library Admin"
admin.site.site_title = "Engineer’s Portal"
admin.site.index_title = "Book Dashboard"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')

    # Enable filters for multiple fields
    list_filter = ('author', 'title', 'published_year')

    # Enable search on specific fields
    search_fields = ('title', 'author')

    # Pagination - show 10 by default
    list_per_page = 10
    list_max_show_all = 200  # Optional: allow all items to be shown

    # Optional: ordering
    ordering = ('title',)
