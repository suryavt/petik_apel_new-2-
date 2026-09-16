from django import forms
from .models import Booking
from django.core.validators import MinValueValidator
import re

class BookingForm(forms.ModelForm):
    visit_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Tanggal Kunjungan"
    )

    whatsapp = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nomor WhatsApp Anda'}),
        label="Nomor WhatsApp",
        help_text="Gunakan format angka saja, tanpa spasi atau tanda (-).",
    )

    pax = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Jumlah orang'}),
        label="Jumlah Orang",
        validators=[MinValueValidator(1)],
        help_text="Minimal 1 orang.",
    )

    def clean_whatsapp(self):
        """ Validasi nomor WhatsApp hanya boleh berisi angka """
        whatsapp = self.cleaned_data.get('whatsapp')
        if not re.fullmatch(r'^\d+$', whatsapp):
            raise forms.ValidationError("Nomor WhatsApp hanya boleh berisi angka.")
        return whatsapp

    def clean_email(self):
        """ Validasi email harus mengandung '@' """
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError("Alamat email harus mengandung simbol '@'.")
        return email

    class Meta:
        model = Booking
        fields = ['name', 'email', 'whatsapp', 'address', 'pax', 'visit_date', 'payment_method']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama lengkap Anda'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan alamat email Anda'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Masukkan alamat lengkap Anda', 'rows': 3}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nama Lengkap',
            'email': 'Alamat Email',
            'address': 'Alamat',
            'payment_method': 'Metode Pembayaran',
        }
