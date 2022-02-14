from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from myAPI.config import baseUrl

import urllib.parse

# Create your views here.

def index(request):
    return HttpResponse("Hello World, from Django !")

class unLivre(APIView):
    def get(self, request, id, format = None):
        response = requests.get(baseUrl + "/" + str(id) + "/")
        jsondata = response.json()
        return Response(jsondata)

class desLivres(APIView):
    def get(self, request, format = None):
        page = request.GET.get("page", "1")
        response = requests.get(baseUrl + "/?page=" + page)
        jsondata = response.json()
        return Response(jsondata)

class rechercheLivres(APIView):
    def get(self, request, strSearch, format = None):
        # Recherche dans les sujets du livre
        response = requests.get(baseUrl + "/?topic=" + urllib.parse.quote_plus(strSearch))
        jsondata = response.json()
        return Response(jsondata)