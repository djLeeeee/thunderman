from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from datetime import date


@require_http_methods(["POST", "GET"])
def signup(request):
    error_dict = {}
    if request.user.is_authenticated:
        return redirect("plans:index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("plans:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
        'error_dict': error_dict,
    }
    return render(request, "accounts/signup.html", context)


@require_http_methods(['POST', 'GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('plans:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'plans:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('plans:index')


def my_page(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    today = date.today()
    coming_plans = person.join_plans.filter(date__gte=today)
    passed_plans = person.join_plans.filter(date__lt=today)
    context = {
        'person': person,
        'coming_plans': coming_plans,
        'passed_plans': passed_plans,
    }
    return render(request, 'accounts/my_page.html', context)