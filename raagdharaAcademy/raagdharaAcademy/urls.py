"""raagdharaAcademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Academy import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel route
    path('', views.home, name='home'),  # Home page route
    path('contact/', views.contact, name='contact'),  # Contact page route
    path('courses/', views.courses, name='courses'),  # Courses page route
    path('reviews/', views.reviews, name='reviews'),  # Reviews page route
    path('about/', views.about, name='about'),  # About page route
    path('submit_review/', views.submit_review, name='submit_review'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('enroll/', views.enroll, name='enroll'),
    path('submit-enrollment/', views.submit_enrollment, name='submit_enrollment'),
    path('enrollment-success/', views.enrollment_success, name='enrollment_success'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
]
