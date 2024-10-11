from django.contrib import admin
from application1.models import stumodel
from django.urls import path
from application1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('addrec/',views.addrec,name='addrec'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('update/uprec/<int:id>/',views.uprec,name='uprec'),
    
]