from django.shortcuts import render, redirect
from .models import Plan
from .forms import PlanForm
from django.views.decorators.http import require_http_methods

# Create your views here.


def index(request):
    return render(request, "plans/index.html")


def plan_date(request):
    return render(request, "plans/plan_date.html")


def plan_detail(request):
    return render(request, "plans/plan_detail.html")


@require_http_methods(["POST", "GET"])
def plan_create(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plans:index")
    else:
        form = PlanForm()
    context = {
        "form": form,
    }
    return render(request, "plans/plan_create.html", context)
