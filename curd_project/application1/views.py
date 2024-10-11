from django.shortcuts import render,redirect
from application1.models import stumodel

def index(request):
  data=stumodel.objects.all()
  return render(request,'application1/index.html',{'data':data})


def add(request):
  return render(request,'application1/add.html')


def addrec(request):
  x=request.POST['first']
  y=request.POST['last']
  z=request.POST['country']
  data=stumodel(first_name=x,last_name=y,country=z)
  data.save()
  return redirect("index")

def delete(request,id):
  data=stumodel.objects.get(id=id)
  data.delete()
  return redirect("/")

def update(request,id):
  data=stumodel.objects.get(id=id)
  return render(request,'application1/update.html',{'data':data})

def uprec(request,id):
  x=request.POST['first']
  y=request.POST['last']
  z=request.POST['country']
  data=stumodel.objects.get(id=id)
  data.first_name=x
  data.last_name=y
  data.country=z
  data.save()
  return redirect("/")
 