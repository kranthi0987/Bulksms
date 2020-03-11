from rest_framework import serializers

from apps.smsReports.models import ReportModel, MessageReportsModel


class ReportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportModel
        fields = "__all__"


class MessageReportsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageReportsModel
        fields = ('__all__')
