from django.urls import path
from wn_website import views

urlpatterns = [
    path('',views.MainPageView.as_view(),name='welcome_page'),
    path('destinations/',views.TourListView.as_view(),name='destination_page'),
    path('registration/user/',views.UserRegisterView.as_view(),name='registration_page'),
    path('login-user/',views.login,name='auth_page'),


]