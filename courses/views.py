from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Course,Category,Enrollment
def course_list(request):
    qs=Course.objects.filter(is_published=True).select_related('category')
    age=request.GET.get('age'); level=request.GET.get('level'); cat=request.GET.get('category'); q=request.GET.get('q')
    if age and age.isdigit(): qs=qs.filter(age_min__lte=int(age),age_max__gte=int(age))
    if level: qs=qs.filter(level=level)
    if cat and cat.isdigit(): qs=qs.filter(category_id=cat)
    if q: qs=qs.filter(Q(title__icontains=q)|Q(summary__icontains=q))
    return render(request,'courses/course_list.html',{'courses':qs,'categories':Category.objects.all(),'selected_age':age,'selected_level':level})
def course_detail(request,slug): return render(request,'courses/course_detail.html',{'course':get_object_or_404(Course,is_published=True,slug=slug)})
@login_required
def enroll(request,slug):
    course=get_object_or_404(Course,slug=slug,is_published=True)
    if request.method=='POST':
        Enrollment.objects.get_or_create(student=request.user,course=course)
        messages.success(request,'درخواست ثبت‌نام شما دریافت شد.')
    return redirect('courses:detail',slug=slug)
