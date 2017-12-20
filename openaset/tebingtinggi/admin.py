### $Id: admin.py,v 1.37 2017/12/18 09:12:01 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahTebingTinggi, KontrakTanahTebingTinggi, HargaTanahTebingTinggi, TanahUsulHapusTebingTinggi, TahunBerkurangUsulHapusTanahTebingTinggi

from umum.models import TanahPenghapusanTebingTinggi, TahunBerkurangTanahTebingTinggi, PenghapusanTanahTebingTinggi

from umum.models import SKPDAsalTanahTebingTinggi, SKPDTujuanTanahTebingTinggi, FotoTanahTebingTinggi

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanTebingTinggi, KontrakGedungBangunanTebingTinggi, HargaGedungBangunanTebingTinggi, GedungBangunanRuanganTebingTinggi, GedungBangunanUsulHapusTebingTinggi, TahunBerkurangUsulHapusGedungTebingTinggi

from gedungbangunan.models import GedungBangunanPenghapusanTebingTinggi, TahunBerkurangGedungBangunanTebingTinggi, PenghapusanGedungBangunanTebingTinggi

from gedungbangunan.models import SKPDAsalGedungBangunanTebingTinggi, SKPDTujuanGedungBangunanTebingTinggi, FotoGedungBangunanTebingTinggi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinTebingTinggi, KontrakPeralatanMesinTebingTinggi, HargaPeralatanMesinTebingTinggi, PeralatanMesinUsulHapusTebingTinggi, TahunBerkurangUsulHapusPeralatanMesinTebingTinggi

from peralatanmesin.models import PeralatanMesinPenghapusanTebingTinggi, TahunBerkurangPeralatanMesinTebingTinggi, PenghapusanPeralatanMesinTebingTinggi

from peralatanmesin.models import SKPDAsalPeralatanMesinTebingTinggi, SKPDTujuanPeralatanMesinTebingTinggi, FotoPeralatanMesinTebingTinggi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahTebingTinggiInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahTebingTinggi



class PenghapusanTanahTebingTinggiInline(PenghapusanTanahInline):
    model = PenghapusanTanahTebingTinggi



class SKPDAsalTanahTebingTinggiInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahTebingTinggi



class SKPDTujuanTanahTebingTinggiInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahTebingTinggi



class FotoTanahTebingTinggiInline(FotoTanahInline):
    model = FotoTanahTebingTinggi



class GedungBangunanTebingTinggiInline(GedungBangunanInline):
    model = GedungBangunanTebingTinggi



class HargaTanahTebingTinggiInline(HargaTanahInline):
    model = HargaTanahTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=38)
        return super(HargaTanahTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahTebingTinggiInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahTebingTinggi


class TanahTebingTinggiAdmin(TanahAdmin):
    inlines = [HargaTanahTebingTinggiInline,
                SKPDAsalTanahTebingTinggiInline,
                FotoTanahTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        return super(TanahTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusTebingTinggiAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahTebingTinggiInline,
                SKPDAsalTanahTebingTinggiInline,
                FotoTanahTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahTebingTinggiAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=38)
        return super(KontrakTanahTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=38)



class HargaTanahTebingTinggiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanTebingTinggiAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahTebingTinggiInline, TahunBerkurangTanahTebingTinggiInline,
                    SKPDAsalTanahTebingTinggiInline,
                    SKPDTujuanTanahTebingTinggiInline,
                    FotoTanahTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah TebingTinggi
admin.site.register(TanahTebingTinggi, TanahTebingTinggiAdmin)
admin.site.register(TanahUsulHapusTebingTinggi, TanahUsulHapusTebingTinggiAdmin)
admin.site.register(KontrakTanahTebingTinggi, KontrakTanahTebingTinggiAdmin)
admin.site.register(HargaTanahTebingTinggi, HargaTanahTebingTinggiAdmin)
admin.site.register(TanahPenghapusanTebingTinggi, TanahPenghapusanTebingTinggiAdmin)



from gedungbangunan.models import KDPGedungBangunanTebingTinggi


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanTebingTinggiInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanTebingTinggi



class PenghapusanGedungBangunanTebingTinggiInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanTebingTinggi



class SKPDAsalGedungBangunanTebingTinggiInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanTebingTinggi



class SKPDTujuanGedungBangunanTebingTinggiInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanTebingTinggi



class FotoGedungBangunanTebingTinggiInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanTebingTinggi



class HargaGedungBangunanTebingTinggiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=38)
        return super(HargaGedungBangunanTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungTebingTinggiInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungTebingTinggi


class GedungBangunanTebingTinggiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanTebingTinggiInline,
                SKPDAsalGedungBangunanTebingTinggiInline,
                FotoGedungBangunanTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        return super(GedungBangunanTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanTebingTinggiAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanTebingTinggiInline,
                SKPDAsalGedungBangunanTebingTinggiInline,
                FotoGedungBangunanTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        return super(KDPGedungBangunanTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganTebingTinggiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusTebingTinggiAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungTebingTinggiInline,
                    SKPDAsalGedungBangunanTebingTinggiInline,
                    FotoGedungBangunanTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanTebingTinggiAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=38)
        return super(KontrakGedungBangunanTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=38)



class HargaGedungBangunanTebingTinggiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanTebingTinggiAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanTebingTinggiInline, TahunBerkurangGedungBangunanTebingTinggiInline,
                    SKPDAsalGedungBangunanTebingTinggiInline,
                    SKPDTujuanGedungBangunanTebingTinggiInline,
                    FotoGedungBangunanTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan TebingTinggi
admin.site.register(GedungBangunanTebingTinggi, GedungBangunanTebingTinggiAdmin)
admin.site.register(KDPGedungBangunanTebingTinggi, KDPGedungBangunanTebingTinggiAdmin)
admin.site.register(GedungBangunanRuanganTebingTinggi, GedungBangunanRuanganTebingTinggiAdmin)
admin.site.register(GedungBangunanUsulHapusTebingTinggi, GedungBangunanUsulHapusTebingTinggiAdmin)
admin.site.register(KontrakGedungBangunanTebingTinggi, KontrakGedungBangunanTebingTinggiAdmin)
admin.site.register(HargaGedungBangunanTebingTinggi, HargaGedungBangunanTebingTinggiAdmin)
admin.site.register(GedungBangunanPenghapusanTebingTinggi, GedungBangunanPenghapusanTebingTinggiAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinTebingTinggiInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinTebingTinggi



class PenghapusanPeralatanMesinTebingTinggiInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinTebingTinggi



class SKPDAsalPeralatanMesinTebingTinggiInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinTebingTinggi



class SKPDTujuanPeralatanMesinTebingTinggiInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinTebingTinggi



class FotoPeralatanMesinTebingTinggiInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinTebingTinggi



class HargaPeralatanMesinTebingTinggiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=38)
        return super(HargaPeralatanMesinTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinTebingTinggiInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinTebingTinggi


class PeralatanMesinTebingTinggiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinTebingTinggiInline,
                    SKPDAsalPeralatanMesinTebingTinggiInline,
                    FotoPeralatanMesinTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=38)
        return super(PeralatanMesinTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusTebingTinggiAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinTebingTinggiInline,
                    SKPDAsalPeralatanMesinTebingTinggiInline,
                    FotoPeralatanMesinTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinTebingTinggiAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=38)
        return super(KontrakPeralatanMesinTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=38)



class HargaPeralatanMesinTebingTinggiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanTebingTinggiAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinTebingTinggiInline, TahunBerkurangPeralatanMesinTebingTinggiInline,
                    SKPDAsalPeralatanMesinTebingTinggiInline,
                    SKPDTujuanPeralatanMesinTebingTinggiInline,
                    FotoPeralatanMesinTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin TebingTinggi
admin.site.register(PeralatanMesinTebingTinggi, PeralatanMesinTebingTinggiAdmin)
admin.site.register(PeralatanMesinUsulHapusTebingTinggi, PeralatanMesinUsulHapusTebingTinggiAdmin)
admin.site.register(KontrakPeralatanMesinTebingTinggi, KontrakPeralatanMesinTebingTinggiAdmin)
admin.site.register(HargaPeralatanMesinTebingTinggi, HargaPeralatanMesinTebingTinggiAdmin)
admin.site.register(PeralatanMesinPenghapusanTebingTinggi, PeralatanMesinPenghapusanTebingTinggiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanTebingTinggi, KontrakJalanIrigasiJaringanTebingTinggi, HargaJalanIrigasiJaringanTebingTinggi, KDPJalanIrigasiJaringanTebingTinggi, JalanIrigasiJaringanUsulHapusTebingTinggi, TahunBerkurangUsulHapusJalanIrigasiJaringanTebingTinggi

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanTebingTinggi, TahunBerkurangJalanIrigasiJaringanTebingTinggi, PenghapusanJalanIrigasiJaringanTebingTinggi

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanTebingTinggi, SKPDTujuanJalanIrigasiJaringanTebingTinggi, FotoJalanIrigasiJaringanTebingTinggi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanTebingTinggiInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanTebingTinggi



class PenghapusanJalanIrigasiJaringanTebingTinggiInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanTebingTinggi



class SKPDAsalJalanIrigasiJaringanTebingTinggiInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanTebingTinggi



class SKPDTujuanJalanIrigasiJaringanTebingTinggiInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanTebingTinggi



class FotoJalanIrigasiJaringanTebingTinggiInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanTebingTinggi





class HargaJalanIrigasiJaringanTebingTinggiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=38)
        return super(HargaJalanIrigasiJaringanTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanTebingTinggiInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanTebingTinggi


class JalanIrigasiJaringanTebingTinggiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanTebingTinggiInline,
                    SKPDAsalJalanIrigasiJaringanTebingTinggiInline,
                    FotoJalanIrigasiJaringanTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        return super(JalanIrigasiJaringanTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusTebingTinggiAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanTebingTinggiInline,
                    SKPDAsalJalanIrigasiJaringanTebingTinggiInline,
                    FotoJalanIrigasiJaringanTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanTebingTinggiAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanTebingTinggiInline,
                    SKPDAsalJalanIrigasiJaringanTebingTinggiInline,
                    FotoJalanIrigasiJaringanTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        return super(KDPJalanIrigasiJaringanTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanTebingTinggiAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=38)
        return super(KontrakJalanIrigasiJaringanTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=38)



class HargaJalanIrigasiJaringanTebingTinggiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanTebingTinggiAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanTebingTinggiInline, TahunBerkurangJalanIrigasiJaringanTebingTinggiInline,
                    SKPDAsalJalanIrigasiJaringanTebingTinggiInline,
                    SKPDTujuanJalanIrigasiJaringanTebingTinggiInline,
                    FotoJalanIrigasiJaringanTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan TebingTinggi
admin.site.register(JalanIrigasiJaringanTebingTinggi, JalanIrigasiJaringanTebingTinggiAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusTebingTinggi, JalanIrigasiJaringanUsulHapusTebingTinggiAdmin)
admin.site.register(KDPJalanIrigasiJaringanTebingTinggi, KDPJalanIrigasiJaringanTebingTinggiAdmin)
admin.site.register(KontrakJalanIrigasiJaringanTebingTinggi, KontrakJalanIrigasiJaringanTebingTinggiAdmin)
admin.site.register(HargaJalanIrigasiJaringanTebingTinggi, HargaJalanIrigasiJaringanTebingTinggiAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanTebingTinggi, JalanIrigasiJaringanPenghapusanTebingTinggiAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLTebingTinggi, KontrakATLTebingTinggi, HargaATLTebingTinggi, ATLUsulHapusTebingTinggi, TahunBerkurangUsulHapusATLTebingTinggi

from atl.models import ATLPenghapusanTebingTinggi, TahunBerkurangATLTebingTinggi, PenghapusanATLTebingTinggi

from atl.models import SKPDAsalATLTebingTinggi, SKPDTujuanATLTebingTinggi, FotoATLTebingTinggi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLTebingTinggiInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLTebingTinggi



class PenghapusanATLTebingTinggiInline(PenghapusanATLInline):
    model = PenghapusanATLTebingTinggi



class SKPDAsalATLTebingTinggiInline(SKPDAsalATLInline):
    model = SKPDAsalATLTebingTinggi



class SKPDTujuanATLTebingTinggiInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLTebingTinggi



class FotoATLTebingTinggiInline(FotoATLInline):
    model = FotoATLTebingTinggi



class HargaATLTebingTinggiInline(HargaATLInline):
    model = HargaATLTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=38)
        return super(HargaATLTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLTebingTinggiInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLTebingTinggi


class ATLTebingTinggiAdmin(ATLAdmin):
    inlines = [HargaATLTebingTinggiInline,
                    SKPDAsalATLTebingTinggiInline,
                    FotoATLTebingTinggiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=38)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=38)
        return super(ATLTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusTebingTinggiAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLTebingTinggiInline,
                    SKPDAsalATLTebingTinggiInline,
                    FotoATLTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLTebingTinggiAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=38)
        return super(KontrakATLTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=38)



class HargaATLTebingTinggiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanTebingTinggiAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLTebingTinggiInline, TahunBerkurangATLTebingTinggiInline,
                    SKPDAsalATLTebingTinggiInline,
                    SKPDTujuanATLTebingTinggiInline,
                    FotoATLTebingTinggiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=38)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL TebingTinggi
admin.site.register(ATLTebingTinggi, ATLTebingTinggiAdmin)
admin.site.register(ATLUsulHapusTebingTinggi, ATLUsulHapusTebingTinggiAdmin)
admin.site.register(KontrakATLTebingTinggi, KontrakATLTebingTinggiAdmin)
admin.site.register(HargaATLTebingTinggi, HargaATLTebingTinggiAdmin)
admin.site.register(ATLPenghapusanTebingTinggi, ATLPenghapusanTebingTinggiAdmin)
