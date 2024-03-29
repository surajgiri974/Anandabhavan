from django.urls import path
from . import views

urlpatterns=[

    path('',views.customer_home.index,name="home"),
    path('about',views.customer_home.about,name="about"),
    path('contact',views.customer_home.contact,name="contact"),
    path('property_list',views.customer_home.property_list,name="property_list"),
    
    path('auth',views.customer_functionality.auth,name='auth'),    
    path('logout',views.customer_functionality.logout,name='logout'),    
    path('sign-up',views.customer_functionality.sign_up,name='sign-up'), 

]