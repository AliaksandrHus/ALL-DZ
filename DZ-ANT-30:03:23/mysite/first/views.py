from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Students


def index(request):
    template = 'main.html'
    return TemplateResponse(request, template)


def students(request):
    all_s = Students.objects.all()

    if all_s:
        template = 'students.html'
        return render(request, template, {"all_s": all_s})

    else:
        template = 'empty.html'
        return render(request, template, {"all_s": all_s})


def add(request):

    if request.method == "POST":
        if len(request.POST) == 5:

            person = Students()
            person.name = request.POST.get("name")
            person.sex = request.POST.get("sex")
            person.group_id = request.POST.get("group_id")
            person.description = request.POST.get("description")
            person.save()

            template = 'add_fin.html'
            return TemplateResponse(request, template)

        else:
            template = 'add_error.html'
            return TemplateResponse(request, template)

    template = 'add.html'
    return TemplateResponse(request, template)


def show(request, id):
    template = 'show.html'
    all_s = Students.objects.get(id=id)
    return render(request, template, {"all_s": all_s})
