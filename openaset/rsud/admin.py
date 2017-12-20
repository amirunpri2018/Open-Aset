### $Id: admin.py,v 1.31 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahRSUD, KontrakTanahRSUD, HargaTanahRSUD, TanahUsulHapusRSUD, TahunBerkurangUsulHapusTanahRSUD

from umum.models import TanahPenghapusanRSUD, TahunBerkurangTanahRSUD, PenghapusanTanahRSUD

from umum.models import SKPDAsalTanahRSUD, SKPDTujuanTanahRSUD, FotoTanahRSUD

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanRSUD, KontrakGedungBangunanRSUD, HargaGedungBangunanRSUD, GedungBangunanRuanganRSUD, GedungBangunanUsulHapusRSUD, TahunBerkurangUsulHapusGedungRSUD

from gedungbangunan.models import GedungBangunanPenghapusanRSUD, TahunBerkurangGedungBangunanRSUD, PenghapusanGedungBangunanRSUD

from gedungbangunan.models import SKPDAsalGedungBangunanRSUD, SKPDTujuanGedungBangunanRSUD, FotoGedungBangunanRSUD

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinRSUD, KontrakPeralatanMesinRSUD, HargaPeralatanMesinRSUD, PeralatanMesinUsulHapusRSUD, TahunBerkurangUsulHapusPeralatanMesinRSUD

from peralatanmesin.models import PeralatanMesinPenghapusanRSUD, TahunBerkurangPeralatanMesinRSUD, PenghapusanPeralatanMesinRSUD

from peralatanmesin.models import SKPDAsalPeralatanMesinRSUD, SKPDTujuanPeralatanMesinRSUD, FotoPeralatanMesinRSUD

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahRSUDInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahRSUD



class PenghapusanTanahRSUDInline(PenghapusanTanahInline):
    model = PenghapusanTanahRSUD



class SKPDAsalTanahRSUDInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahRSUD



class SKPDTujuanTanahRSUDInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahRSUD



class FotoTanahRSUDInline(FotoTanahInline):
    model = FotoTanahRSUD



class GedungBangunanRSUDInline(GedungBangunanInline):
    model = GedungBangunanRSUD



class HargaTanahRSUDInline(HargaTanahInline):
    model = HargaTanahRSUD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=6)
        return super(HargaTanahRSUDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahRSUDInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahRSUD


class TanahRSUDAdmin(TanahAdmin):
    inlines = [HargaTanahRSUDInline,
                SKPDAsalTanahRSUDInline,
                FotoTanahRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        return super(TanahRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusRSUDAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahRSUDInline,
                SKPDAsalTanahRSUDInline,
                FotoTanahRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahRSUDAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=6)
        return super(KontrakTanahRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=6)



class HargaTanahRSUDAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanRSUDAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahRSUDInline, TahunBerkurangTanahRSUDInline,
                    SKPDAsalTanahRSUDInline,
                    SKPDTujuanTanahRSUDInline,
                    FotoTanahRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah RSUD
admin.site.register(TanahRSUD, TanahRSUDAdmin)
admin.site.register(TanahUsulHapusRSUD, TanahUsulHapusRSUDAdmin)
admin.site.register(KontrakTanahRSUD, KontrakTanahRSUDAdmin)
admin.site.register(HargaTanahRSUD, HargaTanahRSUDAdmin)
admin.site.register(TanahPenghapusanRSUD, TanahPenghapusanRSUDAdmin)



from gedungbangunan.models import KDPGedungBangunanRSUD


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanRSUDInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanRSUD



class PenghapusanGedungBangunanRSUDInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanRSUD



class SKPDAsalGedungBangunanRSUDInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanRSUD



class SKPDTujuanGedungBangunanRSUDInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanRSUD



class FotoGedungBangunanRSUDInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanRSUD



class HargaGedungBangunanRSUDInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanRSUD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=6)
        return super(HargaGedungBangunanRSUDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungRSUDInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungRSUD


class GedungBangunanRSUDAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanRSUDInline,
                SKPDAsalGedungBangunanRSUDInline,
                FotoGedungBangunanRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        return super(GedungBangunanRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanRSUDAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanRSUDInline,
                SKPDAsalGedungBangunanRSUDInline,
                FotoGedungBangunanRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        return super(KDPGedungBangunanRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganRSUDAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusRSUDAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungRSUDInline,
                    SKPDAsalGedungBangunanRSUDInline,
                    FotoGedungBangunanRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanRSUDAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=6)
        return super(KontrakGedungBangunanRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=6)



class HargaGedungBangunanRSUDAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanRSUDAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanRSUDInline, TahunBerkurangGedungBangunanRSUDInline,
                    SKPDAsalGedungBangunanRSUDInline,
                    SKPDTujuanGedungBangunanRSUDInline,
                    FotoGedungBangunanRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan RSUD
admin.site.register(GedungBangunanRSUD, GedungBangunanRSUDAdmin)
admin.site.register(KDPGedungBangunanRSUD, KDPGedungBangunanRSUDAdmin)
admin.site.register(GedungBangunanRuanganRSUD, GedungBangunanRuanganRSUDAdmin)
admin.site.register(GedungBangunanUsulHapusRSUD, GedungBangunanUsulHapusRSUDAdmin)
admin.site.register(KontrakGedungBangunanRSUD, KontrakGedungBangunanRSUDAdmin)
admin.site.register(HargaGedungBangunanRSUD, HargaGedungBangunanRSUDAdmin)
admin.site.register(GedungBangunanPenghapusanRSUD, GedungBangunanPenghapusanRSUDAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinRSUDInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinRSUD



class PenghapusanPeralatanMesinRSUDInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinRSUD



class SKPDAsalPeralatanMesinRSUDInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinRSUD



class SKPDTujuanPeralatanMesinRSUDInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinRSUD



class FotoPeralatanMesinRSUDInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinRSUD



class HargaPeralatanMesinRSUDInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinRSUD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=6)
        return super(HargaPeralatanMesinRSUDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinRSUDInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinRSUD


class PeralatanMesinRSUDAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinRSUDInline,
                    SKPDAsalPeralatanMesinRSUDInline,
                    FotoPeralatanMesinRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=6)
        return super(PeralatanMesinRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusRSUDAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinRSUDInline,
                    SKPDAsalPeralatanMesinRSUDInline,
                    FotoPeralatanMesinRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinRSUDAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=6)
        return super(KontrakPeralatanMesinRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=6)



class HargaPeralatanMesinRSUDAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanRSUDAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinRSUDInline, TahunBerkurangPeralatanMesinRSUDInline,
                    SKPDAsalPeralatanMesinRSUDInline,
                    SKPDTujuanPeralatanMesinRSUDInline,
                    FotoPeralatanMesinRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin RSUD
admin.site.register(PeralatanMesinRSUD, PeralatanMesinRSUDAdmin)
admin.site.register(PeralatanMesinUsulHapusRSUD, PeralatanMesinUsulHapusRSUDAdmin)
admin.site.register(KontrakPeralatanMesinRSUD, KontrakPeralatanMesinRSUDAdmin)
admin.site.register(HargaPeralatanMesinRSUD, HargaPeralatanMesinRSUDAdmin)
admin.site.register(PeralatanMesinPenghapusanRSUD, PeralatanMesinPenghapusanRSUDAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanRSUD, KontrakJalanIrigasiJaringanRSUD, HargaJalanIrigasiJaringanRSUD, KDPJalanIrigasiJaringanRSUD, JalanIrigasiJaringanUsulHapusRSUD, TahunBerkurangUsulHapusJalanIrigasiJaringanRSUD

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanRSUD, TahunBerkurangJalanIrigasiJaringanRSUD, PenghapusanJalanIrigasiJaringanRSUD

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanRSUD, SKPDTujuanJalanIrigasiJaringanRSUD, FotoJalanIrigasiJaringanRSUD

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanRSUDInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanRSUD



class PenghapusanJalanIrigasiJaringanRSUDInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanRSUD



class SKPDAsalJalanIrigasiJaringanRSUDInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanRSUD



class SKPDTujuanJalanIrigasiJaringanRSUDInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanRSUD



class FotoJalanIrigasiJaringanRSUDInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanRSUD





class HargaJalanIrigasiJaringanRSUDInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanRSUD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=6)
        return super(HargaJalanIrigasiJaringanRSUDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanRSUDInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanRSUD


class JalanIrigasiJaringanRSUDAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanRSUDInline,
                    SKPDAsalJalanIrigasiJaringanRSUDInline,
                    FotoJalanIrigasiJaringanRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        return super(JalanIrigasiJaringanRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusRSUDAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanRSUDInline,
                    SKPDAsalJalanIrigasiJaringanRSUDInline,
                    FotoJalanIrigasiJaringanRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanRSUDAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanRSUDInline,
                    SKPDAsalJalanIrigasiJaringanRSUDInline,
                    FotoJalanIrigasiJaringanRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        return super(KDPJalanIrigasiJaringanRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanRSUDAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=6)
        return super(KontrakJalanIrigasiJaringanRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=6)



class HargaJalanIrigasiJaringanRSUDAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanRSUDAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanRSUDInline, TahunBerkurangJalanIrigasiJaringanRSUDInline,
                    SKPDAsalJalanIrigasiJaringanRSUDInline,
                    SKPDTujuanJalanIrigasiJaringanRSUDInline,
                    FotoJalanIrigasiJaringanRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan RSUD
admin.site.register(JalanIrigasiJaringanRSUD, JalanIrigasiJaringanRSUDAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusRSUD, JalanIrigasiJaringanUsulHapusRSUDAdmin)
admin.site.register(KDPJalanIrigasiJaringanRSUD, KDPJalanIrigasiJaringanRSUDAdmin)
admin.site.register(KontrakJalanIrigasiJaringanRSUD, KontrakJalanIrigasiJaringanRSUDAdmin)
admin.site.register(HargaJalanIrigasiJaringanRSUD, HargaJalanIrigasiJaringanRSUDAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanRSUD, JalanIrigasiJaringanPenghapusanRSUDAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLRSUD, KontrakATLRSUD, HargaATLRSUD, ATLUsulHapusRSUD, TahunBerkurangUsulHapusATLRSUD

from atl.models import ATLPenghapusanRSUD, TahunBerkurangATLRSUD, PenghapusanATLRSUD

from atl.models import SKPDAsalATLRSUD, SKPDTujuanATLRSUD, FotoATLRSUD

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLRSUDInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLRSUD



class PenghapusanATLRSUDInline(PenghapusanATLInline):
    model = PenghapusanATLRSUD



class SKPDAsalATLRSUDInline(SKPDAsalATLInline):
    model = SKPDAsalATLRSUD



class SKPDTujuanATLRSUDInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLRSUD



class FotoATLRSUDInline(FotoATLInline):
    model = FotoATLRSUD



class HargaATLRSUDInline(HargaATLInline):
    model = HargaATLRSUD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=6)
        return super(HargaATLRSUDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLRSUDInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLRSUD


class ATLRSUDAdmin(ATLAdmin):
    inlines = [HargaATLRSUDInline,
                    SKPDAsalATLRSUDInline,
                    FotoATLRSUDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=6)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=6)
        return super(ATLRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusRSUDAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLRSUDInline,
                    SKPDAsalATLRSUDInline,
                    FotoATLRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLRSUDAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=6)
        return super(KontrakATLRSUDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=6)



class HargaATLRSUDAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanRSUDAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLRSUDInline, TahunBerkurangATLRSUDInline,
                    SKPDAsalATLRSUDInline,
                    SKPDTujuanATLRSUDInline,
                    FotoATLRSUDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=6)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL RSUD
admin.site.register(ATLRSUD, ATLRSUDAdmin)
admin.site.register(ATLUsulHapusRSUD, ATLUsulHapusRSUDAdmin)
admin.site.register(KontrakATLRSUD, KontrakATLRSUDAdmin)
admin.site.register(HargaATLRSUD, HargaATLRSUDAdmin)
admin.site.register(ATLPenghapusanRSUD, ATLPenghapusanRSUDAdmin)
