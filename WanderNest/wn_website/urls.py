from django.urls import path
from wn_website import views

urlpatterns = [
    path('',views.main_page,name='welcome_page')

]