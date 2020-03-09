from rest_framework import serializers

from apps.smsCredits.models import SmsCreditsModel


class SmsCreditsModelSerializer(serializers.ModelSerializer):
    model = SmsCreditsModel

    class Meta:
        fields = ('__all__')
