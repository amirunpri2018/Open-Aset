### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBPPD, KontrakTanahBPPD, HargaTanahBPPD, TanahUsulHapusBPPD, TahunBerkurangUsulHapusTanahBPPD

from umum.models import TanahPenghapusanBPPD, TahunBerkurangTanahBPPD, PenghapusanTanahBPPD

from umum.models import SKPDAsalTanahBPPD, SKPDTujuanTanahBPPD, FotoTanahBPPD

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBPPD, KontrakGedungBangunanBPPD, HargaGedungBangunanBPPD, GedungBangunanRuanganBPPD, GedungBangunanUsulHapusBPPD, TahunBerkurangUsulHapusGedungBPPD

from gedungbangunan.models import GedungBangunanPenghapusanBPPD, TahunBerkurangGedungBangunanBPPD, PenghapusanGedungBangunanBPPD

from gedungbangunan.models import SKPDAsalGedungBangunanBPPD, SKPDTujuanGedungBangunanBPPD, FotoGedungBangunanBPPD

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBPPD, KontrakPeralatanMesinBPPD, HargaPeralatanMesinBPPD, PeralatanMesinUsulHapusBPPD, TahunBerkurangUsulHapusPeralatanMesinBPPD

from peralatanmesin.models import PeralatanMesinPenghapusanBPPD, TahunBerkurangPeralatanMesinBPPD, PenghapusanPeralatanMesinBPPD

from peralatanmesin.models import SKPDAsalPeralatanMesinBPPD, SKPDTujuanPeralatanMesinBPPD, FotoPeralatanMesinBPPD

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBPPDInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBPPD



class PenghapusanTanahBPPDInline(PenghapusanTanahInline):
    model = PenghapusanTanahBPPD



class SKPDAsalTanahBPPDInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBPPD



class SKPDTujuanTanahBPPDInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBPPD



class FotoTanahBPPDInline(FotoTanahInline):
    model = FotoTanahBPPD



class GedungBangunanBPPDInline(GedungBangunanInline):
    model = GedungBangunanBPPD



class HargaTanahBPPDInline(HargaTanahInline):
    model = HargaTanahBPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=48)
        return super(HargaTanahBPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBPPDInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBPPD


class TanahBPPDAdmin(TanahAdmin):
    inlines = [HargaTanahBPPDInline,
                SKPDAsalTanahBPPDInline,
                FotoTanahBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        return super(TanahBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBPPDAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBPPDInline,
                SKPDAsalTanahBPPDInline,
                FotoTanahBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBPPDAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=48)
        return super(KontrakTanahBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=48)



class HargaTanahBPPDAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBPPDAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBPPDInline, TahunBerkurangTanahBPPDInline,
                    SKPDAsalTanahBPPDInline,
                    SKPDTujuanTanahBPPDInline,
                    FotoTanahBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah BPPD
admin.site.register(TanahBPPD, TanahBPPDAdmin)
admin.site.register(TanahUsulHapusBPPD, TanahUsulHapusBPPDAdmin)
admin.site.register(KontrakTanahBPPD, KontrakTanahBPPDAdmin)
admin.site.register(HargaTanahBPPD, HargaTanahBPPDAdmin)
admin.site.register(TanahPenghapusanBPPD, TanahPenghapusanBPPDAdmin)



from gedungbangunan.models import KDPGedungBangunanBPPD


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBPPDInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBPPD



class PenghapusanGedungBangunanBPPDInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBPPD



class SKPDAsalGedungBangunanBPPDInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBPPD



class SKPDTujuanGedungBangunanBPPDInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBPPD



class FotoGedungBangunanBPPDInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBPPD



class HargaGedungBangunanBPPDInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=48)
        return super(HargaGedungBangunanBPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBPPDInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBPPD


class GedungBangunanBPPDAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBPPDInline,
                SKPDAsalGedungBangunanBPPDInline,
                FotoGedungBangunanBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        return super(GedungBangunanBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBPPDAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBPPDInline,
                SKPDAsalGedungBangunanBPPDInline,
                FotoGedungBangunanBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        return super(KDPGedungBangunanBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBPPDAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBPPDAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBPPDInline,
                    SKPDAsalGedungBangunanBPPDInline,
                    FotoGedungBangunanBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBPPDAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=48)
        return super(KontrakGedungBangunanBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=48)



class HargaGedungBangunanBPPDAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBPPDAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBPPDInline, TahunBerkurangGedungBangunanBPPDInline,
                    SKPDAsalGedungBangunanBPPDInline,
                    SKPDTujuanGedungBangunanBPPDInline,
                    FotoGedungBangunanBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan BPPD
admin.site.register(GedungBangunanBPPD, GedungBangunanBPPDAdmin)
admin.site.register(KDPGedungBangunanBPPD, KDPGedungBangunanBPPDAdmin)
admin.site.register(GedungBangunanRuanganBPPD, GedungBangunanRuanganBPPDAdmin)
admin.site.register(GedungBangunanUsulHapusBPPD, GedungBangunanUsulHapusBPPDAdmin)
admin.site.register(KontrakGedungBangunanBPPD, KontrakGedungBangunanBPPDAdmin)
admin.site.register(HargaGedungBangunanBPPD, HargaGedungBangunanBPPDAdmin)
admin.site.register(GedungBangunanPenghapusanBPPD, GedungBangunanPenghapusanBPPDAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBPPDInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBPPD



class PenghapusanPeralatanMesinBPPDInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBPPD



class SKPDAsalPeralatanMesinBPPDInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBPPD



class SKPDTujuanPeralatanMesinBPPDInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBPPD



class FotoPeralatanMesinBPPDInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBPPD



class HargaPeralatanMesinBPPDInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=48)
        return super(HargaPeralatanMesinBPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBPPDInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBPPD


class PeralatanMesinBPPDAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBPPDInline,
                    SKPDAsalPeralatanMesinBPPDInline,
                    FotoPeralatanMesinBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=48)
        return super(PeralatanMesinBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBPPDAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBPPDInline,
                    SKPDAsalPeralatanMesinBPPDInline,
                    FotoPeralatanMesinBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBPPDAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=48)
        return super(KontrakPeralatanMesinBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=48)



class HargaPeralatanMesinBPPDAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBPPDAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBPPDInline, TahunBerkurangPeralatanMesinBPPDInline,
                    SKPDAsalPeralatanMesinBPPDInline,
                    SKPDTujuanPeralatanMesinBPPDInline,
                    FotoPeralatanMesinBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin BPPD
admin.site.register(PeralatanMesinBPPD, PeralatanMesinBPPDAdmin)
admin.site.register(PeralatanMesinUsulHapusBPPD, PeralatanMesinUsulHapusBPPDAdmin)
admin.site.register(KontrakPeralatanMesinBPPD, KontrakPeralatanMesinBPPDAdmin)
admin.site.register(HargaPeralatanMesinBPPD, HargaPeralatanMesinBPPDAdmin)
admin.site.register(PeralatanMesinPenghapusanBPPD, PeralatanMesinPenghapusanBPPDAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBPPD, KontrakJalanIrigasiJaringanBPPD, HargaJalanIrigasiJaringanBPPD, KDPJalanIrigasiJaringanBPPD, JalanIrigasiJaringanUsulHapusBPPD, TahunBerkurangUsulHapusJalanIrigasiJaringanBPPD

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBPPD, TahunBerkurangJalanIrigasiJaringanBPPD, PenghapusanJalanIrigasiJaringanBPPD

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBPPD, SKPDTujuanJalanIrigasiJaringanBPPD, FotoJalanIrigasiJaringanBPPD

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBPPDInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBPPD



class PenghapusanJalanIrigasiJaringanBPPDInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBPPD



class SKPDAsalJalanIrigasiJaringanBPPDInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBPPD



class SKPDTujuanJalanIrigasiJaringanBPPDInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBPPD



class FotoJalanIrigasiJaringanBPPDInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBPPD





class HargaJalanIrigasiJaringanBPPDInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=48)
        return super(HargaJalanIrigasiJaringanBPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBPPDInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBPPD


class JalanIrigasiJaringanBPPDAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBPPDInline,
                    SKPDAsalJalanIrigasiJaringanBPPDInline,
                    FotoJalanIrigasiJaringanBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        return super(JalanIrigasiJaringanBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBPPDAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBPPDInline,
                    SKPDAsalJalanIrigasiJaringanBPPDInline,
                    FotoJalanIrigasiJaringanBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBPPDAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBPPDInline,
                    SKPDAsalJalanIrigasiJaringanBPPDInline,
                    FotoJalanIrigasiJaringanBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        return super(KDPJalanIrigasiJaringanBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBPPDAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=48)
        return super(KontrakJalanIrigasiJaringanBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=48)



class HargaJalanIrigasiJaringanBPPDAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBPPDAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBPPDInline, TahunBerkurangJalanIrigasiJaringanBPPDInline,
                    SKPDAsalJalanIrigasiJaringanBPPDInline,
                    SKPDTujuanJalanIrigasiJaringanBPPDInline,
                    FotoJalanIrigasiJaringanBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan BPPD
admin.site.register(JalanIrigasiJaringanBPPD, JalanIrigasiJaringanBPPDAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBPPD, JalanIrigasiJaringanUsulHapusBPPDAdmin)
admin.site.register(KDPJalanIrigasiJaringanBPPD, KDPJalanIrigasiJaringanBPPDAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBPPD, KontrakJalanIrigasiJaringanBPPDAdmin)
admin.site.register(HargaJalanIrigasiJaringanBPPD, HargaJalanIrigasiJaringanBPPDAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBPPD, JalanIrigasiJaringanPenghapusanBPPDAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBPPD, KontrakATLBPPD, HargaATLBPPD, ATLUsulHapusBPPD, TahunBerkurangUsulHapusATLBPPD

from atl.models import ATLPenghapusanBPPD, TahunBerkurangATLBPPD, PenghapusanATLBPPD

from atl.models import SKPDAsalATLBPPD, SKPDTujuanATLBPPD, FotoATLBPPD

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBPPDInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBPPD



class PenghapusanATLBPPDInline(PenghapusanATLInline):
    model = PenghapusanATLBPPD



class SKPDAsalATLBPPDInline(SKPDAsalATLInline):
    model = SKPDAsalATLBPPD



class SKPDTujuanATLBPPDInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBPPD



class FotoATLBPPDInline(FotoATLInline):
    model = FotoATLBPPD



class HargaATLBPPDInline(HargaATLInline):
    model = HargaATLBPPD

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=48)
        return super(HargaATLBPPDInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBPPDInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBPPD


class ATLBPPDAdmin(ATLAdmin):
    inlines = [HargaATLBPPDInline,
                    SKPDAsalATLBPPDInline,
                    FotoATLBPPDInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=48)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=48)
        return super(ATLBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBPPDAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBPPDInline,
                    SKPDAsalATLBPPDInline,
                    FotoATLBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBPPDAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=48)
        return super(KontrakATLBPPDAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=48)



class HargaATLBPPDAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBPPDAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBPPDInline, TahunBerkurangATLBPPDInline,
                    SKPDAsalATLBPPDInline,
                    SKPDTujuanATLBPPDInline,
                    FotoATLBPPDInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=48)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL BPPD
admin.site.register(ATLBPPD, ATLBPPDAdmin)
admin.site.register(ATLUsulHapusBPPD, ATLUsulHapusBPPDAdmin)
admin.site.register(KontrakATLBPPD, KontrakATLBPPDAdmin)
admin.site.register(HargaATLBPPD, HargaATLBPPDAdmin)
admin.site.register(ATLPenghapusanBPPD, ATLPenghapusanBPPDAdmin)
