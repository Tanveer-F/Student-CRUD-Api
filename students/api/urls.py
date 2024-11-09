from django.urls import path, include
from students.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('crud', views.MyStudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
