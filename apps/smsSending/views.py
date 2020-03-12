import csv
import io

import pandas as pandas
from django.http import QueryDict
from django.shortcuts import render
import requests
import urllib
from urllib.request import urlopen
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from contextlib import closing
import codecs

from Bulksms.settings import APPLICATION_SMS_URL, APPLICATION_SMS_USER, APPLICATION_SMS_PASSWORD, \
    APPLICATION_SMS_SENDER, APPLICATION_SMS_PRIORITY, APPLICATION_SMS_TYPE
from apps.smsReports.serializers import ReportModelSerializer


def BulkTextMessageSendingRequest(CONTACTS, MESSAGE):
    r = requests.post(
        APPLICATION_SMS_URL + "user=" + APPLICATION_SMS_USER + "&pass=" + APPLICATION_SMS_PASSWORD + "&sender=" + APPLICATION_SMS_SENDER + "&phone=" + str(
            CONTACTS) + "&text=" + MESSAGE + "&priority=" + APPLICATION_SMS_PRIORITY + "&stype=" + APPLICATION_SMS_TYPE)
    if r.status_code == 200:
        print(r.content)
        return Response(r.content, status=status.HTTP_200_OK)
    elif r.status_code == 400:
        return Response(r.content, status=status.HTTP_400_BAD_REQUEST)
    elif r.status_code == 500:
        return Response(r.content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def convert(text):
    try:
        return int(text)
    except ValueError:
        pass

    try:
        return float(text)
    except ValueError:
        return text


class BulkMessageProcessView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    # with open(file_obj,'r') as r:
    #     reader = csv.reader(r,delimiter=',')
    #     n = []
    #     for row in reader:
    #         n.append(row[8])
    #     print(reader)
    # for row in reader:

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['vcardfile']
        print(type(file_obj))
        data_set = file_obj.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        mylist = []
        for row in io_string:
            mylist.append(convert(row.strip()))
        contacts = ", ".join(repr(e) for e in mylist)
        message = BulkTextMessageSendingRequest(contacts, request.data['message'])
        shoot_id = message.data.split("/")[1]
        listtt = dict({'reports': shoot_id})
        query_dict = QueryDict('', mutable=True)
        query_dict.update(listtt)
        message_list_serializer = ReportModelSerializer(data=query_dict)
        if message_list_serializer.is_valid():
            message_list_serializer.save()
        return Response(shoot_id, status=message.status_code)
#     SMS-SHOOT-ID/iconassociates5e591ba59652b
