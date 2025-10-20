from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from wn_website.forms import UserLogin, UserCreation


# Create your views here.

def main_page(request):
    return render(request,'wn_website/welcome_page.html')

def destination_page(request):
    return render(request,'wn_website/destinations_page.html')

class UserRegister(CreateView):
    form_class = UserCreation
    model = get_user_model()
    template_name = 'wn_website/register_page.html'
    success_url = reverse_lazy('welcome_page')

def login(request):
    if request.method == 'POST':
        form = UserLogin(request,data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user and user.is_active:
                login(request,user)
                return render(request,'wn_website/welcome_page.html')
    else:
        form = UserLogin
        return render(request,'wn_website/login_form.html',{'form':form})