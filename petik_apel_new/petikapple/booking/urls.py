from django.urls import path
from .views import book_ticket, booking_summary, confirm_booking, success_page

urlpatterns = [
    path('pesan-tiket/', book_ticket, name='book_ticket'),
    path('ringkasan/', booking_summary, name='booking_summary'),
    path('konfirmasi/', confirm_booking, name='confirm_booking'),  # Konfirmasi
    path('success/', success_page, name='success_page'),
]

