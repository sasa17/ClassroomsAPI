from rest_framework import serializers
from classes.models import Classroom, Student
from django.contrib.auth.models import User

class ClassroomListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'grade']


class ClassroomDetailSerializer(serializers.ModelSerializer):
	students = serializers.SerializerMethodField()
	class Meta:
		model = Classroom
		fields = ['subject', 'grade', 'year', 'teacher', 'students']

	def get_students(self, obj):
		return StudentUpdateSerializer(obj.students.all(), many=True).data


class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'grade', 'year']


class StudentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"


class StudentUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		exclude = ['classroom']


class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data

