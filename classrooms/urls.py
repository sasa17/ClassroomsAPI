
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('classrooms/', views.ClassroomList.as_view(), name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.ClassroomDetail.as_view(), name='classroom-detail'),

    path('classrooms/create/', views.CreateClassroom.as_view(), name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.UpdateClassroom.as_view(), name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.DeleteClassroom.as_view(), name='classroom-delete'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
