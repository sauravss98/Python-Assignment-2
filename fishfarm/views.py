import os

from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect
from .forms import DamForm,  FishForm, DepartmentForm,StaffForm
from .models import ManageDam, ManageFish, ManageDepartment,ManageStaff


# Create your views here.
def DashboardView(request):
    dams = ManageDam.objects.all()
    return render(request, 'dashboard.html', {"dams": dams})


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


# staff
def StaffAdd(request):
    if request.method=="POST":
        form=ManageStaff()
        form.staffid=request.POST.get('staffid')
        form.staffname=request.POST.get('staffname')
        form.staffEmail=request.POST.get('staffEmail')

        if len(request.FILES)!=0:
            form.staffImage=request.FILES['staffImage']

        form.save()
        messages.success(request,"data added")
        return redirect('/staffshow')

    return render(request,'fishfarm/staffadd.html')


def StaffView(request):
    staffs = ManageStaff.objects.all()
    return render(request, "fishfarm/staffshow.html", {"staffs": staffs})


def EditViewStaff(request, pk):
    staff = ManageStaff.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(staff.staffImage) > 0:
                os.remove(staff.staffImage.path)
                staff.staffImage = request.FILES['staffImage']
                staff.staffid = request.POST.get('staffid')
                staff.staffname = request.POST.get('staffname')
                staff.staffEmail = request.POST.get('staffEmail')
                staff.save()
        messages.success(request,"Staff section updated successfully")
        return redirect('/staffshow')
    else:
        return render(request, "fishfarm/staffedit.html", {"staff": staff})


'''
def UpdateViewStaff(request, id):
    staff = ManageStaff.objects.get(id=id)
    form = StaffForm(request.POST, instance=staff)
    if form.is_valid():
        form.save()
        return redirect("/staffshow")
    return render(request, "fishfarm/staffedit.html", {"staff": staff})
    '''



def DestroyViewStaff(request, pk):
    staff = ManageStaff.objects.get(id=pk)
    if len(staff.staffImage) > 0:
        os.remove(staff.staffImage.path)
    staff.delete()
    messages.success(request,"Staff deleted")
    return redirect("/staffshow")


# Fish
def FishAdd(request):
    if request.method == "POST":
        form = FishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/fishshow")
    else:
        form = FishForm()
    return render(request, "fishfarm/fishadd.html", {"form": form})


def ViewFish(request):
    fishs = ManageFish.objects.all()
    return render(request, "fishfarm/fishshow.html", {"fishs": fishs})


def EditViewFish(request, id):
    fish = ManageFish.objects.get(id=id)
    return render(request, "fishfarm/fishedit.html", {"fish": fish})


def UpdateViewFish(request, id):
    fish = ManageFish.objects.get(id=id)
    form = FishForm(request.POST, instance=fish)
    if form.is_valid():
        form.save()
        return redirect("/fishshow")
    return render(request, "fishfarm/fishedit.html", {"fish": fish})


def DestroyViewFish(request, id):
    dam = ManageFish.objects.get(id=id)
    dam.delete()
    return redirect("/fishshow")


# Department
def DepartmentAdd(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/departmentshow")
    else:
        form = DepartmentForm()
    return render(request, "fishfarm/departmentadd.html", {"form": form})


def ViewDepartment(request):
    departments = ManageDepartment.objects.all()
    return render(request, "fishfarm/departmentshow.html", {"departments": departments})


def EditViewDepartment(request, id):
    department = ManageDepartment.objects.get(id=id)
    return render(request, "fishfarm/departmentedit.html", {"department": department})


def UpdateViewDepartment(request, id):
    department = ManageDepartment.objects.get(id=id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect("/departmentshow")
    return render(request, "fishfarm/departmentedit.html", {"department": department})


def DestroyViewDepartment(request, id):
    department = ManageDepartment.objects.get(id=id)
    department.delete()
    return redirect("/departmentshow")
