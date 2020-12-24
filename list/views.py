from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import mylist
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import *



# Create your views here.
@csrf_exempt
def index(request):
    totaldata=mylist.objects.all()[3:]
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            #Adds logged in username to specific object
            lastobjid=max([i.id for i in totaldata])
            obj=mylist.objects.get(id=lastobjid)
            obj.username33=str(request.user)
            obj.save()
    loginusername=str(request.user)
    theuserdata=mylist.objects.filter(username33=str(request.user))
    context = {"form": form, "names": theuserdata, "loginuser2": loginusername}
    return render(request, 'index.html', context)

def delete(request, pk):
    mylist.objects.get(id=pk).delete()
    return redirect('/')

def delete_all(request):
    total=mylist.objects.all()[3:]
    for i in total:
        mylist.objects.get(id=i.id).delete()
    return redirect('/')


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form=RegisterForm()
    context={"register":form}
    return render(request, 'registration/register.html', context)

def created_account(request):
    return render(request, 'registration/createdaccount.html')
