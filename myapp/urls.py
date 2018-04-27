from django.urls import path


from . import views


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('morning/', views.morning, name='morning'),
    path('article/<int:articleId>', views.viewArticleById, name='article'),
    path('article/<int:month>/<int:year>', views.viewArticleByDate, name = 'articles'),
    path('index/', views.index, name='index')
]

""" 
pour acceder aux URL ci-dessus, il suffit de taper les adresses suivantes
apres avoir lancer le server :
http://127.0.0.1:8000/myapp/hello/
http://127.0.0.1:8000/myapp/morning/
http://127.0.0.1:8000/myapp/article/(un chiffre)
http://127.0.0.1:8000/myapp/article/(un chiffre)/(un chiffre)
http://127.0.0.1:8000/myapp/index/
 """
