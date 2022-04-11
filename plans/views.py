from django.shortcuts import render, redirect
from .models import Plan
from .forms import PlanForm


# Create your views here.

def index(request):
    return render(request, 'plans/index.html')


def plan_date(request):
    return render(request, 'plans/plan_date.html')


def plan_detail(request):
    return render(request, 'plans/plan_detail.html')


def plan_create(request):
    form = PlanForm()
    context = {
        'form': form
    }
    return render(request, 'plans/plan_create.html', context)
