
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView
from wn_website.forms import UserUpdateForm, UserCreationForm, UserLoginFrom
from wn_website.models import Tour, Booking


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
    paginator_class = Paginator(queryset,10)


class TourInfoView(DetailView):
    model = Tour
    template_name = 'wn_website/main_pages/destination_info.html'
    context_object_name = 'tour'


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    model = get_user_model()
    template_name = 'wn_website/forms/register_page.html'
    success_url = reverse_lazy('welcome_page')


class LoginUserView(LoginView):
    form_class = UserLoginFrom
    template_name ='wn_website/forms/login_form.html'

    def get_success_url(self):
        return reverse_lazy('welcome_page')


class UserPageView(LoginRequiredMixin,TemplateView):
    template_name = 'wn_website/user/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bookings = Booking.objects.filter(user=self.request.user)

        context['user'] = self.request.user
        context['bookings'] = bookings
        context['booking_count'] = bookings.count()
        return context


class UserUpdateView(LoginRequiredMixin,UpdateView):
    form_class = UserUpdateForm
    template_name ='wn_website/user/user_update.html'
    success_url = 'wn_website/user/user.html'

    def get_object(self):
        return self.request.user
