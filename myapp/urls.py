from django.conf.urls import url
from myapp.views import hello, morning, viewArticle

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^morning/', morning, name='morning'),
    url(r'^article/(\d+)', viewArticle, name='article'),
    url(r'^articles/(\d{2})/(\d{4})', viewArticle, name = 'articles'),
]
