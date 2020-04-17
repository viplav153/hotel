from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm ,UserUpdateForm,ProfileUpadteForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from lists.models import List
from datetime import date,timedelta


# Create your views here.
'''def signup(request):
    if request.method =='POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            user= form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.User_type = form.cleaned_data.get('User_type')
            user.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html',{'form':form})'''


def signup_customer(request):
    if request.method == "POST":#if any value is is given by user
        if request.POST['password1'] == request.POST['password2']:#when password and confirming password is equal
            try:
                user=User.objects.get(username=request.POST['username'])#when username is already present
                return render(request, 'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],)#if username is unique and both the password are same it stores the data
                user.email=request.POST['username']
                user.profile.first_name = request.POST['first_name']
                user.profile.last_name = request.POST['last_name']
                user.profile.email = request.POST['username']
                user.profile.User_type = "Customer"
                user.save()
                auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')#for logging user in
                return redirect('profile_view')
        else:
            return render(request, 'lists/home.html', {'error':'password must match'})#if password and confirming password misses matched        
    else:
        return render(request, 'lists/home.html')#if fields are empty and user clicks signup


def signup_hotel(request):
    
    if request.method == "POST":#if any value is is given by user
        if request.POST['password1'] == request.POST['password2']:#when password and confirming password is equal
            try:
                user=User.objects.get(username=request.POST['username'])#when username is already present
                return render(request, 'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],)#if username is unique and both the password are same it stores the data
                user.email=request.POST['username']
                user.profile.first_name = request.POST['first_name']
                user.profile.last_name = request.POST['last_name']
                user.profile.email = request.POST['username']
                user.profile.User_type = "Hotel"
                user.save()
                auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')#for logging user in
                return redirect('profile_view')
        else:
            return render(request, 'lists/home.html', {'error':'password must match',})#if password and confirming password misses matched        
    else:
        return render(request, 'lists/home.html')#if fields are empty and user clicks signup
     
def login_customer(request):
    lists=List.objects.all()
    if request.method=='POST':#if any value is is given by user
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
        
            if user.profile.User_type == "Customer":
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request, 'lists/home.html',{'error':'your user type is hotel','lists':lists})
            
        else:
            return render(request, 'lists/home.html',{'error':'username or password is incorrect','lists':lists})
    else:
        return render(request, 'lists/home.html')

def login_hotel(request):
    if request.method=='POST':#if any value is is given by user
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            
            if user.profile.User_type == "Hotel":
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request, 'lists/home.html',{'error':'your user type is Customer'})
            
        else:
            return render(request, 'lists/home.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'lists/home.html')

        


@login_required
def profile(request):
    if request.method =='POST' :
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpadteForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid()and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account Account updated !!')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpadteForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    
    }

    return render(request,'accounts/profileupdate.html',context)




    #if request.method =='POST' :
    #    a=Profile.objects.get(id=2
    #    a-=1
    #    a.save()
    #    return render(request,'accounts/profile.html')

@login_required    
def change_password(request):
    if request.method =='POST' :
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,f'Your account Password has been updated !!')
            return redirect('profile_view')
        else:
            messages.error(request,f'something went wrong!!')
            return redirect('change_password')


    else:
        form =PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/password.html',args)



@login_required
def profile_view(request):
    p_form=ProfileUpadteForm(instance=request.user.profile)
    return render(request,'accounts/profile.html',{'p_form':p_form,})
   
        

        


    
    
    

