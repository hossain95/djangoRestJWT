from django.urls import path
from .import views

from .views import SubjectView, SemesterView, StudentView, TeacherView, StudentDetailView

urlpatterns = [
    path('subjects/', views.SubjectView.as_view(), name="subjects"),
    path('semesters/', views.SemesterView.as_view(), name="semesters"),
    path('students/', views.StudentView.as_view(), name="students"),
    path('student/detail/<int:pk>/', views.StudentDetailView.as_view(), name="student-detail"),

    path('teachers/', views.TeacherView.as_view(), name="teachers"),

]