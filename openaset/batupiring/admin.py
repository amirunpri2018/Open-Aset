### $Id: admin.py,v 1.31 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBatuPiring, KontrakTanahBatuPiring, HargaTanahBatuPiring, TanahUsulHapusBatuPiring, TahunBerkurangUsulHapusTanahBatuPiring

from umum.models import TanahPenghapusanBatuPiring, TahunBerkurangTanahBatuPiring, PenghapusanTanahBatuPiring

from umum.models import SKPDAsalTanahBatuPiring, SKPDTujuanTanahBatuPiring, FotoTanahBatuPiring

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBatuPiring, KontrakGedungBangunanBatuPiring, HargaGedungBangunanBatuPiring, GedungBangunanRuanganBatuPiring, GedungBangunanUsulHapusBatuPiring, TahunBerkurangUsulHapusGedungBatuPiring

from gedungbangunan.models import GedungBangunanPenghapusanBatuPiring, TahunBerkurangGedungBangunanBatuPiring, PenghapusanGedungBangunanBatuPiring

from gedungbangunan.models import SKPDAsalGedungBangunanBatuPiring, SKPDTujuanGedungBangunanBatuPiring, FotoGedungBangunanBatuPiring

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBatuPiring, KontrakPeralatanMesinBatuPiring, HargaPeralatanMesinBatuPiring, PeralatanMesinUsulHapusBatuPiring, TahunBerkurangUsulHapusPeralatanMesinBatuPiring

from peralatanmesin.models import PeralatanMesinPenghapusanBatuPiring, TahunBerkurangPeralatanMesinBatuPiring, PenghapusanPeralatanMesinBatuPiring

from peralatanmesin.models import SKPDAsalPeralatanMesinBatuPiring, SKPDTujuanPeralatanMesinBatuPiring, FotoPeralatanMesinBatuPiring

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBatuPiringInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBatuPiring



class PenghapusanTanahBatuPiringInline(PenghapusanTanahInline):
    model = PenghapusanTanahBatuPiring



class SKPDAsalTanahBatuPiringInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBatuPiring



class SKPDTujuanTanahBatuPiringInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBatuPiring



class FotoTanahBatuPiringInline(FotoTanahInline):
    model = FotoTanahBatuPiring



class GedungBangunanBatuPiringInline(GedungBangunanInline):
    model = GedungBangunanBatuPiring



class HargaTanahBatuPiringInline(HargaTanahInline):
    model = HargaTanahBatuPiring

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=37)
        return super(HargaTanahBatuPiringInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBatuPiringInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBatuPiring


class TanahBatuPiringAdmin(TanahAdmin):
    inlines = [HargaTanahBatuPiringInline,
                SKPDAsalTanahBatuPiringInline,
                FotoTanahBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        return super(TanahBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBatuPiringAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBatuPiringInline,
                SKPDAsalTanahBatuPiringInline,
                FotoTanahBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBatuPiringAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=37)
        return super(KontrakTanahBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=37)



class HargaTanahBatuPiringAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBatuPiringAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBatuPiringInline, TahunBerkurangTanahBatuPiringInline,
                    SKPDAsalTanahBatuPiringInline,
                    SKPDTujuanTanahBatuPiringInline,
                    FotoTanahBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah BatuPiring
admin.site.register(TanahBatuPiring, TanahBatuPiringAdmin)
admin.site.register(TanahUsulHapusBatuPiring, TanahUsulHapusBatuPiringAdmin)
admin.site.register(KontrakTanahBatuPiring, KontrakTanahBatuPiringAdmin)
admin.site.register(HargaTanahBatuPiring, HargaTanahBatuPiringAdmin)
admin.site.register(TanahPenghapusanBatuPiring, TanahPenghapusanBatuPiringAdmin)



from gedungbangunan.models import KDPGedungBangunanBatuPiring


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBatuPiringInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBatuPiring



class PenghapusanGedungBangunanBatuPiringInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBatuPiring



class SKPDAsalGedungBangunanBatuPiringInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBatuPiring



class SKPDTujuanGedungBangunanBatuPiringInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBatuPiring



class FotoGedungBangunanBatuPiringInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBatuPiring



class HargaGedungBangunanBatuPiringInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBatuPiring

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=37)
        return super(HargaGedungBangunanBatuPiringInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBatuPiringInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBatuPiring


class GedungBangunanBatuPiringAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBatuPiringInline,
                SKPDAsalGedungBangunanBatuPiringInline,
                FotoGedungBangunanBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        return super(GedungBangunanBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBatuPiringAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBatuPiringInline,
                SKPDAsalGedungBangunanBatuPiringInline,
                FotoGedungBangunanBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        return super(KDPGedungBangunanBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBatuPiringAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBatuPiringAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBatuPiringInline,
                    SKPDAsalGedungBangunanBatuPiringInline,
                    FotoGedungBangunanBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBatuPiringAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=37)
        return super(KontrakGedungBangunanBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=37)



class HargaGedungBangunanBatuPiringAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBatuPiringAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBatuPiringInline, TahunBerkurangGedungBangunanBatuPiringInline,
                    SKPDAsalGedungBangunanBatuPiringInline,
                    SKPDTujuanGedungBangunanBatuPiringInline,
                    FotoGedungBangunanBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan BatuPiring
admin.site.register(GedungBangunanBatuPiring, GedungBangunanBatuPiringAdmin)
admin.site.register(KDPGedungBangunanBatuPiring, KDPGedungBangunanBatuPiringAdmin)
admin.site.register(GedungBangunanRuanganBatuPiring, GedungBangunanRuanganBatuPiringAdmin)
admin.site.register(GedungBangunanUsulHapusBatuPiring, GedungBangunanUsulHapusBatuPiringAdmin)
admin.site.register(KontrakGedungBangunanBatuPiring, KontrakGedungBangunanBatuPiringAdmin)
admin.site.register(HargaGedungBangunanBatuPiring, HargaGedungBangunanBatuPiringAdmin)
admin.site.register(GedungBangunanPenghapusanBatuPiring, GedungBangunanPenghapusanBatuPiringAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBatuPiringInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBatuPiring



class PenghapusanPeralatanMesinBatuPiringInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBatuPiring



class SKPDAsalPeralatanMesinBatuPiringInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBatuPiring



class SKPDTujuanPeralatanMesinBatuPiringInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBatuPiring



class FotoPeralatanMesinBatuPiringInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBatuPiring



class HargaPeralatanMesinBatuPiringInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBatuPiring

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=37)
        return super(HargaPeralatanMesinBatuPiringInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBatuPiringInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBatuPiring


class PeralatanMesinBatuPiringAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBatuPiringInline,
                    SKPDAsalPeralatanMesinBatuPiringInline,
                    FotoPeralatanMesinBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=37)
        return super(PeralatanMesinBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBatuPiringAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBatuPiringInline,
                    SKPDAsalPeralatanMesinBatuPiringInline,
                    FotoPeralatanMesinBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBatuPiringAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=37)
        return super(KontrakPeralatanMesinBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=37)



class HargaPeralatanMesinBatuPiringAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBatuPiringAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBatuPiringInline, TahunBerkurangPeralatanMesinBatuPiringInline,
                    SKPDAsalPeralatanMesinBatuPiringInline,
                    SKPDTujuanPeralatanMesinBatuPiringInline,
                    FotoPeralatanMesinBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin BatuPiring
admin.site.register(PeralatanMesinBatuPiring, PeralatanMesinBatuPiringAdmin)
admin.site.register(PeralatanMesinUsulHapusBatuPiring, PeralatanMesinUsulHapusBatuPiringAdmin)
admin.site.register(KontrakPeralatanMesinBatuPiring, KontrakPeralatanMesinBatuPiringAdmin)
admin.site.register(HargaPeralatanMesinBatuPiring, HargaPeralatanMesinBatuPiringAdmin)
admin.site.register(PeralatanMesinPenghapusanBatuPiring, PeralatanMesinPenghapusanBatuPiringAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBatuPiring, KontrakJalanIrigasiJaringanBatuPiring, HargaJalanIrigasiJaringanBatuPiring, KDPJalanIrigasiJaringanBatuPiring, JalanIrigasiJaringanUsulHapusBatuPiring, TahunBerkurangUsulHapusJalanIrigasiJaringanBatuPiring

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBatuPiring, TahunBerkurangJalanIrigasiJaringanBatuPiring, PenghapusanJalanIrigasiJaringanBatuPiring

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBatuPiring, SKPDTujuanJalanIrigasiJaringanBatuPiring, FotoJalanIrigasiJaringanBatuPiring

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBatuPiringInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBatuPiring



class PenghapusanJalanIrigasiJaringanBatuPiringInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBatuPiring



class SKPDAsalJalanIrigasiJaringanBatuPiringInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBatuPiring



class SKPDTujuanJalanIrigasiJaringanBatuPiringInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBatuPiring



class FotoJalanIrigasiJaringanBatuPiringInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBatuPiring





class HargaJalanIrigasiJaringanBatuPiringInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBatuPiring

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=37)
        return super(HargaJalanIrigasiJaringanBatuPiringInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBatuPiringInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBatuPiring


class JalanIrigasiJaringanBatuPiringAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBatuPiringInline,
                    SKPDAsalJalanIrigasiJaringanBatuPiringInline,
                    FotoJalanIrigasiJaringanBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        return super(JalanIrigasiJaringanBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBatuPiringAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBatuPiringInline,
                    SKPDAsalJalanIrigasiJaringanBatuPiringInline,
                    FotoJalanIrigasiJaringanBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBatuPiringAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBatuPiringInline,
                    SKPDAsalJalanIrigasiJaringanBatuPiringInline,
                    FotoJalanIrigasiJaringanBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        return super(KDPJalanIrigasiJaringanBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBatuPiringAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=37)
        return super(KontrakJalanIrigasiJaringanBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=37)



class HargaJalanIrigasiJaringanBatuPiringAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBatuPiringAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBatuPiringInline, TahunBerkurangJalanIrigasiJaringanBatuPiringInline,
                    SKPDAsalJalanIrigasiJaringanBatuPiringInline,
                    SKPDTujuanJalanIrigasiJaringanBatuPiringInline,
                    FotoJalanIrigasiJaringanBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan BatuPiring
admin.site.register(JalanIrigasiJaringanBatuPiring, JalanIrigasiJaringanBatuPiringAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBatuPiring, JalanIrigasiJaringanUsulHapusBatuPiringAdmin)
admin.site.register(KDPJalanIrigasiJaringanBatuPiring, KDPJalanIrigasiJaringanBatuPiringAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBatuPiring, KontrakJalanIrigasiJaringanBatuPiringAdmin)
admin.site.register(HargaJalanIrigasiJaringanBatuPiring, HargaJalanIrigasiJaringanBatuPiringAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBatuPiring, JalanIrigasiJaringanPenghapusanBatuPiringAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBatuPiring, KontrakATLBatuPiring, HargaATLBatuPiring, ATLUsulHapusBatuPiring, TahunBerkurangUsulHapusATLBatuPiring

from atl.models import ATLPenghapusanBatuPiring, TahunBerkurangATLBatuPiring, PenghapusanATLBatuPiring

from atl.models import SKPDAsalATLBatuPiring, SKPDTujuanATLBatuPiring, FotoATLBatuPiring

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBatuPiringInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBatuPiring



class PenghapusanATLBatuPiringInline(PenghapusanATLInline):
    model = PenghapusanATLBatuPiring



class SKPDAsalATLBatuPiringInline(SKPDAsalATLInline):
    model = SKPDAsalATLBatuPiring



class SKPDTujuanATLBatuPiringInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBatuPiring



class FotoATLBatuPiringInline(FotoATLInline):
    model = FotoATLBatuPiring



class HargaATLBatuPiringInline(HargaATLInline):
    model = HargaATLBatuPiring

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=37)
        return super(HargaATLBatuPiringInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBatuPiringInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBatuPiring


class ATLBatuPiringAdmin(ATLAdmin):
    inlines = [HargaATLBatuPiringInline,
                    SKPDAsalATLBatuPiringInline,
                    FotoATLBatuPiringInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=37)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=37)
        return super(ATLBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBatuPiringAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBatuPiringInline,
                    SKPDAsalATLBatuPiringInline,
                    FotoATLBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBatuPiringAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=37)
        return super(KontrakATLBatuPiringAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=37)



class HargaATLBatuPiringAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBatuPiringAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBatuPiringInline, TahunBerkurangATLBatuPiringInline,
                    SKPDAsalATLBatuPiringInline,
                    SKPDTujuanATLBatuPiringInline,
                    FotoATLBatuPiringInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=37)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL BatuPiring
admin.site.register(ATLBatuPiring, ATLBatuPiringAdmin)
admin.site.register(ATLUsulHapusBatuPiring, ATLUsulHapusBatuPiringAdmin)
admin.site.register(KontrakATLBatuPiring, KontrakATLBatuPiringAdmin)
admin.site.register(HargaATLBatuPiring, HargaATLBatuPiringAdmin)
admin.site.register(ATLPenghapusanBatuPiring, ATLPenghapusanBatuPiringAdmin)
