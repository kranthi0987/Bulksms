import uuid

from django.db import models


# Create your models here.

class ReportModel(models.Model):
    report_uuid = models.UUIDField(default=uuid.uuid4)
    reports = models.TextField(blank=True, null=True)


class MessageReportsModel(models.Model):
    message_report_uuid = models.UUIDField(default=uuid.uuid4)
    message_receipt_phone_number = models.TextField()
    message_delivery_report = models.TextField()
    message_report_description = models.TextField()
