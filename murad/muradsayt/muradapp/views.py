from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
def index(request):
    return HttpResponse("MURAD IMANZADE")
def about(request):
    return HttpResponse("azerbaycan")
# Create your views here.
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Sehife tapilmadi</h1>')