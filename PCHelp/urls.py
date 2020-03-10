
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name= 'home'),
    path('detailblocks/main', views.main, name = 'main'),
    path('detailblocks/addcomment', views.addcomment, name = 'addcomment'),
    path('createbid', views.createbid, name = 'createbid'),
]