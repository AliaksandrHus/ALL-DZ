from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'rest'

urlpatterns = [

    path('students/create/', StudentsCreateView.as_view()),
    path('students/', StudentsListView.as_view()),
    path('students/detail/<int:pk>/', StudentsDetailView.as_view()),

    path('grop/create/', GropCreateView.as_view()),
    path('grop/', GropListView.as_view()),
    path('grop/detail/<int:pk>/', GropDetailView.as_view()),

]
