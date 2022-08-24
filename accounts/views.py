
from django.shortcuts import render,redirect
from .models import Account
from .forms import UserRegisterForm
from django.contrib import messages,auth
from .verify import send_otp,verify_otp
from .forms import *
from .models import *
from django.contrib.auth import authenticate,logout
# Create your views here.


#user registration
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid:
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            mobile=request.POST['mobile']
            password=request.POST['password']

            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['mobile'] = mobile
            request.session['password'] = password

            send_otp(mobile)
            return redirect(verify_code)
        
    form=UserRegisterForm()
    context = {'form':form}
    return render(request,'register.html',context)


#user login
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home') 
        else:
            messages.error(request,'Incorrect Email or Password')
            return redirect('login')
    return render(request,'login.html')





#verify_otp
def verify_code(request):
    if request.method == 'POST':  
        otp_check = request.POST.get('otp')
        mobile = request.session['mobile']
        verify = verify_otp(mobile,otp_check)
        
        if verify:
            first_name = request.session['first_name']
            last_name = request.session['last_name']
            email = request.session['email']
            mobile = request.session['mobile']
            password = request.session['password']
            user = Account.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                mobile = mobile ,
                password = password
            )
            user.is_verified = True
            user.save()
            messages.success(request,'Account created successfylly')
            return redirect(login_page)        
        else:
            messages.error(request,'Invalid OTP')
            return redirect(verify_code)

            
    return render(request,'verify.html')

#user logout
def logout_page(request):
    logout(request)
    return redirect('home')