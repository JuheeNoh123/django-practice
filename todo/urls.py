from django.urls import path

from todo.views import index, todos

urlpatterns = [
	path('todo/', todos),
    path('index/', index),
]