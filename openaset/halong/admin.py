### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahHalong, KontrakTanahHalong, HargaTanahHalong, TanahUsulHapusHalong, TahunBerkurangUsulHapusTanahHalong

from umum.models import TanahPenghapusanHalong, TahunBerkurangTanahHalong, PenghapusanTanahHalong

from umum.models import SKPDAsalTanahHalong, SKPDTujuanTanahHalong, FotoTanahHalong

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanHalong, KontrakGedungBangunanHalong, HargaGedungBangunanHalong, GedungBangunanRuanganHalong, GedungBangunanUsulHapusHalong, TahunBerkurangUsulHapusGedungHalong

from gedungbangunan.models import GedungBangunanPenghapusanHalong, TahunBerkurangGedungBangunanHalong, PenghapusanGedungBangunanHalong

from gedungbangunan.models import SKPDAsalGedungBangunanHalong, SKPDTujuanGedungBangunanHalong, FotoGedungBangunanHalong

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinHalong, KontrakPeralatanMesinHalong, HargaPeralatanMesinHalong, PeralatanMesinUsulHapusHalong, TahunBerkurangUsulHapusPeralatanMesinHalong

from peralatanmesin.models import PeralatanMesinPenghapusanHalong, TahunBerkurangPeralatanMesinHalong, PenghapusanPeralatanMesinHalong

from peralatanmesin.models import SKPDAsalPeralatanMesinHalong, SKPDTujuanPeralatanMesinHalong, FotoPeralatanMesinHalong

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahHalongInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahHalong



class PenghapusanTanahHalongInline(PenghapusanTanahInline):
    model = PenghapusanTanahHalong



class SKPDAsalTanahHalongInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahHalong



class SKPDTujuanTanahHalongInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahHalong



class FotoTanahHalongInline(FotoTanahInline):
    model = FotoTanahHalong



class GedungBangunanHalongInline(GedungBangunanInline):
    model = GedungBangunanHalong



class HargaTanahHalongInline(HargaTanahInline):
    model = HargaTanahHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=35)
        return super(HargaTanahHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahHalongInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahHalong


class TanahHalongAdmin(TanahAdmin):
    inlines = [HargaTanahHalongInline,
                SKPDAsalTanahHalongInline,
                FotoTanahHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        return super(TanahHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusHalongAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahHalongInline,
                SKPDAsalTanahHalongInline,
                FotoTanahHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahHalongAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=35)
        return super(KontrakTanahHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=35)



class HargaTanahHalongAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanHalongAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahHalongInline, TahunBerkurangTanahHalongInline,
                    SKPDAsalTanahHalongInline,
                    SKPDTujuanTanahHalongInline,
                    FotoTanahHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Halong
admin.site.register(TanahHalong, TanahHalongAdmin)
admin.site.register(TanahUsulHapusHalong, TanahUsulHapusHalongAdmin)
admin.site.register(KontrakTanahHalong, KontrakTanahHalongAdmin)
admin.site.register(HargaTanahHalong, HargaTanahHalongAdmin)
admin.site.register(TanahPenghapusanHalong, TanahPenghapusanHalongAdmin)



from gedungbangunan.models import KDPGedungBangunanHalong


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanHalongInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanHalong



class PenghapusanGedungBangunanHalongInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanHalong



class SKPDAsalGedungBangunanHalongInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanHalong



class SKPDTujuanGedungBangunanHalongInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanHalong



class FotoGedungBangunanHalongInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanHalong



class HargaGedungBangunanHalongInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=35)
        return super(HargaGedungBangunanHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungHalongInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungHalong


class GedungBangunanHalongAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanHalongInline,
                SKPDAsalGedungBangunanHalongInline,
                FotoGedungBangunanHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        return super(GedungBangunanHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanHalongAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanHalongInline,
                SKPDAsalGedungBangunanHalongInline,
                FotoGedungBangunanHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        return super(KDPGedungBangunanHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganHalongAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusHalongAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungHalongInline,
                    SKPDAsalGedungBangunanHalongInline,
                    FotoGedungBangunanHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanHalongAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=35)
        return super(KontrakGedungBangunanHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=35)



class HargaGedungBangunanHalongAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanHalongAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanHalongInline, TahunBerkurangGedungBangunanHalongInline,
                    SKPDAsalGedungBangunanHalongInline,
                    SKPDTujuanGedungBangunanHalongInline,
                    FotoGedungBangunanHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Halong
admin.site.register(GedungBangunanHalong, GedungBangunanHalongAdmin)
admin.site.register(KDPGedungBangunanHalong, KDPGedungBangunanHalongAdmin)
admin.site.register(GedungBangunanRuanganHalong, GedungBangunanRuanganHalongAdmin)
admin.site.register(GedungBangunanUsulHapusHalong, GedungBangunanUsulHapusHalongAdmin)
admin.site.register(KontrakGedungBangunanHalong, KontrakGedungBangunanHalongAdmin)
admin.site.register(HargaGedungBangunanHalong, HargaGedungBangunanHalongAdmin)
admin.site.register(GedungBangunanPenghapusanHalong, GedungBangunanPenghapusanHalongAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinHalongInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinHalong



class PenghapusanPeralatanMesinHalongInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinHalong



class SKPDAsalPeralatanMesinHalongInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinHalong



class SKPDTujuanPeralatanMesinHalongInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinHalong



class FotoPeralatanMesinHalongInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinHalong



class HargaPeralatanMesinHalongInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=35)
        return super(HargaPeralatanMesinHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinHalongInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinHalong


class PeralatanMesinHalongAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinHalongInline,
                    SKPDAsalPeralatanMesinHalongInline,
                    FotoPeralatanMesinHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=35)
        return super(PeralatanMesinHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusHalongAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinHalongInline,
                    SKPDAsalPeralatanMesinHalongInline,
                    FotoPeralatanMesinHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinHalongAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=35)
        return super(KontrakPeralatanMesinHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=35)



class HargaPeralatanMesinHalongAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanHalongAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinHalongInline, TahunBerkurangPeralatanMesinHalongInline,
                    SKPDAsalPeralatanMesinHalongInline,
                    SKPDTujuanPeralatanMesinHalongInline,
                    FotoPeralatanMesinHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Halong
admin.site.register(PeralatanMesinHalong, PeralatanMesinHalongAdmin)
admin.site.register(PeralatanMesinUsulHapusHalong, PeralatanMesinUsulHapusHalongAdmin)
admin.site.register(KontrakPeralatanMesinHalong, KontrakPeralatanMesinHalongAdmin)
admin.site.register(HargaPeralatanMesinHalong, HargaPeralatanMesinHalongAdmin)
admin.site.register(PeralatanMesinPenghapusanHalong, PeralatanMesinPenghapusanHalongAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanHalong, KontrakJalanIrigasiJaringanHalong, HargaJalanIrigasiJaringanHalong, KDPJalanIrigasiJaringanHalong, JalanIrigasiJaringanUsulHapusHalong, TahunBerkurangUsulHapusJalanIrigasiJaringanHalong

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanHalong, TahunBerkurangJalanIrigasiJaringanHalong, PenghapusanJalanIrigasiJaringanHalong

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanHalong, SKPDTujuanJalanIrigasiJaringanHalong, FotoJalanIrigasiJaringanHalong

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanHalongInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanHalong



class PenghapusanJalanIrigasiJaringanHalongInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanHalong



class SKPDAsalJalanIrigasiJaringanHalongInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanHalong



class SKPDTujuanJalanIrigasiJaringanHalongInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanHalong



class FotoJalanIrigasiJaringanHalongInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanHalong





class HargaJalanIrigasiJaringanHalongInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=35)
        return super(HargaJalanIrigasiJaringanHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanHalongInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanHalong


class JalanIrigasiJaringanHalongAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanHalongInline,
                    SKPDAsalJalanIrigasiJaringanHalongInline,
                    FotoJalanIrigasiJaringanHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        return super(JalanIrigasiJaringanHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusHalongAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanHalongInline,
                    SKPDAsalJalanIrigasiJaringanHalongInline,
                    FotoJalanIrigasiJaringanHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanHalongAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanHalongInline,
                    SKPDAsalJalanIrigasiJaringanHalongInline,
                    FotoJalanIrigasiJaringanHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        return super(KDPJalanIrigasiJaringanHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanHalongAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=35)
        return super(KontrakJalanIrigasiJaringanHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=35)



class HargaJalanIrigasiJaringanHalongAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanHalongAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanHalongInline, TahunBerkurangJalanIrigasiJaringanHalongInline,
                    SKPDAsalJalanIrigasiJaringanHalongInline,
                    SKPDTujuanJalanIrigasiJaringanHalongInline,
                    FotoJalanIrigasiJaringanHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Halong
admin.site.register(JalanIrigasiJaringanHalong, JalanIrigasiJaringanHalongAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusHalong, JalanIrigasiJaringanUsulHapusHalongAdmin)
admin.site.register(KDPJalanIrigasiJaringanHalong, KDPJalanIrigasiJaringanHalongAdmin)
admin.site.register(KontrakJalanIrigasiJaringanHalong, KontrakJalanIrigasiJaringanHalongAdmin)
admin.site.register(HargaJalanIrigasiJaringanHalong, HargaJalanIrigasiJaringanHalongAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanHalong, JalanIrigasiJaringanPenghapusanHalongAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLHalong, KontrakATLHalong, HargaATLHalong, ATLUsulHapusHalong, TahunBerkurangUsulHapusATLHalong

from atl.models import ATLPenghapusanHalong, TahunBerkurangATLHalong, PenghapusanATLHalong

from atl.models import SKPDAsalATLHalong, SKPDTujuanATLHalong, FotoATLHalong

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLHalongInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLHalong



class PenghapusanATLHalongInline(PenghapusanATLInline):
    model = PenghapusanATLHalong



class SKPDAsalATLHalongInline(SKPDAsalATLInline):
    model = SKPDAsalATLHalong



class SKPDTujuanATLHalongInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLHalong



class FotoATLHalongInline(FotoATLInline):
    model = FotoATLHalong



class HargaATLHalongInline(HargaATLInline):
    model = HargaATLHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=35)
        return super(HargaATLHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLHalongInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLHalong


class ATLHalongAdmin(ATLAdmin):
    inlines = [HargaATLHalongInline,
                    SKPDAsalATLHalongInline,
                    FotoATLHalongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=35)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=35)
        return super(ATLHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusHalongAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLHalongInline,
                    SKPDAsalATLHalongInline,
                    FotoATLHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLHalongAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=35)
        return super(KontrakATLHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=35)



class HargaATLHalongAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanHalongAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLHalongInline, TahunBerkurangATLHalongInline,
                    SKPDAsalATLHalongInline,
                    SKPDTujuanATLHalongInline,
                    FotoATLHalongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=35)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Halong
admin.site.register(ATLHalong, ATLHalongAdmin)
admin.site.register(ATLUsulHapusHalong, ATLUsulHapusHalongAdmin)
admin.site.register(KontrakATLHalong, KontrakATLHalongAdmin)
admin.site.register(HargaATLHalong, HargaATLHalongAdmin)
admin.site.register(ATLPenghapusanHalong, ATLPenghapusanHalongAdmin)
