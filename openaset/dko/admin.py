### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDKO, KontrakTanahDKO, HargaTanahDKO, TanahUsulHapusDKO, TahunBerkurangUsulHapusTanahDKO

from umum.models import TanahPenghapusanDKO, TahunBerkurangTanahDKO, PenghapusanTanahDKO

from umum.models import SKPDAsalTanahDKO, SKPDTujuanTanahDKO, FotoTanahDKO

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDKO, KontrakGedungBangunanDKO, HargaGedungBangunanDKO, GedungBangunanRuanganDKO, GedungBangunanUsulHapusDKO, TahunBerkurangUsulHapusGedungDKO

from gedungbangunan.models import GedungBangunanPenghapusanDKO, TahunBerkurangGedungBangunanDKO, PenghapusanGedungBangunanDKO

from gedungbangunan.models import SKPDAsalGedungBangunanDKO, SKPDTujuanGedungBangunanDKO, FotoGedungBangunanDKO

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDKO, KontrakPeralatanMesinDKO, HargaPeralatanMesinDKO, PeralatanMesinUsulHapusDKO, TahunBerkurangUsulHapusPeralatanMesinDKO

from peralatanmesin.models import PeralatanMesinPenghapusanDKO, TahunBerkurangPeralatanMesinDKO, PenghapusanPeralatanMesinDKO

from peralatanmesin.models import SKPDAsalPeralatanMesinDKO, SKPDTujuanPeralatanMesinDKO, FotoPeralatanMesinDKO

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDKOInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDKO



class PenghapusanTanahDKOInline(PenghapusanTanahInline):
    model = PenghapusanTanahDKO



class SKPDAsalTanahDKOInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDKO



class SKPDTujuanTanahDKOInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDKO



class FotoTanahDKOInline(FotoTanahInline):
    model = FotoTanahDKO



class GedungBangunanDKOInline(GedungBangunanInline):
    model = GedungBangunanDKO



class HargaTanahDKOInline(HargaTanahInline):
    model = HargaTanahDKO

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=23)
        return super(HargaTanahDKOInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDKOInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDKO


class TanahDKOAdmin(TanahAdmin):
    inlines = [HargaTanahDKOInline,
                SKPDAsalTanahDKOInline,
                FotoTanahDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        return super(TanahDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDKOAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDKOInline,
                SKPDAsalTanahDKOInline,
                FotoTanahDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDKOAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=23)
        return super(KontrakTanahDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=23)



class HargaTanahDKOAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDKOAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDKOInline, TahunBerkurangTanahDKOInline,
                    SKPDAsalTanahDKOInline,
                    SKPDTujuanTanahDKOInline,
                    FotoTanahDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DKO
admin.site.register(TanahDKO, TanahDKOAdmin)
admin.site.register(TanahUsulHapusDKO, TanahUsulHapusDKOAdmin)
admin.site.register(KontrakTanahDKO, KontrakTanahDKOAdmin)
admin.site.register(HargaTanahDKO, HargaTanahDKOAdmin)
admin.site.register(TanahPenghapusanDKO, TanahPenghapusanDKOAdmin)



from gedungbangunan.models import KDPGedungBangunanDKO


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDKOInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDKO



class PenghapusanGedungBangunanDKOInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDKO



class SKPDAsalGedungBangunanDKOInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDKO



class SKPDTujuanGedungBangunanDKOInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDKO



class FotoGedungBangunanDKOInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDKO



class HargaGedungBangunanDKOInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDKO

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=23)
        return super(HargaGedungBangunanDKOInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDKOInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDKO


class GedungBangunanDKOAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDKOInline,
                SKPDAsalGedungBangunanDKOInline,
                FotoGedungBangunanDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        return super(GedungBangunanDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDKOAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDKOInline,
                SKPDAsalGedungBangunanDKOInline,
                FotoGedungBangunanDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        return super(KDPGedungBangunanDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDKOAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDKOAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDKOInline,
                    SKPDAsalGedungBangunanDKOInline,
                    FotoGedungBangunanDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDKOAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=23)
        return super(KontrakGedungBangunanDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=23)



class HargaGedungBangunanDKOAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDKOAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDKOInline, TahunBerkurangGedungBangunanDKOInline,
                    SKPDAsalGedungBangunanDKOInline,
                    SKPDTujuanGedungBangunanDKOInline,
                    FotoGedungBangunanDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DKO
admin.site.register(GedungBangunanDKO, GedungBangunanDKOAdmin)
admin.site.register(KDPGedungBangunanDKO, KDPGedungBangunanDKOAdmin)
admin.site.register(GedungBangunanRuanganDKO, GedungBangunanRuanganDKOAdmin)
admin.site.register(GedungBangunanUsulHapusDKO, GedungBangunanUsulHapusDKOAdmin)
admin.site.register(KontrakGedungBangunanDKO, KontrakGedungBangunanDKOAdmin)
admin.site.register(HargaGedungBangunanDKO, HargaGedungBangunanDKOAdmin)
admin.site.register(GedungBangunanPenghapusanDKO, GedungBangunanPenghapusanDKOAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDKOInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDKO



class PenghapusanPeralatanMesinDKOInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDKO



class SKPDAsalPeralatanMesinDKOInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDKO



class SKPDTujuanPeralatanMesinDKOInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDKO



class FotoPeralatanMesinDKOInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDKO



class HargaPeralatanMesinDKOInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDKO

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=23)
        return super(HargaPeralatanMesinDKOInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDKOInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDKO


class PeralatanMesinDKOAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDKOInline,
                    SKPDAsalPeralatanMesinDKOInline,
                    FotoPeralatanMesinDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=23)
        return super(PeralatanMesinDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDKOAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDKOInline,
                    SKPDAsalPeralatanMesinDKOInline,
                    FotoPeralatanMesinDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDKOAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=23)
        return super(KontrakPeralatanMesinDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=23)



class HargaPeralatanMesinDKOAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDKOAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDKOInline, TahunBerkurangPeralatanMesinDKOInline,
                    SKPDAsalPeralatanMesinDKOInline,
                    SKPDTujuanPeralatanMesinDKOInline,
                    FotoPeralatanMesinDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DKO
admin.site.register(PeralatanMesinDKO, PeralatanMesinDKOAdmin)
admin.site.register(PeralatanMesinUsulHapusDKO, PeralatanMesinUsulHapusDKOAdmin)
admin.site.register(KontrakPeralatanMesinDKO, KontrakPeralatanMesinDKOAdmin)
admin.site.register(HargaPeralatanMesinDKO, HargaPeralatanMesinDKOAdmin)
admin.site.register(PeralatanMesinPenghapusanDKO, PeralatanMesinPenghapusanDKOAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDKO, KontrakJalanIrigasiJaringanDKO, HargaJalanIrigasiJaringanDKO, KDPJalanIrigasiJaringanDKO, JalanIrigasiJaringanUsulHapusDKO, TahunBerkurangUsulHapusJalanIrigasiJaringanDKO

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDKO, TahunBerkurangJalanIrigasiJaringanDKO, PenghapusanJalanIrigasiJaringanDKO

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDKO, SKPDTujuanJalanIrigasiJaringanDKO, FotoJalanIrigasiJaringanDKO

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDKOInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDKO



class PenghapusanJalanIrigasiJaringanDKOInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDKO



class SKPDAsalJalanIrigasiJaringanDKOInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDKO



class SKPDTujuanJalanIrigasiJaringanDKOInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDKO



class FotoJalanIrigasiJaringanDKOInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDKO





class HargaJalanIrigasiJaringanDKOInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDKO

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=23)
        return super(HargaJalanIrigasiJaringanDKOInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDKOInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDKO


class JalanIrigasiJaringanDKOAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDKOInline,
                    SKPDAsalJalanIrigasiJaringanDKOInline,
                    FotoJalanIrigasiJaringanDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        return super(JalanIrigasiJaringanDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDKOAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDKOInline,
                    SKPDAsalJalanIrigasiJaringanDKOInline,
                    FotoJalanIrigasiJaringanDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDKOAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDKOInline,
                    SKPDAsalJalanIrigasiJaringanDKOInline,
                    FotoJalanIrigasiJaringanDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        return super(KDPJalanIrigasiJaringanDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDKOAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=23)
        return super(KontrakJalanIrigasiJaringanDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=23)



class HargaJalanIrigasiJaringanDKOAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDKOAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDKOInline, TahunBerkurangJalanIrigasiJaringanDKOInline,
                    SKPDAsalJalanIrigasiJaringanDKOInline,
                    SKPDTujuanJalanIrigasiJaringanDKOInline,
                    FotoJalanIrigasiJaringanDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DKO
admin.site.register(JalanIrigasiJaringanDKO, JalanIrigasiJaringanDKOAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDKO, JalanIrigasiJaringanUsulHapusDKOAdmin)
admin.site.register(KDPJalanIrigasiJaringanDKO, KDPJalanIrigasiJaringanDKOAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDKO, KontrakJalanIrigasiJaringanDKOAdmin)
admin.site.register(HargaJalanIrigasiJaringanDKO, HargaJalanIrigasiJaringanDKOAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDKO, JalanIrigasiJaringanPenghapusanDKOAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDKO, KontrakATLDKO, HargaATLDKO, ATLUsulHapusDKO, TahunBerkurangUsulHapusATLDKO

from atl.models import ATLPenghapusanDKO, TahunBerkurangATLDKO, PenghapusanATLDKO

from atl.models import SKPDAsalATLDKO, SKPDTujuanATLDKO, FotoATLDKO

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDKOInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDKO



class PenghapusanATLDKOInline(PenghapusanATLInline):
    model = PenghapusanATLDKO



class SKPDAsalATLDKOInline(SKPDAsalATLInline):
    model = SKPDAsalATLDKO



class SKPDTujuanATLDKOInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDKO



class FotoATLDKOInline(FotoATLInline):
    model = FotoATLDKO



class HargaATLDKOInline(HargaATLInline):
    model = HargaATLDKO

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=23)
        return super(HargaATLDKOInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDKOInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDKO


class ATLDKOAdmin(ATLAdmin):
    inlines = [HargaATLDKOInline,
                    SKPDAsalATLDKOInline,
                    FotoATLDKOInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=23)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=23)
        return super(ATLDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDKOAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDKOInline,
                    SKPDAsalATLDKOInline,
                    FotoATLDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDKOAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=23)
        return super(KontrakATLDKOAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=23)



class HargaATLDKOAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDKOAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDKOInline, TahunBerkurangATLDKOInline,
                    SKPDAsalATLDKOInline,
                    SKPDTujuanATLDKOInline,
                    FotoATLDKOInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=23)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DKO
admin.site.register(ATLDKO, ATLDKOAdmin)
admin.site.register(ATLUsulHapusDKO, ATLUsulHapusDKOAdmin)
admin.site.register(KontrakATLDKO, KontrakATLDKOAdmin)
admin.site.register(HargaATLDKO, HargaATLDKOAdmin)
admin.site.register(ATLPenghapusanDKO, ATLPenghapusanDKOAdmin)
