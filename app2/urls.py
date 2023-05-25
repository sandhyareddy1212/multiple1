from django.urls import path
from app2.views import *
app_name='sanjayreddy'
urlpatterns=[
    path('youngtiger/',youngtiger,name='youngtiger'),
]