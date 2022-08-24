from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
# Create your views here.
def Admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect(Admin_page) 
        else:
            messages.error(request,'user does not exist..')
            return redirect(Admin_login)
    return render(request,'admin/admin-login.html')


def Admin_page(request):
    return render(request,'admin/admin-dashbord.html')


def Admin_logout(request):
    logout(request)
    return redirect(Admin_login)
