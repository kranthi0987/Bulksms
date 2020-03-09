from django.contrib import admin

# Register your models here.
from apps.smsReports.models import ReportModel, MessageReportsModel

admin.site.register(ReportModel)
admin.site.register(MessageReportsModel)