from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from wn_website.forms import UserLogin, UserCreation
from wn_website.models import Tour


# Create your views here.

class MainPageView(TemplateView):
    template_name = 'wn_website/main_pages/welcome_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        return context



class TourListView(ListView):
    template_name = 'wn_website/main_pages/destinations_page.html'
    queryset = Tour.objects.all()


class UserRegisterView(CreateView):
    form_class = UserCreation
    model = get_user_model()
    template_name = 'wn_website/forms/register_page.html'
    success_url = reverse_lazy('welcome_page')


# def login_user(request):
#     if request.method == 'POST':
#         form = UserLogin(request,data=request.POST)
#         if form.is_valid():
#
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#
#             user = authenticate(username=username,password=password)
#             if user and user.is_active:
#                 login(request,user)
#                 return render(request,'wn_website/main_pages/welcome_page.html')
#     else:
#         form = UserLogin
#         return render(request,'wn_website/forms/login_form.html',{'form':form})

class LoginUserView(LoginView):
    form_class = UserLogin
    template_name ='wn_website/forms/login_form.html'

    def get_success_url(self):
        return reverse_lazy('welcome_page')
