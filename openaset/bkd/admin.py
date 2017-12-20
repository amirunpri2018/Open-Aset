### $Id: admin.py,v 1.30 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBKD, KontrakTanahBKD, HargaTanahBKD, TanahUsulHapusBKD, TahunBerkurangUsulHapusTanahBKD

from umum.models import TanahPenghapusanBKD, TahunBerkurangTanahBKD, PenghapusanTanahBKD

from umum.models import SKPDAsalTanahBKD, SKPDTujuanTanahBKD, FotoTanahBKD

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBKD, KontrakGedungBangunanBKD, HargaGedungBangunanBKD, GedungBangunanRuanganBKD, GedungBangunanUsulHapusBKD, TahunBerkurangUsulHapusGedungBKD

from gedungbangunan.models import GedungBangunanPenghapusanBKD, TahunBerkurangGedungBangunanBKD, PenghapusanGedungBangunanBKD

from gedungbangunan.models import SKPDAsalGedungBangunanBKD, SKPDTujuanGedungBangunanBKD, FotoGedungBangunanBKD

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBKD, KontrakPeralatanMesinBKD, HargaPeralatanMesinBKD, PeralatanMesinUsulHapusBKD, TahunBerkurangUsulHapusPeralatanMesinBKD

from peralatanmesin.models import PeralatanMesinPenghapusanBKD, TahunBerkurangPeralatanMesinBKD, PenghapusanPeralatanMesinBKD

from peralatanmesin.models import SKPDAsalPeralatanMesinBKD, SKPDTujuanPeralatanMesinBKD, FotoPeralatanMesinBKD

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBKDInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBKD



class PenghapusanTanahBKDInline(PenghapusanTanahInline):
    model = PenghapusanTanahBKD



class SKPDAsalTanahBKDInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBKD



class SKPDTujuanTanahBKDInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBKD



class FotoTanahBKDInline(FotoTanahInline):
    model = FotoTanahBKD



class GedungBangunanBKDInline(GedungBangunanInline):
    model = GedungBangunanBKD



class HargaTanahBKDInline(HargaTanahInline):
    model = HargaTanahBKD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=19)
        return super(HargaTanahBKDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBKDInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBKD


class TanahBKDAdmin(TanahAdmin):
    inlines = [HargaTanahBKDInline,
                SKPDAsalTanahBKDInline,
                FotoTanahBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        return super(TanahBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBKDAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBKDInline,
                SKPDAsalTanahBKDInline,
                FotoTanahBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBKDAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=19)
        return super(KontrakTanahBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=19)



class HargaTanahBKDAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBKDAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBKDInline, TahunBerkurangTanahBKDInline,
                    SKPDAsalTanahBKDInline,
                    SKPDTujuanTanahBKDInline,
                    FotoTanahBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah BKD
admin.site.register(TanahBKD, TanahBKDAdmin)
admin.site.register(TanahUsulHapusBKD, TanahUsulHapusBKDAdmin)
admin.site.register(KontrakTanahBKD, KontrakTanahBKDAdmin)
admin.site.register(HargaTanahBKD, HargaTanahBKDAdmin)
admin.site.register(TanahPenghapusanBKD, TanahPenghapusanBKDAdmin)



from gedungbangunan.models import KDPGedungBangunanBKD


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBKDInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBKD



class PenghapusanGedungBangunanBKDInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBKD



class SKPDAsalGedungBangunanBKDInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBKD



class SKPDTujuanGedungBangunanBKDInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBKD



class FotoGedungBangunanBKDInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBKD



class HargaGedungBangunanBKDInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBKD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=19)
        return super(HargaGedungBangunanBKDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBKDInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBKD


class GedungBangunanBKDAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBKDInline,
                SKPDAsalGedungBangunanBKDInline,
                FotoGedungBangunanBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        return super(GedungBangunanBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBKDAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBKDInline,
                SKPDAsalGedungBangunanBKDInline,
                FotoGedungBangunanBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        return super(KDPGedungBangunanBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBKDAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBKDAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBKDInline,
                    SKPDAsalGedungBangunanBKDInline,
                    FotoGedungBangunanBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBKDAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=19)
        return super(KontrakGedungBangunanBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=19)



class HargaGedungBangunanBKDAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBKDAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBKDInline, TahunBerkurangGedungBangunanBKDInline,
                    SKPDAsalGedungBangunanBKDInline,
                    SKPDTujuanGedungBangunanBKDInline,
                    FotoGedungBangunanBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan BKD
admin.site.register(GedungBangunanBKD, GedungBangunanBKDAdmin)
admin.site.register(KDPGedungBangunanBKD, KDPGedungBangunanBKDAdmin)
admin.site.register(GedungBangunanRuanganBKD, GedungBangunanRuanganBKDAdmin)
admin.site.register(GedungBangunanUsulHapusBKD, GedungBangunanUsulHapusBKDAdmin)
admin.site.register(KontrakGedungBangunanBKD, KontrakGedungBangunanBKDAdmin)
admin.site.register(HargaGedungBangunanBKD, HargaGedungBangunanBKDAdmin)
admin.site.register(GedungBangunanPenghapusanBKD, GedungBangunanPenghapusanBKDAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBKDInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBKD



class PenghapusanPeralatanMesinBKDInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBKD



class SKPDAsalPeralatanMesinBKDInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBKD



class SKPDTujuanPeralatanMesinBKDInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBKD



class FotoPeralatanMesinBKDInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBKD



class HargaPeralatanMesinBKDInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBKD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=19)
        return super(HargaPeralatanMesinBKDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBKDInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBKD


class PeralatanMesinBKDAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBKDInline,
                    SKPDAsalPeralatanMesinBKDInline,
                    FotoPeralatanMesinBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=19)
        return super(PeralatanMesinBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBKDAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBKDInline,
                    SKPDAsalPeralatanMesinBKDInline,
                    FotoPeralatanMesinBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBKDAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=19)
        return super(KontrakPeralatanMesinBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=19)



class HargaPeralatanMesinBKDAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBKDAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBKDInline, TahunBerkurangPeralatanMesinBKDInline,
                    SKPDAsalPeralatanMesinBKDInline,
                    SKPDTujuanPeralatanMesinBKDInline,
                    FotoPeralatanMesinBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin BKD
admin.site.register(PeralatanMesinBKD, PeralatanMesinBKDAdmin)
admin.site.register(PeralatanMesinUsulHapusBKD, PeralatanMesinUsulHapusBKDAdmin)
admin.site.register(KontrakPeralatanMesinBKD, KontrakPeralatanMesinBKDAdmin)
admin.site.register(HargaPeralatanMesinBKD, HargaPeralatanMesinBKDAdmin)
admin.site.register(PeralatanMesinPenghapusanBKD, PeralatanMesinPenghapusanBKDAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBKD, KontrakJalanIrigasiJaringanBKD, HargaJalanIrigasiJaringanBKD, KDPJalanIrigasiJaringanBKD, JalanIrigasiJaringanUsulHapusBKD, TahunBerkurangUsulHapusJalanIrigasiJaringanBKD

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBKD, TahunBerkurangJalanIrigasiJaringanBKD, PenghapusanJalanIrigasiJaringanBKD

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBKD, SKPDTujuanJalanIrigasiJaringanBKD, FotoJalanIrigasiJaringanBKD

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBKDInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBKD



class PenghapusanJalanIrigasiJaringanBKDInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBKD



class SKPDAsalJalanIrigasiJaringanBKDInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBKD



class SKPDTujuanJalanIrigasiJaringanBKDInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBKD



class FotoJalanIrigasiJaringanBKDInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBKD





class HargaJalanIrigasiJaringanBKDInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBKD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=19)
        return super(HargaJalanIrigasiJaringanBKDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBKDInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBKD


class JalanIrigasiJaringanBKDAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBKDInline,
                    SKPDAsalJalanIrigasiJaringanBKDInline,
                    FotoJalanIrigasiJaringanBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        return super(JalanIrigasiJaringanBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBKDAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBKDInline,
                    SKPDAsalJalanIrigasiJaringanBKDInline,
                    FotoJalanIrigasiJaringanBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBKDAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBKDInline,
                    SKPDAsalJalanIrigasiJaringanBKDInline,
                    FotoJalanIrigasiJaringanBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        return super(KDPJalanIrigasiJaringanBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBKDAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=19)
        return super(KontrakJalanIrigasiJaringanBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=19)



class HargaJalanIrigasiJaringanBKDAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBKDAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBKDInline, TahunBerkurangJalanIrigasiJaringanBKDInline,
                    SKPDAsalJalanIrigasiJaringanBKDInline,
                    SKPDTujuanJalanIrigasiJaringanBKDInline,
                    FotoJalanIrigasiJaringanBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan BKD
admin.site.register(JalanIrigasiJaringanBKD, JalanIrigasiJaringanBKDAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBKD, JalanIrigasiJaringanUsulHapusBKDAdmin)
admin.site.register(KDPJalanIrigasiJaringanBKD, KDPJalanIrigasiJaringanBKDAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBKD, KontrakJalanIrigasiJaringanBKDAdmin)
admin.site.register(HargaJalanIrigasiJaringanBKD, HargaJalanIrigasiJaringanBKDAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBKD, JalanIrigasiJaringanPenghapusanBKDAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBKD, KontrakATLBKD, HargaATLBKD, ATLUsulHapusBKD, TahunBerkurangUsulHapusATLBKD

from atl.models import ATLPenghapusanBKD, TahunBerkurangATLBKD, PenghapusanATLBKD

from atl.models import SKPDAsalATLBKD, SKPDTujuanATLBKD, FotoATLBKD

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBKDInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBKD



class PenghapusanATLBKDInline(PenghapusanATLInline):
    model = PenghapusanATLBKD



class SKPDAsalATLBKDInline(SKPDAsalATLInline):
    model = SKPDAsalATLBKD



class SKPDTujuanATLBKDInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBKD



class FotoATLBKDInline(FotoATLInline):
    model = FotoATLBKD



class HargaATLBKDInline(HargaATLInline):
    model = HargaATLBKD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=19)
        return super(HargaATLBKDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBKDInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBKD


class ATLBKDAdmin(ATLAdmin):
    inlines = [HargaATLBKDInline,
                    SKPDAsalATLBKDInline,
                    FotoATLBKDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=19)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=19)
        return super(ATLBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBKDAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBKDInline,
                    SKPDAsalATLBKDInline,
                    FotoATLBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBKDAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=19)
        return super(KontrakATLBKDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=19)



class HargaATLBKDAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBKDAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBKDInline, TahunBerkurangATLBKDInline,
                    SKPDAsalATLBKDInline,
                    SKPDTujuanATLBKDInline,
                    FotoATLBKDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=19)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL BKD
admin.site.register(ATLBKD, ATLBKDAdmin)
admin.site.register(ATLUsulHapusBKD, ATLUsulHapusBKDAdmin)
admin.site.register(KontrakATLBKD, KontrakATLBKDAdmin)
admin.site.register(HargaATLBKD, HargaATLBKDAdmin)
admin.site.register(ATLPenghapusanBKD, ATLPenghapusanBKDAdmin)
