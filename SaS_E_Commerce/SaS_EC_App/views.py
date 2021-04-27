from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import  auth
from SaS_EC_App.models import registration
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request,'index.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            authenticate.login(request,user)
        else:
            messages.info(request,'Invalid Credentials!')


def Registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        image = request.POST.get('image')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        Registration= registration(first_name =first_name, last_name=last_name, email=email, mobile=mobile, image=image, address=address, password=password)
        Registration.save()
    return render(request, 'index.html')
                    
    
    