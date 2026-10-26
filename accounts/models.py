from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    ROLE=[('student','دانش‌آموز'),('instructor','مدرس'),('parent','والد'),('admin','مدیر')]
    role=models.CharField('نقش',max_length=20,choices=ROLE,default='student')
    phone=models.CharField('تلفن',max_length=30,blank=True)
    def is_student(self): return self.role=='student'
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio=models.TextField('درباره من',blank=True)
    birth_year=models.PositiveIntegerField('سال تولد',null=True,blank=True)
    avatar=models.ImageField(upload_to='avatars/',blank=True,null=True)
    def __str__(self): return f'پروفایل {self.user}'
