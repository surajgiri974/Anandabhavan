from django.urls import path
from . import views

urlpatterns=[
    path('',views.customer_home.index,name="home"),
    path('about',views.customer_home.about,name="about"),
    path('contact',views.customer_home.contact,name="contact"),
    
    
    

]