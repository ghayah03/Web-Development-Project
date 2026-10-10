from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm
from django.db.models import Q

def index(request):
    return render(request, 'exam/index.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'exam/list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = BookForm()
    return render(request, 'exam/add.html', {'form': form})

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'exam/detail.html', {'book': book})

def search_books(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
    return render(request, 'exam/search.html', {'results': results, 'query': query})
