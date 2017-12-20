### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahParinginTimur, KontrakTanahParinginTimur, HargaTanahParinginTimur, TanahUsulHapusParinginTimur, TahunBerkurangUsulHapusTanahParinginTimur

from umum.models import TanahPenghapusanParinginTimur, TahunBerkurangTanahParinginTimur, PenghapusanTanahParinginTimur

from umum.models import SKPDAsalTanahParinginTimur, SKPDTujuanTanahParinginTimur, FotoTanahParinginTimur

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanParinginTimur, KontrakGedungBangunanParinginTimur, HargaGedungBangunanParinginTimur, GedungBangunanRuanganParinginTimur, GedungBangunanUsulHapusParinginTimur, TahunBerkurangUsulHapusGedungParinginTimur

from gedungbangunan.models import GedungBangunanPenghapusanParinginTimur, TahunBerkurangGedungBangunanParinginTimur, PenghapusanGedungBangunanParinginTimur

from gedungbangunan.models import SKPDAsalGedungBangunanParinginTimur, SKPDTujuanGedungBangunanParinginTimur, FotoGedungBangunanParinginTimur

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinParinginTimur, KontrakPeralatanMesinParinginTimur, HargaPeralatanMesinParinginTimur, PeralatanMesinUsulHapusParinginTimur, TahunBerkurangUsulHapusPeralatanMesinParinginTimur

from peralatanmesin.models import PeralatanMesinPenghapusanParinginTimur, TahunBerkurangPeralatanMesinParinginTimur, PenghapusanPeralatanMesinParinginTimur

from peralatanmesin.models import SKPDAsalPeralatanMesinParinginTimur, SKPDTujuanPeralatanMesinParinginTimur, FotoPeralatanMesinParinginTimur

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahParinginTimurInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahParinginTimur



class PenghapusanTanahParinginTimurInline(PenghapusanTanahInline):
    model = PenghapusanTanahParinginTimur



class SKPDAsalTanahParinginTimurInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahParinginTimur



class SKPDTujuanTanahParinginTimurInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahParinginTimur



class FotoTanahParinginTimurInline(FotoTanahInline):
    model = FotoTanahParinginTimur



class GedungBangunanParinginTimurInline(GedungBangunanInline):
    model = GedungBangunanParinginTimur



class HargaTanahParinginTimurInline(HargaTanahInline):
    model = HargaTanahParinginTimur

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=30)
        return super(HargaTanahParinginTimurInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahParinginTimurInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahParinginTimur


class TanahParinginTimurAdmin(TanahAdmin):
    inlines = [HargaTanahParinginTimurInline,
                SKPDAsalTanahParinginTimurInline,
                FotoTanahParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        return super(TanahParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusParinginTimurAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahParinginTimurInline,
                SKPDAsalTanahParinginTimurInline,
                FotoTanahParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahParinginTimurAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=30)
        return super(KontrakTanahParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=30)



class HargaTanahParinginTimurAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanParinginTimurAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahParinginTimurInline, TahunBerkurangTanahParinginTimurInline,
                    SKPDAsalTanahParinginTimurInline,
                    SKPDTujuanTanahParinginTimurInline,
                    FotoTanahParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah ParinginTimur
admin.site.register(TanahParinginTimur, TanahParinginTimurAdmin)
admin.site.register(TanahUsulHapusParinginTimur, TanahUsulHapusParinginTimurAdmin)
admin.site.register(KontrakTanahParinginTimur, KontrakTanahParinginTimurAdmin)
admin.site.register(HargaTanahParinginTimur, HargaTanahParinginTimurAdmin)
admin.site.register(TanahPenghapusanParinginTimur, TanahPenghapusanParinginTimurAdmin)



from gedungbangunan.models import KDPGedungBangunanParinginTimur


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanParinginTimurInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanParinginTimur



class PenghapusanGedungBangunanParinginTimurInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanParinginTimur



class SKPDAsalGedungBangunanParinginTimurInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanParinginTimur



class SKPDTujuanGedungBangunanParinginTimurInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanParinginTimur



class FotoGedungBangunanParinginTimurInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanParinginTimur



class HargaGedungBangunanParinginTimurInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanParinginTimur

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=30)
        return super(HargaGedungBangunanParinginTimurInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungParinginTimurInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungParinginTimur


class GedungBangunanParinginTimurAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginTimurInline,
                SKPDAsalGedungBangunanParinginTimurInline,
                FotoGedungBangunanParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        return super(GedungBangunanParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanParinginTimurAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanParinginTimurInline,
                SKPDAsalGedungBangunanParinginTimurInline,
                FotoGedungBangunanParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        return super(KDPGedungBangunanParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganParinginTimurAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusParinginTimurAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungParinginTimurInline,
                    SKPDAsalGedungBangunanParinginTimurInline,
                    FotoGedungBangunanParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanParinginTimurAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=30)
        return super(KontrakGedungBangunanParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=30)



class HargaGedungBangunanParinginTimurAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanParinginTimurAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanParinginTimurInline, TahunBerkurangGedungBangunanParinginTimurInline,
                    SKPDAsalGedungBangunanParinginTimurInline,
                    SKPDTujuanGedungBangunanParinginTimurInline,
                    FotoGedungBangunanParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan ParinginTimur
admin.site.register(GedungBangunanParinginTimur, GedungBangunanParinginTimurAdmin)
admin.site.register(KDPGedungBangunanParinginTimur, KDPGedungBangunanParinginTimurAdmin)
admin.site.register(GedungBangunanRuanganParinginTimur, GedungBangunanRuanganParinginTimurAdmin)
admin.site.register(GedungBangunanUsulHapusParinginTimur, GedungBangunanUsulHapusParinginTimurAdmin)
admin.site.register(KontrakGedungBangunanParinginTimur, KontrakGedungBangunanParinginTimurAdmin)
admin.site.register(HargaGedungBangunanParinginTimur, HargaGedungBangunanParinginTimurAdmin)
admin.site.register(GedungBangunanPenghapusanParinginTimur, GedungBangunanPenghapusanParinginTimurAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinParinginTimurInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinParinginTimur



class PenghapusanPeralatanMesinParinginTimurInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinParinginTimur



class SKPDAsalPeralatanMesinParinginTimurInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinParinginTimur



class SKPDTujuanPeralatanMesinParinginTimurInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinParinginTimur



class FotoPeralatanMesinParinginTimurInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinParinginTimur



class HargaPeralatanMesinParinginTimurInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinParinginTimur

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=30)
        return super(HargaPeralatanMesinParinginTimurInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinParinginTimurInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinParinginTimur


class PeralatanMesinParinginTimurAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinParinginTimurInline,
                    SKPDAsalPeralatanMesinParinginTimurInline,
                    FotoPeralatanMesinParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=30)
        return super(PeralatanMesinParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusParinginTimurAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinParinginTimurInline,
                    SKPDAsalPeralatanMesinParinginTimurInline,
                    FotoPeralatanMesinParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinParinginTimurAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=30)
        return super(KontrakPeralatanMesinParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=30)



class HargaPeralatanMesinParinginTimurAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanParinginTimurAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinParinginTimurInline, TahunBerkurangPeralatanMesinParinginTimurInline,
                    SKPDAsalPeralatanMesinParinginTimurInline,
                    SKPDTujuanPeralatanMesinParinginTimurInline,
                    FotoPeralatanMesinParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin ParinginTimur
admin.site.register(PeralatanMesinParinginTimur, PeralatanMesinParinginTimurAdmin)
admin.site.register(PeralatanMesinUsulHapusParinginTimur, PeralatanMesinUsulHapusParinginTimurAdmin)
admin.site.register(KontrakPeralatanMesinParinginTimur, KontrakPeralatanMesinParinginTimurAdmin)
admin.site.register(HargaPeralatanMesinParinginTimur, HargaPeralatanMesinParinginTimurAdmin)
admin.site.register(PeralatanMesinPenghapusanParinginTimur, PeralatanMesinPenghapusanParinginTimurAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanParinginTimur, KontrakJalanIrigasiJaringanParinginTimur, HargaJalanIrigasiJaringanParinginTimur, KDPJalanIrigasiJaringanParinginTimur, JalanIrigasiJaringanUsulHapusParinginTimur, TahunBerkurangUsulHapusJalanIrigasiJaringanParinginTimur

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanParinginTimur, TahunBerkurangJalanIrigasiJaringanParinginTimur, PenghapusanJalanIrigasiJaringanParinginTimur

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanParinginTimur, SKPDTujuanJalanIrigasiJaringanParinginTimur, FotoJalanIrigasiJaringanParinginTimur

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanParinginTimurInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanParinginTimur



class PenghapusanJalanIrigasiJaringanParinginTimurInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanParinginTimur



class SKPDAsalJalanIrigasiJaringanParinginTimurInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanParinginTimur



class SKPDTujuanJalanIrigasiJaringanParinginTimurInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanParinginTimur



class FotoJalanIrigasiJaringanParinginTimurInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanParinginTimur





class HargaJalanIrigasiJaringanParinginTimurInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanParinginTimur

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=30)
        return super(HargaJalanIrigasiJaringanParinginTimurInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginTimurInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanParinginTimur


class JalanIrigasiJaringanParinginTimurAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginTimurInline,
                    SKPDAsalJalanIrigasiJaringanParinginTimurInline,
                    FotoJalanIrigasiJaringanParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        return super(JalanIrigasiJaringanParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusParinginTimurAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanParinginTimurInline,
                    SKPDAsalJalanIrigasiJaringanParinginTimurInline,
                    FotoJalanIrigasiJaringanParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanParinginTimurAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanParinginTimurInline,
                    SKPDAsalJalanIrigasiJaringanParinginTimurInline,
                    FotoJalanIrigasiJaringanParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        return super(KDPJalanIrigasiJaringanParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanParinginTimurAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=30)
        return super(KontrakJalanIrigasiJaringanParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=30)



class HargaJalanIrigasiJaringanParinginTimurAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanParinginTimurAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanParinginTimurInline, TahunBerkurangJalanIrigasiJaringanParinginTimurInline,
                    SKPDAsalJalanIrigasiJaringanParinginTimurInline,
                    SKPDTujuanJalanIrigasiJaringanParinginTimurInline,
                    FotoJalanIrigasiJaringanParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan ParinginTimur
admin.site.register(JalanIrigasiJaringanParinginTimur, JalanIrigasiJaringanParinginTimurAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusParinginTimur, JalanIrigasiJaringanUsulHapusParinginTimurAdmin)
admin.site.register(KDPJalanIrigasiJaringanParinginTimur, KDPJalanIrigasiJaringanParinginTimurAdmin)
admin.site.register(KontrakJalanIrigasiJaringanParinginTimur, KontrakJalanIrigasiJaringanParinginTimurAdmin)
admin.site.register(HargaJalanIrigasiJaringanParinginTimur, HargaJalanIrigasiJaringanParinginTimurAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanParinginTimur, JalanIrigasiJaringanPenghapusanParinginTimurAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLParinginTimur, KontrakATLParinginTimur, HargaATLParinginTimur, ATLUsulHapusParinginTimur, TahunBerkurangUsulHapusATLParinginTimur

from atl.models import ATLPenghapusanParinginTimur, TahunBerkurangATLParinginTimur, PenghapusanATLParinginTimur

from atl.models import SKPDAsalATLParinginTimur, SKPDTujuanATLParinginTimur, FotoATLParinginTimur

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLParinginTimurInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLParinginTimur



class PenghapusanATLParinginTimurInline(PenghapusanATLInline):
    model = PenghapusanATLParinginTimur



class SKPDAsalATLParinginTimurInline(SKPDAsalATLInline):
    model = SKPDAsalATLParinginTimur



class SKPDTujuanATLParinginTimurInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLParinginTimur



class FotoATLParinginTimurInline(FotoATLInline):
    model = FotoATLParinginTimur



class HargaATLParinginTimurInline(HargaATLInline):
    model = HargaATLParinginTimur

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=30)
        return super(HargaATLParinginTimurInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLParinginTimurInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLParinginTimur


class ATLParinginTimurAdmin(ATLAdmin):
    inlines = [HargaATLParinginTimurInline,
                    SKPDAsalATLParinginTimurInline,
                    FotoATLParinginTimurInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=30)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=30)
        return super(ATLParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusParinginTimurAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLParinginTimurInline,
                    SKPDAsalATLParinginTimurInline,
                    FotoATLParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLParinginTimurAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=30)
        return super(KontrakATLParinginTimurAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=30)



class HargaATLParinginTimurAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanParinginTimurAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLParinginTimurInline, TahunBerkurangATLParinginTimurInline,
                    SKPDAsalATLParinginTimurInline,
                    SKPDTujuanATLParinginTimurInline,
                    FotoATLParinginTimurInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=30)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL ParinginTimur
admin.site.register(ATLParinginTimur, ATLParinginTimurAdmin)
admin.site.register(ATLUsulHapusParinginTimur, ATLUsulHapusParinginTimurAdmin)
admin.site.register(KontrakATLParinginTimur, KontrakATLParinginTimurAdmin)
admin.site.register(HargaATLParinginTimur, HargaATLParinginTimurAdmin)
admin.site.register(ATLPenghapusanParinginTimur, ATLPenghapusanParinginTimurAdmin)
