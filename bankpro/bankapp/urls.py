from django.urls import path,include
from . import views


app_name='bankapp'

urlpatterns = [
    path('',views.index,name='home'),
  ]