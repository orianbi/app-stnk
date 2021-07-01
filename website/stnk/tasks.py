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
    waktu_peringatan = waktu_sekrang + timezone.timedelta(days=30)
    assets_peringatan = Asset.objects.filter(masa_aktif__range=(waktu_sekrang, waktu_peringatan))
    for asset_p in assets_peringatan:
        asset_p.status = 'peringatan'
        asset_p.save() 


    # if assets_peringatan:
        
    #     assets_peringatan.save()
    # if assets_mati:
       
    #     assets_mati.save()


    assets_mati = Asset.objects.filter(status__in=['hidup', 'peringatan'], masa_aktif__date__lt=waktu_sekrang)
    for asset_m in assets_mati:
        asset_m.status = 'mati'
        asset_m.save()


    return 'Selesai....'
      
   