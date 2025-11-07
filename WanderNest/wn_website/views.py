from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from wn_website.forms import UserLogin, UserCreation
from wn_website.models import Tour


# Create your views here.

class MainPageView(TemplateView):
    template_name = 'wn_website/welcome_page.html'

class TourListView(ListView):
    template_name = 'wn_website/destinations_page'
    queryset = Tour.objects.all()
    context_object_name = 'tour_list'

class UserRegisterView(CreateView):
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
