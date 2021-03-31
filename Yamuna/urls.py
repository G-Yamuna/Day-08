from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home),
    path('yamu/',views.chk),
    path('homep/',views.homepage),
    path('loginp/',views.login),
    path('reg/',views.registration),
]