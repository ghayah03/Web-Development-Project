from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='exam_index'),
    path('list/', views.list_books, name='exam_list'),
    path('add/', views.add_book, name='exam_add'),
    path('<int:book_id>/', views.view_book, name='exam_view'),
    path('search/', views.search_books, name='exam_search'),
]