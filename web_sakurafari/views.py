from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html',{})

def contact(request):
    if request.method == "POST":
        # do stuff
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Send mail
        send_mail(subject,message,email,['sakurafarisarl@gmail.com'],fail_silently=True)

        return render(request, 'contact.html',{'name':name, 'email':email, 'subject':subject, 'message':message})
    else:
        # return the page
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
