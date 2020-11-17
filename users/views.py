from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')


class UserLoginView(LoginRequiredMixin, View):
    pass


class UserRegister(View):
    pass
