from django.contrib import admin
from .models import Category,Course,Enrollment
admin.site.register(Category)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): list_display=('title','category','level','price','is_published'); list_filter=('level','mode','is_published'); prepopulated_fields={'slug':('title',)}
admin.site.register(Enrollment)
