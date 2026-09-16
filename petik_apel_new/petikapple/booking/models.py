from django.db import models
import uuid

class Booking(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash on Kebun'),
        ('shopeepay', 'ShopeePay'),
        ('bri', 'Bank BRI'),
        ('bca', 'Bank BCA'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    address = models.TextField()
    pax = models.IntegerField()
    visit_date = models.DateField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)
    booking_code = models.CharField(max_length=10, unique=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.visit_date}"
    
    def save(self, *args, **kwargs):
        if not self.booking_code:
            self.booking_code = str(uuid.uuid4().hex[:8]).upper()  # Buat kode unik
        super().save(*args, **kwargs)
    

