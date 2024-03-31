from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
import MySQLdb as mysql

# Create your views here.

class customer_home:

    def index(request):
        return render(request,'customer_pages/index.html')
    
    def about(request):
        return render(request,'customer_pages/about.html')
   
    def contact(request):
        return render(request,'customer_pages/contact.html')
    
    def property_list(request):
        return render(request,'customer_pages/property_list.html')
    

class customer_functionality:

    def auth(request):
        try:
            email = request.POST.get('email',False)
            password = request.POST.get('password',False)
            customer = Customer.objects.get(customer_email = email)
            if customer.customer_email == email:
                if customer.customer_password == password:
                    request.session['customer_email'] = email
                    return HttpResponseRedirect('/property_list')
                else:
                    messages.add_message(request,messages.ERROR,'Invalid Credential')
                    return HttpResponseRedirect('/')
        except Customer.DoesNotExist:
            messages.add_message(request,messages.ERROR,'User Does Not Exist')
            return HttpResponseRedirect('/')
        except:
            messages.add_message(request,messages.ERROR,'ERROR')
            return HttpResponseRedirect('/')
            
            
    def logout(request):
        try:
            request.session.flush()
            return redirect(customer_home.home)
        except:
            print("ERROR")
            request.session.flush()
            return HttpResponseRedirect('/')
    
    def sign_up(request):
        try:
            customer_name = request.POST.get('customer_name', False)
            customer_email = request.POST.get('customer_email',False)
            customer_phone = request.POST.get('customer_phone',False)
            password = request.POST.get('password',False)
            customer = Customer(
                customer_name = customer_name,
                customer_email = customer_email,
                customer_mobile = customer_phone,
                customer_password = password,
                account_type = 1)
            customer.save()
            return HttpResponseRedirect('/')        
        except:
            return HttpResponseRedirect('/')   
