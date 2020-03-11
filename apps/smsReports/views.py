

import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.smsReports.models import ReportModel, MessageReportsModel
from apps.smsReports.serializers import ReportModelSerializer


class ReportsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    queryset = ReportModel.objects.all()
    # filter(from_whom=request.data['from_whom'])
    serializer_class = ReportModelSerializer


def callDeliveryApi(shootid):
    r = requests.get("http://websms.smsxperts.com/app/miscapi/25E5518ACC02A6/getDLR/iconassociates5e591ba59652b")
    if r.status_code == 200:
        return Response(r.text, status=status.HTTP_200_OK)
    elif r.status_code == 400:
        return Response(r.text, status=status.HTTP_400_BAD_REQUEST)
    elif r.status_code == 500:
        return Response(r.text, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MessageDeliveryReports(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        Message_me = MessageReportsModel.objects.count()
        return Response({"messagecount": Message_me}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        statuss=callDeliveryApi("")
        if statuss.status_code==200:
            result = statuss.data
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(statuss, status=status.HTTP_400_BAD_REQUEST)