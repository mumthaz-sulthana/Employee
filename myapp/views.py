from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Employee,Work
from myapp.forms import WorkForm

# Create your views here.

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"employee_list.html",{"employee":qs})
    
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"employee-create.html")
    def post(self,request,*args,**kwargs):
        name_box_value=request.POST.get("nameBox")
        age_box_value=request.POST.get("ageBox")
        designation_box_value=request.POST.get("designationBox")
        salary_box_value=request.POST.get("salaryBox")
        email_box_value=request.POST.get("emailBox")
        phone_box_value=request.POST.get("phoneBox")
        place_box_value=request.POST.get("placeBox")
        Employee.objects.create(
            name=name_box_value,
            age=age_box_value,
            designation=designation_box_value,
            salary=salary_box_value,
            email=email_box_value,
            phone=phone_box_value,
            place=place_box_value
        )
        #return render(request,"employee-create.html")
        return redirect("emp-list")
        
        
        
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"employee_detail.html",{"employee":qs})
    
    
class WorkCreateView(View):
    
    def get(self,request,*args,**kwargs):
        
        form_instance=WorkForm()
        
        return render(request,"work_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=WorkForm(request.POST)
    
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            Work.objects.create(**data)
            
            return redirect("work-all")
            
        return render(request,"work_add.html")
    
class WorkListView(View):
    
    def get(self,request,*args,**kwargs):
        
        qs=Work.objects.all()
        
        return render(request,"work_list.html",{"works":qs})

class WorkUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        work_object=Work.objects.get(id=id)
        
        data={
            "title":work_object.title,
            "description":work_object.description,
            "start_date":work_object.start_date,
            "end_date":work_object.end_date,
            "status":work_object.status
        }
        
        form_instance=WorkForm(initial=data)
        
        
        return render(request,"work_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        form_instance=WorkForm(request.POST)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            Work.objects.filter(id=id).update(**data)
            
            return redirect("work-all")
        
        else:
            
            return render(request,"work_edit.html",{"form":form_instance})
        
class WorkDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Work.objects.get(id=id).delete()
        
        return redirect("work-all")
            
            
        
        
            
            
        
    
        


