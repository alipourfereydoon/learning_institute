from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User

def register(request):
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip()
        password = request.POST.get('password') or ''
        password2 = request.POST.get('password2') or ''
        if not username:
            messages.error(request, 'نام کاربری را وارد کنید.')
        elif len(password) < 6:
            messages.error(request, 'رمز عبور باید حداقل ۶ کاراکتر باشد.')
        elif password != password2:
            messages.error(request, 'رمزها یکسان نیستند.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً ثبت شده است.')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=request.POST.get('role', 'student'),
            )
            login(request, user)  # ورود خودکار پس از ثبت‌نام
            messages.success(request, 'ثبت‌نام انجام شد! خوش آمدی 🎉')
            return redirect('accounts:dashboard')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        password = request.POST.get('password') or ''
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'خوش آمدی {user.username} 👋')
            return redirect('accounts:dashboard')
        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدی.')
    return redirect('core:home')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html',
                  {'enrollments': request.user.enrollments.select_related('course')})
