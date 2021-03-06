# Generated by Django 3.2.4 on 2021-06-21 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_opd', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.CharField(max_length=15)),
                ('nama_barang', models.CharField(max_length=255)),
                ('nama_pemegang', models.CharField(max_length=100)),
                ('nomor_register', models.IntegerField()),
                ('tahun_pembelian', models.IntegerField()),
                ('nomor_polisi', models.CharField(max_length=100)),
                ('bpkb', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=15)),
                ('roda', models.IntegerField()),
                ('bpkb_disimpan', models.CharField(choices=[('BPKAD', 'BPKAD'), ('HILANG', 'HILANG'), ('OPD', 'OPD')], max_length=100)),
                ('pajak', models.DateField()),
                ('pengesahan', models.DecimalField(decimal_places=2, max_digits=15)),
                ('penggantian_stnk', models.DecimalField(decimal_places=2, max_digits=15)),
                ('kondisi', models.CharField(choices=[('B', 'B'), ('RR', 'RR'), ('RB', 'RB')], max_length=100)),
                ('aktif', models.BooleanField(default=False)),
                ('masa_aktif', models.DateField()),
                ('opd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stnk.opd')),
            ],
        ),
    ]
