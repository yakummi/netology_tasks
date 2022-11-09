from django.contrib import admin
from django.urls import path

from books.views import books_view, book_info

urlpatterns = [
    path('books', books_view, name='books'),
    path('admin/', admin.site.urls),
    path('books/<pub_date>/', book_info, name='book')
]
