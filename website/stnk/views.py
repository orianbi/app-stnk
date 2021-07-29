from django.shortcuts import render,redirect,reverse, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Opd, Asset, Profile
from .forms import FormOpd, FormAsset, FormUser, InfoUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .resources import AssetResource
from django.contrib.auth.models import User





# # Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def user(request):
    judul = "Halaman User"
    users = User.objects.all()

    konteks = {
        'judul': judul,
        'users':users,
    }


    return render(request,'stnk/user.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambahUser(request):
    judul = "Halaman Tambah User"
    if request.method == 'POST':
        user_form = FormUser(request.POST)
        role = InfoUser(request.POST)       
        if user_form.is_valid() and role.is_valid():
            user = user_form.save()
            user.save()
            prof = role.save(commit=False)
            prof.user = user
            prof.save()            

            return redirect('user')
    else:
       user_form = FormUser()
       role = InfoUser()

    konteks = {
        'judul':judul,
        'user_form':user_form,
        'role':role,
        
    }
    return render(request,'stnk/tambah_user.html',konteks)

@login_required(login_url=settings.LOGIN_URL)
def editUser(request, id):
    users = User.objects.get(id=id)
    user_form = FormUser(instance=users)
    if request.method == 'POST':
        user_form = FormUser(request.POST, instance=users)
        if user_form.is_valid():
            user_form.save()
            return redirect('user')
    konteks = {
        'user_form':user_form,
    }

    return render(request, 'stnk/edit_user.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapusUser(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('user')
@login_required(login_url=settings.LOGIN_URL)
def exportExcel(request):
    assets = AssetResource()
    dataset = assets.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=asset.xls'
    return response


@login_required(login_url=settings.LOGIN_URL)
def home(request):
    judul = "Halaman Home"
    assets = Asset.objects.all()  
    assets_hidup = assets.filter(status='hidup').count()
    assets_peringatan = assets.filter(status='peringatan').count()
    assets_mati = assets.filter(status='mati').count()

    konteks = {
        'judul':judul,
        'assets':assets,
        'assets_hidup':assets_hidup,
        'assets_peringatan':assets_peringatan,
        'assets_mati':assets_mati,
    }

    return render(request,'stnk/home.html', konteks)
@login_required(login_url=settings.LOGIN_URL)
def statusPeringatan(request):
    judul = "Detail Status Peringatan"

    detail_peringatan = Asset.objects.filter(status='peringatan')
    
    konteks = {
        'judul':judul,
        'detail_peringatan':detail_peringatan,        
    }


    return render(request, 'stnk/status_peringatan.html', konteks)
@login_required(login_url=settings.LOGIN_URL)
def statusMati(request):
    judul = "Detail Status Mati"

    detail_mati = Asset.objects.filter(status='mati')
    
    konteks = {
        'judul':judul,
        'detail_mati':detail_mati,        
    }


    return render(request, 'stnk/status_mati.html', konteks)

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


  


