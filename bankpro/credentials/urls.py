from . import views
from django.urls import path,include
app_name='auth'
urlpatterns = [

 path('register',views.register,name='register'),
 path('login',views.login,name='login'),
 path('logout',views.logout,name='logout'),
 path('Welcome',views.logedin,name='logedin'),
 path('form',views.form1,name='form1'),
]

