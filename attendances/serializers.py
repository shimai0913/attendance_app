from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = (
          'id',
          'employee_id',
        #   'attendance_id',
          'work_type',
          'opening_time',
          'closing_time',
          'break_time',
          # 'working_hours',
          'date',
          'created_at',
          'updated_at',
          # 'deleted',
          'attendance_details_id',
        )
        # fields = '__all__'
