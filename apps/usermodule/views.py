from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def list_books(request):
    books = [
        {'id': 1, 'title': 'Internet & World Wide Web How to Program', 'author': 'Deitel'},
        {'id': 2, 'title': 'C++ How to Program', 'author': 'Deitel'},
        {'id': 3, 'title': 'Python Crash Course', 'author': 'Matthes'},
    ]
    return render(request, 'bookmodule/list_books.html', {'books': books})

def viewbook(request, bookId):
    books = {
        1: {'id': 1, 'title': 'Internet & World Wide Web How to Program', 'author': 'Deitel', 'description': 'A comprehensive introduction to web programming.'},
        2: {'id': 2, 'title': 'C++ How to Program', 'author': 'Deitel', 'description': 'A comprehensive introduction to C++ programming.'},
        3: {'id': 3, 'title': 'Python Crash Course', 'author': 'Matthes', 'description': 'A hands-on, project-based introduction to Python.'},
    }
    book = books.get(bookId)
    return render(request, 'bookmodule/one_book.html', {'book': book})

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def html_links(request):
    return render(request, 'bookmodule/html_links.html')

def html_formatting(request):
    return render(request, 'bookmodule/html_formatting.html')

def html_listing(request):
    return render(request, 'bookmodule/html_listing.html')

def html_tables(request):
    return render(request, 'bookmodule/html_tables.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'usermodule/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('books.index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'usermodule/login.html')



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
