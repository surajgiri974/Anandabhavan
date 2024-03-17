from django.shortcuts import render

# Create your views here.

class customer_home:

    def index(request):
        demo1 = { 'NAME' : 'ROHAN',}
        return render(request,'customer_pages/index.html',{'demo' : demo1,})
    
    def about(request):
        return render(request,'customer_pages/about.html')
   
    def contact(request):
        return render(request,'customer_pages/contact.html')
    
    def property_list(request):
        return render(request,'customer_pages/property_list.html')