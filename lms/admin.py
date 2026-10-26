from django.contrib import admin
from .models import Lesson,Assignment,Quiz,Submission
admin.site.register(Lesson); admin.site.register(Assignment); admin.site.register(Quiz); admin.site.register(Submission)
