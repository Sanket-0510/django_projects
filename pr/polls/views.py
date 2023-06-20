from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from .models import Feature
from .models import registrationDetails
from django.contrib.auth.models import  auth
from django.contrib import messages
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    
    print(Feature.objects.all())
    
    data = {
         'feature' :Feature.objects.all(),
         'fullName': 'sanket',
         'age':20,
         'friends':[
            'hemant', 'soham', 'jitesh', 'vedant'
         ], 
         'projects':{
             'frontend':['amazonClone', 'optiimind-chatbot', 'portfolio.io'],
             'backend':['optiimind', 'node-crud-application']
         }
    }
   
    return render(request, 'home.html', data)

def counter(request):
   
    inputdata = request.POST['words']

    wordcount= len(inputdata.split())
    
    return render(request,'counter.html',{'number':wordcount})

def register(request):
    if request.method == 'POST':
      name = request.POST['name']
      email= request.POST['email']
      password= request.POST['password']
      cpassword = request.POST['cpassword']
      if password == cpassword:
          if registrationDetails.objects.filter(email=email).exists():
              messages.info(request,'email already exist')
              return redirect('register')
          elif registrationDetails.objects.filter(name= name).exists():
              messages.info(request,"username already exists")
              return redirect('register')
          else:
            user = registrationDetails(name=name, email=email, password=password)
            user.save();
            messages.success(request, 'Registration successful')
            return redirect('login')
          
      else:
          messages.info("passwords did not match")
          return redirect('register')
      
    else:
        return render(request, 'register.html')  
   
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if registrationDetails.objects.filter(name= username).exists():
            #now we will retrive the requested user
            requestedUser = registrationDetails.objects.get(name= username)
            print(requestedUser)
            if requestedUser.password == password:
                messages.info(request, "successfull login")
                return redirect('index2')
            else:
                messages.info(request, "wrong password")
                return redirect('login')
        #if user not found we will show error as username does not found
        else:
            messages.info(request, "user does not found")
            return redirect('login')
    #anything else post method we will just render the login page ok!
    return render(request, 'login.html')