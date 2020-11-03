from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext, gettext_lazy as _

# admin.site.register(User, UserAdmin)


@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'birthday', 'phone_number', 'email','employee_id')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'employee_id', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'employee_id', 'first_name', 'last_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')
