from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("v2/Employees",views.EmployeeViewSetView,basename="Employees")

urlpatterns=[
    
    path('Employees/',views.EmployeeListCreateView.as_view()),
    path('Employees/<int:pk>/',views.EmployeeRetrieveUpdateDestroyView.as_view()),
    
]+router.urls