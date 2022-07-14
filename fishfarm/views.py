from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect
from .forms import DamForm,StaffForm
from .models import ManageDam,ManageStaff

# Create your views here.
def DashboardView(request):
    dams = ManageDam.objects.all()
    return render(request,'dashboard.html', {"dams":dams})

def DamView(request):
    if request.method == "POST":
        form = DamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/damentry")
    else:
            form = DamForm()
    return render(request, "fishfarm/damindex.html", {"form": form})


def ShowViewDam(request):
    dams = ManageDam.objects.all()
    return render(request, "fishfarm/damshow.html", {"dams": dams})


def EditViewDam(request, id):
    dam = ManageDam.objects.get(id=id)
    return render(request, "fishfarm/damedit.html", {"dam": dam})


def UpdateViewDam(request, id):
    dam = ManageDam.objects.get(id=id)
    form = DamForm(request.POST, instance=dam)
    if form.is_valid():
        form.save()
        return redirect("/damentry")
    return render(request, "fishfarm/damedit.html", {"dam": dam})


def DestroyViewDam(request, id):
    dam = ManageDam.objects.get(id=id)
    dam.delete()
    return redirect("/damentry")

def StaffAdd(request):
    if request.method == "POST":
        form = StaffForm()
        form.staffid=request.POST.get('staffid')
        form.staffname=request.POST.get('staffname')
        form.staffEmail=request.POST.get('staffEmail')
        if len(request.FILES)!=0:
            form.staffImage=request.FILES['staffImage']
        form.save()
        messages.success(request,"Details added succesfully")
        return redirect("/staffshow")
    return redirect(request,'fishfarm/staffadd.html')

def StaffView():
    staffs = ManageStaff.objects.all()
    return render(request,"fishfarm/staffshow.html",{"staffs":staffs})

def EditViewStaff(request, id):
    staff = ManageStaff.objects.get(id=id)
    return render(request, "fishfarm/staffedit.html", {"staff": staff})

def UpdateViewStaff(request, id):
    staff = ManageStaff.objects.get(id=id)
    form = StaffForm(request.POST, instance=staff)
    if form.is_valid():
        form.save()
        return redirect("/staffshow")
    return render(request, "fishfarm/staffedit.html", {"staff": staff})


def DestroyViewStaff(request, id):
    dam = ManageStaff.objects.get(id=id)
    dam.delete()
    return redirect("/staffshow")