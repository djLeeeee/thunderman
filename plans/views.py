from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Plan
from .forms import PlanForm
from datetime import date, timedelta

# Create your views here.

@require_safe
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


def plan_date(request, month, day):
    plandate = date(2022, month, day)
    plans = Plan.objects.filter(date=plandate)
    context = {
        "plans": plans
    }
    return render(request, 'plans/plan_date.html', context)


def plan_detail(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    context = {
        'plan' : plan,
    }
    return render(request, 'plans/plan_detail.html', context)

# @login_required
@require_http_methods(['GET', 'POST'])
def plan_create(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect("plans:index")
    else:
        form = PlanForm()
    context = {
        'form': form
    }
    return render(request, 'plans/plan_create.html', context)

# @login_required
@require_http_methods(['GET', 'POST'])
def plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if plan.user == request.user:
        if request.method == 'POST':
            form = PlanForm(request.POST, instance=plan)
            if form.is_valid():
                plan = form.save()
                return redirect('plans:index')
        else:
            form = PlanForm(instance=plan)
    else:
        return redirect('plans:index')
    context = {
        'plan': plan,
        'form': form,
    }
    return render(request, 'plans/plan_update.html', context)
