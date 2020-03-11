from django.conf.urls import url

from apps.smsSending.views import BulkMessageProcessView

urlpatterns = [
    url('sendsms', BulkMessageProcessView.as_view()),
    ]