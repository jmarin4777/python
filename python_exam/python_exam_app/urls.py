from django.urls import path
from . import views

urlpatterns = [
    # templates
    path('', views.root),
    path('quotes', views.quotes),
    path('user/<int:id>', views.displayUser),
    path('edit', views.edit),

    # forms
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('addQuote', views.addQuote),
    path('like/<int:id>', views.like),
    path('editAccount', views.editAccount),
    path('delete/<int:id>', views.delete),
]