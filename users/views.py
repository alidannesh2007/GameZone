from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import userRegisterForm
from users.forms import *



def register(request):
    if request.method == "POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'account created. now login')
            return redirect('GameZone')
    else:
        form = userRegisterForm()
    return render (request , 'register.html', {'form' : form})

# @login_required
def profile(request):
    if request.method == "POST":
        u_form = userUpdateForm(request.POST, instance=request.user)
        a_form = profileImgUpdate(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and a_form.is_valid():
            u_form.save()
            a_form.save()
            messages.success(request, 'account updated')
            return redirect('profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        a_form = profileImgUpdate(instance=request.user.profile)       
    
    context = {
        'u_form' : u_form,
        'a_form' : a_form
    }
    
    
    
    
    
    return render(request, 'profile.html', context)

