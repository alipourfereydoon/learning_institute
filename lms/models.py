from django.db import models
from django.conf import settings
class Lesson(models.Model):
    course=models.ForeignKey('courses.Course',on_delete=models.CASCADE,related_name='lessons')
    title=models.CharField('عنوان درس',max_length=180)
    order=models.PositiveSmallIntegerField('ترتیب',default=1)
    content=models.TextField('محتوا',blank=True)
    video_url=models.URLField('لینک ویدیو',blank=True)
    class Meta: ordering=['order']
    def __str__(self): return self.title
class Assignment(models.Model):
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='assignments')
    title=models.CharField(max_length=180); description=models.TextField(blank=True)
    due_date=models.DateField(null=True,blank=True); max_score=models.PositiveSmallIntegerField(default=100)
    def __str__(self): return self.title
class Quiz(models.Model):
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='quizzes')
    title=models.CharField(max_length=180); description=models.TextField(blank=True)
    def __str__(self): return self.title
class Submission(models.Model):
    STATUS=[('pending','در انتظار بررسی'),('graded','نمره داده شد')]
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name='submissions')
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='submissions')
    file=models.FileField(upload_to='submissions/',blank=True,null=True)
    text=models.TextField(blank=True)
    score=models.PositiveSmallIntegerField(null=True,blank=True)
    feedback=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.student} — {self.assignment}'
