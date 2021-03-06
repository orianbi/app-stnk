from django import forms
from django.forms import ModelForm
from .models import Opd, Asset, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class FormOpd(ModelForm):

    class Meta:
        model = Opd
        fields = '__all__'

        widgets = {
            'nama_opd': forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
        } 

        labels = {
            'nama_opd':'NAMA OPD',
        }

class FormAsset(ModelForm):

    class Meta:
        model = Asset
        fields = '__all__'

        widgets = {
            'opd':forms.Select(attrs={'class':'form-control'}),
            'kode_barang':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'nama_barang':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'nama_pemegang':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'nomor_register':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'tahun_pembelian':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'nomor_polisi':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'bpkb':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'harga':forms.NumberInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'roda':forms.TextInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'bpkb_disimpan':forms.Select(attrs={'class':'form-control',"autocomplete":"off"}),
            'pajak': forms.DateInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'pengesahan':forms.NumberInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'penggantian_stnk':forms.NumberInput(attrs={'class':'form-control',"autocomplete":"off"}),
            'kondisi':forms.Select(attrs={'class':'form-control',"autocomplete":"off"}),
            'status':forms.Select(attrs={'class':'form-control',"autocomplete":"off"}),
            'masa_aktif': forms.DateTimeInput(attrs={'class':'form-control',"autocomplete":"off"})
        } 

        labels = {
            'opd':'OPD',
            'kode_barang':'KODE BARANG',
            'nama_barang':'NAMA BARANG',
            'nama_pemegang':'NAMA PEMEGANG',
            'nomor_register':'NOMOR REGISTER',
            'tahun_pembelian':'TAHUN PEMBELIAN',
            'nomor_polisi':'NOMOR POLISI',
            'bpkb':'BPKB',
            'harga':'HARGA',
            'roda':'RODA',
            'bpkb_disimpan':'BPKB DISIMPAN',
            'pajak':'PAJAK',
            'pengesahan':'PENGESAHAN',
            'penggantian_stnk':'PENGGANTIAN STNK',
            'kondisi':'KONDISI',
            'status':'STATUS',
            'masa_aktif':'MASA AKTIF',
        }

class FormUser(UserCreationForm):        
    class Meta:
         model = User
         fields = ('username','email','password1','password2',)

         widgets = {
            "username": forms.TextInput({"class": "form-control"}),
            "email": forms.EmailInput({"class": "form-control"}),            
            "password1": forms.PasswordInput({"class": "form-control"}),
            "password2": forms.PasswordInput({"class": "form-control"}),
        }

         labels = {
            'username': _('Username'),            
            'email': _('Email')
            
        }


class InfoUser(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('role',)

        widgets = {
            'role':forms.Select(attrs={'class':'form-control',"autocomplete":"off"}),          
        }

        labels = {                     
            'role':'Level User',

         }