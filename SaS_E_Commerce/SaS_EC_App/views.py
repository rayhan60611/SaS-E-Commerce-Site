from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import  auth 
from SaS_EC_App.models import Registration as registration
from django.contrib import messages
from django.http import JsonResponse

# from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render (request,'index.html')

# def Login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(email=email,password=password)
#         if user is not None:
#             authenticate.login(request,user)
#         else:
#             messages.info(request,'Invalid Credentials!')


# def Registration(request):
#     if request.method == 'POST' and request.FILES['image']:
#         # image = request.FILES['image']
#         # fs = FileSystemStorage()
#         # filename = fs.save(image.name , image)
#         # url = fs.url(filename)
        
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         mobile = request.POST.get('mobile')
#         image = request.FILES.get("image")
#         address = request.POST.get('address')
#         password1 = request.POST.get('password')
#         password2 = request.POST.get('confirm_password')
#         context={
#                     'err' : {
#                                 'email':None,
#                                 'password':None
#                             }
#                 }
#         if password1 == password2:
#             context['err']['password'] = '''Your Password and Confirm Password Didn't Match'''
#             if registration.object.filter(email=email).exists():
#                 context['err']['email'] = 'Email Already Taken'
#             else:
#                 Registration = registration.object.create_user(first_name =first_name, last_name=last_name, email=email, mobile=mobile, image=image, address=address, password=password1)
#                 Registration.save()
#                 print('reg done!!!!')
#                 return redirect ('/')
#         else:
#             print('password not matched')
       
       
#         # messages.info(request,"Registration Succesfull")
#     else: 
#         return render(request,'/',context)
                    


def Registration(request):
    if request.method == 'POST' and request.FILES['image']:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        image = request.FILES.get("image")
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if registration.object.filter(email=email).exists():
            return JsonResponse({"err": {"email": "Email already exists"}})
        else:
            Registration = registration.object.create_user(first_name =first_name, last_name=last_name, email=email, mobile=mobile, image=image, address=address, password=password1)
            Registration.save()
            return JsonResponse({'data' : 'success'})
       
       
        # messages.info(request,"Registration Succesfull")
    else: 
        return render(request,'/')