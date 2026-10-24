from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course
from .models import SiteSetting

def home(request):
    courses = Course.objects.filter(is_published=True).select_related('category')[:6]
    return render(request,'core/index.html',{'courses':courses})
def about(request): return render(request,'core/about.html')
def contact(request):
    if request.method=='POST':
        messages.success(request,'درخواست شما ثبت شد؛ به‌زودی با شما تماس می‌گیریم.')
        return redirect('core:contact')
    return render(request,'core/contact.html')
def faq(request):
    items=[('برای شرکت در دوره‌ها چه پیش‌نیازی لازم است؟','بیشتر دوره‌های مقدماتی پیش‌نیاز ندارند؛ توضیحات هر دوره را ببینید.'),('آیا دوره‌ها حضوری هستند؟','دوره‌ها به‌صورت حضوری، آنلاین یا ترکیبی برگزار می‌شوند.'),('چطور مشاوره بگیرم؟','فرم مشاوره را پر کنید تا همکاران ما با شما تماس بگیرند.')]
    return render(request,'core/faq.html',{'faqs':items})
