from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username").lower()
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form":form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect("/")

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect("/account/login")
    context = {
        "form":form,
    }
    return render(request, "register.html", context)