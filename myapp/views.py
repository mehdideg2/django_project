# Create your views here.
import sqlite3 as sq
from django.http import HttpResponse
from django.shortcuts import render


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
    return render(request, 'index.htm', {'table_header': table_header, 'participant': participant})


con = sq.connect("myapp/data.db")
cur = con.cursor()
cur.execute("SELECT * FROM Django_Project_Participant")

table_header = [tuple[0] for tuple in cur.description]
participant = cur.fetchall()

con.close()
