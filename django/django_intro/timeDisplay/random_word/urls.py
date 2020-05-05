from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('random_word', views.random_word),
    path('reset', views.reset),
]
