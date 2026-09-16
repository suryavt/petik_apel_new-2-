"""
URL configuration for petikapple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from booking import views as booking_views

urlpatterns = [
    # URL untuk admin Django
    path('admin/', admin.site.urls),
    
    # URL untuk aplikasi booking yang sudah ada
    path('booking/', include('booking.urls')),  # URL booking tetap dipertahankan
    
    # URL untuk halaman utama atau beranda
    path('', booking_views.home, name='home'),  # Halaman Beranda
    
    # URL untuk halaman profil
    path('profile/', booking_views.profile, name='profile'),  # Halaman Profil
    
    # URL untuk halaman blog
    path('blog/', booking_views.blog, name='blog'),  # Halaman Blog
    
    # URL untuk halaman pemesanan tiket
    path('book_ticket/', booking_views.book_ticket, name='book_ticket'),  # Halaman Pemesanan Tiket
    
]



