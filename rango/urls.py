from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^S',views.index,name='index'),
    url(r'^$',views.about,name='about'),
]
