### $Id: admin.py,v 1.26 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBPBD, KontrakTanahBPBD, HargaTanahBPBD, TanahUsulHapusBPBD, TahunBerkurangUsulHapusTanahBPBD

from umum.models import TanahPenghapusanBPBD, TahunBerkurangTanahBPBD, PenghapusanTanahBPBD

from umum.models import SKPDAsalTanahBPBD, SKPDTujuanTanahBPBD, FotoTanahBPBD

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBPBD, KontrakGedungBangunanBPBD, HargaGedungBangunanBPBD, GedungBangunanRuanganBPBD, GedungBangunanUsulHapusBPBD, TahunBerkurangUsulHapusGedungBPBD

from gedungbangunan.models import GedungBangunanPenghapusanBPBD, TahunBerkurangGedungBangunanBPBD, PenghapusanGedungBangunanBPBD

from gedungbangunan.models import SKPDAsalGedungBangunanBPBD, SKPDTujuanGedungBangunanBPBD, FotoGedungBangunanBPBD

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBPBD, KontrakPeralatanMesinBPBD, HargaPeralatanMesinBPBD, PeralatanMesinUsulHapusBPBD, TahunBerkurangUsulHapusPeralatanMesinBPBD

from peralatanmesin.models import PeralatanMesinPenghapusanBPBD, TahunBerkurangPeralatanMesinBPBD, PenghapusanPeralatanMesinBPBD

from peralatanmesin.models import SKPDAsalPeralatanMesinBPBD, SKPDTujuanPeralatanMesinBPBD, FotoPeralatanMesinBPBD

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBPBDInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBPBD



class PenghapusanTanahBPBDInline(PenghapusanTanahInline):
    model = PenghapusanTanahBPBD



class SKPDAsalTanahBPBDInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBPBD



class SKPDTujuanTanahBPBDInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBPBD



class FotoTanahBPBDInline(FotoTanahInline):
    model = FotoTanahBPBD



class GedungBangunanBPBDInline(GedungBangunanInline):
    model = GedungBangunanBPBD



class HargaTanahBPBDInline(HargaTanahInline):
    model = HargaTanahBPBD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=39)
        return super(HargaTanahBPBDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBPBDInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBPBD


class TanahBPBDAdmin(TanahAdmin):
    inlines = [HargaTanahBPBDInline,
                SKPDAsalTanahBPBDInline,
                FotoTanahBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        return super(TanahBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBPBDAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBPBDInline,
                SKPDAsalTanahBPBDInline,
                FotoTanahBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBPBDAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=39)
        return super(KontrakTanahBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=39)



class HargaTanahBPBDAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBPBDAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBPBDInline, TahunBerkurangTanahBPBDInline,
                    SKPDAsalTanahBPBDInline,
                    SKPDTujuanTanahBPBDInline,
                    FotoTanahBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah BPBD
admin.site.register(TanahBPBD, TanahBPBDAdmin)
admin.site.register(TanahUsulHapusBPBD, TanahUsulHapusBPBDAdmin)
admin.site.register(KontrakTanahBPBD, KontrakTanahBPBDAdmin)
admin.site.register(HargaTanahBPBD, HargaTanahBPBDAdmin)
admin.site.register(TanahPenghapusanBPBD, TanahPenghapusanBPBDAdmin)



from gedungbangunan.models import KDPGedungBangunanBPBD


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBPBDInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBPBD



class PenghapusanGedungBangunanBPBDInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBPBD



class SKPDAsalGedungBangunanBPBDInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBPBD



class SKPDTujuanGedungBangunanBPBDInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBPBD



class FotoGedungBangunanBPBDInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBPBD



class HargaGedungBangunanBPBDInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBPBD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=39)
        return super(HargaGedungBangunanBPBDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBPBDInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBPBD


class GedungBangunanBPBDAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBPBDInline,
                SKPDAsalGedungBangunanBPBDInline,
                FotoGedungBangunanBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        return super(GedungBangunanBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBPBDAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBPBDInline,
                SKPDAsalGedungBangunanBPBDInline,
                FotoGedungBangunanBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        return super(KDPGedungBangunanBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBPBDAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBPBDAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBPBDInline,
                    SKPDAsalGedungBangunanBPBDInline,
                    FotoGedungBangunanBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBPBDAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=39)
        return super(KontrakGedungBangunanBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=39)



class HargaGedungBangunanBPBDAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBPBDAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBPBDInline, TahunBerkurangGedungBangunanBPBDInline,
                    SKPDAsalGedungBangunanBPBDInline,
                    SKPDTujuanGedungBangunanBPBDInline,
                    FotoGedungBangunanBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan BPBD
admin.site.register(GedungBangunanBPBD, GedungBangunanBPBDAdmin)
admin.site.register(KDPGedungBangunanBPBD, KDPGedungBangunanBPBDAdmin)
admin.site.register(GedungBangunanRuanganBPBD, GedungBangunanRuanganBPBDAdmin)
admin.site.register(GedungBangunanUsulHapusBPBD, GedungBangunanUsulHapusBPBDAdmin)
admin.site.register(KontrakGedungBangunanBPBD, KontrakGedungBangunanBPBDAdmin)
admin.site.register(HargaGedungBangunanBPBD, HargaGedungBangunanBPBDAdmin)
admin.site.register(GedungBangunanPenghapusanBPBD, GedungBangunanPenghapusanBPBDAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBPBDInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBPBD



class PenghapusanPeralatanMesinBPBDInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBPBD



class SKPDAsalPeralatanMesinBPBDInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBPBD



class SKPDTujuanPeralatanMesinBPBDInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBPBD



class FotoPeralatanMesinBPBDInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBPBD



class HargaPeralatanMesinBPBDInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBPBD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=39)
        return super(HargaPeralatanMesinBPBDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBPBDInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBPBD


class PeralatanMesinBPBDAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBPBDInline,
                    SKPDAsalPeralatanMesinBPBDInline,
                    FotoPeralatanMesinBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=39)
        return super(PeralatanMesinBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBPBDAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBPBDInline,
                    SKPDAsalPeralatanMesinBPBDInline,
                    FotoPeralatanMesinBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBPBDAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=39)
        return super(KontrakPeralatanMesinBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=39)



class HargaPeralatanMesinBPBDAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBPBDAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBPBDInline, TahunBerkurangPeralatanMesinBPBDInline,
                    SKPDAsalPeralatanMesinBPBDInline,
                    SKPDTujuanPeralatanMesinBPBDInline,
                    FotoPeralatanMesinBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin BPBD
admin.site.register(PeralatanMesinBPBD, PeralatanMesinBPBDAdmin)
admin.site.register(PeralatanMesinUsulHapusBPBD, PeralatanMesinUsulHapusBPBDAdmin)
admin.site.register(KontrakPeralatanMesinBPBD, KontrakPeralatanMesinBPBDAdmin)
admin.site.register(HargaPeralatanMesinBPBD, HargaPeralatanMesinBPBDAdmin)
admin.site.register(PeralatanMesinPenghapusanBPBD, PeralatanMesinPenghapusanBPBDAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBPBD, KontrakJalanIrigasiJaringanBPBD, HargaJalanIrigasiJaringanBPBD, KDPJalanIrigasiJaringanBPBD, JalanIrigasiJaringanUsulHapusBPBD, TahunBerkurangUsulHapusJalanIrigasiJaringanBPBD

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBPBD, TahunBerkurangJalanIrigasiJaringanBPBD, PenghapusanJalanIrigasiJaringanBPBD

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBPBD, SKPDTujuanJalanIrigasiJaringanBPBD, FotoJalanIrigasiJaringanBPBD

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBPBDInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBPBD



class PenghapusanJalanIrigasiJaringanBPBDInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBPBD



class SKPDAsalJalanIrigasiJaringanBPBDInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBPBD



class SKPDTujuanJalanIrigasiJaringanBPBDInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBPBD



class FotoJalanIrigasiJaringanBPBDInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBPBD





class HargaJalanIrigasiJaringanBPBDInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBPBD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=39)
        return super(HargaJalanIrigasiJaringanBPBDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBPBDInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBPBD


class JalanIrigasiJaringanBPBDAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBPBDInline,
                    SKPDAsalJalanIrigasiJaringanBPBDInline,
                    FotoJalanIrigasiJaringanBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        return super(JalanIrigasiJaringanBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBPBDAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBPBDInline,
                    SKPDAsalJalanIrigasiJaringanBPBDInline,
                    FotoJalanIrigasiJaringanBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBPBDAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBPBDInline,
                    SKPDAsalJalanIrigasiJaringanBPBDInline,
                    FotoJalanIrigasiJaringanBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        return super(KDPJalanIrigasiJaringanBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBPBDAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=39)
        return super(KontrakJalanIrigasiJaringanBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=39)



class HargaJalanIrigasiJaringanBPBDAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBPBDAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBPBDInline, TahunBerkurangJalanIrigasiJaringanBPBDInline,
                    SKPDAsalJalanIrigasiJaringanBPBDInline,
                    SKPDTujuanJalanIrigasiJaringanBPBDInline,
                    FotoJalanIrigasiJaringanBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan BPBD
admin.site.register(JalanIrigasiJaringanBPBD, JalanIrigasiJaringanBPBDAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBPBD, JalanIrigasiJaringanUsulHapusBPBDAdmin)
admin.site.register(KDPJalanIrigasiJaringanBPBD, KDPJalanIrigasiJaringanBPBDAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBPBD, KontrakJalanIrigasiJaringanBPBDAdmin)
admin.site.register(HargaJalanIrigasiJaringanBPBD, HargaJalanIrigasiJaringanBPBDAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBPBD, JalanIrigasiJaringanPenghapusanBPBDAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBPBD, KontrakATLBPBD, HargaATLBPBD, ATLUsulHapusBPBD, TahunBerkurangUsulHapusATLBPBD

from atl.models import ATLPenghapusanBPBD, TahunBerkurangATLBPBD, PenghapusanATLBPBD

from atl.models import SKPDAsalATLBPBD, SKPDTujuanATLBPBD, FotoATLBPBD

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBPBDInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBPBD



class PenghapusanATLBPBDInline(PenghapusanATLInline):
    model = PenghapusanATLBPBD



class SKPDAsalATLBPBDInline(SKPDAsalATLInline):
    model = SKPDAsalATLBPBD



class SKPDTujuanATLBPBDInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBPBD



class FotoATLBPBDInline(FotoATLInline):
    model = FotoATLBPBD



class HargaATLBPBDInline(HargaATLInline):
    model = HargaATLBPBD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=39)
        return super(HargaATLBPBDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBPBDInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBPBD


class ATLBPBDAdmin(ATLAdmin):
    inlines = [HargaATLBPBDInline,
                    SKPDAsalATLBPBDInline,
                    FotoATLBPBDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=39)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=39)
        return super(ATLBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBPBDAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBPBDInline,
                    SKPDAsalATLBPBDInline,
                    FotoATLBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBPBDAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=39)
        return super(KontrakATLBPBDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=39)



class HargaATLBPBDAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBPBDAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBPBDInline, TahunBerkurangATLBPBDInline,
                    SKPDAsalATLBPBDInline,
                    SKPDTujuanATLBPBDInline,
                    FotoATLBPBDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=39)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL BPBD
admin.site.register(ATLBPBD, ATLBPBDAdmin)
admin.site.register(ATLUsulHapusBPBD, ATLUsulHapusBPBDAdmin)
admin.site.register(KontrakATLBPBD, KontrakATLBPBDAdmin)
admin.site.register(HargaATLBPBD, HargaATLBPBDAdmin)
admin.site.register(ATLPenghapusanBPBD, ATLPenghapusanBPBDAdmin)
