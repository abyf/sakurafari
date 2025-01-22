from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def about_us(request):
    return render(request, 'about-us.html',{})
