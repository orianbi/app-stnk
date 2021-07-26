from import_export import resources
from .models import Asset
from import_export.fields import Field


class AssetResource(resources.ModelResource):
    opd__nama_opd = Field(attribute='opd', column_name='Nama Opd')
    kode_barang = Field(attribute='kode_barang',column_name='Kode Barang')
    nama_barang = Field(attribute='nama_barang',column_name='Nama Barang')
    nomor_register = Field(attribute='nomor_register',column_name='Nomor Register')

    class Meta:
        model = Asset
        fields = ['opd__nama_opd', 'kode_barang', 'nama_barang', 'nomor_register', 'tahun_pembelian','nomor_polisi', 'bpkb', 'harga', 'status','masa_aktif',]
        export_order = ('opd__nama_opd', 'kode_barang', 'nama_barang', 'nomor_register', 'tahun_pembelian','nomor_polisi', 'bpkb', 'harga', 'status','masa_aktif',)
