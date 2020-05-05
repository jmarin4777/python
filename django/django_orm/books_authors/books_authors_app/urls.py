from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('addBook', views.addBook),
    path('books/<int:id>', views.displayBook),
    path('addAuthor/<int:id>', views.addAuthorToBook),
    path('authors', views.authors),
    path('addAuthor', views.addAuthor),
    path('authors/<int:id>', views.displayAuthor),
    path('addBook/<int:id>', views.addBookToAuthor),
]