from django.urls import path

from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('opd/', views.formOpd, name='opd'),
    path('tambah_opd/', views.tambahOpd, name='tambah_opd'),
    path('tambah_asset/', views.tambahAsset, name='tambah_asset'),
    path('hapus/<int:id>/', views.hapusAsset, name='hapus-asset'),
    path('edit/<int:id>/', views.editAsset, name='edit-asset'),
    path('detail_peringatan/', views.statusPeringatan, name='detail_peringatan'),
    path('detail_mati/', views.statusMati, name='detail_mati'),
    path('export_excel/', views.exportExcel, name='export_excel'),
    path('user/', views.user, name='user'),
    path('tambah_user/', views.tambahUser, name='tambah_user'),
]


