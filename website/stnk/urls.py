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
]


