from datetime import date
from multiprocessing import context
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'plans/index.html')


def plan_date(request):
    return


def plan_detail(request):
    return


def plan_create(request):
    return
