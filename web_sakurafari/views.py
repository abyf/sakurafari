from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def about_us(request):
    return render(request, 'about-us.html',{})

def service(request):
    return render(request, 'service.html',{})

def portfolio(request):
    return render(request, 'portfolio.html',{})

def blog(request):
    return render(request, 'blog.html',{})

def single_blog(request):
    return render(request, 'single-blog.html',{})

def elements(request):
    return render(request, 'elements.html',{})
