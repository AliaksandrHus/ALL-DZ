from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentsDetailSerializer, StudentsListSerializer, GropDetailSerializer, GropListSerializer
from .models import Student, Group


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


class GropListView(generics.ListAPIView):
    serializer_class = GropListSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated, )


class GropDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GropDetailSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated, )


