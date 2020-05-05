from django.urls import path
from . import views

urlpatterns = [
    #templates
    path('', views.root, name='root'),
    path('shows', views.shows, name='show'),
    path('shows/new', views.new, name='new'),
    path('shows/<int:id>', views.displayShow, name='display'),
    path('shows/<int:id>/edit', views.edit, name='edit'),

    #forms
    path('add', views.add, name='add'),
    path('edit', views.editShow, name='editShow'),
    path('shows/<int:id>/delete', views.delete, name='delete'),
]