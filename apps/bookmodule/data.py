from apps.bookmodule.models import Book

def add_books():
    books = [
        {'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley', 'price': 120.00, 'edition': 3},
        {'title': 'Reversing: Secrets of Reverse Engineer', 'author': 'E. Eilam', 'price': 97.00, 'edition': 2},
        {'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov', 'price': 100.00, 'edition': 4},
    ]
    
    for book_data in books:
        Book.objects.create(**book_data)
    
    print(f"Added {len(books)} books")

if name == "__main__":
    add_books()
    