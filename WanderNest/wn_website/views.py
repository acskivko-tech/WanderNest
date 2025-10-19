from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request,'wn_website/welcome_page.html')

def destination_page(request):
    return render(request,'wn_website/destinations_page.html')