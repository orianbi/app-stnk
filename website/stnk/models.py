from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Opd(models.Model):
    nama_opd = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_opd

class Asset(models.Model):
    ket_bpkb = (
        ('BPKAD','BPKAD'),
        ('HILANG','HILANG',),
        ('OPD', 'OPD',),
    )
    kon = (
        ('B', 'B'),
        ('RR', 'RR'),
        ('RB', 'RB'),
    )
    stts = (
        ('hidup','hidup'),
        ('mati','mati'),
        ('peringatan','peringatan'),
    )

    opd              = models.ForeignKey(Opd, on_delete=models.CASCADE)
    kode_barang      = models.CharField(max_length=15)
    nama_barang      = models.CharField(max_length=255)
    nama_pemegang    = models.CharField(max_length=100)
    nomor_register   = models.IntegerField()
    tahun_pembelian  = models.IntegerField()    
    nomor_polisi     = models.CharField(max_length=100)
    bpkb             = models.CharField(max_length=100)
    harga            = models.DecimalField(max_digits=15, decimal_places=2)    
    roda             = models.IntegerField()
    bpkb_disimpan    = models.CharField(choices=ket_bpkb, max_length=100)
    pajak            = models.DateField()
    pengesahan       = models.DecimalField(max_digits=15, decimal_places=2)
    penggantian_stnk = models.DecimalField(max_digits=15, decimal_places=2)
    kondisi          = models.CharField(choices=kon, max_length=100)
    status            = models.CharField(max_length=200, null=True, choices=stts)
    masa_aktif       = models.DateTimeField()


    def __str__(self):
        return self.nama_barang

class Profile(models.Model):

    ROLE_CHOICES = (
        ('Admin','Admin'),
        ('Supervisor','Supervisor'),
        ('User','User')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

  
