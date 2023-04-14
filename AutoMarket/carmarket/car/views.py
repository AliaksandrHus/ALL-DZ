from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cars

import re


def index(request):

    data = {'title': 'Главная'}
    return render(request, 'main/index.html', data)


def car_list(request):

    car = Cars.objects.all()
    data = {'title': 'Каталог автомобилей', 'car': car}
    return render(request, 'main/car_list.html', data)


class NewsDetailView(DetailView):
    model = Cars
    template_name = 'main/car_view.html'
    context_object_name = 'car'


def contacts(request):

    data = {'title': 'Контакты'}
    return render(request, 'main/contacts.html', data)
