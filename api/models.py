from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Employee(models.Model):
    
    name=models.CharField(max_length=200)
    
    age=models.PositiveIntegerField()
    
    designation=models.CharField(max_length=200)
    
    salary=models.PositiveIntegerField()
    
    email=models.EmailField()
    
    phone=models.PositiveBigIntegerField()
    
    place=models.CharField(max_length=200)
    
    def __str__(self):
        
        return self.name
    
    
    @property    
    def task(self):
        
        return Task.objects.filter(emp_object=self)
    
    
class Task(models.Model):
    
    emp_object=models.ForeignKey(Employee,on_delete=models.CASCADE)
    
    task_name=models.CharField(max_length=200)
    
    user=models.CharField(max_length=200)
    
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    