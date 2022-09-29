#Django Methods
from django.urls import path

#Django manually function,models,forms or etc...
from .views import *

app_name='coin'
urlpatterns = [
    path('',indexView,name='indexView')
]
