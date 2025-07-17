from django.urls import path

from api import views

urlpatterns = [
    path("students/",views.studentsView),
    path("student/<int:pk>",views.studentDetailView),
    path("employees/",views.Employees.as_view()),
    path("employees/<int:pk>/",views.EmployeeDetail.as_view()),
]