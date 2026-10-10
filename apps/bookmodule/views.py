from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Book, Address, Student
from django.db.models import Count, Sum, Avg, Max, Min, Q
from .models import Book, Address, Student, Department, Course, Card, Enrollment , Address2, Student2
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    books = [
        {
            "title": "Python Programming",
            "author": "John Smith",
            "year": 2020
        },
        {
            "title": "Django Web Development",
            "author": "David Brown",
            "year": 2022
        },
        {
            "title": "Web Technologies",
            "author": "Mark Lee",
            "year": 2023
        }
    ]

    context = {
        "books": books
    }

    return render(request, "bookmodule/index.html", context)



def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def book_detail(request, book_id):
    books = [
        {
            "id": 1,
            "title": "Python Programming",
            "author": "John Smith",
            "year": 2020
        },
        {
            "id": 2,
            "title": "Django Web Development",
            "author": "David Brown",
            "year": 2022
        }
    ]

    book = None

    for b in books:
        if b["id"] == book_id:
            book = b

    context = {
        "book": book
    }

    return render(request, "bookmodule/detail.html", context)


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def html_links(request):
    return render(request, 'bookmodule/html_links.html')

def html_formatting(request):
    return render(request, 'bookmodule/html_formatting.html')

def html_listing(request):
    return render(request, 'bookmodule/html_listing.html')

def html_tables(request):
    return render(request, 'bookmodule/html_tables.html')





def __getBooksList():
    
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley', 'price': 45.99}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam', 'price': 39.99}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov', 'price': 29.99}
    return [book1, book2, book3]

def search(request):
    
    books = __getBooksList()  
    context = {'books': books}
    
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')  
        isAuthor = request.POST.get('option2')  
        
        newBooks = []
        for item in books:
            contained = False
            if isTitle and keyword in item['title'].lower():
                contained = True
            if not contained and isAuthor and keyword in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        
        context = {'books': newBooks}
    
    return render(request, 'bookmodule/search.html', context)





def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]
    
  
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
   

def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_bookList.html', {'books': mybooks})


def lab8_task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_bookList.html', {'books': mybooks})

def lab8_task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) & 
        ~Q(title__icontains='co') & 
        ~Q(author__icontains='co')
    )
    return render(request, 'bookmodule/lab8_bookList.html', {'books': mybooks})

def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_bookList.html', {'books': mybooks})


def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_stats.html', {'stats': stats})

def lab8_task7(request):
   
    stats = Student.objects.values('address__city').annotate(
        student_count=Count('id')
    ).order_by('address__city')
    
    return render(request, 'bookmodule/lab8_task7.html', {'stats': stats})



def lab9_task1(request):
    stats = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task1.html', {'stats': stats})

def lab9_task2(request):
    stats = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task2.html', {'stats': stats})

def lab9_task3(request):
    from django.db.models import Min
    stats = Department.objects.annotate(oldest=Min('student__age'))
    return render(request, 'bookmodule/lab9_task3.html', {'stats': stats})

def lab9_task4(request):
    stats = Department.objects.annotate(student_count=Count('student'))\
                               .filter(student_count__gt=2)\
                               .order_by('-student_count')
    return render(request, 'bookmodule/lab9_task4.html', {'stats': stats})



def lab10_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part1_listbooks.html', {'books': books})    

def lab10_part1_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        
        if title and author and price:
            Book.objects.create(
                title=title,
                author=author,
                price=float(price),
                edition=int(edition) if edition else 1
            )
            return redirect('books.lab10_part1_listbooks')
    
    return render(request, 'bookmodule/lab10_part1_addbook.html')    


def lab10_part1_editbook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price'))
        book.edition = int(request.POST.get('edition')) if request.POST.get('edition') else 1
        book.save()
        return redirect('books.lab10_part1_listbooks')
    
    return render(request, 'bookmodule/lab10_part1_editbook.html', {'book': book})

def lab10_part1_deletebook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('books.lab10_part1_listbooks')
    
    return render(request, 'bookmodule/lab10_part1_deletebook.html', {'book': book})


# ===== LAB 10 - CRUD for SimpleStudent =====
# ===== LAB 10 - CRUD for Student2 =====

def student_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student_list.html', {'students': students})

def student_add(request):
    addresses = Address2.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address_id = request.POST.get('address')
        if name and age and address_id:
            Student2.objects.create(
                name=name,
                age=int(age),
                address_id=int(address_id)
            )
            return redirect('student_list')
    return render(request, 'bookmodule/student_add.html', {'addresses': addresses})

def student_edit(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    addresses = Address2.objects.all()
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = int(request.POST.get('age'))
        student.address_id = int(request.POST.get('address'))
        student.save()
        return redirect('student_list')
    return render(request, 'bookmodule/student_edit.html', {'student': student, 'addresses': addresses})

def student_delete(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'bookmodule/student_delete.html', {'student': student})




from .forms import Student2Form

def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student2_list.html', {'students': students})

def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/student2_add.html', {'form': form})

def student2_edit(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/student2_edit.html', {'form': form, 'student': student})

def student2_delete(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'bookmodule/student2_delete.html', {'student': student})




from .models import Student3, Address3
from django import forms

class Student3Form(forms.ModelForm):
    class Meta:
        model = Student3
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.SelectMultiple(),
        }

def student3_list(request):
    students = Student3.objects.all()
    return render(request, 'bookmodule/student3_list.html', {'students': students})

def student3_add(request):
    if request.method == 'POST':
        form = Student3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student3_list')
    else:
        form = Student3Form()
    return render(request, 'bookmodule/student3_add.html', {'form': form})

def student3_edit(request, student_id):
    student = get_object_or_404(Student3, id=student_id)
    if request.method == 'POST':
        form = Student3Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student3_list')
    else:
        form = Student3Form(instance=student)
    return render(request, 'bookmodule/student3_edit.html', {'form': form, 'student': student})

def student3_delete(request, student_id):
    student = get_object_or_404(Student3, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student3_list')
    return render(request, 'bookmodule/student3_delete.html', {'student': student})


# ===== LAB 11 - TASK 3 (Image Upload) =====

from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'image']

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'bookmodule/profile_list.html', {'profiles': profiles})

def profile_add(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'bookmodule/profile_add.html', {'form': form})

def profile_edit(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'bookmodule/profile_edit.html', {'form': form, 'profile': profile})

def profile_delete(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'bookmodule/profile_delete.html', {'profile': profile})


from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})

@login_required
def viewbook(request, bookId):
    book = get_object_or_404(Book, id=bookId)
    return render(request, 'bookmodule/one_book.html', {'book': book})

@login_required
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')




def lab13_task1(request):
    return render(request, 'bookmodule/lab13_task1.html')

def lab13_task2(request):
    return render(request, 'bookmodule/lab13_task2.html')

def lab13_task3(request):
    return render(request, 'bookmodule/lab13_task3.html')

def lab13_task4(request):
    return render(request, 'bookmodule/lab13_task4.html')

def lab13_task5(request):
    return render(request, 'bookmodule/lab13_task5.html')
