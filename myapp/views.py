# Create your views here.
from django.http import HttpResponse
from django.template import loader


def hello(request, number=0):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)

def morning(request, number=0):
   text = "<h1>Good Morning, you have the number %s!</h1>"% number
   return HttpResponse(text)

def viewArticleById(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticleByDate(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def index(request):
    template = loader.get_template('index.htm')
    return HttpResponse(template.render())
