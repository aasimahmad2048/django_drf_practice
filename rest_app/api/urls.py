from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from api import views

router=DefaultRouter()
router.register('employees',views.EmployeeViewSet, basename='employee')




urlpatterns = [
    # path("students/",views.studentsView), 
    # path("student/<int:pk>",views.studentDetailView),
    # path("employees/",views.Employees.as_view()),
    # path("employees/<int:pk>/",views.EmployeeDetail.as_view()),


     
    # path("employees_mixins/",views.Employees.as_view()),
    # path("employees_mixins/<int:pk>/",views.EmployeeDetail.as_view()),
    

    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view())

    
]

