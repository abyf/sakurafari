from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('contact.html', views.contact, name="contact"),
   path('about-us.html', views.about_us, name="about_us"),
   path('service.html', views.service, name="service"),
   path('portfolio.html', views.portfolio, name="portfolio"),
   path('blog.html', views.blog, name="blog"),
   path('single-blog.html', views.single_blog, name="single_blog"),
   path('elements.html', views.elements, name="elements"),
]
