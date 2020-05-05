from django.urls import path
from . import views

urlpatterns = [
# templates
    path('', views.root),
    path('success', views.success),

# forms
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]