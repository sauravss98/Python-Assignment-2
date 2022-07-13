from django.shortcuts import render, redirect
from .forms import DamForm
from .models import ManageDam

# Create your views here.
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
