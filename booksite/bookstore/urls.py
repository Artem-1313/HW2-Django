from django.urls import path, include
from .views import get_list_of_books, description_of_book, detail_info_book,author_info, authors_list
urlpatterns = [
    path('', get_list_of_books, name="index"),
    path('description_of_book/<int:id>/', description_of_book, name="description_of_book"),
    path('detail_info/<int:id>/', detail_info_book, name="detail_info_book"),
    path('detail_author/<int:id>/', author_info, name="detail_author"),
    path('authors_list/', authors_list, name="authors_list")
]
