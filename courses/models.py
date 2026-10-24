from django.db import models
from django.conf import settings
from django.utils.text import slugify
class Category(models.Model):
    name=models.CharField('نام دسته',max_length=100)
    slug=models.SlugField(unique=True,blank=True,allow_unicode=True)
    icon=models.CharField('آیکون ایموجی',max_length=10,default='✨')
    def save(self,*args,**kwargs):
        if not self.slug: self.slug=slugify(self.name,allow_unicode=True)
        super().save(*args,**kwargs)
    def __str__(self): return self.name
class Course(models.Model):
    MODE_CHOICES=[('online','آنلاین'),('in-person','حضوری'),('hybrid','ترکیبی')]
    LEVEL_CHOICES=[('beginner','مقدماتی'),('intermediate','متوسط'),('advanced','پیشرفته')]
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='courses',verbose_name='دسته‌بندی')
    title=models.CharField('عنوان دوره',max_length=180)
    slug=models.SlugField(unique=True,blank=True,allow_unicode=True)
    summary=models.CharField('توضیح کوتاه',max_length=260)
    description=models.TextField('توضیحات',blank=True)
    age_min=models.PositiveSmallIntegerField('حداقل سن',default=12); age_max=models.PositiveSmallIntegerField('حداکثر سن',default=24)
    price=models.PositiveIntegerField('شهریه (تومان)',default=0)
    level=models.CharField('سطح',max_length=20,choices=LEVEL_CHOICES,default='beginner')
    capacity=models.PositiveSmallIntegerField('ظرفیت',default=12)
    duration=models.CharField('مدت دوره',max_length=80,default='۸ هفته')
    syllabus=models.TextField('سرفصل‌ها',blank=True,help_text='هر سرفصل در یک خط')
    prerequisites=models.CharField('پیش‌نیاز',max_length=250,blank=True,default='علاقه به یادگیری')
    mode=models.CharField('شیوه برگزاری',max_length=20,choices=MODE_CHOICES,default='hybrid')
    instructor=models.CharField('مدرس',max_length=100,blank=True,default='تیم آموزشی هوش نو')
    start_date=models.DateField('تاریخ شروع',null=True,blank=True)
    is_featured=models.BooleanField('ویژه',default=False); is_published=models.BooleanField('منتشر شده',default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def save(self,*args,**kwargs):
        if not self.slug: self.slug=slugify(self.title,allow_unicode=True)
        super().save(*args,**kwargs)
    def __str__(self): return self.title
class Enrollment(models.Model):
    STATUS=[('pending','در انتظار'),('approved','تایید شده'),('cancelled','لغو شده')]
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='enrollments')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments')
    status=models.CharField(max_length=20,choices=STATUS,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=('student','course')
    def __str__(self): return f'{self.student} — {self.course}'
