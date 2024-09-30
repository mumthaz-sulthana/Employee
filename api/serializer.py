from rest_framework import serializers

from api.models import Employee ,Task


        
class TaskSerializer(serializers.ModelSerializer):
    
    emp_object=serializers.StringRelatedField()
    
    class Meta:
        
        model=Task
        
        fields="__all__"
        
        read_only_fields=["id","emp_object"]
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    
    task=TaskSerializer(read_only=True,many=True)
    
    class Meta:
        
        model=Employee
        
        fields=["id","name","age","designation","salary","email","phone","place","task"]
        