from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from classes.models import Classroom
from .serializer import *
# Create your views here.

class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassSerializer

class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class DeleteClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class CreateClassroom(CreateAPIView):
	serializer_class = UpdateClassSerializer
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)