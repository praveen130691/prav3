from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Praveen
def home(request):
    return render(request, "home.html")
def sanjeev(request):
    return render(request, "registration.html")
def regi(request):
    if request.method == "POST":
        name1 = request.POST["t1"]
        pwd1 = request.POST["t2"]
        mobno1 = request.POST["t3"]
        p1 = Praveen(user=name1, pwd=pwd1, mob=mobno1)
        p1.save()
        return redirect(home)
def saroja(request):
    return render(request, "login.html")


def login(request):
    if request.method == "POST":
        un = request.POST["t1"]
        pwd1 = request.POST["t2"]
        dbuser = Praveen.objects.filter(user=un, pwd=pwd1)
        if not dbuser:
            return HttpResponse("plz enter correct details")
        else:
            return redirect(input)


def input(request):
    return render(request, "main.html")


def grand(request):
    return render(request, "grand.html")


def gra1(request):
    return redirect(input)


def edu(request):
    return render(request, "educatin.html")


def psn(request):
    return redirect(input)


def sibling(request):
    return render(request, "siblin.html")


def naveen(request):
    return redirect(input)


def parent(request):
    return render(request, "parent.html")


def praveen(request):
    return redirect(input)


def nick(request):
    return render(request, "nickname.html")


def apple(request):
    return redirect(input)

