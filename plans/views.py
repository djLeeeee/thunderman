from django.shortcuts import render, redirect
from .models import Plan
from .forms import PlanForm
from datetime import date, timedelta

# Create your views here.

def index(request):
    # 30일 간격 조회
    startdate = date.today()
    interval = 30
    enddate = startdate + timedelta(days=interval)

    dates = Plan.objects.filter(date__range=[startdate, enddate]).values_list('date', flat=True).order_by('date')
    plan_cnt = {}

    for plandate in dates:
        if plandate not in plan_cnt:
            plan_cnt[plandate] = 1
        else:
            plan_cnt[plandate] += 1

    context = {
        "plan_cnt": plan_cnt,
    }
    return render(request, 'plans/index.html', context)


def plan_date(request):
    return render(request, 'plans/plan_date.html')


def plan_detail(request):
    return render(request, 'plans/plan_detail.html')


def plan_create(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plans:index")
    else:
        form = PlanForm()
    context = {
        'form': form
    }
    return render(request, 'plans/plan_create.html', context)
