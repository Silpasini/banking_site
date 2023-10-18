
# Create your views here.
from django.http import HttpResponse,request
from django.template import loader
from django.shortcuts import render

def demo(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())