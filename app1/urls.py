from django.urls import path
from app1.views import *
app_name='sumanreddy'
urlpatterns=[
    path('alluarjun/',alluarjun,name='alluarjun'),
]