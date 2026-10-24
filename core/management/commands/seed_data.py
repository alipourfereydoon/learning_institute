from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import SiteSetting
from courses.models import Category, Course
from lms.models import Lesson, Assignment, Quiz

COURSES = [
    dict(cat='برنامه‌نویسی', icon='🐍', title='پایتون مقدماتی برای نوجوانان', summary='اولین قدم برنامه‌نویسی با پایتون؛ از متغیرها تا ساخت بازی و پروژه‌های کوچک.', price=2400000, level='beginner', age_min=12, age_max=17, duration='۱۰ هفته', mode='hybrid', instructor='مهندس سارا رضایی', capacity=14, featured=True,
         syllabus='آشنایی با پایتون و نصب آن\nمتغیرها و انواع داده\nشرط‌ها و حلقه‌ها\nتوابع و ماژول‌ها\nکار با فایل و کتابخانه‌ها\nپروژه: ساخت بازی حدس عدد', prereq='خواندن و نوشتن پایه'),
    dict(cat='هوش مصنوعی', icon='🤖', title='هوش مصنوعی و یادگیری ماشین', summary='ساخت مدل‌های هوشمند با Python, scikit-learn و TensorFlow به‌صورت پروژه‌محور.', price=4200000, level='intermediate', age_min=15, age_max=24, duration='۱۲ هفته', mode='online', instructor='دکتر امیر کریمی', capacity=12, featured=True,
         syllabus='مروری بر NumPy و Pandas\nرگرسیون و طبقه‌بندی\nارزیابی مدل‌ها\nشبکه‌های عصبی مقدماتی\nپردازش تصویر و متن\nپروژه: دسته‌بند تصویر', prereq='پایتون مقدماتی'),
    dict(cat='رباتیک', icon='🔧', title='رباتیک و آردوینو', summary='از مدارهای ساده تا ربات متحرک؛ یادگیری سخت‌افزار با هیجان ساخت واقعی.', price=3800000, level='beginner', age_min=12, age_max=18, duration='۸ هفته', mode='in-person', instructor='مهندس نوید حسینی', capacity=10, featured=True,
         syllabus='آشنایی با الکترونیک\nبرنامه‌نویسی آردوینو\nسنسورها و موتورها\nبلوتوث و کنترل از راه دور\nپروژه: ماشین مانع‌یاب', prereq='ندارد'),
    dict(cat='هوش مصنوعی', icon='👁️', title='بینایی ماشین با پایتون', summary='تشخیص چهره، اشیا و حرکات با OpenCV و یادگیری عمیق.', price=4500000, level='advanced', age_min=16, age_max=24, duration='۱۰ هفته', mode='hybrid', instructor='دکتر مریم احمدی', capacity=8,
         syllabus='مبانی تصویر دیجیتال\nOpenCV و فیلترها\nتشخیص چهره و اشیا\nشبکه‌های کانولوشنی\nپروژه: دستیار بینایی', prereq='پایتون + آشنایی با ML'),
    dict(cat='الکترونیک', icon='⚡', title='الکترونیک و سیستم‌های تعبیه‌شده', summary='طراحی مدار، کار با میکروکنترلر و ساخت پروژه‌های IoT.', price=3200000, level='intermediate', age_min=14, age_max=22, duration='۹ هفته', mode='in-person', instructor='مهندس رضا صادقی', capacity=12,
         syllabus='قطعات و نقشه مدار\nآزمایشگاه و ایمنی\nمیکروکنترلر و سنسور\nاینترنت اشیا\nپروژه: خانه هوشمند', prereq='علاقه به الکترونیک'),
    dict(cat='طراحی', icon='🎨', title='طراحی وب و خلاقیت دیجیتال', summary='HTML, CSS و JavaScript برای ساخت سایت‌های زیبا و واکنش‌گرا.', price=2900000, level='beginner', age_min=13, age_max=20, duration='۸ هفته', mode='online', instructor='خانم نیلوفر مرادی', capacity=15,
         syllabus='HTML و ساختار صفحه\nCSS و طراحی واکنش‌گرا\nJavaScript مقدماتی\nطراحی رابط کاربری\nپروژه: سایت شخصی', prereq='ندارد'),
]

class Command(BaseCommand):
    help = 'درج داده‌های نمونه دوره‌ها و تنظیمات سایت'
    def handle(self, *args, **kw):
        SiteSetting.objects.get_or_create(pk=1)
        for i, c in enumerate(COURSES):
            cat, _ = Category.objects.get_or_create(name=c['cat'], defaults={'icon': c['icon']})
            course, created = Course.objects.get_or_create(title=c['title'], defaults=dict(
                category=cat, summary=c['summary'], description=c['summary'] + ' ' + 'کلاس‌ها با تمرین عملی و پروژه واقعی همراه است.',
                price=c['price'], level=c['level'], age_min=c['age_min'], age_max=c['age_max'],
                duration=c['duration'], mode=c['mode'], instructor=c['instructor'], capacity=c['capacity'],
                syllabus=c['syllabus'], prerequisites=c['prereq'], is_featured=c.get('featured', False),
                start_date=date.today() + timedelta(days=14 * (i + 1))))
            if created:
                for n, line in enumerate(c['syllabus'].split('\n'), 1):
                    Lesson.objects.create(course=course, title=line, order=n, content=line)
                les = course.lessons.first()
                Assignment.objects.create(lesson=les, title='تمرین هفته اول', description='تمرین‌های کلاسی را حل و ارسال کنید.')
                Quiz.objects.create(lesson=les, title='آزمون کوتاه هفته اول')
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@hooshno.academy', 'admin1234', role='admin')
        self.stdout.write(self.style.SUCCESS('داده‌های نمونه با موفقیت درج شد.'))
