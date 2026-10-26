from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
@admin.register(User)
class CustomUserAdmin(UserAdmin): list_display=('username','email','role'); fieldsets=UserAdmin.fieldsets+((None,{'fields':('role','phone')}),)
admin.site.register(Profile)
