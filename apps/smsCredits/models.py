import uuid

from django.db import models


# Create your models here.
class SmsCreditsModel(models.Model):
    sms_credits_uuid = models.UUIDField(default=uuid.uuid4)
    sms_route_id = models.TextField()
    sms_route = models.TextField()
    sms_balance = models.TextField()
