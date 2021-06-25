from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fastOrder.users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'created', 'modified')

admin.site.register(User, CustomUserAdmin)