from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from wn_website import views
from wn_website.views import *

urlpatterns = [
    path('',MainPageView.as_view(),name='welcome_page'),
    path('destinations/',TourListView.as_view(),name='destinations_page'),
    path('destination/<slug:slug>',TourInfoView.as_view(),name='destination_info'),
    path('registration/user/',UserRegisterView.as_view(),name='registration_page'),
    path('login/user/',LoginUserView.as_view(),name='auth_page'),
    path('logout/user/',LogoutView.as_view(next_page=reverse_lazy('welcome_page')),name='logout'),
    path('user/page',UserPageView.as_view(),name='user_page'),
    path('user/edit/',UserUpdateView.as_view(),name='user_update_page'),


]