from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
import datetime

def books_view(request):
    book = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': book}
    return render(request, template, context)

def book_info(request, pub_date):
    books = Book.objects.all().order_by('pub_date')
    date_list = [book.pub_date.strftime('%Y-%m-%d') for book in books]
    paginator = Paginator(list(books), 1)
    books_info = list(zip(books, date_list))
    template = 'books/books_info.html'
    context = {
        'books_info': books_info,
        'date': pub_date,
    }
    if pub_date:
        books = books.filter(pub_date=pub_date)
        date_list = [book.pub_date.strftime('%Y-%m-%d') for book in books]
        books_info = list(zip(books, date_list))
        id_ = books[0].id
        context['books_info'] = books_info

        next_page = paginator.get_page(id_).next_page_number() \
            if paginator.get_page(id_).has_next() else None
        previous_page = paginator.get_page(id_).previous_page_number() \
            if paginator.get_page(id_).has_previous() else None

    if next_page:
        next_book = Book.objects.filter(id=next_page)[0]
        next_date = next_book.pub_date.strftime("%Y-%m-%d")
        context['next_date'] = next_date

    if previous_page:
        previous_book = Book.objects.filter(id=previous_page)[0]
        previous_date = previous_book.pub_date.strftime("%Y-%m-%d")
        context['previous_date'] = previous_date

    return render(request, template, context)
