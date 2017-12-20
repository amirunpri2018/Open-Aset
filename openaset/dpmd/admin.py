### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDPMD, KontrakTanahDPMD, HargaTanahDPMD, TanahUsulHapusDPMD, TahunBerkurangUsulHapusTanahDPMD

from umum.models import TanahPenghapusanDPMD, TahunBerkurangTanahDPMD, PenghapusanTanahDPMD

from umum.models import SKPDAsalTanahDPMD, SKPDTujuanTanahDPMD, FotoTanahDPMD

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDPMD, KontrakGedungBangunanDPMD, HargaGedungBangunanDPMD, GedungBangunanRuanganDPMD, GedungBangunanUsulHapusDPMD, TahunBerkurangUsulHapusGedungDPMD

from gedungbangunan.models import GedungBangunanPenghapusanDPMD, TahunBerkurangGedungBangunanDPMD, PenghapusanGedungBangunanDPMD

from gedungbangunan.models import SKPDAsalGedungBangunanDPMD, SKPDTujuanGedungBangunanDPMD, FotoGedungBangunanDPMD

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDPMD, KontrakPeralatanMesinDPMD, HargaPeralatanMesinDPMD, PeralatanMesinUsulHapusDPMD, TahunBerkurangUsulHapusPeralatanMesinDPMD

from peralatanmesin.models import PeralatanMesinPenghapusanDPMD, TahunBerkurangPeralatanMesinDPMD, PenghapusanPeralatanMesinDPMD

from peralatanmesin.models import SKPDAsalPeralatanMesinDPMD, SKPDTujuanPeralatanMesinDPMD, FotoPeralatanMesinDPMD

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDPMDInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDPMD



class PenghapusanTanahDPMDInline(PenghapusanTanahInline):
    model = PenghapusanTanahDPMD



class SKPDAsalTanahDPMDInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDPMD



class SKPDTujuanTanahDPMDInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDPMD



class FotoTanahDPMDInline(FotoTanahInline):
    model = FotoTanahDPMD



class GedungBangunanDPMDInline(GedungBangunanInline):
    model = GedungBangunanDPMD



class HargaTanahDPMDInline(HargaTanahInline):
    model = HargaTanahDPMD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=10)
        return super(HargaTanahDPMDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDPMDInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDPMD


class TanahDPMDAdmin(TanahAdmin):
    inlines = [HargaTanahDPMDInline,
                SKPDAsalTanahDPMDInline,
                FotoTanahDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        return super(TanahDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDPMDAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDPMDInline,
                SKPDAsalTanahDPMDInline,
                FotoTanahDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDPMDAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=10)
        return super(KontrakTanahDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=10)



class HargaTanahDPMDAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDPMDAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDPMDInline, TahunBerkurangTanahDPMDInline,
                    SKPDAsalTanahDPMDInline,
                    SKPDTujuanTanahDPMDInline,
                    FotoTanahDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DPMD
admin.site.register(TanahDPMD, TanahDPMDAdmin)
admin.site.register(TanahUsulHapusDPMD, TanahUsulHapusDPMDAdmin)
admin.site.register(KontrakTanahDPMD, KontrakTanahDPMDAdmin)
admin.site.register(HargaTanahDPMD, HargaTanahDPMDAdmin)
admin.site.register(TanahPenghapusanDPMD, TanahPenghapusanDPMDAdmin)



from gedungbangunan.models import KDPGedungBangunanDPMD


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDPMDInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDPMD



class PenghapusanGedungBangunanDPMDInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDPMD



class SKPDAsalGedungBangunanDPMDInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDPMD



class SKPDTujuanGedungBangunanDPMDInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDPMD



class FotoGedungBangunanDPMDInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDPMD



class HargaGedungBangunanDPMDInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDPMD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=10)
        return super(HargaGedungBangunanDPMDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDPMDInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDPMD


class GedungBangunanDPMDAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPMDInline,
                SKPDAsalGedungBangunanDPMDInline,
                FotoGedungBangunanDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        return super(GedungBangunanDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDPMDAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPMDInline,
                SKPDAsalGedungBangunanDPMDInline,
                FotoGedungBangunanDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        return super(KDPGedungBangunanDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDPMDAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDPMDAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDPMDInline,
                    SKPDAsalGedungBangunanDPMDInline,
                    FotoGedungBangunanDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDPMDAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=10)
        return super(KontrakGedungBangunanDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=10)



class HargaGedungBangunanDPMDAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDPMDAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDPMDInline, TahunBerkurangGedungBangunanDPMDInline,
                    SKPDAsalGedungBangunanDPMDInline,
                    SKPDTujuanGedungBangunanDPMDInline,
                    FotoGedungBangunanDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DPMD
admin.site.register(GedungBangunanDPMD, GedungBangunanDPMDAdmin)
admin.site.register(KDPGedungBangunanDPMD, KDPGedungBangunanDPMDAdmin)
admin.site.register(GedungBangunanRuanganDPMD, GedungBangunanRuanganDPMDAdmin)
admin.site.register(GedungBangunanUsulHapusDPMD, GedungBangunanUsulHapusDPMDAdmin)
admin.site.register(KontrakGedungBangunanDPMD, KontrakGedungBangunanDPMDAdmin)
admin.site.register(HargaGedungBangunanDPMD, HargaGedungBangunanDPMDAdmin)
admin.site.register(GedungBangunanPenghapusanDPMD, GedungBangunanPenghapusanDPMDAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDPMDInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDPMD



class PenghapusanPeralatanMesinDPMDInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDPMD



class SKPDAsalPeralatanMesinDPMDInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDPMD



class SKPDTujuanPeralatanMesinDPMDInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDPMD



class FotoPeralatanMesinDPMDInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDPMD



class HargaPeralatanMesinDPMDInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDPMD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=10)
        return super(HargaPeralatanMesinDPMDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDPMDInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDPMD


class PeralatanMesinDPMDAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDPMDInline,
                    SKPDAsalPeralatanMesinDPMDInline,
                    FotoPeralatanMesinDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=10)
        return super(PeralatanMesinDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDPMDAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDPMDInline,
                    SKPDAsalPeralatanMesinDPMDInline,
                    FotoPeralatanMesinDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDPMDAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=10)
        return super(KontrakPeralatanMesinDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=10)



class HargaPeralatanMesinDPMDAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDPMDAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDPMDInline, TahunBerkurangPeralatanMesinDPMDInline,
                    SKPDAsalPeralatanMesinDPMDInline,
                    SKPDTujuanPeralatanMesinDPMDInline,
                    FotoPeralatanMesinDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DPMD
admin.site.register(PeralatanMesinDPMD, PeralatanMesinDPMDAdmin)
admin.site.register(PeralatanMesinUsulHapusDPMD, PeralatanMesinUsulHapusDPMDAdmin)
admin.site.register(KontrakPeralatanMesinDPMD, KontrakPeralatanMesinDPMDAdmin)
admin.site.register(HargaPeralatanMesinDPMD, HargaPeralatanMesinDPMDAdmin)
admin.site.register(PeralatanMesinPenghapusanDPMD, PeralatanMesinPenghapusanDPMDAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDPMD, KontrakJalanIrigasiJaringanDPMD, HargaJalanIrigasiJaringanDPMD, KDPJalanIrigasiJaringanDPMD, JalanIrigasiJaringanUsulHapusDPMD, TahunBerkurangUsulHapusJalanIrigasiJaringanDPMD

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDPMD, TahunBerkurangJalanIrigasiJaringanDPMD, PenghapusanJalanIrigasiJaringanDPMD

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDPMD, SKPDTujuanJalanIrigasiJaringanDPMD, FotoJalanIrigasiJaringanDPMD

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDPMDInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDPMD



class PenghapusanJalanIrigasiJaringanDPMDInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDPMD



class SKPDAsalJalanIrigasiJaringanDPMDInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDPMD



class SKPDTujuanJalanIrigasiJaringanDPMDInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDPMD



class FotoJalanIrigasiJaringanDPMDInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDPMD





class HargaJalanIrigasiJaringanDPMDInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDPMD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=10)
        return super(HargaJalanIrigasiJaringanDPMDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPMDInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDPMD


class JalanIrigasiJaringanDPMDAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPMDInline,
                    SKPDAsalJalanIrigasiJaringanDPMDInline,
                    FotoJalanIrigasiJaringanDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        return super(JalanIrigasiJaringanDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDPMDAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDPMDInline,
                    SKPDAsalJalanIrigasiJaringanDPMDInline,
                    FotoJalanIrigasiJaringanDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDPMDAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPMDInline,
                    SKPDAsalJalanIrigasiJaringanDPMDInline,
                    FotoJalanIrigasiJaringanDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        return super(KDPJalanIrigasiJaringanDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDPMDAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=10)
        return super(KontrakJalanIrigasiJaringanDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=10)



class HargaJalanIrigasiJaringanDPMDAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDPMDAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDPMDInline, TahunBerkurangJalanIrigasiJaringanDPMDInline,
                    SKPDAsalJalanIrigasiJaringanDPMDInline,
                    SKPDTujuanJalanIrigasiJaringanDPMDInline,
                    FotoJalanIrigasiJaringanDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DPMD
admin.site.register(JalanIrigasiJaringanDPMD, JalanIrigasiJaringanDPMDAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDPMD, JalanIrigasiJaringanUsulHapusDPMDAdmin)
admin.site.register(KDPJalanIrigasiJaringanDPMD, KDPJalanIrigasiJaringanDPMDAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDPMD, KontrakJalanIrigasiJaringanDPMDAdmin)
admin.site.register(HargaJalanIrigasiJaringanDPMD, HargaJalanIrigasiJaringanDPMDAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDPMD, JalanIrigasiJaringanPenghapusanDPMDAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDPMD, KontrakATLDPMD, HargaATLDPMD, ATLUsulHapusDPMD, TahunBerkurangUsulHapusATLDPMD

from atl.models import ATLPenghapusanDPMD, TahunBerkurangATLDPMD, PenghapusanATLDPMD

from atl.models import SKPDAsalATLDPMD, SKPDTujuanATLDPMD, FotoATLDPMD

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDPMDInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDPMD



class PenghapusanATLDPMDInline(PenghapusanATLInline):
    model = PenghapusanATLDPMD



class SKPDAsalATLDPMDInline(SKPDAsalATLInline):
    model = SKPDAsalATLDPMD



class SKPDTujuanATLDPMDInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDPMD



class FotoATLDPMDInline(FotoATLInline):
    model = FotoATLDPMD



class HargaATLDPMDInline(HargaATLInline):
    model = HargaATLDPMD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=10)
        return super(HargaATLDPMDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDPMDInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDPMD


class ATLDPMDAdmin(ATLAdmin):
    inlines = [HargaATLDPMDInline,
                    SKPDAsalATLDPMDInline,
                    FotoATLDPMDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=10)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=10)
        return super(ATLDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDPMDAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDPMDInline,
                    SKPDAsalATLDPMDInline,
                    FotoATLDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDPMDAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=10)
        return super(KontrakATLDPMDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=10)



class HargaATLDPMDAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDPMDAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDPMDInline, TahunBerkurangATLDPMDInline,
                    SKPDAsalATLDPMDInline,
                    SKPDTujuanATLDPMDInline,
                    FotoATLDPMDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=10)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DPMD
admin.site.register(ATLDPMD, ATLDPMDAdmin)
admin.site.register(ATLUsulHapusDPMD, ATLUsulHapusDPMDAdmin)
admin.site.register(KontrakATLDPMD, KontrakATLDPMDAdmin)
admin.site.register(HargaATLDPMD, HargaATLDPMDAdmin)
admin.site.register(ATLPenghapusanDPMD, ATLPenghapusanDPMDAdmin)
