### $Id: admin.py,v 1.5 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahPerpustakaan, KontrakTanahPerpustakaan, HargaTanahPerpustakaan, TanahUsulHapusPerpustakaan, TahunBerkurangUsulHapusTanahPerpustakaan

from umum.models import TanahPenghapusanPerpustakaan, TahunBerkurangTanahPerpustakaan, PenghapusanTanahPerpustakaan

from umum.models import SKPDAsalTanahPerpustakaan, SKPDTujuanTanahPerpustakaan, FotoTanahPerpustakaan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanPerpustakaan, KontrakGedungBangunanPerpustakaan, HargaGedungBangunanPerpustakaan, GedungBangunanRuanganPerpustakaan, GedungBangunanUsulHapusPerpustakaan, TahunBerkurangUsulHapusGedungPerpustakaan

from gedungbangunan.models import GedungBangunanPenghapusanPerpustakaan, TahunBerkurangGedungBangunanPerpustakaan, PenghapusanGedungBangunanPerpustakaan

from gedungbangunan.models import SKPDAsalGedungBangunanPerpustakaan, SKPDTujuanGedungBangunanPerpustakaan, FotoGedungBangunanPerpustakaan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinPerpustakaan, KontrakPeralatanMesinPerpustakaan, HargaPeralatanMesinPerpustakaan, PeralatanMesinUsulHapusPerpustakaan, TahunBerkurangUsulHapusPeralatanMesinPerpustakaan

from peralatanmesin.models import PeralatanMesinPenghapusanPerpustakaan, TahunBerkurangPeralatanMesinPerpustakaan, PenghapusanPeralatanMesinPerpustakaan

from peralatanmesin.models import SKPDAsalPeralatanMesinPerpustakaan, SKPDTujuanPeralatanMesinPerpustakaan, FotoPeralatanMesinPerpustakaan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahPerpustakaanInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahPerpustakaan



class PenghapusanTanahPerpustakaanInline(PenghapusanTanahInline):
    model = PenghapusanTanahPerpustakaan



class SKPDAsalTanahPerpustakaanInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahPerpustakaan



class SKPDTujuanTanahPerpustakaanInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahPerpustakaan



class FotoTanahPerpustakaanInline(FotoTanahInline):
    model = FotoTanahPerpustakaan



class GedungBangunanPerpustakaanInline(GedungBangunanInline):
    model = GedungBangunanPerpustakaan



class HargaTanahPerpustakaanInline(HargaTanahInline):
    model = HargaTanahPerpustakaan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=8)
        return super(HargaTanahPerpustakaanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahPerpustakaanInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahPerpustakaan


class TanahPerpustakaanAdmin(TanahAdmin):
    inlines = [HargaTanahPerpustakaanInline,
                SKPDAsalTanahPerpustakaanInline,
                FotoTanahPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        return super(TanahPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusPerpustakaanAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahPerpustakaanInline,
                SKPDAsalTanahPerpustakaanInline,
                FotoTanahPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahPerpustakaanAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=8)
        return super(KontrakTanahPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=8)



class HargaTanahPerpustakaanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanPerpustakaanAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahPerpustakaanInline, TahunBerkurangTanahPerpustakaanInline,
                    SKPDAsalTanahPerpustakaanInline,
                    SKPDTujuanTanahPerpustakaanInline,
                    FotoTanahPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Perpustakaan
admin.site.register(TanahPerpustakaan, TanahPerpustakaanAdmin)
admin.site.register(TanahUsulHapusPerpustakaan, TanahUsulHapusPerpustakaanAdmin)
admin.site.register(KontrakTanahPerpustakaan, KontrakTanahPerpustakaanAdmin)
admin.site.register(HargaTanahPerpustakaan, HargaTanahPerpustakaanAdmin)
admin.site.register(TanahPenghapusanPerpustakaan, TanahPenghapusanPerpustakaanAdmin)



from gedungbangunan.models import KDPGedungBangunanPerpustakaan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanPerpustakaanInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanPerpustakaan



class PenghapusanGedungBangunanPerpustakaanInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanPerpustakaan



class SKPDAsalGedungBangunanPerpustakaanInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanPerpustakaan



class SKPDTujuanGedungBangunanPerpustakaanInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanPerpustakaan



class FotoGedungBangunanPerpustakaanInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanPerpustakaan



class HargaGedungBangunanPerpustakaanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanPerpustakaan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=8)
        return super(HargaGedungBangunanPerpustakaanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungPerpustakaanInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungPerpustakaan


class GedungBangunanPerpustakaanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanPerpustakaanInline,
                SKPDAsalGedungBangunanPerpustakaanInline,
                FotoGedungBangunanPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        return super(GedungBangunanPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanPerpustakaanAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanPerpustakaanInline,
                SKPDAsalGedungBangunanPerpustakaanInline,
                FotoGedungBangunanPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        return super(KDPGedungBangunanPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganPerpustakaanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusPerpustakaanAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungPerpustakaanInline,
                    SKPDAsalGedungBangunanPerpustakaanInline,
                    FotoGedungBangunanPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanPerpustakaanAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=8)
        return super(KontrakGedungBangunanPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=8)



class HargaGedungBangunanPerpustakaanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanPerpustakaanAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanPerpustakaanInline, TahunBerkurangGedungBangunanPerpustakaanInline,
                    SKPDAsalGedungBangunanPerpustakaanInline,
                    SKPDTujuanGedungBangunanPerpustakaanInline,
                    FotoGedungBangunanPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Perpustakaan
admin.site.register(GedungBangunanPerpustakaan, GedungBangunanPerpustakaanAdmin)
admin.site.register(KDPGedungBangunanPerpustakaan, KDPGedungBangunanPerpustakaanAdmin)
admin.site.register(GedungBangunanRuanganPerpustakaan, GedungBangunanRuanganPerpustakaanAdmin)
admin.site.register(GedungBangunanUsulHapusPerpustakaan, GedungBangunanUsulHapusPerpustakaanAdmin)
admin.site.register(KontrakGedungBangunanPerpustakaan, KontrakGedungBangunanPerpustakaanAdmin)
admin.site.register(HargaGedungBangunanPerpustakaan, HargaGedungBangunanPerpustakaanAdmin)
admin.site.register(GedungBangunanPenghapusanPerpustakaan, GedungBangunanPenghapusanPerpustakaanAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinPerpustakaanInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinPerpustakaan



class PenghapusanPeralatanMesinPerpustakaanInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinPerpustakaan



class SKPDAsalPeralatanMesinPerpustakaanInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinPerpustakaan



class SKPDTujuanPeralatanMesinPerpustakaanInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinPerpustakaan



class FotoPeralatanMesinPerpustakaanInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinPerpustakaan



class HargaPeralatanMesinPerpustakaanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinPerpustakaan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=8)
        return super(HargaPeralatanMesinPerpustakaanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinPerpustakaanInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinPerpustakaan


class PeralatanMesinPerpustakaanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinPerpustakaanInline,
                    SKPDAsalPeralatanMesinPerpustakaanInline,
                    FotoPeralatanMesinPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=8)
        return super(PeralatanMesinPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusPerpustakaanAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinPerpustakaanInline,
                    SKPDAsalPeralatanMesinPerpustakaanInline,
                    FotoPeralatanMesinPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinPerpustakaanAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=8)
        return super(KontrakPeralatanMesinPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=8)



class HargaPeralatanMesinPerpustakaanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanPerpustakaanAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinPerpustakaanInline, TahunBerkurangPeralatanMesinPerpustakaanInline,
                    SKPDAsalPeralatanMesinPerpustakaanInline,
                    SKPDTujuanPeralatanMesinPerpustakaanInline,
                    FotoPeralatanMesinPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Perpustakaan
admin.site.register(PeralatanMesinPerpustakaan, PeralatanMesinPerpustakaanAdmin)
admin.site.register(PeralatanMesinUsulHapusPerpustakaan, PeralatanMesinUsulHapusPerpustakaanAdmin)
admin.site.register(KontrakPeralatanMesinPerpustakaan, KontrakPeralatanMesinPerpustakaanAdmin)
admin.site.register(HargaPeralatanMesinPerpustakaan, HargaPeralatanMesinPerpustakaanAdmin)
admin.site.register(PeralatanMesinPenghapusanPerpustakaan, PeralatanMesinPenghapusanPerpustakaanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanPerpustakaan, KontrakJalanIrigasiJaringanPerpustakaan, HargaJalanIrigasiJaringanPerpustakaan, KDPJalanIrigasiJaringanPerpustakaan, JalanIrigasiJaringanUsulHapusPerpustakaan, TahunBerkurangUsulHapusJalanIrigasiJaringanPerpustakaan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanPerpustakaan, TahunBerkurangJalanIrigasiJaringanPerpustakaan, PenghapusanJalanIrigasiJaringanPerpustakaan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanPerpustakaan, SKPDTujuanJalanIrigasiJaringanPerpustakaan, FotoJalanIrigasiJaringanPerpustakaan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanPerpustakaanInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanPerpustakaan



class PenghapusanJalanIrigasiJaringanPerpustakaanInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanPerpustakaan



class SKPDAsalJalanIrigasiJaringanPerpustakaanInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanPerpustakaan



class SKPDTujuanJalanIrigasiJaringanPerpustakaanInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanPerpustakaan



class FotoJalanIrigasiJaringanPerpustakaanInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanPerpustakaan





class HargaJalanIrigasiJaringanPerpustakaanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanPerpustakaan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=8)
        return super(HargaJalanIrigasiJaringanPerpustakaanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanPerpustakaanInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanPerpustakaan


class JalanIrigasiJaringanPerpustakaanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPerpustakaanInline,
                    SKPDAsalJalanIrigasiJaringanPerpustakaanInline,
                    FotoJalanIrigasiJaringanPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        return super(JalanIrigasiJaringanPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusPerpustakaanAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanPerpustakaanInline,
                    SKPDAsalJalanIrigasiJaringanPerpustakaanInline,
                    FotoJalanIrigasiJaringanPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanPerpustakaanAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPerpustakaanInline,
                    SKPDAsalJalanIrigasiJaringanPerpustakaanInline,
                    FotoJalanIrigasiJaringanPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        return super(KDPJalanIrigasiJaringanPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanPerpustakaanAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=8)
        return super(KontrakJalanIrigasiJaringanPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=8)



class HargaJalanIrigasiJaringanPerpustakaanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanPerpustakaanAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanPerpustakaanInline, TahunBerkurangJalanIrigasiJaringanPerpustakaanInline,
                    SKPDAsalJalanIrigasiJaringanPerpustakaanInline,
                    SKPDTujuanJalanIrigasiJaringanPerpustakaanInline,
                    FotoJalanIrigasiJaringanPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Perpustakaan
admin.site.register(JalanIrigasiJaringanPerpustakaan, JalanIrigasiJaringanPerpustakaanAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusPerpustakaan, JalanIrigasiJaringanUsulHapusPerpustakaanAdmin)
admin.site.register(KDPJalanIrigasiJaringanPerpustakaan, KDPJalanIrigasiJaringanPerpustakaanAdmin)
admin.site.register(KontrakJalanIrigasiJaringanPerpustakaan, KontrakJalanIrigasiJaringanPerpustakaanAdmin)
admin.site.register(HargaJalanIrigasiJaringanPerpustakaan, HargaJalanIrigasiJaringanPerpustakaanAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanPerpustakaan, JalanIrigasiJaringanPenghapusanPerpustakaanAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLPerpustakaan, KontrakATLPerpustakaan, HargaATLPerpustakaan, ATLUsulHapusPerpustakaan, TahunBerkurangUsulHapusATLPerpustakaan

from atl.models import ATLPenghapusanPerpustakaan, TahunBerkurangATLPerpustakaan, PenghapusanATLPerpustakaan

from atl.models import SKPDAsalATLPerpustakaan, SKPDTujuanATLPerpustakaan, FotoATLPerpustakaan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLPerpustakaanInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLPerpustakaan



class PenghapusanATLPerpustakaanInline(PenghapusanATLInline):
    model = PenghapusanATLPerpustakaan



class SKPDAsalATLPerpustakaanInline(SKPDAsalATLInline):
    model = SKPDAsalATLPerpustakaan



class SKPDTujuanATLPerpustakaanInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLPerpustakaan



class FotoATLPerpustakaanInline(FotoATLInline):
    model = FotoATLPerpustakaan



class HargaATLPerpustakaanInline(HargaATLInline):
    model = HargaATLPerpustakaan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=8)
        return super(HargaATLPerpustakaanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLPerpustakaanInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLPerpustakaan


class ATLPerpustakaanAdmin(ATLAdmin):
    inlines = [HargaATLPerpustakaanInline,
                    SKPDAsalATLPerpustakaanInline,
                    FotoATLPerpustakaanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=8)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=8)
        return super(ATLPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusPerpustakaanAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLPerpustakaanInline,
                    SKPDAsalATLPerpustakaanInline,
                    FotoATLPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLPerpustakaanAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=8)
        return super(KontrakATLPerpustakaanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=8)



class HargaATLPerpustakaanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanPerpustakaanAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLPerpustakaanInline, TahunBerkurangATLPerpustakaanInline,
                    SKPDAsalATLPerpustakaanInline,
                    SKPDTujuanATLPerpustakaanInline,
                    FotoATLPerpustakaanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=8)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Perpustakaan
admin.site.register(ATLPerpustakaan, ATLPerpustakaanAdmin)
admin.site.register(ATLUsulHapusPerpustakaan, ATLUsulHapusPerpustakaanAdmin)
admin.site.register(KontrakATLPerpustakaan, KontrakATLPerpustakaanAdmin)
admin.site.register(HargaATLPerpustakaan, HargaATLPerpustakaanAdmin)
admin.site.register(ATLPenghapusanPerpustakaan, ATLPenghapusanPerpustakaanAdmin)
