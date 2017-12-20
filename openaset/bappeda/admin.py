### $Id: admin.py,v 1.30 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBAPPEDA, KontrakTanahBAPPEDA, HargaTanahBAPPEDA, TanahUsulHapusBAPPEDA, TahunBerkurangUsulHapusTanahBAPPEDA

from umum.models import TanahPenghapusanBAPPEDA, TahunBerkurangTanahBAPPEDA, PenghapusanTanahBAPPEDA

from umum.models import SKPDAsalTanahBAPPEDA, SKPDTujuanTanahBAPPEDA, FotoTanahBAPPEDA

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBAPPEDA, KontrakGedungBangunanBAPPEDA, HargaGedungBangunanBAPPEDA, GedungBangunanRuanganBAPPEDA, GedungBangunanUsulHapusBAPPEDA, TahunBerkurangUsulHapusGedungBAPPEDA

from gedungbangunan.models import GedungBangunanPenghapusanBAPPEDA, TahunBerkurangGedungBangunanBAPPEDA, PenghapusanGedungBangunanBAPPEDA

from gedungbangunan.models import SKPDAsalGedungBangunanBAPPEDA, SKPDTujuanGedungBangunanBAPPEDA, FotoGedungBangunanBAPPEDA

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBAPPEDA, KontrakPeralatanMesinBAPPEDA, HargaPeralatanMesinBAPPEDA, PeralatanMesinUsulHapusBAPPEDA, TahunBerkurangUsulHapusPeralatanMesinBAPPEDA

from peralatanmesin.models import PeralatanMesinPenghapusanBAPPEDA, TahunBerkurangPeralatanMesinBAPPEDA, PenghapusanPeralatanMesinBAPPEDA

from peralatanmesin.models import SKPDAsalPeralatanMesinBAPPEDA, SKPDTujuanPeralatanMesinBAPPEDA, FotoPeralatanMesinBAPPEDA

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBAPPEDAInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBAPPEDA



class PenghapusanTanahBAPPEDAInline(PenghapusanTanahInline):
    model = PenghapusanTanahBAPPEDA



class SKPDAsalTanahBAPPEDAInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBAPPEDA



class SKPDTujuanTanahBAPPEDAInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBAPPEDA



class FotoTanahBAPPEDAInline(FotoTanahInline):
    model = FotoTanahBAPPEDA



class GedungBangunanBAPPEDAInline(GedungBangunanInline):
    model = GedungBangunanBAPPEDA



class HargaTanahBAPPEDAInline(HargaTanahInline):
    model = HargaTanahBAPPEDA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=21)
        return super(HargaTanahBAPPEDAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBAPPEDAInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBAPPEDA


class TanahBAPPEDAAdmin(TanahAdmin):
    inlines = [HargaTanahBAPPEDAInline,
                SKPDAsalTanahBAPPEDAInline,
                FotoTanahBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        return super(TanahBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBAPPEDAAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBAPPEDAInline,
                SKPDAsalTanahBAPPEDAInline,
                FotoTanahBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBAPPEDAAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=21)
        return super(KontrakTanahBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=21)



class HargaTanahBAPPEDAAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBAPPEDAAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBAPPEDAInline, TahunBerkurangTanahBAPPEDAInline,
                    SKPDAsalTanahBAPPEDAInline,
                    SKPDTujuanTanahBAPPEDAInline,
                    FotoTanahBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah BAPPEDA
admin.site.register(TanahBAPPEDA, TanahBAPPEDAAdmin)
admin.site.register(TanahUsulHapusBAPPEDA, TanahUsulHapusBAPPEDAAdmin)
admin.site.register(KontrakTanahBAPPEDA, KontrakTanahBAPPEDAAdmin)
admin.site.register(HargaTanahBAPPEDA, HargaTanahBAPPEDAAdmin)
admin.site.register(TanahPenghapusanBAPPEDA, TanahPenghapusanBAPPEDAAdmin)



from gedungbangunan.models import KDPGedungBangunanBAPPEDA


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBAPPEDAInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBAPPEDA



class PenghapusanGedungBangunanBAPPEDAInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBAPPEDA



class SKPDAsalGedungBangunanBAPPEDAInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBAPPEDA



class SKPDTujuanGedungBangunanBAPPEDAInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBAPPEDA



class FotoGedungBangunanBAPPEDAInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBAPPEDA



class HargaGedungBangunanBAPPEDAInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBAPPEDA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=21)
        return super(HargaGedungBangunanBAPPEDAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBAPPEDAInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBAPPEDA


class GedungBangunanBAPPEDAAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBAPPEDAInline,
                SKPDAsalGedungBangunanBAPPEDAInline,
                FotoGedungBangunanBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        return super(GedungBangunanBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBAPPEDAAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBAPPEDAInline,
                SKPDAsalGedungBangunanBAPPEDAInline,
                FotoGedungBangunanBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        return super(KDPGedungBangunanBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBAPPEDAAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBAPPEDAAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBAPPEDAInline,
                    SKPDAsalGedungBangunanBAPPEDAInline,
                    FotoGedungBangunanBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBAPPEDAAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=21)
        return super(KontrakGedungBangunanBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=21)



class HargaGedungBangunanBAPPEDAAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBAPPEDAAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBAPPEDAInline, TahunBerkurangGedungBangunanBAPPEDAInline,
                    SKPDAsalGedungBangunanBAPPEDAInline,
                    SKPDTujuanGedungBangunanBAPPEDAInline,
                    FotoGedungBangunanBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan BAPPEDA
admin.site.register(GedungBangunanBAPPEDA, GedungBangunanBAPPEDAAdmin)
admin.site.register(KDPGedungBangunanBAPPEDA, KDPGedungBangunanBAPPEDAAdmin)
admin.site.register(GedungBangunanRuanganBAPPEDA, GedungBangunanRuanganBAPPEDAAdmin)
admin.site.register(GedungBangunanUsulHapusBAPPEDA, GedungBangunanUsulHapusBAPPEDAAdmin)
admin.site.register(KontrakGedungBangunanBAPPEDA, KontrakGedungBangunanBAPPEDAAdmin)
admin.site.register(HargaGedungBangunanBAPPEDA, HargaGedungBangunanBAPPEDAAdmin)
admin.site.register(GedungBangunanPenghapusanBAPPEDA, GedungBangunanPenghapusanBAPPEDAAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBAPPEDAInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBAPPEDA



class PenghapusanPeralatanMesinBAPPEDAInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBAPPEDA



class SKPDAsalPeralatanMesinBAPPEDAInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBAPPEDA



class SKPDTujuanPeralatanMesinBAPPEDAInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBAPPEDA



class FotoPeralatanMesinBAPPEDAInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBAPPEDA



class HargaPeralatanMesinBAPPEDAInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBAPPEDA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=21)
        return super(HargaPeralatanMesinBAPPEDAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBAPPEDAInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBAPPEDA


class PeralatanMesinBAPPEDAAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBAPPEDAInline,
                    SKPDAsalPeralatanMesinBAPPEDAInline,
                    FotoPeralatanMesinBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=21)
        return super(PeralatanMesinBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBAPPEDAAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBAPPEDAInline,
                    SKPDAsalPeralatanMesinBAPPEDAInline,
                    FotoPeralatanMesinBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBAPPEDAAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=21)
        return super(KontrakPeralatanMesinBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=21)



class HargaPeralatanMesinBAPPEDAAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBAPPEDAAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBAPPEDAInline, TahunBerkurangPeralatanMesinBAPPEDAInline,
                    SKPDAsalPeralatanMesinBAPPEDAInline,
                    SKPDTujuanPeralatanMesinBAPPEDAInline,
                    FotoPeralatanMesinBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin BAPPEDA
admin.site.register(PeralatanMesinBAPPEDA, PeralatanMesinBAPPEDAAdmin)
admin.site.register(PeralatanMesinUsulHapusBAPPEDA, PeralatanMesinUsulHapusBAPPEDAAdmin)
admin.site.register(KontrakPeralatanMesinBAPPEDA, KontrakPeralatanMesinBAPPEDAAdmin)
admin.site.register(HargaPeralatanMesinBAPPEDA, HargaPeralatanMesinBAPPEDAAdmin)
admin.site.register(PeralatanMesinPenghapusanBAPPEDA, PeralatanMesinPenghapusanBAPPEDAAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBAPPEDA, KontrakJalanIrigasiJaringanBAPPEDA, HargaJalanIrigasiJaringanBAPPEDA, KDPJalanIrigasiJaringanBAPPEDA, JalanIrigasiJaringanUsulHapusBAPPEDA, TahunBerkurangUsulHapusJalanIrigasiJaringanBAPPEDA

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBAPPEDA, TahunBerkurangJalanIrigasiJaringanBAPPEDA, PenghapusanJalanIrigasiJaringanBAPPEDA

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBAPPEDA, SKPDTujuanJalanIrigasiJaringanBAPPEDA, FotoJalanIrigasiJaringanBAPPEDA

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBAPPEDAInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBAPPEDA



class PenghapusanJalanIrigasiJaringanBAPPEDAInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBAPPEDA



class SKPDAsalJalanIrigasiJaringanBAPPEDAInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBAPPEDA



class SKPDTujuanJalanIrigasiJaringanBAPPEDAInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBAPPEDA



class FotoJalanIrigasiJaringanBAPPEDAInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBAPPEDA





class HargaJalanIrigasiJaringanBAPPEDAInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBAPPEDA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=21)
        return super(HargaJalanIrigasiJaringanBAPPEDAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBAPPEDAInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBAPPEDA


class JalanIrigasiJaringanBAPPEDAAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBAPPEDAInline,
                    SKPDAsalJalanIrigasiJaringanBAPPEDAInline,
                    FotoJalanIrigasiJaringanBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        return super(JalanIrigasiJaringanBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBAPPEDAAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBAPPEDAInline,
                    SKPDAsalJalanIrigasiJaringanBAPPEDAInline,
                    FotoJalanIrigasiJaringanBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBAPPEDAAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBAPPEDAInline,
                    SKPDAsalJalanIrigasiJaringanBAPPEDAInline,
                    FotoJalanIrigasiJaringanBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        return super(KDPJalanIrigasiJaringanBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBAPPEDAAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=21)
        return super(KontrakJalanIrigasiJaringanBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=21)



class HargaJalanIrigasiJaringanBAPPEDAAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBAPPEDAAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBAPPEDAInline, TahunBerkurangJalanIrigasiJaringanBAPPEDAInline,
                    SKPDAsalJalanIrigasiJaringanBAPPEDAInline,
                    SKPDTujuanJalanIrigasiJaringanBAPPEDAInline,
                    FotoJalanIrigasiJaringanBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan BAPPEDA
admin.site.register(JalanIrigasiJaringanBAPPEDA, JalanIrigasiJaringanBAPPEDAAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBAPPEDA, JalanIrigasiJaringanUsulHapusBAPPEDAAdmin)
admin.site.register(KDPJalanIrigasiJaringanBAPPEDA, KDPJalanIrigasiJaringanBAPPEDAAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBAPPEDA, KontrakJalanIrigasiJaringanBAPPEDAAdmin)
admin.site.register(HargaJalanIrigasiJaringanBAPPEDA, HargaJalanIrigasiJaringanBAPPEDAAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBAPPEDA, JalanIrigasiJaringanPenghapusanBAPPEDAAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBAPPEDA, KontrakATLBAPPEDA, HargaATLBAPPEDA, ATLUsulHapusBAPPEDA, TahunBerkurangUsulHapusATLBAPPEDA

from atl.models import ATLPenghapusanBAPPEDA, TahunBerkurangATLBAPPEDA, PenghapusanATLBAPPEDA

from atl.models import SKPDAsalATLBAPPEDA, SKPDTujuanATLBAPPEDA, FotoATLBAPPEDA

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBAPPEDAInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBAPPEDA



class PenghapusanATLBAPPEDAInline(PenghapusanATLInline):
    model = PenghapusanATLBAPPEDA



class SKPDAsalATLBAPPEDAInline(SKPDAsalATLInline):
    model = SKPDAsalATLBAPPEDA



class SKPDTujuanATLBAPPEDAInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBAPPEDA



class FotoATLBAPPEDAInline(FotoATLInline):
    model = FotoATLBAPPEDA



class HargaATLBAPPEDAInline(HargaATLInline):
    model = HargaATLBAPPEDA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=21)
        return super(HargaATLBAPPEDAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBAPPEDAInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBAPPEDA


class ATLBAPPEDAAdmin(ATLAdmin):
    inlines = [HargaATLBAPPEDAInline,
                    SKPDAsalATLBAPPEDAInline,
                    FotoATLBAPPEDAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=21)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=21)
        return super(ATLBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBAPPEDAAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBAPPEDAInline,
                    SKPDAsalATLBAPPEDAInline,
                    FotoATLBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBAPPEDAAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=21)
        return super(KontrakATLBAPPEDAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=21)



class HargaATLBAPPEDAAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBAPPEDAAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBAPPEDAInline, TahunBerkurangATLBAPPEDAInline,
                    SKPDAsalATLBAPPEDAInline,
                    SKPDTujuanATLBAPPEDAInline,
                    FotoATLBAPPEDAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=21)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL BAPPEDA
admin.site.register(ATLBAPPEDA, ATLBAPPEDAAdmin)
admin.site.register(ATLUsulHapusBAPPEDA, ATLUsulHapusBAPPEDAAdmin)
admin.site.register(KontrakATLBAPPEDA, KontrakATLBAPPEDAAdmin)
admin.site.register(HargaATLBAPPEDA, HargaATLBAPPEDAAdmin)
admin.site.register(ATLPenghapusanBAPPEDA, ATLPenghapusanBAPPEDAAdmin)
