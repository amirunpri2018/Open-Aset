### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDPPKB, KontrakTanahDPPKB, HargaTanahDPPKB, TanahUsulHapusDPPKB, TahunBerkurangUsulHapusTanahDPPKB

from umum.models import TanahPenghapusanDPPKB, TahunBerkurangTanahDPPKB, PenghapusanTanahDPPKB

from umum.models import SKPDAsalTanahDPPKB, SKPDTujuanTanahDPPKB, FotoTanahDPPKB

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDPPKB, KontrakGedungBangunanDPPKB, HargaGedungBangunanDPPKB, GedungBangunanRuanganDPPKB, GedungBangunanUsulHapusDPPKB, TahunBerkurangUsulHapusGedungDPPKB

from gedungbangunan.models import GedungBangunanPenghapusanDPPKB, TahunBerkurangGedungBangunanDPPKB, PenghapusanGedungBangunanDPPKB

from gedungbangunan.models import SKPDAsalGedungBangunanDPPKB, SKPDTujuanGedungBangunanDPPKB, FotoGedungBangunanDPPKB

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDPPKB, KontrakPeralatanMesinDPPKB, HargaPeralatanMesinDPPKB, PeralatanMesinUsulHapusDPPKB, TahunBerkurangUsulHapusPeralatanMesinDPPKB

from peralatanmesin.models import PeralatanMesinPenghapusanDPPKB, TahunBerkurangPeralatanMesinDPPKB, PenghapusanPeralatanMesinDPPKB

from peralatanmesin.models import SKPDAsalPeralatanMesinDPPKB, SKPDTujuanPeralatanMesinDPPKB, FotoPeralatanMesinDPPKB

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDPPKBInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDPPKB



class PenghapusanTanahDPPKBInline(PenghapusanTanahInline):
    model = PenghapusanTanahDPPKB



class SKPDAsalTanahDPPKBInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDPPKB



class SKPDTujuanTanahDPPKBInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDPPKB



class FotoTanahDPPKBInline(FotoTanahInline):
    model = FotoTanahDPPKB



class GedungBangunanDPPKBInline(GedungBangunanInline):
    model = GedungBangunanDPPKB



class HargaTanahDPPKBInline(HargaTanahInline):
    model = HargaTanahDPPKB

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=42)
        return super(HargaTanahDPPKBInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDPPKBInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDPPKB


class TanahDPPKBAdmin(TanahAdmin):
    inlines = [HargaTanahDPPKBInline,
                SKPDAsalTanahDPPKBInline,
                FotoTanahDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        return super(TanahDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDPPKBAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDPPKBInline,
                SKPDAsalTanahDPPKBInline,
                FotoTanahDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDPPKBAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=42)
        return super(KontrakTanahDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=42)



class HargaTanahDPPKBAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDPPKBAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDPPKBInline, TahunBerkurangTanahDPPKBInline,
                    SKPDAsalTanahDPPKBInline,
                    SKPDTujuanTanahDPPKBInline,
                    FotoTanahDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DPPKB
admin.site.register(TanahDPPKB, TanahDPPKBAdmin)
admin.site.register(TanahUsulHapusDPPKB, TanahUsulHapusDPPKBAdmin)
admin.site.register(KontrakTanahDPPKB, KontrakTanahDPPKBAdmin)
admin.site.register(HargaTanahDPPKB, HargaTanahDPPKBAdmin)
admin.site.register(TanahPenghapusanDPPKB, TanahPenghapusanDPPKBAdmin)



from gedungbangunan.models import KDPGedungBangunanDPPKB


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDPPKBInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDPPKB



class PenghapusanGedungBangunanDPPKBInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDPPKB



class SKPDAsalGedungBangunanDPPKBInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDPPKB



class SKPDTujuanGedungBangunanDPPKBInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDPPKB



class FotoGedungBangunanDPPKBInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDPPKB



class HargaGedungBangunanDPPKBInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDPPKB

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=42)
        return super(HargaGedungBangunanDPPKBInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDPPKBInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDPPKB


class GedungBangunanDPPKBAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPPKBInline,
                SKPDAsalGedungBangunanDPPKBInline,
                FotoGedungBangunanDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        return super(GedungBangunanDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDPPKBAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPPKBInline,
                SKPDAsalGedungBangunanDPPKBInline,
                FotoGedungBangunanDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        return super(KDPGedungBangunanDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDPPKBAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDPPKBAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDPPKBInline,
                    SKPDAsalGedungBangunanDPPKBInline,
                    FotoGedungBangunanDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDPPKBAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=42)
        return super(KontrakGedungBangunanDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=42)



class HargaGedungBangunanDPPKBAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDPPKBAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDPPKBInline, TahunBerkurangGedungBangunanDPPKBInline,
                    SKPDAsalGedungBangunanDPPKBInline,
                    SKPDTujuanGedungBangunanDPPKBInline,
                    FotoGedungBangunanDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DPPKB
admin.site.register(GedungBangunanDPPKB, GedungBangunanDPPKBAdmin)
admin.site.register(KDPGedungBangunanDPPKB, KDPGedungBangunanDPPKBAdmin)
admin.site.register(GedungBangunanRuanganDPPKB, GedungBangunanRuanganDPPKBAdmin)
admin.site.register(GedungBangunanUsulHapusDPPKB, GedungBangunanUsulHapusDPPKBAdmin)
admin.site.register(KontrakGedungBangunanDPPKB, KontrakGedungBangunanDPPKBAdmin)
admin.site.register(HargaGedungBangunanDPPKB, HargaGedungBangunanDPPKBAdmin)
admin.site.register(GedungBangunanPenghapusanDPPKB, GedungBangunanPenghapusanDPPKBAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDPPKBInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDPPKB



class PenghapusanPeralatanMesinDPPKBInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDPPKB



class SKPDAsalPeralatanMesinDPPKBInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDPPKB



class SKPDTujuanPeralatanMesinDPPKBInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDPPKB



class FotoPeralatanMesinDPPKBInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDPPKB



class HargaPeralatanMesinDPPKBInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDPPKB

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=42)
        return super(HargaPeralatanMesinDPPKBInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDPPKBInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDPPKB


class PeralatanMesinDPPKBAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDPPKBInline,
                    SKPDAsalPeralatanMesinDPPKBInline,
                    FotoPeralatanMesinDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=42)
        return super(PeralatanMesinDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDPPKBAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDPPKBInline,
                    SKPDAsalPeralatanMesinDPPKBInline,
                    FotoPeralatanMesinDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDPPKBAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=42)
        return super(KontrakPeralatanMesinDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=42)



class HargaPeralatanMesinDPPKBAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDPPKBAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDPPKBInline, TahunBerkurangPeralatanMesinDPPKBInline,
                    SKPDAsalPeralatanMesinDPPKBInline,
                    SKPDTujuanPeralatanMesinDPPKBInline,
                    FotoPeralatanMesinDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DPPKB
admin.site.register(PeralatanMesinDPPKB, PeralatanMesinDPPKBAdmin)
admin.site.register(PeralatanMesinUsulHapusDPPKB, PeralatanMesinUsulHapusDPPKBAdmin)
admin.site.register(KontrakPeralatanMesinDPPKB, KontrakPeralatanMesinDPPKBAdmin)
admin.site.register(HargaPeralatanMesinDPPKB, HargaPeralatanMesinDPPKBAdmin)
admin.site.register(PeralatanMesinPenghapusanDPPKB, PeralatanMesinPenghapusanDPPKBAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDPPKB, KontrakJalanIrigasiJaringanDPPKB, HargaJalanIrigasiJaringanDPPKB, KDPJalanIrigasiJaringanDPPKB, JalanIrigasiJaringanUsulHapusDPPKB, TahunBerkurangUsulHapusJalanIrigasiJaringanDPPKB

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDPPKB, TahunBerkurangJalanIrigasiJaringanDPPKB, PenghapusanJalanIrigasiJaringanDPPKB

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDPPKB, SKPDTujuanJalanIrigasiJaringanDPPKB, FotoJalanIrigasiJaringanDPPKB

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDPPKBInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDPPKB



class PenghapusanJalanIrigasiJaringanDPPKBInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDPPKB



class SKPDAsalJalanIrigasiJaringanDPPKBInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDPPKB



class SKPDTujuanJalanIrigasiJaringanDPPKBInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDPPKB



class FotoJalanIrigasiJaringanDPPKBInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDPPKB





class HargaJalanIrigasiJaringanDPPKBInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDPPKB

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=42)
        return super(HargaJalanIrigasiJaringanDPPKBInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPPKBInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDPPKB


class JalanIrigasiJaringanDPPKBAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPPKBInline,
                    SKPDAsalJalanIrigasiJaringanDPPKBInline,
                    FotoJalanIrigasiJaringanDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        return super(JalanIrigasiJaringanDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDPPKBAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDPPKBInline,
                    SKPDAsalJalanIrigasiJaringanDPPKBInline,
                    FotoJalanIrigasiJaringanDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDPPKBAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPPKBInline,
                    SKPDAsalJalanIrigasiJaringanDPPKBInline,
                    FotoJalanIrigasiJaringanDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        return super(KDPJalanIrigasiJaringanDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDPPKBAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=42)
        return super(KontrakJalanIrigasiJaringanDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=42)



class HargaJalanIrigasiJaringanDPPKBAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDPPKBAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDPPKBInline, TahunBerkurangJalanIrigasiJaringanDPPKBInline,
                    SKPDAsalJalanIrigasiJaringanDPPKBInline,
                    SKPDTujuanJalanIrigasiJaringanDPPKBInline,
                    FotoJalanIrigasiJaringanDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DPPKB
admin.site.register(JalanIrigasiJaringanDPPKB, JalanIrigasiJaringanDPPKBAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDPPKB, JalanIrigasiJaringanUsulHapusDPPKBAdmin)
admin.site.register(KDPJalanIrigasiJaringanDPPKB, KDPJalanIrigasiJaringanDPPKBAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDPPKB, KontrakJalanIrigasiJaringanDPPKBAdmin)
admin.site.register(HargaJalanIrigasiJaringanDPPKB, HargaJalanIrigasiJaringanDPPKBAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDPPKB, JalanIrigasiJaringanPenghapusanDPPKBAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDPPKB, KontrakATLDPPKB, HargaATLDPPKB, ATLUsulHapusDPPKB, TahunBerkurangUsulHapusATLDPPKB

from atl.models import ATLPenghapusanDPPKB, TahunBerkurangATLDPPKB, PenghapusanATLDPPKB

from atl.models import SKPDAsalATLDPPKB, SKPDTujuanATLDPPKB, FotoATLDPPKB

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDPPKBInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDPPKB



class PenghapusanATLDPPKBInline(PenghapusanATLInline):
    model = PenghapusanATLDPPKB



class SKPDAsalATLDPPKBInline(SKPDAsalATLInline):
    model = SKPDAsalATLDPPKB



class SKPDTujuanATLDPPKBInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDPPKB



class FotoATLDPPKBInline(FotoATLInline):
    model = FotoATLDPPKB



class HargaATLDPPKBInline(HargaATLInline):
    model = HargaATLDPPKB

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=42)
        return super(HargaATLDPPKBInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDPPKBInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDPPKB


class ATLDPPKBAdmin(ATLAdmin):
    inlines = [HargaATLDPPKBInline,
                    SKPDAsalATLDPPKBInline,
                    FotoATLDPPKBInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=42)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=42)
        return super(ATLDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDPPKBAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDPPKBInline,
                    SKPDAsalATLDPPKBInline,
                    FotoATLDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDPPKBAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=42)
        return super(KontrakATLDPPKBAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=42)



class HargaATLDPPKBAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDPPKBAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDPPKBInline, TahunBerkurangATLDPPKBInline,
                    SKPDAsalATLDPPKBInline,
                    SKPDTujuanATLDPPKBInline,
                    FotoATLDPPKBInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=42)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DPPKB
admin.site.register(ATLDPPKB, ATLDPPKBAdmin)
admin.site.register(ATLUsulHapusDPPKB, ATLUsulHapusDPPKBAdmin)
admin.site.register(KontrakATLDPPKB, KontrakATLDPPKBAdmin)
admin.site.register(HargaATLDPPKB, HargaATLDPPKBAdmin)
admin.site.register(ATLPenghapusanDPPKB, ATLPenghapusanDPPKBAdmin)
