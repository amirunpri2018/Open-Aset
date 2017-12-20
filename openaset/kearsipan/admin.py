### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahKearsipan, KontrakTanahKearsipan, HargaTanahKearsipan, TanahUsulHapusKearsipan, TahunBerkurangUsulHapusTanahKearsipan

from umum.models import TanahPenghapusanKearsipan, TahunBerkurangTanahKearsipan, PenghapusanTanahKearsipan

from umum.models import SKPDAsalTanahKearsipan, SKPDTujuanTanahKearsipan, FotoTanahKearsipan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanKearsipan, KontrakGedungBangunanKearsipan, HargaGedungBangunanKearsipan, GedungBangunanRuanganKearsipan, GedungBangunanUsulHapusKearsipan, TahunBerkurangUsulHapusGedungKearsipan

from gedungbangunan.models import GedungBangunanPenghapusanKearsipan, TahunBerkurangGedungBangunanKearsipan, PenghapusanGedungBangunanKearsipan

from gedungbangunan.models import SKPDAsalGedungBangunanKearsipan, SKPDTujuanGedungBangunanKearsipan, FotoGedungBangunanKearsipan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinKearsipan, KontrakPeralatanMesinKearsipan, HargaPeralatanMesinKearsipan, PeralatanMesinUsulHapusKearsipan, TahunBerkurangUsulHapusPeralatanMesinKearsipan

from peralatanmesin.models import PeralatanMesinPenghapusanKearsipan, TahunBerkurangPeralatanMesinKearsipan, PenghapusanPeralatanMesinKearsipan

from peralatanmesin.models import SKPDAsalPeralatanMesinKearsipan, SKPDTujuanPeralatanMesinKearsipan, FotoPeralatanMesinKearsipan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahKearsipanInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahKearsipan



class PenghapusanTanahKearsipanInline(PenghapusanTanahInline):
    model = PenghapusanTanahKearsipan



class SKPDAsalTanahKearsipanInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahKearsipan



class SKPDTujuanTanahKearsipanInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahKearsipan



class FotoTanahKearsipanInline(FotoTanahInline):
    model = FotoTanahKearsipan



class GedungBangunanKearsipanInline(GedungBangunanInline):
    model = GedungBangunanKearsipan



class HargaTanahKearsipanInline(HargaTanahInline):
    model = HargaTanahKearsipan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=44)
        return super(HargaTanahKearsipanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahKearsipanInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahKearsipan


class TanahKearsipanAdmin(TanahAdmin):
    inlines = [HargaTanahKearsipanInline,
                SKPDAsalTanahKearsipanInline,
                FotoTanahKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        return super(TanahKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusKearsipanAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahKearsipanInline,
                SKPDAsalTanahKearsipanInline,
                FotoTanahKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahKearsipanAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=44)
        return super(KontrakTanahKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=44)



class HargaTanahKearsipanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanKearsipanAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahKearsipanInline, TahunBerkurangTanahKearsipanInline,
                    SKPDAsalTanahKearsipanInline,
                    SKPDTujuanTanahKearsipanInline,
                    FotoTanahKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Kearsipan
admin.site.register(TanahKearsipan, TanahKearsipanAdmin)
admin.site.register(TanahUsulHapusKearsipan, TanahUsulHapusKearsipanAdmin)
admin.site.register(KontrakTanahKearsipan, KontrakTanahKearsipanAdmin)
admin.site.register(HargaTanahKearsipan, HargaTanahKearsipanAdmin)
admin.site.register(TanahPenghapusanKearsipan, TanahPenghapusanKearsipanAdmin)



from gedungbangunan.models import KDPGedungBangunanKearsipan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanKearsipanInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanKearsipan



class PenghapusanGedungBangunanKearsipanInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanKearsipan



class SKPDAsalGedungBangunanKearsipanInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanKearsipan



class SKPDTujuanGedungBangunanKearsipanInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanKearsipan



class FotoGedungBangunanKearsipanInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanKearsipan



class HargaGedungBangunanKearsipanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanKearsipan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=44)
        return super(HargaGedungBangunanKearsipanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungKearsipanInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungKearsipan


class GedungBangunanKearsipanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanKearsipanInline,
                SKPDAsalGedungBangunanKearsipanInline,
                FotoGedungBangunanKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        return super(GedungBangunanKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanKearsipanAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanKearsipanInline,
                SKPDAsalGedungBangunanKearsipanInline,
                FotoGedungBangunanKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        return super(KDPGedungBangunanKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganKearsipanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusKearsipanAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungKearsipanInline,
                    SKPDAsalGedungBangunanKearsipanInline,
                    FotoGedungBangunanKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanKearsipanAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=44)
        return super(KontrakGedungBangunanKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=44)



class HargaGedungBangunanKearsipanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanKearsipanAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanKearsipanInline, TahunBerkurangGedungBangunanKearsipanInline,
                    SKPDAsalGedungBangunanKearsipanInline,
                    SKPDTujuanGedungBangunanKearsipanInline,
                    FotoGedungBangunanKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Kearsipan
admin.site.register(GedungBangunanKearsipan, GedungBangunanKearsipanAdmin)
admin.site.register(KDPGedungBangunanKearsipan, KDPGedungBangunanKearsipanAdmin)
admin.site.register(GedungBangunanRuanganKearsipan, GedungBangunanRuanganKearsipanAdmin)
admin.site.register(GedungBangunanUsulHapusKearsipan, GedungBangunanUsulHapusKearsipanAdmin)
admin.site.register(KontrakGedungBangunanKearsipan, KontrakGedungBangunanKearsipanAdmin)
admin.site.register(HargaGedungBangunanKearsipan, HargaGedungBangunanKearsipanAdmin)
admin.site.register(GedungBangunanPenghapusanKearsipan, GedungBangunanPenghapusanKearsipanAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinKearsipanInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinKearsipan



class PenghapusanPeralatanMesinKearsipanInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinKearsipan



class SKPDAsalPeralatanMesinKearsipanInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinKearsipan



class SKPDTujuanPeralatanMesinKearsipanInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinKearsipan



class FotoPeralatanMesinKearsipanInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinKearsipan



class HargaPeralatanMesinKearsipanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinKearsipan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=44)
        return super(HargaPeralatanMesinKearsipanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinKearsipanInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinKearsipan


class PeralatanMesinKearsipanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinKearsipanInline,
                    SKPDAsalPeralatanMesinKearsipanInline,
                    FotoPeralatanMesinKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=44)
        return super(PeralatanMesinKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusKearsipanAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinKearsipanInline,
                    SKPDAsalPeralatanMesinKearsipanInline,
                    FotoPeralatanMesinKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinKearsipanAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=44)
        return super(KontrakPeralatanMesinKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=44)



class HargaPeralatanMesinKearsipanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanKearsipanAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinKearsipanInline, TahunBerkurangPeralatanMesinKearsipanInline,
                    SKPDAsalPeralatanMesinKearsipanInline,
                    SKPDTujuanPeralatanMesinKearsipanInline,
                    FotoPeralatanMesinKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Kearsipan
admin.site.register(PeralatanMesinKearsipan, PeralatanMesinKearsipanAdmin)
admin.site.register(PeralatanMesinUsulHapusKearsipan, PeralatanMesinUsulHapusKearsipanAdmin)
admin.site.register(KontrakPeralatanMesinKearsipan, KontrakPeralatanMesinKearsipanAdmin)
admin.site.register(HargaPeralatanMesinKearsipan, HargaPeralatanMesinKearsipanAdmin)
admin.site.register(PeralatanMesinPenghapusanKearsipan, PeralatanMesinPenghapusanKearsipanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanKearsipan, KontrakJalanIrigasiJaringanKearsipan, HargaJalanIrigasiJaringanKearsipan, KDPJalanIrigasiJaringanKearsipan, JalanIrigasiJaringanUsulHapusKearsipan, TahunBerkurangUsulHapusJalanIrigasiJaringanKearsipan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanKearsipan, TahunBerkurangJalanIrigasiJaringanKearsipan, PenghapusanJalanIrigasiJaringanKearsipan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanKearsipan, SKPDTujuanJalanIrigasiJaringanKearsipan, FotoJalanIrigasiJaringanKearsipan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanKearsipanInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanKearsipan



class PenghapusanJalanIrigasiJaringanKearsipanInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanKearsipan



class SKPDAsalJalanIrigasiJaringanKearsipanInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanKearsipan



class SKPDTujuanJalanIrigasiJaringanKearsipanInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanKearsipan



class FotoJalanIrigasiJaringanKearsipanInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanKearsipan





class HargaJalanIrigasiJaringanKearsipanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanKearsipan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=44)
        return super(HargaJalanIrigasiJaringanKearsipanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanKearsipanInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanKearsipan


class JalanIrigasiJaringanKearsipanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKearsipanInline,
                    SKPDAsalJalanIrigasiJaringanKearsipanInline,
                    FotoJalanIrigasiJaringanKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        return super(JalanIrigasiJaringanKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusKearsipanAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanKearsipanInline,
                    SKPDAsalJalanIrigasiJaringanKearsipanInline,
                    FotoJalanIrigasiJaringanKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanKearsipanAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKearsipanInline,
                    SKPDAsalJalanIrigasiJaringanKearsipanInline,
                    FotoJalanIrigasiJaringanKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        return super(KDPJalanIrigasiJaringanKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanKearsipanAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=44)
        return super(KontrakJalanIrigasiJaringanKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=44)



class HargaJalanIrigasiJaringanKearsipanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanKearsipanAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanKearsipanInline, TahunBerkurangJalanIrigasiJaringanKearsipanInline,
                    SKPDAsalJalanIrigasiJaringanKearsipanInline,
                    SKPDTujuanJalanIrigasiJaringanKearsipanInline,
                    FotoJalanIrigasiJaringanKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Kearsipan
admin.site.register(JalanIrigasiJaringanKearsipan, JalanIrigasiJaringanKearsipanAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusKearsipan, JalanIrigasiJaringanUsulHapusKearsipanAdmin)
admin.site.register(KDPJalanIrigasiJaringanKearsipan, KDPJalanIrigasiJaringanKearsipanAdmin)
admin.site.register(KontrakJalanIrigasiJaringanKearsipan, KontrakJalanIrigasiJaringanKearsipanAdmin)
admin.site.register(HargaJalanIrigasiJaringanKearsipan, HargaJalanIrigasiJaringanKearsipanAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanKearsipan, JalanIrigasiJaringanPenghapusanKearsipanAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLKearsipan, KontrakATLKearsipan, HargaATLKearsipan, ATLUsulHapusKearsipan, TahunBerkurangUsulHapusATLKearsipan

from atl.models import ATLPenghapusanKearsipan, TahunBerkurangATLKearsipan, PenghapusanATLKearsipan

from atl.models import SKPDAsalATLKearsipan, SKPDTujuanATLKearsipan, FotoATLKearsipan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLKearsipanInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLKearsipan



class PenghapusanATLKearsipanInline(PenghapusanATLInline):
    model = PenghapusanATLKearsipan



class SKPDAsalATLKearsipanInline(SKPDAsalATLInline):
    model = SKPDAsalATLKearsipan



class SKPDTujuanATLKearsipanInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLKearsipan



class FotoATLKearsipanInline(FotoATLInline):
    model = FotoATLKearsipan



class HargaATLKearsipanInline(HargaATLInline):
    model = HargaATLKearsipan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=44)
        return super(HargaATLKearsipanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLKearsipanInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLKearsipan


class ATLKearsipanAdmin(ATLAdmin):
    inlines = [HargaATLKearsipanInline,
                    SKPDAsalATLKearsipanInline,
                    FotoATLKearsipanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=44)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=44)
        return super(ATLKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusKearsipanAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLKearsipanInline,
                    SKPDAsalATLKearsipanInline,
                    FotoATLKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLKearsipanAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=44)
        return super(KontrakATLKearsipanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=44)



class HargaATLKearsipanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanKearsipanAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLKearsipanInline, TahunBerkurangATLKearsipanInline,
                    SKPDAsalATLKearsipanInline,
                    SKPDTujuanATLKearsipanInline,
                    FotoATLKearsipanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=44)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Kearsipan
admin.site.register(ATLKearsipan, ATLKearsipanAdmin)
admin.site.register(ATLUsulHapusKearsipan, ATLUsulHapusKearsipanAdmin)
admin.site.register(KontrakATLKearsipan, KontrakATLKearsipanAdmin)
admin.site.register(HargaATLKearsipan, HargaATLKearsipanAdmin)
admin.site.register(ATLPenghapusanKearsipan, ATLPenghapusanKearsipanAdmin)
