from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_active', 'is_staff']
    list_filter = ['role']

admin.site.register(User, CustomUserAdmin)