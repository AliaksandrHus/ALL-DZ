from rest_framework import serializers
from .models import Student, Group


# - Students Serializer

class StudentsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class StudentsListSerializer(serializers.ModelSerializer):

    student_in_grop = serializers.CharField(source='group.grop_num')

    class Meta:
        model = Student
        fields = ('name', 'age', 'student_in_grop')


# - Grop Serializer

class GropDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GropListSerializer(serializers.ModelSerializer):

    students = serializers.CharField(source='student_set.all')

    class Meta:
        model = Group
        fields = ('grop_num', 'description', 'students')
        depth = 1

