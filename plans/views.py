from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.db.models import Count
from .models import Plan, Comment
from .forms import PlanForm, CommentForm
from datetime import date, datetime, timedelta

# Create your views here.

@require_safe
def index(request):
    # 30일 간격 조회
    startdate = date.today()
    interval = 30
    enddate = startdate + timedelta(days=interval)
    plan_cnt = Plan.objects.filter(date__range=[startdate, enddate]).values('date').annotate(total=Count('date')).order_by('date')
    endtime = datetime.now()
    starttime = endtime - timedelta(hours=24)
    plan_new = Plan.objects.filter(created_at__range=[starttime, endtime]).values_list('date', flat=True)
    context = {
        "plan_cnt": plan_cnt,
        "plan_new": plan_new,
    }
    return render(request, 'plans/index.html', context)


def plan_coming(request):
    # 그 이후의 약속 조회
    startdate = date.today()
    interval = 30
    enddate = startdate + timedelta(days=interval)

    plan_cnt = Plan.objects.filter(date__gt=enddate).values('date').annotate(total=Count('date')).order_by('date')
    
    # new 만들려고 한 거니 그대로 가져오면 된다
    endtime = datetime.now()
    starttime = endtime - timedelta(hours=24)
    plan_new = Plan.objects.filter(created_at__range=[starttime, endtime]).values_list('date', flat=True)

    context = {
        "plan_cnt": plan_cnt,
        'plan_new': plan_new,
    }

    return render(request, 'plans/plan_coming.html', context)



def plan_date(request, month, day):
    plandate = date(2022, month, day)
    plans = Plan.objects.filter(date=plandate)
    context = {
        "plans": plans,
        "plandate": plandate,
    }
    return render(request, 'plans/plan_date.html', context)


def plan_detail(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    comment_form = CommentForm()
    comments = plan.comment_set.all()
    context = {
        'plan' : plan,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'plans/plan_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def plan_create(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            plan.join_users.add(request.user)
            return redirect('plans:plan_detail', plan.pk)
    else:
        form = PlanForm()
    context = {
        'form': form
    }
    return render(request, 'plans/plan_create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if plan.user == request.user:
        if request.method == 'POST':
            form = PlanForm(request.POST, instance=plan)
            if form.is_valid():
                plan = form.save()
                return redirect('plans:plan_detail', plan.pk)
        else:
            form = PlanForm(instance=plan)
    else:
        return redirect('plans:index')
    context = {
        'plan': plan,
        'form': form,
    }
    return render(request, 'plans/plan_update.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def comment_create(request, pk):
    if request.user.is_authenticated:
        plan = get_object_or_404(Plan, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.plan = plan
            comment.user = request.user
            comment.save()
        return redirect('plans:plan_detail', plan.pk)
    return redirect('accounts:login')


@require_POST
def comment_delete(request, plan_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('plans:plan_detail', plan_pk)


@require_POST
def join_users(request, plan_pk):
    if request.user.is_authenticated:
        plan = get_object_or_404(Plan, pk=plan_pk)
        if plan.join_users.filter(pk=request.user.pk).exists():
            plan.join_users.remove(request.user)
        else:
            plan.join_users.add(request.user)
        return redirect('plans:plan_detail', plan_pk)
    return redirect('accounts:login')

@require_POST
def plan_delete(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.user.is_authenticated:
        if request.user == plan.user:
            plan.delete()
    return redirect('plans:index')

