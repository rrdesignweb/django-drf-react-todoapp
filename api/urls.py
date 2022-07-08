from django.urls import path
from .views import TodosHandler, TodoHandler, index

urlpatterns = [
    path('', index),
    path('todos/', TodosHandler),
    path('todo/<int:pk>/', TodoHandler),
]