from django.views.generic import ListView
# handle the request/response logic for our web app
# Create your views here.
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
