#from django.shortcuts import render

# Create your views here.
import os

from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import FileResponse

from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *
from api.serializers import TcrRequestSerializer

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

import json, datetime, pytz
from django.core import serializers
import requests
from django.http import JsonResponse
from PDBS.process_pdb_request import *


PDB_URL = "1bd2.pdb"

class FetchPdb(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        global PDB_URL
        pdb = request.data.get('pdb')
        PDB_URL = pdb
        return Response("Success", status=status.HTTP_200_OK)


class ActionList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        Return_Choices = []
        for each in FUNCTION_CHOICES:
            Return_Choices.append({"method": each[0], "name": each[1]})
        return Response(Return_Choices, status=status.HTTP_200_OK)


class PdbList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response([pdb[0] for pdb in PDB_CHOICES], status=status.HTTP_200_OK)


class TcrRequestList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request, format=None):
        tcrrequest = TcrRequest.objects.all()
        json_data = serializers.serialize('json', tcrrequest)
        content = {'tcrrequest': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):
        print("We have received api call")
        pdb = request.data.get('pdb')
        action1 = request.data.get('action1')
        action2 = request.data.get('action2')
        action3 = request.data.get('action3')

        newRequest = TcrRequest(
            pdb=pdb,
            action1=action1,
            action2=action2,
            action3=action3,
        )

        newRequest.save()

        # Process PDB request and return pdb
        pdb = request.POST.get('pdb')
        actions = [request.POST.get('action1'), request.POST.get('action2'), request.POST.get('action3')]
        print("ACTIONS: ", actions)
        context = {"pdb": pdb, "actions": actions}
        pdb_path = process_modification(context)
        pdb = pdb_path.split('/')[-1]
        print('New Event Logged')
        pdb_file = open(pdb_path, "rb")
        response = FileResponse(pdb_file, content_type="application/text")
        response['Content-Length'] = os.path.getsize(pdb_path)
        response['Content-Disposition'] = 'attachment; filename="%s"' % pdb
        return response
        # return Response({'success': True}, status=status.HTTP_200_OK)


class TcrRequestDetail(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return TcrRequest.objects.get(pk=pk)
        except TcrRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tcrrequest = self.get_object(pk)
        serializers = TcrRequestSerializer(tcrrequest)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        tcrrequest = self.get_object(pk)
        serializers = TcrRequestSerializer(tcrrequest, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tcrrequest = self.get_object(pk)
        tcrrequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
