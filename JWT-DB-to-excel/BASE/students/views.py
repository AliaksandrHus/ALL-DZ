from .serializers import StudentsDetailSerializer, StudentsListSerializer, GropDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import FileResponse
import pandas

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Student, Group
from .group_members import members_in_group


@api_view()
def menu(request):

    return Response({"СТУДЕНТЫ": "",
                     "Все студенты": "http://127.0.0.1:8000/api/v1/students/",
                     "Добавить студента": "http://127.0.0.1:8000/api/v1/students/create/",
                     "Скачать базу студентов": "http://127.0.0.1:8000/api/v1/students-download/",
                     "ГРУППЫ": "",
                     "Все группы": "http://127.0.0.1:8000/api/v1/group/",
                     "Добавить группу": "http://127.0.0.1:8000/api/v1/group/create/",
                     "Скачать базу учебных групп": "http://127.0.0.1:8000/api/v1/group-download/",
                     "ВХОД": "",
                     "Войти": "http://127.0.0.1:8000/api/v1/user/login/?next=/api/v1/",
                     "Регистрация": "http://127.0.0.1:8000/api/v1/auth/users/",
                     "JWT ТОКЕНЫ": "",
                     "Получить токены": "http://127.0.0.1:8000/api/token/",
                     "Обновить токены": "http://127.0.0.1:8000/api/token/refresh/",

                     })


# - Students view

class StudentsCreateView(generics.CreateAPIView):

    serializer_class = StudentsDetailSerializer
    permission_classes = (IsAuthenticated, )


class StudentsListView(generics.ListAPIView):

    serializer_class = StudentsListSerializer
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated, )


class StudentsDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = StudentsDetailSerializer
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated, )


# - Grop view

class GropCreateView(generics.CreateAPIView):

    serializer_class = GropDetailSerializer
    permission_classes = (IsAuthenticated, )


class GropDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = GropDetailSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated, )


@api_view()
@permission_classes([IsAuthenticated])
def group_list(request):

    group_query = members_in_group()
    return Response(group_query)


# - Download

@api_view()
@permission_classes([IsAuthenticated])
def students_to_exsel(request):

    all_student = Student.objects.all()

    db_dict = {'id': {}, 'name': {}, 'age': {}, 'sex': {}, 'in_group': {}}

    for num, person in enumerate(all_student, start=1):
        db_dict['id'][num] = person.id                              # обращаемся к атрибуту объекта = person.id
        db_dict['name'][num] = person.name                          #
        db_dict['age'][num] = person.age                            #
        db_dict['sex'][num] = 'Ж' if person.sex == 1 else 'М'       #
        db_dict['in_group'][num] = person.in_group                  #

    data = pandas.DataFrame(db_dict)
    data.to_excel('output/student.xlsx', index=False)

    response = FileResponse(open('output/student.xlsx', "rb"))
    return response


@api_view()
@permission_classes([IsAuthenticated])
def group_to_exsel(request):

    group_query = members_in_group()

    db_dict = {'id': {}, 'group_num': {}, 'description': {}, 'members': {}}

    for num, group in enumerate(group_query, start=1):

        db_dict['id'][num] = group['id']                            # обращаемся к ключу в словаре = group['id']
        db_dict['group_num'][num] = group['group_num']              #
        db_dict['description'][num] = group['description']          #
        db_dict['members'][num] = ', '.join(group['members'])       #

    data = pandas.DataFrame(db_dict)
    data.to_excel('output/group.xlsx', index=False)

    response = FileResponse(open('output/group.xlsx', "rb"))
    return response


