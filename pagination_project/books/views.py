from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    filter_by = request.GET.get('filter_by', 'author')
    query = request.GET.get('q', '')
    year = request.GET.get('year', '')
    per_page = request.GET.get('per_page', 10)

    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10

    books = Book.objects.all().order_by('title')

    if filter_by == 'author' and query:
        books = books.filter(author__icontains=query)
    elif filter_by == 'title' and query:
        books = books.filter(title__icontains=query)
    elif filter_by == 'year' and year:
        books = books.filter(published_year=year)

    paginator = Paginator(books, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {
        'page_obj': page_obj,
        'filter_by': filter_by,
        'query': query,
        'year': year,
        'per_page': per_page,
        'per_page_choices': [5, 10, 20],
        'year_choices': Book.objects.values_list('published_year', flat=True).distinct().order_by('published_year'),
        'author_list': Book.objects.values_list('author', flat=True).distinct().order_by('author'),
        'title_list': Book.objects.values_list('title', flat=True).distinct().order_by('title'),
    })
