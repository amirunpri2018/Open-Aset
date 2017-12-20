### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDukCatPil, KontrakTanahDukCatPil, HargaTanahDukCatPil, TanahUsulHapusDukCatPil, TahunBerkurangUsulHapusTanahDukCatPil

from umum.models import TanahPenghapusanDukCatPil, TahunBerkurangTanahDukCatPil, PenghapusanTanahDukCatPil

from umum.models import SKPDAsalTanahDukCatPil, SKPDTujuanTanahDukCatPil, FotoTanahDukCatPil

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDukCatPil, KontrakGedungBangunanDukCatPil, HargaGedungBangunanDukCatPil, GedungBangunanRuanganDukCatPil, GedungBangunanUsulHapusDukCatPil, TahunBerkurangUsulHapusGedungDukCatPil

from gedungbangunan.models import GedungBangunanPenghapusanDukCatPil, TahunBerkurangGedungBangunanDukCatPil, PenghapusanGedungBangunanDukCatPil

from gedungbangunan.models import SKPDAsalGedungBangunanDukCatPil, SKPDTujuanGedungBangunanDukCatPil, FotoGedungBangunanDukCatPil

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDukCatPil, KontrakPeralatanMesinDukCatPil, HargaPeralatanMesinDukCatPil, PeralatanMesinUsulHapusDukCatPil, TahunBerkurangUsulHapusPeralatanMesinDukCatPil

from peralatanmesin.models import PeralatanMesinPenghapusanDukCatPil, TahunBerkurangPeralatanMesinDukCatPil, PenghapusanPeralatanMesinDukCatPil

from peralatanmesin.models import SKPDAsalPeralatanMesinDukCatPil, SKPDTujuanPeralatanMesinDukCatPil, FotoPeralatanMesinDukCatPil

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDukCatPilInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDukCatPil



class PenghapusanTanahDukCatPilInline(PenghapusanTanahInline):
    model = PenghapusanTanahDukCatPil



class SKPDAsalTanahDukCatPilInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDukCatPil



class SKPDTujuanTanahDukCatPilInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDukCatPil



class FotoTanahDukCatPilInline(FotoTanahInline):
    model = FotoTanahDukCatPil



class GedungBangunanDukCatPilInline(GedungBangunanInline):
    model = GedungBangunanDukCatPil



class HargaTanahDukCatPilInline(HargaTanahInline):
    model = HargaTanahDukCatPil

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=12)
        return super(HargaTanahDukCatPilInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDukCatPilInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDukCatPil


class TanahDukCatPilAdmin(TanahAdmin):
    inlines = [HargaTanahDukCatPilInline,
                SKPDAsalTanahDukCatPilInline,
                FotoTanahDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        return super(TanahDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDukCatPilAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDukCatPilInline,
                SKPDAsalTanahDukCatPilInline,
                FotoTanahDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDukCatPilAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=12)
        return super(KontrakTanahDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=12)



class HargaTanahDukCatPilAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDukCatPilAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDukCatPilInline, TahunBerkurangTanahDukCatPilInline,
                    SKPDAsalTanahDukCatPilInline,
                    SKPDTujuanTanahDukCatPilInline,
                    FotoTanahDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DukCatPil
admin.site.register(TanahDukCatPil, TanahDukCatPilAdmin)
admin.site.register(TanahUsulHapusDukCatPil, TanahUsulHapusDukCatPilAdmin)
admin.site.register(KontrakTanahDukCatPil, KontrakTanahDukCatPilAdmin)
admin.site.register(HargaTanahDukCatPil, HargaTanahDukCatPilAdmin)
admin.site.register(TanahPenghapusanDukCatPil, TanahPenghapusanDukCatPilAdmin)



from gedungbangunan.models import KDPGedungBangunanDukCatPil


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDukCatPilInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDukCatPil



class PenghapusanGedungBangunanDukCatPilInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDukCatPil



class SKPDAsalGedungBangunanDukCatPilInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDukCatPil



class SKPDTujuanGedungBangunanDukCatPilInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDukCatPil



class FotoGedungBangunanDukCatPilInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDukCatPil



class HargaGedungBangunanDukCatPilInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDukCatPil

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=12)
        return super(HargaGedungBangunanDukCatPilInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDukCatPilInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDukCatPil


class GedungBangunanDukCatPilAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDukCatPilInline,
                SKPDAsalGedungBangunanDukCatPilInline,
                FotoGedungBangunanDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        return super(GedungBangunanDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDukCatPilAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDukCatPilInline,
                SKPDAsalGedungBangunanDukCatPilInline,
                FotoGedungBangunanDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        return super(KDPGedungBangunanDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDukCatPilAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDukCatPilAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDukCatPilInline,
                    SKPDAsalGedungBangunanDukCatPilInline,
                    FotoGedungBangunanDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDukCatPilAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=12)
        return super(KontrakGedungBangunanDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=12)



class HargaGedungBangunanDukCatPilAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDukCatPilAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDukCatPilInline, TahunBerkurangGedungBangunanDukCatPilInline,
                    SKPDAsalGedungBangunanDukCatPilInline,
                    SKPDTujuanGedungBangunanDukCatPilInline,
                    FotoGedungBangunanDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DukCatPil
admin.site.register(GedungBangunanDukCatPil, GedungBangunanDukCatPilAdmin)
admin.site.register(KDPGedungBangunanDukCatPil, KDPGedungBangunanDukCatPilAdmin)
admin.site.register(GedungBangunanRuanganDukCatPil, GedungBangunanRuanganDukCatPilAdmin)
admin.site.register(GedungBangunanUsulHapusDukCatPil, GedungBangunanUsulHapusDukCatPilAdmin)
admin.site.register(KontrakGedungBangunanDukCatPil, KontrakGedungBangunanDukCatPilAdmin)
admin.site.register(HargaGedungBangunanDukCatPil, HargaGedungBangunanDukCatPilAdmin)
admin.site.register(GedungBangunanPenghapusanDukCatPil, GedungBangunanPenghapusanDukCatPilAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDukCatPilInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDukCatPil



class PenghapusanPeralatanMesinDukCatPilInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDukCatPil



class SKPDAsalPeralatanMesinDukCatPilInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDukCatPil



class SKPDTujuanPeralatanMesinDukCatPilInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDukCatPil



class FotoPeralatanMesinDukCatPilInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDukCatPil



class HargaPeralatanMesinDukCatPilInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDukCatPil

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=12)
        return super(HargaPeralatanMesinDukCatPilInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDukCatPilInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDukCatPil


class PeralatanMesinDukCatPilAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDukCatPilInline,
                    SKPDAsalPeralatanMesinDukCatPilInline,
                    FotoPeralatanMesinDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=12)
        return super(PeralatanMesinDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDukCatPilAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDukCatPilInline,
                    SKPDAsalPeralatanMesinDukCatPilInline,
                    FotoPeralatanMesinDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDukCatPilAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=12)
        return super(KontrakPeralatanMesinDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=12)



class HargaPeralatanMesinDukCatPilAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDukCatPilAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDukCatPilInline, TahunBerkurangPeralatanMesinDukCatPilInline,
                    SKPDAsalPeralatanMesinDukCatPilInline,
                    SKPDTujuanPeralatanMesinDukCatPilInline,
                    FotoPeralatanMesinDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DukCatPil
admin.site.register(PeralatanMesinDukCatPil, PeralatanMesinDukCatPilAdmin)
admin.site.register(PeralatanMesinUsulHapusDukCatPil, PeralatanMesinUsulHapusDukCatPilAdmin)
admin.site.register(KontrakPeralatanMesinDukCatPil, KontrakPeralatanMesinDukCatPilAdmin)
admin.site.register(HargaPeralatanMesinDukCatPil, HargaPeralatanMesinDukCatPilAdmin)
admin.site.register(PeralatanMesinPenghapusanDukCatPil, PeralatanMesinPenghapusanDukCatPilAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDukCatPil, KontrakJalanIrigasiJaringanDukCatPil, HargaJalanIrigasiJaringanDukCatPil, KDPJalanIrigasiJaringanDukCatPil, JalanIrigasiJaringanUsulHapusDukCatPil, TahunBerkurangUsulHapusJalanIrigasiJaringanDukCatPil

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDukCatPil, TahunBerkurangJalanIrigasiJaringanDukCatPil, PenghapusanJalanIrigasiJaringanDukCatPil

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDukCatPil, SKPDTujuanJalanIrigasiJaringanDukCatPil, FotoJalanIrigasiJaringanDukCatPil

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDukCatPilInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDukCatPil



class PenghapusanJalanIrigasiJaringanDukCatPilInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDukCatPil



class SKPDAsalJalanIrigasiJaringanDukCatPilInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDukCatPil



class SKPDTujuanJalanIrigasiJaringanDukCatPilInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDukCatPil



class FotoJalanIrigasiJaringanDukCatPilInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDukCatPil





class HargaJalanIrigasiJaringanDukCatPilInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDukCatPil

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=12)
        return super(HargaJalanIrigasiJaringanDukCatPilInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDukCatPilInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDukCatPil


class JalanIrigasiJaringanDukCatPilAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDukCatPilInline,
                    SKPDAsalJalanIrigasiJaringanDukCatPilInline,
                    FotoJalanIrigasiJaringanDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        return super(JalanIrigasiJaringanDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDukCatPilAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDukCatPilInline,
                    SKPDAsalJalanIrigasiJaringanDukCatPilInline,
                    FotoJalanIrigasiJaringanDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDukCatPilAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDukCatPilInline,
                    SKPDAsalJalanIrigasiJaringanDukCatPilInline,
                    FotoJalanIrigasiJaringanDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        return super(KDPJalanIrigasiJaringanDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDukCatPilAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=12)
        return super(KontrakJalanIrigasiJaringanDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=12)



class HargaJalanIrigasiJaringanDukCatPilAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDukCatPilAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDukCatPilInline, TahunBerkurangJalanIrigasiJaringanDukCatPilInline,
                    SKPDAsalJalanIrigasiJaringanDukCatPilInline,
                    SKPDTujuanJalanIrigasiJaringanDukCatPilInline,
                    FotoJalanIrigasiJaringanDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DukCatPil
admin.site.register(JalanIrigasiJaringanDukCatPil, JalanIrigasiJaringanDukCatPilAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDukCatPil, JalanIrigasiJaringanUsulHapusDukCatPilAdmin)
admin.site.register(KDPJalanIrigasiJaringanDukCatPil, KDPJalanIrigasiJaringanDukCatPilAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDukCatPil, KontrakJalanIrigasiJaringanDukCatPilAdmin)
admin.site.register(HargaJalanIrigasiJaringanDukCatPil, HargaJalanIrigasiJaringanDukCatPilAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDukCatPil, JalanIrigasiJaringanPenghapusanDukCatPilAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDukCatPil, KontrakATLDukCatPil, HargaATLDukCatPil, ATLUsulHapusDukCatPil, TahunBerkurangUsulHapusATLDukCatPil

from atl.models import ATLPenghapusanDukCatPil, TahunBerkurangATLDukCatPil, PenghapusanATLDukCatPil

from atl.models import SKPDAsalATLDukCatPil, SKPDTujuanATLDukCatPil, FotoATLDukCatPil

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDukCatPilInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDukCatPil



class PenghapusanATLDukCatPilInline(PenghapusanATLInline):
    model = PenghapusanATLDukCatPil



class SKPDAsalATLDukCatPilInline(SKPDAsalATLInline):
    model = SKPDAsalATLDukCatPil



class SKPDTujuanATLDukCatPilInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDukCatPil



class FotoATLDukCatPilInline(FotoATLInline):
    model = FotoATLDukCatPil



class HargaATLDukCatPilInline(HargaATLInline):
    model = HargaATLDukCatPil

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=12)
        return super(HargaATLDukCatPilInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDukCatPilInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDukCatPil


class ATLDukCatPilAdmin(ATLAdmin):
    inlines = [HargaATLDukCatPilInline,
                    SKPDAsalATLDukCatPilInline,
                    FotoATLDukCatPilInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=12)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=12)
        return super(ATLDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDukCatPilAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDukCatPilInline,
                    SKPDAsalATLDukCatPilInline,
                    FotoATLDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDukCatPilAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=12)
        return super(KontrakATLDukCatPilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=12)



class HargaATLDukCatPilAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDukCatPilAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDukCatPilInline, TahunBerkurangATLDukCatPilInline,
                    SKPDAsalATLDukCatPilInline,
                    SKPDTujuanATLDukCatPilInline,
                    FotoATLDukCatPilInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=12)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DukCatPil
admin.site.register(ATLDukCatPil, ATLDukCatPilAdmin)
admin.site.register(ATLUsulHapusDukCatPil, ATLUsulHapusDukCatPilAdmin)
admin.site.register(KontrakATLDukCatPil, KontrakATLDukCatPilAdmin)
admin.site.register(HargaATLDukCatPil, HargaATLDukCatPilAdmin)
admin.site.register(ATLPenghapusanDukCatPil, ATLPenghapusanDukCatPilAdmin)
