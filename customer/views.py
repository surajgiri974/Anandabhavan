from django.shortcuts import render

# Create your views here.

class customer_home:

    def index(request):
        return render(request,'customer_pages/index.html')
    
    def about(request):
        return render(request,'customer_pages/about.html')
   
    def contact(request):
        return render(request,'customer_pages/contact.html')