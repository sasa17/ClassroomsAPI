from rest_framework import serializers
from django.contrib.auth.models import User
from classes.models import Classroom

class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher']

class ClassDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class UpdateClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'
