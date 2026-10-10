from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('book/<int:bookid>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    
    path('html5/links/', views.html_links, name="books.html_links"),
    path('html5/text/formatting/', views.html_formatting, name="books.html_formatting"),
    path('html5/listing/', views.html_listing, name="books.html_listing"),
    path('html5/tables/', views.html_tables, name="books.html_tables"),
    path('search/', views.search, name="books.search"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('lab8/task1/', views.lab8_task1, name="books.lab8_task1"),
    path('lab8/task2/', views.lab8_task2, name="books.lab8_task2"),
    path('lab8/task3/', views.lab8_task3, name="books.lab8_task3"),
    path('lab8/task4/', views.lab8_task4, name="books.lab8_task4"),
    path('lab8/task5/', views.lab8_task5, name="books.lab8_task5"),
    path('lab8/task7/', views.lab8_task7, name="books.lab8_task7"),
    path('lab9/task1/', views.lab9_task1, name="books.lab9_task1"),
    path('lab9/task2/', views.lab9_task2, name="books.lab9_task2"),
    path('lab9/task3/', views.lab9_task3, name="books.lab9_task3"),
    path('lab9/task4/', views.lab9_task4, name="books.lab9_task4"),
    path('lab10_part1/listbooks/', views.lab10_part1_listbooks, name="books.lab10_part1_listbooks"),
    path('lab10_part1/addbook/', views.lab10_part1_addbook, name="books.lab10_part1_addbook"),
    path('lab10_part1/editbook/<int:book_id>/', views.lab10_part1_editbook, name="books.lab10_part1_editbook"),
    path('lab10_part1/deletebook/<int:book_id>/', views.lab10_part1_deletebook, name="books.lab10_part1_deletebook"),
   
    path('students/', views.student_list, name="student_list"),
    path('students/add/', views.student_add, name="student_add"),
    path('students/edit/<int:student_id>/', views.student_edit, name="student_edit"),
    path('students/delete/<int:student_id>/', views.student_delete, name="student_delete"),
  
    path('student2/list/', views.student2_list, name="student2_list"),
    path('student2/add/', views.student2_add, name="student2_add"),
    path('student2/edit/<int:student_id>/', views.student2_edit, name="student2_edit"),
    path('student2/delete/<int:student_id>/', views.student2_delete, name="student2_delete"),
   
    path('student3/list/', views.student3_list, name="student3_list"),
    path('student3/add/', views.student3_add, name="student3_add"),
    path('student3/edit/<int:student_id>/', views.student3_edit, name="student3_edit"),
    path('student3/delete/<int:student_id>/', views.student3_delete, name="student3_delete"),
    
    path('profile/list/', views.profile_list, name="profile_list"),
    path('profile/add/', views.profile_add, name="profile_add"),
    path('profile/edit/<int:profile_id>/', views.profile_edit, name="profile_edit"),
    path('profile/delete/<int:profile_id>/', views.profile_delete, name="profile_delete"),
    
    path('lab13/task1/', views.lab13_task1, name="books.lab13_task1"),
    path('lab13/task2/', views.lab13_task2, name="books.lab13_task2"),
    path('lab13/task3/', views.lab13_task3, name="books.lab13_task3"),
    path('lab13/task4/', views.lab13_task4, name="books.lab13_task4"),
    path('lab13/task5/', views.lab13_task5, name="books.lab13_task5"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)