from django.shortcuts import render
from .models import Books

# Create your views here.

def home(request):
    return render (request, 'book/index.html')

def book(request):
    books = {
        'books': Books.objects.all()
    }
    
    return render (request, 'book/book.html', books)
