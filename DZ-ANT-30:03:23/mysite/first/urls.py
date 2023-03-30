from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='index'),
    path('add', views.add, name='index'),
    path('students/<int:id>', views.show, name='students_show'),
]
