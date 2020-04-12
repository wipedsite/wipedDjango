from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('wipers.html', views.wipers, name="wipers"),
	path('service.html', views.service, name="service"),
	path('blog.html', views.blog, name="blog"),
	path('blog_details.html', views.blog_details, name="blog_details"),
	path('booking.html', views.booking, name="booking"),
]

