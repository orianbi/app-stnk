from django.contrib import admin
from .models import Opd, Asset, Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','role',)

class OpdAdmin(admin.ModelAdmin):
    list_display = ('nama_opd',)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('opd', 'kode_barang', 'nama_barang', 'nomor_register', 'tahun_pembelian','nomor_polisi', 'bpkb', 'harga', 'status','masa_aktif',)

admin.site.register(Opd, OpdAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Profile, ProfileAdmin)