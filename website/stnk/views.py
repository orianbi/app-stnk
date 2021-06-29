from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Opd, Asset
from .forms import FormOpd, FormAsset
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings




# # Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def home(request):
    judul = "Halaman Home"
    assets = Asset.objects.all()
    total_assets = assets.count()
    assets_hidup = assets.filter(status='hidup').count()
    assets_mati = assets.filter(status='mati').count()

    konteks = {
        'judul':judul,
        'assets':assets,
        'total_assets':total_assets,
        'assets_hidup':assets_hidup,
        'assets_mati':assets_mati,
    }

    return render(request,'stnk/home.html', konteks)

@login_required(login_url=settings.LOGIN_URL)    
def tambahAsset(request):
    judul = "Halaman Tambah Asset"
    if request.method == 'POST':
        form = FormAsset(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('tambah_asset')

    else:
        form = FormAsset()

    konteks = {
        'judul':judul,
        'form':form,
    }
    return render(request,'stnk/tambah_asset.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapusAsset(request, id):
    assets = Asset.objects.get(id=id)
    assets.delete()
    return redirect('home')

@login_required(login_url=settings.LOGIN_URL)
def editAsset(request, id):
    assets = Asset.objects.get(id=id)
    form = FormAsset(instance= assets)
    if request.method == 'POST':
        form = FormAsset(request.POST, instance=assets)
        if form.is_valid():
            form.save()
            return redirect('home')
    isi = {'form':form}
    return render(request, 'stnk/edit_asset.html', isi)



def user_login(request):
    judul = "Halaman Login"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.warning(request,'Akun Anda Belum Aktif!!')

    
    konteks = {
        'judul':judul,
        
    }

    return render(request,'auth/login.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def user_logout(request):
    logout(request)
    messages.success(request,'Logout Berhasil!!!')
    return HttpResponseRedirect(reverse('login'))

@login_required(login_url=settings.LOGIN_URL)
def formOpd(request):
    judul = "Halaman Opd"
    opds = Opd.objects.all()
    konteks = {
        'judul':judul,
        'opds':opds,
    }
    
    return render(request, 'stnk/opd.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambahOpd(request):
    judul = "Tambah Opd"
    if request.method == "POST":
        form = FormOpd(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('opd')
        else:
            return redirect('tambah_opd')

    else:    
        form=FormOpd()
    konteks = {
        'judul':judul,
        'form':form,
    }

    return render(request,'stnk/tambah_opd.html', konteks)


  


