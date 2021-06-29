from website import celery_app
from stnk.models import Asset
from django.utils import timezone

@celery_app.task
def test(arg):
    print(arg)
    return arg


@celery_app.task
def update_stnk_status():
    waktu_sekrang = timezone.now()
    waktu_peringatan = waktu_sekrang - timezone.timedelta(days=30)
    assets = Asset.objects.filter(masa_aktif__range=(waktu_peringatan, waktu_sekrang))
    
    for asset in assets:
        asset.status = 'peringatan'
        asset.save()

    return 'Selesai....'
