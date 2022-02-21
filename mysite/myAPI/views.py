from http.client import HTTPResponse
import json, os
from lib2to3.pytree import convert
from pydoc import resolve
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings

import requests
import re
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

class livreHTML(APIView):
    def get(self, request, format = None):
        prot = request.GET.get("prot")
        adr = request.GET.get("adr")
        response = requests.get(prot + "://" + adr)
        jsondata = json.dumps({"html": response.text.replace("\"", "")})
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

class indexJSON(APIView):
    def get(self, request, format = None):
        staticFile = "static" + os.sep + "myAPI" + os.sep + "indexFinal3.json"
        f = os.path.join(settings.BASE_DIR, staticFile)
        indexFile = open(f)
        jsondata = json.load(indexFile)
        jsondata = json.loads(jsondata)
        return Response(jsondata["project"])

class livresAccueil(APIView):
    def get(self, request, format = None):
        staticFile = "static" + os.sep + "myAPI" + os.sep + "liste_livre.json"
        f = os.path.join(settings.BASE_DIR, staticFile)
        indexFile = open(f)
        jsondata = json.load(indexFile)
        # page = request.GET.get("page", 1)
        # nbCard = 15
        noLimit = request.GET.get("noLimit", False)
        print(noLimit)
        if not bool(noLimit):
            listeId = ",".join(jsondata[0:15])
        else:
            listeId = ",".join(jsondata)

        response = requests.get(baseUrl + "/?ids=" + listeId)
        jsondata = response.json()
        return Response(jsondata)

class advanceSearch(APIView):
    def get(self, request, format = None):
        mot = request.GET.get("mot", "")
        valeur=mot.replace("%", " ")
        valeur = valeur.split(" ")
        mot = ""
        for c in valeur:
            mot += chr(int(c))
        key=[]
        final=[]
        liste_index = []
        staticFile = "static" + os.sep + "myAPI" + os.sep + "indexFinal3.json"
        f = os.path.join(settings.BASE_DIR, staticFile)
        indexFile = open(f)
        jsondata = json.load(indexFile)
        jsondata = json.loads(jsondata)

        for e in jsondata.keys():
            valeur=re.match(mot,e)
            if valeur !=None:
                key.append(e)
                liste_index += jsondata.get(e)[0].keys()
        print(liste_index)        
        liste_index = ",".join(liste_index)
        response = requests.get(baseUrl + "/?ids=" + liste_index)
        jsondata = response.json()
        print(key)
        return Response(jsondata)
 
