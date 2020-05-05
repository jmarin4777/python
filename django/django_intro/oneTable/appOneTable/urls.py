from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('addDungeon', views.addDungeon),
    path('addPrisoner', views.addPrisoner),
    path('delete/<int:i>', views.delete),
    path('dislike/<int:j>', views.dislike),
]