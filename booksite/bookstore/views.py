from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

books = [
    {
        'id': 1,
        'title': 'The Violet and the Tom',
        'released_year': 2015,
        'pages': 300,
        'price': 100,
        'description': 'In what might have been the middle ages, '
                       'had neither Alexander the Great nor Jesus the prophet died young, '
                       'the Greek State is a powerful economic force in southern Europe, and slavery is a profitable and well-entrenched social institution. '
                       'Nygell, a Lord of the Northern Isles, is given the gift of a Grecian slave by the King. Nygell wants no such responsibility',
        'author_id': 1
    },

    {
        'id': 2,
        'title': 'The Student Prince',
        'released_year': 1819,
        'pages': 100,
        'price': 10,
        'description': 'A modern day (BBC) Merlin AU set at the University of St Andrews, '
                       'featuring teetotal kickboxers, secret wizards, magnificent bodyguards of various genders, irate fairies, imprisoned dragons, crumbling gothic architecture, '
                       'arrogant princes, adorable engineering students, stolen gold, magical doorways, attempted assassination, drunken students, shaving foam fights, embarrassing mornings after, The Hammer Dance, duty, responsibility, friendship and true love...',
        'author_id': 2
    },
    {
        'id': 3,
        'title': 'The bad footballer',
        'released_year': 2016,
        'pages': 1,
        'price': 10000,
        'description': "This is a short story about the bad footballer who can not score a goal even from one yard.",
        'author_id': 1
    },
]

authors = [
    {
        'id': 1,
        'first_name': 'Eva',
        'last_name': 'Ocatillo',
        'age': 51
    },
    {
        'id': 2,
        'first_name': 'Harry',
        'last_name': 'Kane',
        'age': 31
    }
]


def get_list_of_books(request):
    return render(request, "bookstore/index.html", context={"books": books, "authors": authors})


def description_of_book(request, id):
    book_description = None
    for book in books:
        if book['id'] == id:
            book_description = book['description']
    return render(request, "bookstore/book_description.html", context={'book_description': book_description})


def detail_info_book(request, id):
    book_info = None
    author_info = None
    for book in books:
         if book['id'] == id:
            book_info = book
            for author in authors:
                if author['id'] == book['author_id']:
                    author_info = author
    return render(request, "bookstore/detail_info_book.html",
                  context={"book_info": book_info, "author_info": author_info})

def author_info(request, id):
    author_detail=None
    books_id=[]
    for author in authors:
        if author['id']==id:
            author_detail=author
            for book in books:
                if author['id'] == book['author_id']:
                    books_id.append(book['id'])
    return render(request, "bookstore/author_info.html", context={'author_detail':author_detail,'books_id': books_id, "books":books})



def authors_list(request):
    return render(request,"bookstore/authors.html", context={"authors":authors})
