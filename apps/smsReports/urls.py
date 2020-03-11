from django.conf.urls import url
from django.urls import path

from apps.smsReports.views import ReportsView, MessageDeliveryReports

urlpatterns = [
    path('reports', ReportsView.as_view()),
    path('deliveryreports', MessageDeliveryReports.as_view()),
    ]