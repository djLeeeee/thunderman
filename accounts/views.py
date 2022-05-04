from distutils.log import error
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from datetime import date
from django.utils import timezone
from django.db.models import Q


@require_http_methods(["POST", "GET"])
def signup(request):
    errors = []
    if request.user.is_authenticated:
        return redirect("plans:index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("plans:index")
        else:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if get_user_model().objects.filter(username=username).exists():
                errors.append('중복된 아이디가 있습니다')
            
            elif password1 != password2:
                errors.append('비밀번호 확인이 틀렸습니다')
            
            elif len(password1) < 8:
                errors.append('8자 이상의 비밀번호를 입력해주세요')
            
            elif password1.isdigit() or password1.isalpha():
                errors.append('숫자와 문자를 함께 입력해주세요')
            
            else:
                errors.append('특수기호는 @ . + - _ 만 가능합니다')
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
        "errors": errors,
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
    nowtime = timezone.now()
    coming_plans = person.join_plans.filter(date__gte=today, time__gte=nowtime).order_by('date', 'time')
    passed_plans = person.join_plans.filter(Q(date__lt=today) |Q(date=today, time__lt=nowtime)).order_by('date')

    today_plans = coming_plans.filter(date = today)
    first_plan = ''
    if today_plans:
        first_plan = today_plans[0]
    context = {
        'person': person,
        'coming_plans': coming_plans,
        'passed_plans': passed_plans,
        'today_plans': today_plans,
        'first_plan': first_plan,
    }
    return render(request, 'accounts/my_page.html', context)