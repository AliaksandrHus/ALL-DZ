from django.contrib import admin
from django.urls import path
from .views import *
from . import views


app_name = 'rest'

urlpatterns = [

    path('', views.menu),

    path('students/create/', StudentsCreateView.as_view()),
    path('students/', StudentsListView.as_view()),
    path('students/detail/<int:pk>/', StudentsDetailView.as_view()),

    path('group/create/', GropCreateView.as_view()),
    path('group/', views.group_list),
    path('group/detail/<int:pk>/', GropDetailView.as_view()),

    path('students-download/', views.students_to_exsel),
    path('group-download/', views.group_to_exsel),

]
