from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    column = ('id', 'user_id', 'work_type', 'opening_time', 'closing_time', 'break_time', 'date', 'created_at', 'updated_at',)
    list_display = column
    ordering = column
    list_filter = column
    search_fields = column

admin.site.register(Attendance, AttendanceAdmin)
