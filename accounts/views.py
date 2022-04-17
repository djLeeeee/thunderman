from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login


@require_http_methods(["POST", "GET"])
def signup(request):
    if request.user.is_authenticated:
        return redirect("plans:index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 나중에 login 기능 구현하고 나서, 붙이면 된다.
            auth_login(request, user)
            return redirect("plans:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


# Create your views here.
