from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from wn_website import views

urlpatterns = [
    path('',views.MainPageView.as_view(),name='welcome_page'),
    path('destinations/',views.TourListView.as_view(),name='destination_page'),
    path('registration/user/',views.UserRegisterView.as_view(),name='registration_page'),
    path('login/user/',views.LoginUserView.as_view(),name='auth_page'),
    path('logout/user/',LogoutView.as_view(next_page=reverse_lazy('welcome_page')),name='logout')


]