from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.
class Attendance(models.Model):
    WORKTYPE_CHOICES = (
        (1,'SES'), (2,'派遣'), (3,'社内業務'), (4,'出勤予定'), (5,'受託'), (6,'内勤'),
    )

    # employee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(_('社員ID'))
    # attendance_id = models.IntegerField(_('Attendance ID'),)
    work_type = models.IntegerField(_('種別'), choices=WORKTYPE_CHOICES)
    opening_time = models.TimeField(_('始業時間'),)
    closing_time = models.TimeField(_('終業時間'),)
    break_time = models.TimeField(_('休憩時間'),)
    # working_hours = models.TimeField(null=True, blank=True)
    date = models.DateField(_('日付'),)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee_id = models.IntegerField(_('社員ID'))
    # deleted = models.DateTimeField(null=True, blank=True)
    attendance_details_id = models.IntegerField(_('Attendance Details ID'), null=True, blank=True)

    # def get_working_hours(self):
    #   """Return the working hours today."""
    #   working_hours = self.closing_time - self.opening_time - self.break_time
    #   return working_hours

    def __int__(self):
        return self.employee_id
