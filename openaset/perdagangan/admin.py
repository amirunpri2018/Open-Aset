### $Id: admin.py,v 1.5 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahPerdagangan, KontrakTanahPerdagangan, HargaTanahPerdagangan, TanahUsulHapusPerdagangan, TahunBerkurangUsulHapusTanahPerdagangan

from umum.models import TanahPenghapusanPerdagangan, TahunBerkurangTanahPerdagangan, PenghapusanTanahPerdagangan

from umum.models import SKPDAsalTanahPerdagangan, SKPDTujuanTanahPerdagangan, FotoTanahPerdagangan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanPerdagangan, KontrakGedungBangunanPerdagangan, HargaGedungBangunanPerdagangan, GedungBangunanRuanganPerdagangan, GedungBangunanUsulHapusPerdagangan, TahunBerkurangUsulHapusGedungPerdagangan

from gedungbangunan.models import GedungBangunanPenghapusanPerdagangan, TahunBerkurangGedungBangunanPerdagangan, PenghapusanGedungBangunanPerdagangan

from gedungbangunan.models import SKPDAsalGedungBangunanPerdagangan, SKPDTujuanGedungBangunanPerdagangan, FotoGedungBangunanPerdagangan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinPerdagangan, KontrakPeralatanMesinPerdagangan, HargaPeralatanMesinPerdagangan, PeralatanMesinUsulHapusPerdagangan, TahunBerkurangUsulHapusPeralatanMesinPerdagangan

from peralatanmesin.models import PeralatanMesinPenghapusanPerdagangan, TahunBerkurangPeralatanMesinPerdagangan, PenghapusanPeralatanMesinPerdagangan

from peralatanmesin.models import SKPDAsalPeralatanMesinPerdagangan, SKPDTujuanPeralatanMesinPerdagangan, FotoPeralatanMesinPerdagangan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahPerdaganganInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahPerdagangan



class PenghapusanTanahPerdaganganInline(PenghapusanTanahInline):
    model = PenghapusanTanahPerdagangan



class SKPDAsalTanahPerdaganganInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahPerdagangan



class SKPDTujuanTanahPerdaganganInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahPerdagangan



class FotoTanahPerdaganganInline(FotoTanahInline):
    model = FotoTanahPerdagangan



class GedungBangunanPerdaganganInline(GedungBangunanInline):
    model = GedungBangunanPerdagangan



class HargaTanahPerdaganganInline(HargaTanahInline):
    model = HargaTanahPerdagangan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=47)
        return super(HargaTanahPerdaganganInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahPerdaganganInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahPerdagangan


class TanahPerdaganganAdmin(TanahAdmin):
    inlines = [HargaTanahPerdaganganInline,
                SKPDAsalTanahPerdaganganInline,
                FotoTanahPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        return super(TanahPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusPerdaganganAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahPerdaganganInline,
                SKPDAsalTanahPerdaganganInline,
                FotoTanahPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahPerdaganganAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=47)
        return super(KontrakTanahPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=47)



class HargaTanahPerdaganganAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanPerdaganganAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahPerdaganganInline, TahunBerkurangTanahPerdaganganInline,
                    SKPDAsalTanahPerdaganganInline,
                    SKPDTujuanTanahPerdaganganInline,
                    FotoTanahPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Perdagangan
admin.site.register(TanahPerdagangan, TanahPerdaganganAdmin)
admin.site.register(TanahUsulHapusPerdagangan, TanahUsulHapusPerdaganganAdmin)
admin.site.register(KontrakTanahPerdagangan, KontrakTanahPerdaganganAdmin)
admin.site.register(HargaTanahPerdagangan, HargaTanahPerdaganganAdmin)
admin.site.register(TanahPenghapusanPerdagangan, TanahPenghapusanPerdaganganAdmin)



from gedungbangunan.models import KDPGedungBangunanPerdagangan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanPerdaganganInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanPerdagangan



class PenghapusanGedungBangunanPerdaganganInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanPerdagangan



class SKPDAsalGedungBangunanPerdaganganInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanPerdagangan



class SKPDTujuanGedungBangunanPerdaganganInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanPerdagangan



class FotoGedungBangunanPerdaganganInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanPerdagangan



class HargaGedungBangunanPerdaganganInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanPerdagangan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=47)
        return super(HargaGedungBangunanPerdaganganInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungPerdaganganInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungPerdagangan


class GedungBangunanPerdaganganAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanPerdaganganInline,
                SKPDAsalGedungBangunanPerdaganganInline,
                FotoGedungBangunanPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        return super(GedungBangunanPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanPerdaganganAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanPerdaganganInline,
                SKPDAsalGedungBangunanPerdaganganInline,
                FotoGedungBangunanPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        return super(KDPGedungBangunanPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganPerdaganganAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusPerdaganganAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungPerdaganganInline,
                    SKPDAsalGedungBangunanPerdaganganInline,
                    FotoGedungBangunanPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanPerdaganganAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=47)
        return super(KontrakGedungBangunanPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=47)



class HargaGedungBangunanPerdaganganAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanPerdaganganAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanPerdaganganInline, TahunBerkurangGedungBangunanPerdaganganInline,
                    SKPDAsalGedungBangunanPerdaganganInline,
                    SKPDTujuanGedungBangunanPerdaganganInline,
                    FotoGedungBangunanPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Perdagangan
admin.site.register(GedungBangunanPerdagangan, GedungBangunanPerdaganganAdmin)
admin.site.register(KDPGedungBangunanPerdagangan, KDPGedungBangunanPerdaganganAdmin)
admin.site.register(GedungBangunanRuanganPerdagangan, GedungBangunanRuanganPerdaganganAdmin)
admin.site.register(GedungBangunanUsulHapusPerdagangan, GedungBangunanUsulHapusPerdaganganAdmin)
admin.site.register(KontrakGedungBangunanPerdagangan, KontrakGedungBangunanPerdaganganAdmin)
admin.site.register(HargaGedungBangunanPerdagangan, HargaGedungBangunanPerdaganganAdmin)
admin.site.register(GedungBangunanPenghapusanPerdagangan, GedungBangunanPenghapusanPerdaganganAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinPerdaganganInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinPerdagangan



class PenghapusanPeralatanMesinPerdaganganInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinPerdagangan



class SKPDAsalPeralatanMesinPerdaganganInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinPerdagangan



class SKPDTujuanPeralatanMesinPerdaganganInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinPerdagangan



class FotoPeralatanMesinPerdaganganInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinPerdagangan



class HargaPeralatanMesinPerdaganganInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinPerdagangan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=47)
        return super(HargaPeralatanMesinPerdaganganInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinPerdaganganInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinPerdagangan


class PeralatanMesinPerdaganganAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinPerdaganganInline,
                    SKPDAsalPeralatanMesinPerdaganganInline,
                    FotoPeralatanMesinPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=47)
        return super(PeralatanMesinPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusPerdaganganAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinPerdaganganInline,
                    SKPDAsalPeralatanMesinPerdaganganInline,
                    FotoPeralatanMesinPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinPerdaganganAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=47)
        return super(KontrakPeralatanMesinPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=47)



class HargaPeralatanMesinPerdaganganAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanPerdaganganAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinPerdaganganInline, TahunBerkurangPeralatanMesinPerdaganganInline,
                    SKPDAsalPeralatanMesinPerdaganganInline,
                    SKPDTujuanPeralatanMesinPerdaganganInline,
                    FotoPeralatanMesinPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Perdagangan
admin.site.register(PeralatanMesinPerdagangan, PeralatanMesinPerdaganganAdmin)
admin.site.register(PeralatanMesinUsulHapusPerdagangan, PeralatanMesinUsulHapusPerdaganganAdmin)
admin.site.register(KontrakPeralatanMesinPerdagangan, KontrakPeralatanMesinPerdaganganAdmin)
admin.site.register(HargaPeralatanMesinPerdagangan, HargaPeralatanMesinPerdaganganAdmin)
admin.site.register(PeralatanMesinPenghapusanPerdagangan, PeralatanMesinPenghapusanPerdaganganAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanPerdagangan, KontrakJalanIrigasiJaringanPerdagangan, HargaJalanIrigasiJaringanPerdagangan, KDPJalanIrigasiJaringanPerdagangan, JalanIrigasiJaringanUsulHapusPerdagangan, TahunBerkurangUsulHapusJalanIrigasiJaringanPerdagangan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanPerdagangan, TahunBerkurangJalanIrigasiJaringanPerdagangan, PenghapusanJalanIrigasiJaringanPerdagangan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanPerdagangan, SKPDTujuanJalanIrigasiJaringanPerdagangan, FotoJalanIrigasiJaringanPerdagangan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanPerdaganganInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanPerdagangan



class PenghapusanJalanIrigasiJaringanPerdaganganInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanPerdagangan



class SKPDAsalJalanIrigasiJaringanPerdaganganInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanPerdagangan



class SKPDTujuanJalanIrigasiJaringanPerdaganganInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanPerdagangan



class FotoJalanIrigasiJaringanPerdaganganInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanPerdagangan





class HargaJalanIrigasiJaringanPerdaganganInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanPerdagangan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=47)
        return super(HargaJalanIrigasiJaringanPerdaganganInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanPerdaganganInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanPerdagangan


class JalanIrigasiJaringanPerdaganganAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPerdaganganInline,
                    SKPDAsalJalanIrigasiJaringanPerdaganganInline,
                    FotoJalanIrigasiJaringanPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        return super(JalanIrigasiJaringanPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusPerdaganganAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanPerdaganganInline,
                    SKPDAsalJalanIrigasiJaringanPerdaganganInline,
                    FotoJalanIrigasiJaringanPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanPerdaganganAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPerdaganganInline,
                    SKPDAsalJalanIrigasiJaringanPerdaganganInline,
                    FotoJalanIrigasiJaringanPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        return super(KDPJalanIrigasiJaringanPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanPerdaganganAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=47)
        return super(KontrakJalanIrigasiJaringanPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=47)



class HargaJalanIrigasiJaringanPerdaganganAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanPerdaganganAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanPerdaganganInline, TahunBerkurangJalanIrigasiJaringanPerdaganganInline,
                    SKPDAsalJalanIrigasiJaringanPerdaganganInline,
                    SKPDTujuanJalanIrigasiJaringanPerdaganganInline,
                    FotoJalanIrigasiJaringanPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Perdagangan
admin.site.register(JalanIrigasiJaringanPerdagangan, JalanIrigasiJaringanPerdaganganAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusPerdagangan, JalanIrigasiJaringanUsulHapusPerdaganganAdmin)
admin.site.register(KDPJalanIrigasiJaringanPerdagangan, KDPJalanIrigasiJaringanPerdaganganAdmin)
admin.site.register(KontrakJalanIrigasiJaringanPerdagangan, KontrakJalanIrigasiJaringanPerdaganganAdmin)
admin.site.register(HargaJalanIrigasiJaringanPerdagangan, HargaJalanIrigasiJaringanPerdaganganAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanPerdagangan, JalanIrigasiJaringanPenghapusanPerdaganganAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLPerdagangan, KontrakATLPerdagangan, HargaATLPerdagangan, ATLUsulHapusPerdagangan, TahunBerkurangUsulHapusATLPerdagangan

from atl.models import ATLPenghapusanPerdagangan, TahunBerkurangATLPerdagangan, PenghapusanATLPerdagangan

from atl.models import SKPDAsalATLPerdagangan, SKPDTujuanATLPerdagangan, FotoATLPerdagangan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLPerdaganganInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLPerdagangan



class PenghapusanATLPerdaganganInline(PenghapusanATLInline):
    model = PenghapusanATLPerdagangan



class SKPDAsalATLPerdaganganInline(SKPDAsalATLInline):
    model = SKPDAsalATLPerdagangan



class SKPDTujuanATLPerdaganganInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLPerdagangan



class FotoATLPerdaganganInline(FotoATLInline):
    model = FotoATLPerdagangan



class HargaATLPerdaganganInline(HargaATLInline):
    model = HargaATLPerdagangan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=47)
        return super(HargaATLPerdaganganInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLPerdaganganInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLPerdagangan


class ATLPerdaganganAdmin(ATLAdmin):
    inlines = [HargaATLPerdaganganInline,
                    SKPDAsalATLPerdaganganInline,
                    FotoATLPerdaganganInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=47)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=47)
        return super(ATLPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusPerdaganganAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLPerdaganganInline,
                    SKPDAsalATLPerdaganganInline,
                    FotoATLPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLPerdaganganAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=47)
        return super(KontrakATLPerdaganganAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=47)



class HargaATLPerdaganganAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanPerdaganganAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLPerdaganganInline, TahunBerkurangATLPerdaganganInline,
                    SKPDAsalATLPerdaganganInline,
                    SKPDTujuanATLPerdaganganInline,
                    FotoATLPerdaganganInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=47)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Perdagangan
admin.site.register(ATLPerdagangan, ATLPerdaganganAdmin)
admin.site.register(ATLUsulHapusPerdagangan, ATLUsulHapusPerdaganganAdmin)
admin.site.register(KontrakATLPerdagangan, KontrakATLPerdaganganAdmin)
admin.site.register(HargaATLPerdagangan, HargaATLPerdaganganAdmin)
admin.site.register(ATLPenghapusanPerdagangan, ATLPenghapusanPerdaganganAdmin)
