### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBKPPD, KontrakTanahBKPPD, HargaTanahBKPPD, TanahUsulHapusBKPPD, TahunBerkurangUsulHapusTanahBKPPD

from umum.models import TanahPenghapusanBKPPD, TahunBerkurangTanahBKPPD, PenghapusanTanahBKPPD

from umum.models import SKPDAsalTanahBKPPD, SKPDTujuanTanahBKPPD, FotoTanahBKPPD

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBKPPD, KontrakGedungBangunanBKPPD, HargaGedungBangunanBKPPD, GedungBangunanRuanganBKPPD, GedungBangunanUsulHapusBKPPD, TahunBerkurangUsulHapusGedungBKPPD

from gedungbangunan.models import GedungBangunanPenghapusanBKPPD, TahunBerkurangGedungBangunanBKPPD, PenghapusanGedungBangunanBKPPD

from gedungbangunan.models import SKPDAsalGedungBangunanBKPPD, SKPDTujuanGedungBangunanBKPPD, FotoGedungBangunanBKPPD

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBKPPD, KontrakPeralatanMesinBKPPD, HargaPeralatanMesinBKPPD, PeralatanMesinUsulHapusBKPPD, TahunBerkurangUsulHapusPeralatanMesinBKPPD

from peralatanmesin.models import PeralatanMesinPenghapusanBKPPD, TahunBerkurangPeralatanMesinBKPPD, PenghapusanPeralatanMesinBKPPD

from peralatanmesin.models import SKPDAsalPeralatanMesinBKPPD, SKPDTujuanPeralatanMesinBKPPD, FotoPeralatanMesinBKPPD

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBKPPDInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBKPPD



class PenghapusanTanahBKPPDInline(PenghapusanTanahInline):
    model = PenghapusanTanahBKPPD



class SKPDAsalTanahBKPPDInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBKPPD



class SKPDTujuanTanahBKPPDInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBKPPD



class FotoTanahBKPPDInline(FotoTanahInline):
    model = FotoTanahBKPPD



class GedungBangunanBKPPDInline(GedungBangunanInline):
    model = GedungBangunanBKPPD



class HargaTanahBKPPDInline(HargaTanahInline):
    model = HargaTanahBKPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=26)
        return super(HargaTanahBKPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBKPPDInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBKPPD


class TanahBKPPDAdmin(TanahAdmin):
    inlines = [HargaTanahBKPPDInline,
                SKPDAsalTanahBKPPDInline,
                FotoTanahBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        return super(TanahBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBKPPDAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBKPPDInline,
                SKPDAsalTanahBKPPDInline,
                FotoTanahBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBKPPDAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=26)
        return super(KontrakTanahBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=26)



class HargaTanahBKPPDAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBKPPDAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBKPPDInline, TahunBerkurangTanahBKPPDInline,
                    SKPDAsalTanahBKPPDInline,
                    SKPDTujuanTanahBKPPDInline,
                    FotoTanahBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah BKPPD
admin.site.register(TanahBKPPD, TanahBKPPDAdmin)
admin.site.register(TanahUsulHapusBKPPD, TanahUsulHapusBKPPDAdmin)
admin.site.register(KontrakTanahBKPPD, KontrakTanahBKPPDAdmin)
admin.site.register(HargaTanahBKPPD, HargaTanahBKPPDAdmin)
admin.site.register(TanahPenghapusanBKPPD, TanahPenghapusanBKPPDAdmin)



from gedungbangunan.models import KDPGedungBangunanBKPPD


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBKPPDInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBKPPD



class PenghapusanGedungBangunanBKPPDInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBKPPD



class SKPDAsalGedungBangunanBKPPDInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBKPPD



class SKPDTujuanGedungBangunanBKPPDInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBKPPD



class FotoGedungBangunanBKPPDInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBKPPD



class HargaGedungBangunanBKPPDInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBKPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=26)
        return super(HargaGedungBangunanBKPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBKPPDInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBKPPD


class GedungBangunanBKPPDAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBKPPDInline,
                SKPDAsalGedungBangunanBKPPDInline,
                FotoGedungBangunanBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        return super(GedungBangunanBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBKPPDAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBKPPDInline,
                SKPDAsalGedungBangunanBKPPDInline,
                FotoGedungBangunanBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        return super(KDPGedungBangunanBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBKPPDAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBKPPDAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBKPPDInline,
                    SKPDAsalGedungBangunanBKPPDInline,
                    FotoGedungBangunanBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBKPPDAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=26)
        return super(KontrakGedungBangunanBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=26)



class HargaGedungBangunanBKPPDAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBKPPDAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBKPPDInline, TahunBerkurangGedungBangunanBKPPDInline,
                    SKPDAsalGedungBangunanBKPPDInline,
                    SKPDTujuanGedungBangunanBKPPDInline,
                    FotoGedungBangunanBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan BKPPD
admin.site.register(GedungBangunanBKPPD, GedungBangunanBKPPDAdmin)
admin.site.register(KDPGedungBangunanBKPPD, KDPGedungBangunanBKPPDAdmin)
admin.site.register(GedungBangunanRuanganBKPPD, GedungBangunanRuanganBKPPDAdmin)
admin.site.register(GedungBangunanUsulHapusBKPPD, GedungBangunanUsulHapusBKPPDAdmin)
admin.site.register(KontrakGedungBangunanBKPPD, KontrakGedungBangunanBKPPDAdmin)
admin.site.register(HargaGedungBangunanBKPPD, HargaGedungBangunanBKPPDAdmin)
admin.site.register(GedungBangunanPenghapusanBKPPD, GedungBangunanPenghapusanBKPPDAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBKPPDInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBKPPD



class PenghapusanPeralatanMesinBKPPDInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBKPPD



class SKPDAsalPeralatanMesinBKPPDInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBKPPD



class SKPDTujuanPeralatanMesinBKPPDInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBKPPD



class FotoPeralatanMesinBKPPDInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBKPPD



class HargaPeralatanMesinBKPPDInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBKPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=26)
        return super(HargaPeralatanMesinBKPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBKPPDInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBKPPD


class PeralatanMesinBKPPDAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBKPPDInline,
                    SKPDAsalPeralatanMesinBKPPDInline,
                    FotoPeralatanMesinBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=26)
        return super(PeralatanMesinBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBKPPDAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBKPPDInline,
                    SKPDAsalPeralatanMesinBKPPDInline,
                    FotoPeralatanMesinBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBKPPDAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=26)
        return super(KontrakPeralatanMesinBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=26)



class HargaPeralatanMesinBKPPDAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBKPPDAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBKPPDInline, TahunBerkurangPeralatanMesinBKPPDInline,
                    SKPDAsalPeralatanMesinBKPPDInline,
                    SKPDTujuanPeralatanMesinBKPPDInline,
                    FotoPeralatanMesinBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin BKPPD
admin.site.register(PeralatanMesinBKPPD, PeralatanMesinBKPPDAdmin)
admin.site.register(PeralatanMesinUsulHapusBKPPD, PeralatanMesinUsulHapusBKPPDAdmin)
admin.site.register(KontrakPeralatanMesinBKPPD, KontrakPeralatanMesinBKPPDAdmin)
admin.site.register(HargaPeralatanMesinBKPPD, HargaPeralatanMesinBKPPDAdmin)
admin.site.register(PeralatanMesinPenghapusanBKPPD, PeralatanMesinPenghapusanBKPPDAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBKPPD, KontrakJalanIrigasiJaringanBKPPD, HargaJalanIrigasiJaringanBKPPD, KDPJalanIrigasiJaringanBKPPD, JalanIrigasiJaringanUsulHapusBKPPD, TahunBerkurangUsulHapusJalanIrigasiJaringanBKPPD

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBKPPD, TahunBerkurangJalanIrigasiJaringanBKPPD, PenghapusanJalanIrigasiJaringanBKPPD

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBKPPD, SKPDTujuanJalanIrigasiJaringanBKPPD, FotoJalanIrigasiJaringanBKPPD

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBKPPDInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBKPPD



class PenghapusanJalanIrigasiJaringanBKPPDInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBKPPD



class SKPDAsalJalanIrigasiJaringanBKPPDInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBKPPD



class SKPDTujuanJalanIrigasiJaringanBKPPDInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBKPPD



class FotoJalanIrigasiJaringanBKPPDInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBKPPD





class HargaJalanIrigasiJaringanBKPPDInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBKPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=26)
        return super(HargaJalanIrigasiJaringanBKPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBKPPDInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBKPPD


class JalanIrigasiJaringanBKPPDAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBKPPDInline,
                    SKPDAsalJalanIrigasiJaringanBKPPDInline,
                    FotoJalanIrigasiJaringanBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        return super(JalanIrigasiJaringanBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBKPPDAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBKPPDInline,
                    SKPDAsalJalanIrigasiJaringanBKPPDInline,
                    FotoJalanIrigasiJaringanBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBKPPDAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBKPPDInline,
                    SKPDAsalJalanIrigasiJaringanBKPPDInline,
                    FotoJalanIrigasiJaringanBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        return super(KDPJalanIrigasiJaringanBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBKPPDAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=26)
        return super(KontrakJalanIrigasiJaringanBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=26)



class HargaJalanIrigasiJaringanBKPPDAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBKPPDAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBKPPDInline, TahunBerkurangJalanIrigasiJaringanBKPPDInline,
                    SKPDAsalJalanIrigasiJaringanBKPPDInline,
                    SKPDTujuanJalanIrigasiJaringanBKPPDInline,
                    FotoJalanIrigasiJaringanBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan BKPPD
admin.site.register(JalanIrigasiJaringanBKPPD, JalanIrigasiJaringanBKPPDAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBKPPD, JalanIrigasiJaringanUsulHapusBKPPDAdmin)
admin.site.register(KDPJalanIrigasiJaringanBKPPD, KDPJalanIrigasiJaringanBKPPDAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBKPPD, KontrakJalanIrigasiJaringanBKPPDAdmin)
admin.site.register(HargaJalanIrigasiJaringanBKPPD, HargaJalanIrigasiJaringanBKPPDAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBKPPD, JalanIrigasiJaringanPenghapusanBKPPDAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBKPPD, KontrakATLBKPPD, HargaATLBKPPD, ATLUsulHapusBKPPD, TahunBerkurangUsulHapusATLBKPPD

from atl.models import ATLPenghapusanBKPPD, TahunBerkurangATLBKPPD, PenghapusanATLBKPPD

from atl.models import SKPDAsalATLBKPPD, SKPDTujuanATLBKPPD, FotoATLBKPPD

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBKPPDInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBKPPD



class PenghapusanATLBKPPDInline(PenghapusanATLInline):
    model = PenghapusanATLBKPPD



class SKPDAsalATLBKPPDInline(SKPDAsalATLInline):
    model = SKPDAsalATLBKPPD



class SKPDTujuanATLBKPPDInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBKPPD



class FotoATLBKPPDInline(FotoATLInline):
    model = FotoATLBKPPD



class HargaATLBKPPDInline(HargaATLInline):
    model = HargaATLBKPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=26)
        return super(HargaATLBKPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBKPPDInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBKPPD


class ATLBKPPDAdmin(ATLAdmin):
    inlines = [HargaATLBKPPDInline,
                    SKPDAsalATLBKPPDInline,
                    FotoATLBKPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=26)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=26)
        return super(ATLBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBKPPDAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBKPPDInline,
                    SKPDAsalATLBKPPDInline,
                    FotoATLBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBKPPDAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=26)
        return super(KontrakATLBKPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=26)



class HargaATLBKPPDAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBKPPDAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBKPPDInline, TahunBerkurangATLBKPPDInline,
                    SKPDAsalATLBKPPDInline,
                    SKPDTujuanATLBKPPDInline,
                    FotoATLBKPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=26)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL BKPPD
admin.site.register(ATLBKPPD, ATLBKPPDAdmin)
admin.site.register(ATLUsulHapusBKPPD, ATLUsulHapusBKPPDAdmin)
admin.site.register(KontrakATLBKPPD, KontrakATLBKPPDAdmin)
admin.site.register(HargaATLBKPPD, HargaATLBKPPDAdmin)
admin.site.register(ATLPenghapusanBKPPD, ATLPenghapusanBKPPDAdmin)
