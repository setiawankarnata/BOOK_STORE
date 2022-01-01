from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg, Max, Min
# from django.http import Http404


# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"), Max("rating"), Min("rating"))

    context = {
        'books': books,
        'total_number_of_books': num_books,
        'average_rating': avg_rating,
    }
    return render(request, 'book_outlet/index.html', context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    context = {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling,
    }
    return render(request, 'book_outlet/book_detail.html', context)
