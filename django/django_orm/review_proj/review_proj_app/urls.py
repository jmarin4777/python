from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('homepage', views.homepage),
    path('profile', views.userProfile),
    path('cat/<int:id>', views.catProfile),

    path('users', views.createUser),
    path('login', views.login),
    path('cats', views.createCat),
    path('deleteCat/<int:id>', views.deleteCat),
    path('voteCat/<int:id>', views.voteCat),
    path('logout', views.logout),
]