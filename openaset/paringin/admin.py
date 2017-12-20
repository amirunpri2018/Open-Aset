### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahParingin, KontrakTanahParingin, HargaTanahParingin, TanahUsulHapusParingin, TahunBerkurangUsulHapusTanahParingin

from umum.models import TanahPenghapusanParingin, TahunBerkurangTanahParingin, PenghapusanTanahParingin

from umum.models import SKPDAsalTanahParingin, SKPDTujuanTanahParingin, FotoTanahParingin

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanParingin, KontrakGedungBangunanParingin, HargaGedungBangunanParingin, GedungBangunanRuanganParingin, GedungBangunanUsulHapusParingin, TahunBerkurangUsulHapusGedungParingin

from gedungbangunan.models import GedungBangunanPenghapusanParingin, TahunBerkurangGedungBangunanParingin, PenghapusanGedungBangunanParingin

from gedungbangunan.models import SKPDAsalGedungBangunanParingin, SKPDTujuanGedungBangunanParingin, FotoGedungBangunanParingin

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinParingin, KontrakPeralatanMesinParingin, HargaPeralatanMesinParingin, PeralatanMesinUsulHapusParingin, TahunBerkurangUsulHapusPeralatanMesinParingin

from peralatanmesin.models import PeralatanMesinPenghapusanParingin, TahunBerkurangPeralatanMesinParingin, PenghapusanPeralatanMesinParingin

from peralatanmesin.models import SKPDAsalPeralatanMesinParingin, SKPDTujuanPeralatanMesinParingin, FotoPeralatanMesinParingin

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahParinginInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahParingin



class PenghapusanTanahParinginInline(PenghapusanTanahInline):
    model = PenghapusanTanahParingin



class SKPDAsalTanahParinginInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahParingin



class SKPDTujuanTanahParinginInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahParingin



class FotoTanahParinginInline(FotoTanahInline):
    model = FotoTanahParingin



class GedungBangunanParinginInline(GedungBangunanInline):
    model = GedungBangunanParingin



class HargaTanahParinginInline(HargaTanahInline):
    model = HargaTanahParingin

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=28)
        return super(HargaTanahParinginInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahParinginInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahParingin


class TanahParinginAdmin(TanahAdmin):
    inlines = [HargaTanahParinginInline,
                SKPDAsalTanahParinginInline,
                FotoTanahParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        return super(TanahParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusParinginAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahParinginInline,
                SKPDAsalTanahParinginInline,
                FotoTanahParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahParinginAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=28)
        return super(KontrakTanahParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=28)



class HargaTanahParinginAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanParinginAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahParinginInline, TahunBerkurangTanahParinginInline,
                    SKPDAsalTanahParinginInline,
                    SKPDTujuanTanahParinginInline,
                    FotoTanahParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Paringin
admin.site.register(TanahParingin, TanahParinginAdmin)
admin.site.register(TanahUsulHapusParingin, TanahUsulHapusParinginAdmin)
admin.site.register(KontrakTanahParingin, KontrakTanahParinginAdmin)
admin.site.register(HargaTanahParingin, HargaTanahParinginAdmin)
admin.site.register(TanahPenghapusanParingin, TanahPenghapusanParinginAdmin)



from gedungbangunan.models import KDPGedungBangunanParingin


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanParinginInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanParingin



class PenghapusanGedungBangunanParinginInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanParingin



class SKPDAsalGedungBangunanParinginInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanParingin



class SKPDTujuanGedungBangunanParinginInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanParingin



class FotoGedungBangunanParinginInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanParingin



class HargaGedungBangunanParinginInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanParingin

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=28)
        return super(HargaGedungBangunanParinginInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungParinginInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungParingin


class GedungBangunanParinginAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginInline,
                SKPDAsalGedungBangunanParinginInline,
                FotoGedungBangunanParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        return super(GedungBangunanParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanParinginAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginInline,
                SKPDAsalGedungBangunanParinginInline,
                FotoGedungBangunanParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        return super(KDPGedungBangunanParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganParinginAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusParinginAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungParinginInline,
                    SKPDAsalGedungBangunanParinginInline,
                    FotoGedungBangunanParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanParinginAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=28)
        return super(KontrakGedungBangunanParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=28)



class HargaGedungBangunanParinginAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanParinginAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanParinginInline, TahunBerkurangGedungBangunanParinginInline,
                    SKPDAsalGedungBangunanParinginInline,
                    SKPDTujuanGedungBangunanParinginInline,
                    FotoGedungBangunanParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Paringin
admin.site.register(GedungBangunanParingin, GedungBangunanParinginAdmin)
admin.site.register(KDPGedungBangunanParingin, KDPGedungBangunanParinginAdmin)
admin.site.register(GedungBangunanRuanganParingin, GedungBangunanRuanganParinginAdmin)
admin.site.register(GedungBangunanUsulHapusParingin, GedungBangunanUsulHapusParinginAdmin)
admin.site.register(KontrakGedungBangunanParingin, KontrakGedungBangunanParinginAdmin)
admin.site.register(HargaGedungBangunanParingin, HargaGedungBangunanParinginAdmin)
admin.site.register(GedungBangunanPenghapusanParingin, GedungBangunanPenghapusanParinginAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinParinginInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinParingin



class PenghapusanPeralatanMesinParinginInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinParingin



class SKPDAsalPeralatanMesinParinginInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinParingin



class SKPDTujuanPeralatanMesinParinginInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinParingin



class FotoPeralatanMesinParinginInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinParingin



class HargaPeralatanMesinParinginInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinParingin

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=28)
        return super(HargaPeralatanMesinParinginInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinParinginInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinParingin


class PeralatanMesinParinginAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinParinginInline,
                    SKPDAsalPeralatanMesinParinginInline,
                    FotoPeralatanMesinParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=28)
        return super(PeralatanMesinParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusParinginAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinParinginInline,
                    SKPDAsalPeralatanMesinParinginInline,
                    FotoPeralatanMesinParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinParinginAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=28)
        return super(KontrakPeralatanMesinParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=28)



class HargaPeralatanMesinParinginAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanParinginAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinParinginInline, TahunBerkurangPeralatanMesinParinginInline,
                    SKPDAsalPeralatanMesinParinginInline,
                    SKPDTujuanPeralatanMesinParinginInline,
                    FotoPeralatanMesinParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Paringin
admin.site.register(PeralatanMesinParingin, PeralatanMesinParinginAdmin)
admin.site.register(PeralatanMesinUsulHapusParingin, PeralatanMesinUsulHapusParinginAdmin)
admin.site.register(KontrakPeralatanMesinParingin, KontrakPeralatanMesinParinginAdmin)
admin.site.register(HargaPeralatanMesinParingin, HargaPeralatanMesinParinginAdmin)
admin.site.register(PeralatanMesinPenghapusanParingin, PeralatanMesinPenghapusanParinginAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanParingin, KontrakJalanIrigasiJaringanParingin, HargaJalanIrigasiJaringanParingin, KDPJalanIrigasiJaringanParingin, JalanIrigasiJaringanUsulHapusParingin, TahunBerkurangUsulHapusJalanIrigasiJaringanParingin

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanParingin, TahunBerkurangJalanIrigasiJaringanParingin, PenghapusanJalanIrigasiJaringanParingin

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanParingin, SKPDTujuanJalanIrigasiJaringanParingin, FotoJalanIrigasiJaringanParingin

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanParinginInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanParingin



class PenghapusanJalanIrigasiJaringanParinginInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanParingin



class SKPDAsalJalanIrigasiJaringanParinginInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanParingin



class SKPDTujuanJalanIrigasiJaringanParinginInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanParingin



class FotoJalanIrigasiJaringanParinginInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanParingin





class HargaJalanIrigasiJaringanParinginInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanParingin

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=28)
        return super(HargaJalanIrigasiJaringanParinginInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanParingin


class JalanIrigasiJaringanParinginAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginInline,
                    SKPDAsalJalanIrigasiJaringanParinginInline,
                    FotoJalanIrigasiJaringanParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        return super(JalanIrigasiJaringanParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusParinginAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanParinginInline,
                    SKPDAsalJalanIrigasiJaringanParinginInline,
                    FotoJalanIrigasiJaringanParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanParinginAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginInline,
                    SKPDAsalJalanIrigasiJaringanParinginInline,
                    FotoJalanIrigasiJaringanParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        return super(KDPJalanIrigasiJaringanParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanParinginAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=28)
        return super(KontrakJalanIrigasiJaringanParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=28)



class HargaJalanIrigasiJaringanParinginAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanParinginAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanParinginInline, TahunBerkurangJalanIrigasiJaringanParinginInline,
                    SKPDAsalJalanIrigasiJaringanParinginInline,
                    SKPDTujuanJalanIrigasiJaringanParinginInline,
                    FotoJalanIrigasiJaringanParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Paringin
admin.site.register(JalanIrigasiJaringanParingin, JalanIrigasiJaringanParinginAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusParingin, JalanIrigasiJaringanUsulHapusParinginAdmin)
admin.site.register(KDPJalanIrigasiJaringanParingin, KDPJalanIrigasiJaringanParinginAdmin)
admin.site.register(KontrakJalanIrigasiJaringanParingin, KontrakJalanIrigasiJaringanParinginAdmin)
admin.site.register(HargaJalanIrigasiJaringanParingin, HargaJalanIrigasiJaringanParinginAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanParingin, JalanIrigasiJaringanPenghapusanParinginAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLParingin, KontrakATLParingin, HargaATLParingin, ATLUsulHapusParingin, TahunBerkurangUsulHapusATLParingin

from atl.models import ATLPenghapusanParingin, TahunBerkurangATLParingin, PenghapusanATLParingin

from atl.models import SKPDAsalATLParingin, SKPDTujuanATLParingin, FotoATLParingin

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLParinginInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLParingin



class PenghapusanATLParinginInline(PenghapusanATLInline):
    model = PenghapusanATLParingin



class SKPDAsalATLParinginInline(SKPDAsalATLInline):
    model = SKPDAsalATLParingin



class SKPDTujuanATLParinginInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLParingin



class FotoATLParinginInline(FotoATLInline):
    model = FotoATLParingin



class HargaATLParinginInline(HargaATLInline):
    model = HargaATLParingin

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=28)
        return super(HargaATLParinginInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLParinginInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLParingin


class ATLParinginAdmin(ATLAdmin):
    inlines = [HargaATLParinginInline,
                    SKPDAsalATLParinginInline,
                    FotoATLParinginInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=28)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=28)
        return super(ATLParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusParinginAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLParinginInline,
                    SKPDAsalATLParinginInline,
                    FotoATLParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLParinginAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=28)
        return super(KontrakATLParinginAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=28)



class HargaATLParinginAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanParinginAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLParinginInline, TahunBerkurangATLParinginInline,
                    SKPDAsalATLParinginInline,
                    SKPDTujuanATLParinginInline,
                    FotoATLParinginInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=28)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Paringin
admin.site.register(ATLParingin, ATLParinginAdmin)
admin.site.register(ATLUsulHapusParingin, ATLUsulHapusParinginAdmin)
admin.site.register(KontrakATLParingin, KontrakATLParinginAdmin)
admin.site.register(HargaATLParingin, HargaATLParinginAdmin)
admin.site.register(ATLPenghapusanParingin, ATLPenghapusanParinginAdmin)
