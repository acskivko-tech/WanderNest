from django.urls import path
from wn_website import views

urlpatterns = [
    path('',views.main_page,name='welcome_page'),
    path('destinations/',views.destination_page,name='destination_page'),
    path('registration/registrate_user/',views.UserRegister.as_view(),name='registration_page'),
    path('login-user/',views.login,name='auth_page'),

]