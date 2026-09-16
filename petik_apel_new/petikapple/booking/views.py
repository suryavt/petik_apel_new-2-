from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings


# Halaman Beranda
def home(request):
    return render(request, 'booking/home.html')

# Halaman Profil
def profile(request):
    return render(request, 'booking/profil.html')

# Halaman Blog
def blog(request):
    return render(request, 'booking/blog.html')

# Halaman Pemesanan Tiket
from django.shortcuts import render

# Dummy data jika belum ada model database
def blog(request):
    artikels = [
        {"judul": "Artikel 1", "deskripsi": "Deskripsi artikel pertama", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/1"},
        {"judul": "Artikel 2", "deskripsi": "Deskripsi artikel kedua", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/2"},
        {"judul": "Artikel 3", "deskripsi": "Deskripsi artikel ketiga", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/3"},
        {"judul": "Artikel 4", "deskripsi": "Deskripsi artikel keempat", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/4"},
        {"judul": "Artikel 5", "deskripsi": "Deskripsi artikel kelima", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/5"},
        {"judul": "Artikel 6", "deskripsi": "Deskripsi artikel keenam", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/6"},
        {"judul": "Artikel 7", "deskripsi": "Deskripsi artikel ketujuh", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/7"},
        {"judul": "Artikel 8", "deskripsi": "Deskripsi artikel kedelapan", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/8"},
        {"judul": "Artikel 9", "deskripsi": "Deskripsi artikel kesembilan", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/9"},
        {"judul": "Artikel 10", "deskripsi": "Deskripsi artikel ketujuh", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/10"},
        {"judul": "Artikel 11", "deskripsi": "Deskripsi artikel kedelapan", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/11"},
        {"judul": "Artikel 12", "deskripsi": "Deskripsi artikel kesembilan", "gambar": "https://via.placeholder.com/150", "url": "https://example.com/12"},
    ]
    
    return render(request, 'booking/blog.html', {"artikels": artikels})


def book_ticket(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Simpan data booking
            return redirect('booking_summary')  # Arahkan ke ringkasan
    else:
        form = BookingForm()

    return render(request, 'booking/book_ticket.html', {'form': form})


def booking_summary(request):
    latest_booking = Booking.objects.latest('id')  # Ambil pesanan terbaru
    return render(request, 'booking/summary.html', {'booking': latest_booking})


def confirm_booking(request):
    if request.method == "POST":
        latest_booking = Booking.objects.latest('id')  # Ambil pesanan terbaru

        # Kirim email ke pemilik kebun
        subject = "Pesanan Tiket Baru - Petik Apel"
        message = f"""
        Halo, ada pesanan tiket baru!

        Kode Booking: {latest_booking.booking_code}
        Nama Pemesan: {latest_booking.name}
        Email: {latest_booking.email}
        Nomor WhatsApp: {latest_booking.whatsapp}
        Alamat: {latest_booking.address}
        Jumlah Tiket: {latest_booking.pax}
        Tanggal Kunjungan: {latest_booking.visit_date}
        Metode Pembayaran: {latest_booking.get_payment_method_display()}

        Harap segera dikonfirmasi. Terima kasih!
        """
        sender_email = settings.EMAIL_HOST_USER  # Ambil email dari settings.py
        recipient_email = ["pemilik.kebun@example.com"]  # Ganti dengan email pemilik kebun

        send_mail(subject, message, sender_email, recipient_email, fail_silently=False)

        return redirect('success_page')  # Redirect ke halaman sukses
    return redirect('home')  # Jika bukan POST, kembalikan ke halaman utama


def payment_summary(request):
    latest_booking = Booking.objects.latest('id')  # Ambil pesanan terbaru
    payment_method = latest_booking.payment_method  # Ambil metode pembayaran

    # Ambil data pembayaran dari settings
    payment_info = settings.PAYMENT_INFO.get(payment_method, {})

    return render(request, 'booking/summary.html', {
        'booking': latest_booking,
        'payment_info': payment_info
    })


def success_page(request):
    return render(request, 'booking/success.html')
