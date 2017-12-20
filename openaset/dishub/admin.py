### $Id: admin.py,v 1.30 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDishub, KontrakTanahDishub, HargaTanahDishub, TanahUsulHapusDishub, TahunBerkurangUsulHapusTanahDishub

from umum.models import TanahPenghapusanDishub, TahunBerkurangTanahDishub, PenghapusanTanahDishub

from umum.models import SKPDAsalTanahDishub, SKPDTujuanTanahDishub, FotoTanahDishub

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDishub, KontrakGedungBangunanDishub, HargaGedungBangunanDishub, GedungBangunanRuanganDishub, GedungBangunanUsulHapusDishub, TahunBerkurangUsulHapusGedungDishub

from gedungbangunan.models import GedungBangunanPenghapusanDishub, TahunBerkurangGedungBangunanDishub, PenghapusanGedungBangunanDishub

from gedungbangunan.models import SKPDAsalGedungBangunanDishub, SKPDTujuanGedungBangunanDishub, FotoGedungBangunanDishub

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDishub, KontrakPeralatanMesinDishub, HargaPeralatanMesinDishub, PeralatanMesinUsulHapusDishub, TahunBerkurangUsulHapusPeralatanMesinDishub

from peralatanmesin.models import PeralatanMesinPenghapusanDishub, TahunBerkurangPeralatanMesinDishub, PenghapusanPeralatanMesinDishub

from peralatanmesin.models import SKPDAsalPeralatanMesinDishub, SKPDTujuanPeralatanMesinDishub, FotoPeralatanMesinDishub

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDishubInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDishub



class PenghapusanTanahDishubInline(PenghapusanTanahInline):
    model = PenghapusanTanahDishub



class SKPDAsalTanahDishubInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDishub



class SKPDTujuanTanahDishubInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDishub



class FotoTanahDishubInline(FotoTanahInline):
    model = FotoTanahDishub



class GedungBangunanDishubInline(GedungBangunanInline):
    model = GedungBangunanDishub



class HargaTanahDishubInline(HargaTanahInline):
    model = HargaTanahDishub

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=4)
        return super(HargaTanahDishubInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDishubInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDishub


class TanahDishubAdmin(TanahAdmin):
    inlines = [HargaTanahDishubInline,
                SKPDAsalTanahDishubInline,
                FotoTanahDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        return super(TanahDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDishubAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDishubInline,
                SKPDAsalTanahDishubInline,
                FotoTanahDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDishubAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=4)
        return super(KontrakTanahDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=4)



class HargaTanahDishubAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDishubAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDishubInline, TahunBerkurangTanahDishubInline,
                    SKPDAsalTanahDishubInline,
                    SKPDTujuanTanahDishubInline,
                    FotoTanahDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Dishub
admin.site.register(TanahDishub, TanahDishubAdmin)
admin.site.register(TanahUsulHapusDishub, TanahUsulHapusDishubAdmin)
admin.site.register(KontrakTanahDishub, KontrakTanahDishubAdmin)
admin.site.register(HargaTanahDishub, HargaTanahDishubAdmin)
admin.site.register(TanahPenghapusanDishub, TanahPenghapusanDishubAdmin)



from gedungbangunan.models import KDPGedungBangunanDishub


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDishubInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDishub



class PenghapusanGedungBangunanDishubInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDishub



class SKPDAsalGedungBangunanDishubInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDishub



class SKPDTujuanGedungBangunanDishubInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDishub



class FotoGedungBangunanDishubInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDishub



class HargaGedungBangunanDishubInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDishub

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=4)
        return super(HargaGedungBangunanDishubInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDishubInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDishub


class GedungBangunanDishubAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDishubInline,
                SKPDAsalGedungBangunanDishubInline,
                FotoGedungBangunanDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        return super(GedungBangunanDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDishubAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDishubInline,
                SKPDAsalGedungBangunanDishubInline,
                FotoGedungBangunanDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        return super(KDPGedungBangunanDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDishubAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDishubAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDishubInline,
                    SKPDAsalGedungBangunanDishubInline,
                    FotoGedungBangunanDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDishubAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=4)
        return super(KontrakGedungBangunanDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=4)



class HargaGedungBangunanDishubAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDishubAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDishubInline, TahunBerkurangGedungBangunanDishubInline,
                    SKPDAsalGedungBangunanDishubInline,
                    SKPDTujuanGedungBangunanDishubInline,
                    FotoGedungBangunanDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Dishub
admin.site.register(GedungBangunanDishub, GedungBangunanDishubAdmin)
admin.site.register(KDPGedungBangunanDishub, KDPGedungBangunanDishubAdmin)
admin.site.register(GedungBangunanRuanganDishub, GedungBangunanRuanganDishubAdmin)
admin.site.register(GedungBangunanUsulHapusDishub, GedungBangunanUsulHapusDishubAdmin)
admin.site.register(KontrakGedungBangunanDishub, KontrakGedungBangunanDishubAdmin)
admin.site.register(HargaGedungBangunanDishub, HargaGedungBangunanDishubAdmin)
admin.site.register(GedungBangunanPenghapusanDishub, GedungBangunanPenghapusanDishubAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDishubInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDishub



class PenghapusanPeralatanMesinDishubInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDishub



class SKPDAsalPeralatanMesinDishubInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDishub



class SKPDTujuanPeralatanMesinDishubInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDishub



class FotoPeralatanMesinDishubInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDishub



class HargaPeralatanMesinDishubInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDishub

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=4)
        return super(HargaPeralatanMesinDishubInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDishubInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDishub


class PeralatanMesinDishubAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDishubInline,
                    SKPDAsalPeralatanMesinDishubInline,
                    FotoPeralatanMesinDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=4)
        return super(PeralatanMesinDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDishubAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDishubInline,
                    SKPDAsalPeralatanMesinDishubInline,
                    FotoPeralatanMesinDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDishubAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=4)
        return super(KontrakPeralatanMesinDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=4)



class HargaPeralatanMesinDishubAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDishubAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDishubInline, TahunBerkurangPeralatanMesinDishubInline,
                    SKPDAsalPeralatanMesinDishubInline,
                    SKPDTujuanPeralatanMesinDishubInline,
                    FotoPeralatanMesinDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Dishub
admin.site.register(PeralatanMesinDishub, PeralatanMesinDishubAdmin)
admin.site.register(PeralatanMesinUsulHapusDishub, PeralatanMesinUsulHapusDishubAdmin)
admin.site.register(KontrakPeralatanMesinDishub, KontrakPeralatanMesinDishubAdmin)
admin.site.register(HargaPeralatanMesinDishub, HargaPeralatanMesinDishubAdmin)
admin.site.register(PeralatanMesinPenghapusanDishub, PeralatanMesinPenghapusanDishubAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDishub, KontrakJalanIrigasiJaringanDishub, HargaJalanIrigasiJaringanDishub, KDPJalanIrigasiJaringanDishub, JalanIrigasiJaringanUsulHapusDishub, TahunBerkurangUsulHapusJalanIrigasiJaringanDishub

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDishub, TahunBerkurangJalanIrigasiJaringanDishub, PenghapusanJalanIrigasiJaringanDishub

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDishub, SKPDTujuanJalanIrigasiJaringanDishub, FotoJalanIrigasiJaringanDishub

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDishubInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDishub



class PenghapusanJalanIrigasiJaringanDishubInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDishub



class SKPDAsalJalanIrigasiJaringanDishubInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDishub



class SKPDTujuanJalanIrigasiJaringanDishubInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDishub



class FotoJalanIrigasiJaringanDishubInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDishub





class HargaJalanIrigasiJaringanDishubInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDishub

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=4)
        return super(HargaJalanIrigasiJaringanDishubInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDishubInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDishub


class JalanIrigasiJaringanDishubAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDishubInline,
                    SKPDAsalJalanIrigasiJaringanDishubInline,
                    FotoJalanIrigasiJaringanDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        return super(JalanIrigasiJaringanDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDishubAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDishubInline,
                    SKPDAsalJalanIrigasiJaringanDishubInline,
                    FotoJalanIrigasiJaringanDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDishubAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDishubInline,
                    SKPDAsalJalanIrigasiJaringanDishubInline,
                    FotoJalanIrigasiJaringanDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        return super(KDPJalanIrigasiJaringanDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDishubAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=4)
        return super(KontrakJalanIrigasiJaringanDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=4)



class HargaJalanIrigasiJaringanDishubAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDishubAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDishubInline, TahunBerkurangJalanIrigasiJaringanDishubInline,
                    SKPDAsalJalanIrigasiJaringanDishubInline,
                    SKPDTujuanJalanIrigasiJaringanDishubInline,
                    FotoJalanIrigasiJaringanDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Dishub
admin.site.register(JalanIrigasiJaringanDishub, JalanIrigasiJaringanDishubAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDishub, JalanIrigasiJaringanUsulHapusDishubAdmin)
admin.site.register(KDPJalanIrigasiJaringanDishub, KDPJalanIrigasiJaringanDishubAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDishub, KontrakJalanIrigasiJaringanDishubAdmin)
admin.site.register(HargaJalanIrigasiJaringanDishub, HargaJalanIrigasiJaringanDishubAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDishub, JalanIrigasiJaringanPenghapusanDishubAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDishub, KontrakATLDishub, HargaATLDishub, ATLUsulHapusDishub, TahunBerkurangUsulHapusATLDishub

from atl.models import ATLPenghapusanDishub, TahunBerkurangATLDishub, PenghapusanATLDishub

from atl.models import SKPDAsalATLDishub, SKPDTujuanATLDishub, FotoATLDishub

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDishubInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDishub



class PenghapusanATLDishubInline(PenghapusanATLInline):
    model = PenghapusanATLDishub



class SKPDAsalATLDishubInline(SKPDAsalATLInline):
    model = SKPDAsalATLDishub



class SKPDTujuanATLDishubInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDishub



class FotoATLDishubInline(FotoATLInline):
    model = FotoATLDishub



class HargaATLDishubInline(HargaATLInline):
    model = HargaATLDishub

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=4)
        return super(HargaATLDishubInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDishubInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDishub


class ATLDishubAdmin(ATLAdmin):
    inlines = [HargaATLDishubInline,
                    SKPDAsalATLDishubInline,
                    FotoATLDishubInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=4)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=4)
        return super(ATLDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDishubAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDishubInline,
                    SKPDAsalATLDishubInline,
                    FotoATLDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDishubAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=4)
        return super(KontrakATLDishubAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=4)



class HargaATLDishubAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDishubAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDishubInline, TahunBerkurangATLDishubInline,
                    SKPDAsalATLDishubInline,
                    SKPDTujuanATLDishubInline,
                    FotoATLDishubInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=4)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Dishub
admin.site.register(ATLDishub, ATLDishubAdmin)
admin.site.register(ATLUsulHapusDishub, ATLUsulHapusDishubAdmin)
admin.site.register(KontrakATLDishub, KontrakATLDishubAdmin)
admin.site.register(HargaATLDishub, HargaATLDishubAdmin)
admin.site.register(ATLPenghapusanDishub, ATLPenghapusanDishubAdmin)
