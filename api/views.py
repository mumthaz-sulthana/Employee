from django.shortcuts import render

from api.models import Employee

from rest_framework.views import APIView

from rest_framework.response import Response

from api.serializer import EmployeeSerializer,TaskSerializer

from rest_framework import viewsets

from rest_framework.decorators import action

# Create your views here.

class EmployeeListCreateView(APIView):
    
    def get(self,request,*args,**kwargs):
        
        qs=Employee.objects.all()
        
        serializer_instance=EmployeeSerializer(qs,many=True)
        
        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):
        
        serializer_instance=EmployeeSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
    
class EmployeeRetrieveUpdateDestroyView(APIView):
    
    def get(self,request,*args,**kwargs):
        
      id=kwargs.get("pk")
      
      qs=Employee.objects.get(id=id)
      
      serializer_instance=EmployeeSerializer(qs)
      
      return Response(data=serializer_instance.data)
      

    def put(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        emp_obj=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(data=request.data,instance=emp_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()
        
        data={"message":"Employee deleted"}
        
        return Response(data=data)


class EmployeeViewSetView(viewsets.ViewSet):
    
    def list(self,request,*args,**kwargs):
        
        qs=Employee.objects.all()
        
        serializer_instance=EmployeeSerializer(qs,many=True)
        
        return Response(data=serializer_instance.data)
    
    def create(self,request,*args,**kwargs):
        
        serializer_instance=EmployeeSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
    def retrieve(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(qs)
        
        return Response(data=serializer_instance.data)
    
    
    def update(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        emp_obj=Employee.objects.get(id=id)
        
        serializer_instance=EmployeeSerializer(data=request.data,instance=emp_obj)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
        
    def destroy(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()
        
        data={"message":"deleted"}
        
        return Response(data=data)

        
    @action(methods=["POST"],detail=True)
    def employee_task(self,request,*args,**kwargs):
        
        employee_id=kwargs.get("pk")
        
        employee_object=Employee.objects.get(id=employee_id)
        
        serializer_instance=TaskSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save(emp_object=employee_object)
            
            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
        
        
        

    
    
            
            
        
        
        
        