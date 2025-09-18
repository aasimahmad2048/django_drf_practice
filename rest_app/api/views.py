from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from employees.models import Employee
from students.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import  Response
from rest_framework import  status
from rest_framework import  mixins,generics ,viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from django.http import Http404
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
# # Create your views here.
# def studentsView(request):
#     # students={
#     #     'id':1,
#     #     "name":'aasim',
#     #     "class":"cs"
#     # }

#     students= Student.objects.all()
#     print(students)
#     students_list=list(students.values())
#     return JsonResponse(students_list,safe=False)
# @api_view(('GET','POST'))
# def studentsView(request):
#     if request.method=="GET":
#         #get all the data from student table
#         students=Student.objects.all()
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method=="POST":
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','delete'])
# def studentDetailView(request,pk):
#     try:
#         student=Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=="GET":
#         serializer=StudentSerializer(student)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method=='PUT':
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else :
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



# class Employees(APIView):
#     def get(self,request):
#         employees=Employee.objects.all()
#         serilizer=EmployeeSerializer(employees,many=True)
#         return Response(serilizer.data,status=status.HTTP_200_OK)

      

#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else :
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class EmployeeDetail(APIView):
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serilizer=EmployeeSerializer(employee)
#         return Response(serilizer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#          employee=self.get_object(pk)
#          employee.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)


#     def get_object(self,pk):
#         try:
#             employees=Employee.objects.get(pk=pk)
#             return employees
#         except:
#             Employee.DoesNotExist
#             raise Http404
        
"""
 #mixin    
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,  generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
 
        
    
class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
     
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)   

    def put(self, request, pk):
        return self.update(request, pk) 


    def delete(self, request, pk):
        ret urn self.destroy(request, pk)
"""


# class Employees(generics.ListAPIView, generics.CreateAPIView):
'''
class Employees( generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


class EmployeeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'
    
'''


'''
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self, request,pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer   # <-- add this


class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer