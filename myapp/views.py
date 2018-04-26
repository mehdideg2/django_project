# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def hello(request, number=0):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

def morning(request, number=0):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticle(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)