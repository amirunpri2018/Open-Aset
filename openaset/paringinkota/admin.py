### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahParinginKota, KontrakTanahParinginKota, HargaTanahParinginKota, TanahUsulHapusParinginKota, TahunBerkurangUsulHapusTanahParinginKota

from umum.models import TanahPenghapusanParinginKota, TahunBerkurangTanahParinginKota, PenghapusanTanahParinginKota

from umum.models import SKPDAsalTanahParinginKota, SKPDTujuanTanahParinginKota, FotoTanahParinginKota

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanParinginKota, KontrakGedungBangunanParinginKota, HargaGedungBangunanParinginKota, GedungBangunanRuanganParinginKota, GedungBangunanUsulHapusParinginKota, TahunBerkurangUsulHapusGedungParinginKota

from gedungbangunan.models import GedungBangunanPenghapusanParinginKota, TahunBerkurangGedungBangunanParinginKota, PenghapusanGedungBangunanParinginKota

from gedungbangunan.models import SKPDAsalGedungBangunanParinginKota, SKPDTujuanGedungBangunanParinginKota, FotoGedungBangunanParinginKota

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinParinginKota, KontrakPeralatanMesinParinginKota, HargaPeralatanMesinParinginKota, PeralatanMesinUsulHapusParinginKota, TahunBerkurangUsulHapusPeralatanMesinParinginKota

from peralatanmesin.models import PeralatanMesinPenghapusanParinginKota, TahunBerkurangPeralatanMesinParinginKota, PenghapusanPeralatanMesinParinginKota

from peralatanmesin.models import SKPDAsalPeralatanMesinParinginKota, SKPDTujuanPeralatanMesinParinginKota, FotoPeralatanMesinParinginKota

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahParinginKotaInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahParinginKota



class PenghapusanTanahParinginKotaInline(PenghapusanTanahInline):
    model = PenghapusanTanahParinginKota



class SKPDAsalTanahParinginKotaInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahParinginKota



class SKPDTujuanTanahParinginKotaInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahParinginKota



class FotoTanahParinginKotaInline(FotoTanahInline):
    model = FotoTanahParinginKota



class GedungBangunanParinginKotaInline(GedungBangunanInline):
    model = GedungBangunanParinginKota



class HargaTanahParinginKotaInline(HargaTanahInline):
    model = HargaTanahParinginKota

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=29)
        return super(HargaTanahParinginKotaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahParinginKotaInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahParinginKota


class TanahParinginKotaAdmin(TanahAdmin):
    inlines = [HargaTanahParinginKotaInline,
                SKPDAsalTanahParinginKotaInline,
                FotoTanahParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        return super(TanahParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusParinginKotaAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahParinginKotaInline,
                SKPDAsalTanahParinginKotaInline,
                FotoTanahParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahParinginKotaAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=29)
        return super(KontrakTanahParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=29)



class HargaTanahParinginKotaAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanParinginKotaAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahParinginKotaInline, TahunBerkurangTanahParinginKotaInline,
                    SKPDAsalTanahParinginKotaInline,
                    SKPDTujuanTanahParinginKotaInline,
                    FotoTanahParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah ParinginKota
admin.site.register(TanahParinginKota, TanahParinginKotaAdmin)
admin.site.register(TanahUsulHapusParinginKota, TanahUsulHapusParinginKotaAdmin)
admin.site.register(KontrakTanahParinginKota, KontrakTanahParinginKotaAdmin)
admin.site.register(HargaTanahParinginKota, HargaTanahParinginKotaAdmin)
admin.site.register(TanahPenghapusanParinginKota, TanahPenghapusanParinginKotaAdmin)



from gedungbangunan.models import KDPGedungBangunanParinginKota


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanParinginKotaInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanParinginKota



class PenghapusanGedungBangunanParinginKotaInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanParinginKota



class SKPDAsalGedungBangunanParinginKotaInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanParinginKota



class SKPDTujuanGedungBangunanParinginKotaInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanParinginKota



class FotoGedungBangunanParinginKotaInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanParinginKota



class HargaGedungBangunanParinginKotaInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanParinginKota

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=29)
        return super(HargaGedungBangunanParinginKotaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungParinginKotaInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungParinginKota


class GedungBangunanParinginKotaAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginKotaInline,
                SKPDAsalGedungBangunanParinginKotaInline,
                FotoGedungBangunanParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        return super(GedungBangunanParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanParinginKotaAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginKotaInline,
                SKPDAsalGedungBangunanParinginKotaInline,
                FotoGedungBangunanParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        return super(KDPGedungBangunanParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganParinginKotaAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusParinginKotaAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungParinginKotaInline,
                    SKPDAsalGedungBangunanParinginKotaInline,
                    FotoGedungBangunanParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanParinginKotaAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=29)
        return super(KontrakGedungBangunanParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=29)



class HargaGedungBangunanParinginKotaAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanParinginKotaAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanParinginKotaInline, TahunBerkurangGedungBangunanParinginKotaInline,
                    SKPDAsalGedungBangunanParinginKotaInline,
                    SKPDTujuanGedungBangunanParinginKotaInline,
                    FotoGedungBangunanParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan ParinginKota
admin.site.register(GedungBangunanParinginKota, GedungBangunanParinginKotaAdmin)
admin.site.register(KDPGedungBangunanParinginKota, KDPGedungBangunanParinginKotaAdmin)
admin.site.register(GedungBangunanRuanganParinginKota, GedungBangunanRuanganParinginKotaAdmin)
admin.site.register(GedungBangunanUsulHapusParinginKota, GedungBangunanUsulHapusParinginKotaAdmin)
admin.site.register(KontrakGedungBangunanParinginKota, KontrakGedungBangunanParinginKotaAdmin)
admin.site.register(HargaGedungBangunanParinginKota, HargaGedungBangunanParinginKotaAdmin)
admin.site.register(GedungBangunanPenghapusanParinginKota, GedungBangunanPenghapusanParinginKotaAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinParinginKotaInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinParinginKota



class PenghapusanPeralatanMesinParinginKotaInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinParinginKota



class SKPDAsalPeralatanMesinParinginKotaInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinParinginKota



class SKPDTujuanPeralatanMesinParinginKotaInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinParinginKota



class FotoPeralatanMesinParinginKotaInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinParinginKota



class HargaPeralatanMesinParinginKotaInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinParinginKota

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=29)
        return super(HargaPeralatanMesinParinginKotaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinParinginKotaInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinParinginKota


class PeralatanMesinParinginKotaAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinParinginKotaInline,
                    SKPDAsalPeralatanMesinParinginKotaInline,
                    FotoPeralatanMesinParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=29)
        return super(PeralatanMesinParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusParinginKotaAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinParinginKotaInline,
                    SKPDAsalPeralatanMesinParinginKotaInline,
                    FotoPeralatanMesinParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinParinginKotaAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=29)
        return super(KontrakPeralatanMesinParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=29)



class HargaPeralatanMesinParinginKotaAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanParinginKotaAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinParinginKotaInline, TahunBerkurangPeralatanMesinParinginKotaInline,
                    SKPDAsalPeralatanMesinParinginKotaInline,
                    SKPDTujuanPeralatanMesinParinginKotaInline,
                    FotoPeralatanMesinParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin ParinginKota
admin.site.register(PeralatanMesinParinginKota, PeralatanMesinParinginKotaAdmin)
admin.site.register(PeralatanMesinUsulHapusParinginKota, PeralatanMesinUsulHapusParinginKotaAdmin)
admin.site.register(KontrakPeralatanMesinParinginKota, KontrakPeralatanMesinParinginKotaAdmin)
admin.site.register(HargaPeralatanMesinParinginKota, HargaPeralatanMesinParinginKotaAdmin)
admin.site.register(PeralatanMesinPenghapusanParinginKota, PeralatanMesinPenghapusanParinginKotaAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanParinginKota, KontrakJalanIrigasiJaringanParinginKota, HargaJalanIrigasiJaringanParinginKota, KDPJalanIrigasiJaringanParinginKota, JalanIrigasiJaringanUsulHapusParinginKota, TahunBerkurangUsulHapusJalanIrigasiJaringanParinginKota

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanParinginKota, TahunBerkurangJalanIrigasiJaringanParinginKota, PenghapusanJalanIrigasiJaringanParinginKota

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanParinginKota, SKPDTujuanJalanIrigasiJaringanParinginKota, FotoJalanIrigasiJaringanParinginKota

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanParinginKotaInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanParinginKota



class PenghapusanJalanIrigasiJaringanParinginKotaInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanParinginKota



class SKPDAsalJalanIrigasiJaringanParinginKotaInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanParinginKota



class SKPDTujuanJalanIrigasiJaringanParinginKotaInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanParinginKota



class FotoJalanIrigasiJaringanParinginKotaInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanParinginKota





class HargaJalanIrigasiJaringanParinginKotaInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanParinginKota

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=29)
        return super(HargaJalanIrigasiJaringanParinginKotaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginKotaInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanParinginKota


class JalanIrigasiJaringanParinginKotaAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginKotaInline,
                    SKPDAsalJalanIrigasiJaringanParinginKotaInline,
                    FotoJalanIrigasiJaringanParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        return super(JalanIrigasiJaringanParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusParinginKotaAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanParinginKotaInline,
                    SKPDAsalJalanIrigasiJaringanParinginKotaInline,
                    FotoJalanIrigasiJaringanParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanParinginKotaAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginKotaInline,
                    SKPDAsalJalanIrigasiJaringanParinginKotaInline,
                    FotoJalanIrigasiJaringanParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        return super(KDPJalanIrigasiJaringanParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanParinginKotaAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=29)
        return super(KontrakJalanIrigasiJaringanParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=29)



class HargaJalanIrigasiJaringanParinginKotaAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanParinginKotaAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanParinginKotaInline, TahunBerkurangJalanIrigasiJaringanParinginKotaInline,
                    SKPDAsalJalanIrigasiJaringanParinginKotaInline,
                    SKPDTujuanJalanIrigasiJaringanParinginKotaInline,
                    FotoJalanIrigasiJaringanParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan ParinginKota
admin.site.register(JalanIrigasiJaringanParinginKota, JalanIrigasiJaringanParinginKotaAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusParinginKota, JalanIrigasiJaringanUsulHapusParinginKotaAdmin)
admin.site.register(KDPJalanIrigasiJaringanParinginKota, KDPJalanIrigasiJaringanParinginKotaAdmin)
admin.site.register(KontrakJalanIrigasiJaringanParinginKota, KontrakJalanIrigasiJaringanParinginKotaAdmin)
admin.site.register(HargaJalanIrigasiJaringanParinginKota, HargaJalanIrigasiJaringanParinginKotaAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanParinginKota, JalanIrigasiJaringanPenghapusanParinginKotaAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLParinginKota, KontrakATLParinginKota, HargaATLParinginKota, ATLUsulHapusParinginKota, TahunBerkurangUsulHapusATLParinginKota

from atl.models import ATLPenghapusanParinginKota, TahunBerkurangATLParinginKota, PenghapusanATLParinginKota

from atl.models import SKPDAsalATLParinginKota, SKPDTujuanATLParinginKota, FotoATLParinginKota

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLParinginKotaInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLParinginKota



class PenghapusanATLParinginKotaInline(PenghapusanATLInline):
    model = PenghapusanATLParinginKota



class SKPDAsalATLParinginKotaInline(SKPDAsalATLInline):
    model = SKPDAsalATLParinginKota



class SKPDTujuanATLParinginKotaInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLParinginKota



class FotoATLParinginKotaInline(FotoATLInline):
    model = FotoATLParinginKota



class HargaATLParinginKotaInline(HargaATLInline):
    model = HargaATLParinginKota

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=29)
        return super(HargaATLParinginKotaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLParinginKotaInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLParinginKota


class ATLParinginKotaAdmin(ATLAdmin):
    inlines = [HargaATLParinginKotaInline,
                    SKPDAsalATLParinginKotaInline,
                    FotoATLParinginKotaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=29)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=29)
        return super(ATLParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusParinginKotaAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLParinginKotaInline,
                    SKPDAsalATLParinginKotaInline,
                    FotoATLParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLParinginKotaAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=29)
        return super(KontrakATLParinginKotaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=29)



class HargaATLParinginKotaAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanParinginKotaAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLParinginKotaInline, TahunBerkurangATLParinginKotaInline,
                    SKPDAsalATLParinginKotaInline,
                    SKPDTujuanATLParinginKotaInline,
                    FotoATLParinginKotaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=29)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL ParinginKota
admin.site.register(ATLParinginKota, ATLParinginKotaAdmin)
admin.site.register(ATLUsulHapusParinginKota, ATLUsulHapusParinginKotaAdmin)
admin.site.register(KontrakATLParinginKota, KontrakATLParinginKotaAdmin)
admin.site.register(HargaATLParinginKota, HargaATLParinginKotaAdmin)
admin.site.register(ATLPenghapusanParinginKota, ATLPenghapusanParinginKotaAdmin)
