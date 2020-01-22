from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


from .views import *

urlpatterns = [
    path('classrooms/list/', ClassroomListAPIView.as_view(), name='api-classroom-list'),
    path('classrooms/detail/<int:classroom_id>/', ClassroomDetailAPIView.as_view(), name='api-classroom-detail'),
    path('classrooms/create/', ClassroomCreateAPIView.as_view(), name='api-classroom-create'),
    path('classrooms/update/<int:classroom_id>/', ClassroomUpdateView.as_view(), name='api-classroom-update'),
    path('classrooms/delete/<int:classroom_id>/', ClassroomDeleteView.as_view(), name='api-classroom-delete'),

    path('students/create/', StudentCreateAPIView.as_view(), name='api-student-create'),
    path('students/update/<int:student_id>/', StudentUpdateView.as_view(), name='api-student-update'),
    path('students/delete/<int:student_id>/', StudentDeleteView.as_view(), name='api-student-delete'),

    path('user/login/', TokenObtainPairView.as_view(), name="api-login"),
    path('user/register/', UserCreateAPIView.as_view(), name="api-register"),

]