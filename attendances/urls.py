from django.urls import path

from .views import AttendanceList, AttendanceDetail
# from .views import AttendanceViewSet


urlpatterns = [
    path('attendances/<int:pk>/', AttendanceDetail.as_view()),
    path('attendances/', AttendanceList.as_view()),
]
