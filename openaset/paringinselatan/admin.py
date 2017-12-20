### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahParinginSelatan, KontrakTanahParinginSelatan, HargaTanahParinginSelatan, TanahUsulHapusParinginSelatan, TahunBerkurangUsulHapusTanahParinginSelatan

from umum.models import TanahPenghapusanParinginSelatan, TahunBerkurangTanahParinginSelatan, PenghapusanTanahParinginSelatan

from umum.models import SKPDAsalTanahParinginSelatan, SKPDTujuanTanahParinginSelatan, FotoTanahParinginSelatan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanParinginSelatan, KontrakGedungBangunanParinginSelatan, HargaGedungBangunanParinginSelatan, GedungBangunanRuanganParinginSelatan, GedungBangunanUsulHapusParinginSelatan, TahunBerkurangUsulHapusGedungParinginSelatan

from gedungbangunan.models import GedungBangunanPenghapusanParinginSelatan, TahunBerkurangGedungBangunanParinginSelatan, PenghapusanGedungBangunanParinginSelatan

from gedungbangunan.models import SKPDAsalGedungBangunanParinginSelatan, SKPDTujuanGedungBangunanParinginSelatan, FotoGedungBangunanParinginSelatan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinParinginSelatan, KontrakPeralatanMesinParinginSelatan, HargaPeralatanMesinParinginSelatan, PeralatanMesinUsulHapusParinginSelatan, TahunBerkurangUsulHapusPeralatanMesinParinginSelatan

from peralatanmesin.models import PeralatanMesinPenghapusanParinginSelatan, TahunBerkurangPeralatanMesinParinginSelatan, PenghapusanPeralatanMesinParinginSelatan

from peralatanmesin.models import SKPDAsalPeralatanMesinParinginSelatan, SKPDTujuanPeralatanMesinParinginSelatan, FotoPeralatanMesinParinginSelatan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahParinginSelatanInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahParinginSelatan



class PenghapusanTanahParinginSelatanInline(PenghapusanTanahInline):
    model = PenghapusanTanahParinginSelatan



class SKPDAsalTanahParinginSelatanInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahParinginSelatan



class SKPDTujuanTanahParinginSelatanInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahParinginSelatan



class FotoTanahParinginSelatanInline(FotoTanahInline):
    model = FotoTanahParinginSelatan



class GedungBangunanParinginSelatanInline(GedungBangunanInline):
    model = GedungBangunanParinginSelatan



class HargaTanahParinginSelatanInline(HargaTanahInline):
    model = HargaTanahParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=36)
        return super(HargaTanahParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahParinginSelatanInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahParinginSelatan


class TanahParinginSelatanAdmin(TanahAdmin):
    inlines = [HargaTanahParinginSelatanInline,
                SKPDAsalTanahParinginSelatanInline,
                FotoTanahParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        return super(TanahParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusParinginSelatanAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahParinginSelatanInline,
                SKPDAsalTanahParinginSelatanInline,
                FotoTanahParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahParinginSelatanAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=36)
        return super(KontrakTanahParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=36)



class HargaTanahParinginSelatanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanParinginSelatanAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahParinginSelatanInline, TahunBerkurangTanahParinginSelatanInline,
                    SKPDAsalTanahParinginSelatanInline,
                    SKPDTujuanTanahParinginSelatanInline,
                    FotoTanahParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah ParinginSelatan
admin.site.register(TanahParinginSelatan, TanahParinginSelatanAdmin)
admin.site.register(TanahUsulHapusParinginSelatan, TanahUsulHapusParinginSelatanAdmin)
admin.site.register(KontrakTanahParinginSelatan, KontrakTanahParinginSelatanAdmin)
admin.site.register(HargaTanahParinginSelatan, HargaTanahParinginSelatanAdmin)
admin.site.register(TanahPenghapusanParinginSelatan, TanahPenghapusanParinginSelatanAdmin)



from gedungbangunan.models import KDPGedungBangunanParinginSelatan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanParinginSelatanInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanParinginSelatan



class PenghapusanGedungBangunanParinginSelatanInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanParinginSelatan



class SKPDAsalGedungBangunanParinginSelatanInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanParinginSelatan



class SKPDTujuanGedungBangunanParinginSelatanInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanParinginSelatan



class FotoGedungBangunanParinginSelatanInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanParinginSelatan



class HargaGedungBangunanParinginSelatanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=36)
        return super(HargaGedungBangunanParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungParinginSelatanInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungParinginSelatan


class GedungBangunanParinginSelatanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginSelatanInline,
                SKPDAsalGedungBangunanParinginSelatanInline,
                FotoGedungBangunanParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        return super(GedungBangunanParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanParinginSelatanAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginSelatanInline,
                SKPDAsalGedungBangunanParinginSelatanInline,
                FotoGedungBangunanParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        return super(KDPGedungBangunanParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganParinginSelatanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusParinginSelatanAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungParinginSelatanInline,
                    SKPDAsalGedungBangunanParinginSelatanInline,
                    FotoGedungBangunanParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanParinginSelatanAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=36)
        return super(KontrakGedungBangunanParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=36)



class HargaGedungBangunanParinginSelatanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanParinginSelatanAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanParinginSelatanInline, TahunBerkurangGedungBangunanParinginSelatanInline,
                    SKPDAsalGedungBangunanParinginSelatanInline,
                    SKPDTujuanGedungBangunanParinginSelatanInline,
                    FotoGedungBangunanParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan ParinginSelatan
admin.site.register(GedungBangunanParinginSelatan, GedungBangunanParinginSelatanAdmin)
admin.site.register(KDPGedungBangunanParinginSelatan, KDPGedungBangunanParinginSelatanAdmin)
admin.site.register(GedungBangunanRuanganParinginSelatan, GedungBangunanRuanganParinginSelatanAdmin)
admin.site.register(GedungBangunanUsulHapusParinginSelatan, GedungBangunanUsulHapusParinginSelatanAdmin)
admin.site.register(KontrakGedungBangunanParinginSelatan, KontrakGedungBangunanParinginSelatanAdmin)
admin.site.register(HargaGedungBangunanParinginSelatan, HargaGedungBangunanParinginSelatanAdmin)
admin.site.register(GedungBangunanPenghapusanParinginSelatan, GedungBangunanPenghapusanParinginSelatanAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinParinginSelatanInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinParinginSelatan



class PenghapusanPeralatanMesinParinginSelatanInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinParinginSelatan



class SKPDAsalPeralatanMesinParinginSelatanInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinParinginSelatan



class SKPDTujuanPeralatanMesinParinginSelatanInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinParinginSelatan



class FotoPeralatanMesinParinginSelatanInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinParinginSelatan



class HargaPeralatanMesinParinginSelatanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=36)
        return super(HargaPeralatanMesinParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinParinginSelatanInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinParinginSelatan


class PeralatanMesinParinginSelatanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinParinginSelatanInline,
                    SKPDAsalPeralatanMesinParinginSelatanInline,
                    FotoPeralatanMesinParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=36)
        return super(PeralatanMesinParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusParinginSelatanAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinParinginSelatanInline,
                    SKPDAsalPeralatanMesinParinginSelatanInline,
                    FotoPeralatanMesinParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinParinginSelatanAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=36)
        return super(KontrakPeralatanMesinParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=36)



class HargaPeralatanMesinParinginSelatanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanParinginSelatanAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinParinginSelatanInline, TahunBerkurangPeralatanMesinParinginSelatanInline,
                    SKPDAsalPeralatanMesinParinginSelatanInline,
                    SKPDTujuanPeralatanMesinParinginSelatanInline,
                    FotoPeralatanMesinParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin ParinginSelatan
admin.site.register(PeralatanMesinParinginSelatan, PeralatanMesinParinginSelatanAdmin)
admin.site.register(PeralatanMesinUsulHapusParinginSelatan, PeralatanMesinUsulHapusParinginSelatanAdmin)
admin.site.register(KontrakPeralatanMesinParinginSelatan, KontrakPeralatanMesinParinginSelatanAdmin)
admin.site.register(HargaPeralatanMesinParinginSelatan, HargaPeralatanMesinParinginSelatanAdmin)
admin.site.register(PeralatanMesinPenghapusanParinginSelatan, PeralatanMesinPenghapusanParinginSelatanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanParinginSelatan, KontrakJalanIrigasiJaringanParinginSelatan, HargaJalanIrigasiJaringanParinginSelatan, KDPJalanIrigasiJaringanParinginSelatan, JalanIrigasiJaringanUsulHapusParinginSelatan, TahunBerkurangUsulHapusJalanIrigasiJaringanParinginSelatan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanParinginSelatan, TahunBerkurangJalanIrigasiJaringanParinginSelatan, PenghapusanJalanIrigasiJaringanParinginSelatan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanParinginSelatan, SKPDTujuanJalanIrigasiJaringanParinginSelatan, FotoJalanIrigasiJaringanParinginSelatan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanParinginSelatanInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanParinginSelatan



class PenghapusanJalanIrigasiJaringanParinginSelatanInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanParinginSelatan



class SKPDAsalJalanIrigasiJaringanParinginSelatanInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanParinginSelatan



class SKPDTujuanJalanIrigasiJaringanParinginSelatanInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanParinginSelatan



class FotoJalanIrigasiJaringanParinginSelatanInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanParinginSelatan





class HargaJalanIrigasiJaringanParinginSelatanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=36)
        return super(HargaJalanIrigasiJaringanParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginSelatanInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanParinginSelatan


class JalanIrigasiJaringanParinginSelatanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginSelatanInline,
                    SKPDAsalJalanIrigasiJaringanParinginSelatanInline,
                    FotoJalanIrigasiJaringanParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        return super(JalanIrigasiJaringanParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusParinginSelatanAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanParinginSelatanInline,
                    SKPDAsalJalanIrigasiJaringanParinginSelatanInline,
                    FotoJalanIrigasiJaringanParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanParinginSelatanAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginSelatanInline,
                    SKPDAsalJalanIrigasiJaringanParinginSelatanInline,
                    FotoJalanIrigasiJaringanParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        return super(KDPJalanIrigasiJaringanParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanParinginSelatanAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=36)
        return super(KontrakJalanIrigasiJaringanParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=36)



class HargaJalanIrigasiJaringanParinginSelatanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanParinginSelatanAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanParinginSelatanInline, TahunBerkurangJalanIrigasiJaringanParinginSelatanInline,
                    SKPDAsalJalanIrigasiJaringanParinginSelatanInline,
                    SKPDTujuanJalanIrigasiJaringanParinginSelatanInline,
                    FotoJalanIrigasiJaringanParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan ParinginSelatan
admin.site.register(JalanIrigasiJaringanParinginSelatan, JalanIrigasiJaringanParinginSelatanAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusParinginSelatan, JalanIrigasiJaringanUsulHapusParinginSelatanAdmin)
admin.site.register(KDPJalanIrigasiJaringanParinginSelatan, KDPJalanIrigasiJaringanParinginSelatanAdmin)
admin.site.register(KontrakJalanIrigasiJaringanParinginSelatan, KontrakJalanIrigasiJaringanParinginSelatanAdmin)
admin.site.register(HargaJalanIrigasiJaringanParinginSelatan, HargaJalanIrigasiJaringanParinginSelatanAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanParinginSelatan, JalanIrigasiJaringanPenghapusanParinginSelatanAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLParinginSelatan, KontrakATLParinginSelatan, HargaATLParinginSelatan, ATLUsulHapusParinginSelatan, TahunBerkurangUsulHapusATLParinginSelatan

from atl.models import ATLPenghapusanParinginSelatan, TahunBerkurangATLParinginSelatan, PenghapusanATLParinginSelatan

from atl.models import SKPDAsalATLParinginSelatan, SKPDTujuanATLParinginSelatan, FotoATLParinginSelatan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLParinginSelatanInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLParinginSelatan



class PenghapusanATLParinginSelatanInline(PenghapusanATLInline):
    model = PenghapusanATLParinginSelatan



class SKPDAsalATLParinginSelatanInline(SKPDAsalATLInline):
    model = SKPDAsalATLParinginSelatan



class SKPDTujuanATLParinginSelatanInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLParinginSelatan



class FotoATLParinginSelatanInline(FotoATLInline):
    model = FotoATLParinginSelatan



class HargaATLParinginSelatanInline(HargaATLInline):
    model = HargaATLParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=36)
        return super(HargaATLParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLParinginSelatanInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLParinginSelatan


class ATLParinginSelatanAdmin(ATLAdmin):
    inlines = [HargaATLParinginSelatanInline,
                    SKPDAsalATLParinginSelatanInline,
                    FotoATLParinginSelatanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=36)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=36)
        return super(ATLParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusParinginSelatanAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLParinginSelatanInline,
                    SKPDAsalATLParinginSelatanInline,
                    FotoATLParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLParinginSelatanAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=36)
        return super(KontrakATLParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=36)



class HargaATLParinginSelatanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanParinginSelatanAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLParinginSelatanInline, TahunBerkurangATLParinginSelatanInline,
                    SKPDAsalATLParinginSelatanInline,
                    SKPDTujuanATLParinginSelatanInline,
                    FotoATLParinginSelatanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=36)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL ParinginSelatan
admin.site.register(ATLParinginSelatan, ATLParinginSelatanAdmin)
admin.site.register(ATLUsulHapusParinginSelatan, ATLUsulHapusParinginSelatanAdmin)
admin.site.register(KontrakATLParinginSelatan, KontrakATLParinginSelatanAdmin)
admin.site.register(HargaATLParinginSelatan, HargaATLParinginSelatanAdmin)
admin.site.register(ATLPenghapusanParinginSelatan, ATLPenghapusanParinginSelatanAdmin)
