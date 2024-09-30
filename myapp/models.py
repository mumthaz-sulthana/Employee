from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    designation=models.CharField(max_length=30)
    salary=models.PositiveBigIntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    place=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.name
    
    
    

# Create your models here.



class Work(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    status_options=(
        ("created","created"),
        ("wip","wip"),
        ("completed","completed"),
        ("due","due")
    )
    status=models.CharField(max_length=30,choices=status_options,default="created")
    
    def __str__(self):
        return self.title