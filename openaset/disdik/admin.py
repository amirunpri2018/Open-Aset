### $Id: admin.py,v 1.46 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDisdik, KontrakTanahDisdik, HargaTanahDisdik, TanahUsulHapusDisdik, TahunBerkurangUsulHapusTanahDisdik

from umum.models import TanahPenghapusanDisdik, TahunBerkurangTanahDisdik, PenghapusanTanahDisdik

from umum.models import SKPDAsalTanahDisdik, SKPDTujuanTanahDisdik, FotoTanahDisdik

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDisdik, KontrakGedungBangunanDisdik, HargaGedungBangunanDisdik, GedungBangunanRuanganDisdik, GedungBangunanUsulHapusDisdik, TahunBerkurangUsulHapusGedungDisdik

from gedungbangunan.models import GedungBangunanPenghapusanDisdik, TahunBerkurangGedungBangunanDisdik, PenghapusanGedungBangunanDisdik

from gedungbangunan.models import SKPDAsalGedungBangunanDisdik, SKPDTujuanGedungBangunanDisdik, FotoGedungBangunanDisdik

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDisdik, KontrakPeralatanMesinDisdik, HargaPeralatanMesinDisdik, PeralatanMesinUsulHapusDisdik, TahunBerkurangUsulHapusPeralatanMesinDisdik

from peralatanmesin.models import PeralatanMesinPenghapusanDisdik, TahunBerkurangPeralatanMesinDisdik, PenghapusanPeralatanMesinDisdik

from peralatanmesin.models import SKPDAsalPeralatanMesinDisdik, SKPDTujuanPeralatanMesinDisdik, FotoPeralatanMesinDisdik

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDisdikInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDisdik



class PenghapusanTanahDisdikInline(PenghapusanTanahInline):
    model = PenghapusanTanahDisdik



class SKPDAsalTanahDisdikInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDisdik



class SKPDTujuanTanahDisdikInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDisdik



class FotoTanahDisdikInline(FotoTanahInline):
    model = FotoTanahDisdik



class GedungBangunanDisdikInline(GedungBangunanInline):
    model = GedungBangunanDisdik



class HargaTanahDisdikInline(HargaTanahInline):
    model = HargaTanahDisdik

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDisdikInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDisdik


class TanahDisdikAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikInline,
                SKPDAsalTanahDisdikInline,
                FotoTanahDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        return super(TanahDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDisdikAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDisdikInline,
                SKPDAsalTanahDisdikInline,
                FotoTanahDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDisdikAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=7)
        return super(KontrakTanahDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=7)



class HargaTanahDisdikAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDisdikAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDisdikInline, TahunBerkurangTanahDisdikInline,
                    SKPDAsalTanahDisdikInline,
                    SKPDTujuanTanahDisdikInline,
                    FotoTanahDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Disdik
admin.site.register(TanahDisdik, TanahDisdikAdmin)
admin.site.register(TanahUsulHapusDisdik, TanahUsulHapusDisdikAdmin)
admin.site.register(KontrakTanahDisdik, KontrakTanahDisdikAdmin)
admin.site.register(HargaTanahDisdik, HargaTanahDisdikAdmin)
admin.site.register(TanahPenghapusanDisdik, TanahPenghapusanDisdikAdmin)



from gedungbangunan.models import KDPGedungBangunanDisdik


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDisdikInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDisdik



class PenghapusanGedungBangunanDisdikInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDisdik



class SKPDAsalGedungBangunanDisdikInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDisdik



class SKPDTujuanGedungBangunanDisdikInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDisdik



class FotoGedungBangunanDisdikInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDisdik



class HargaGedungBangunanDisdikInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdik

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDisdikInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDisdik


class GedungBangunanDisdikAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikInline,
                SKPDAsalGedungBangunanDisdikInline,
                FotoGedungBangunanDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        return super(GedungBangunanDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDisdikAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikInline,
                SKPDAsalGedungBangunanDisdikInline,
                FotoGedungBangunanDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        return super(KDPGedungBangunanDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDisdikAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDisdikInline,
                    SKPDAsalGedungBangunanDisdikInline,
                    FotoGedungBangunanDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDisdikAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=7)
        return super(KontrakGedungBangunanDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=7)



class HargaGedungBangunanDisdikAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDisdikAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDisdikInline, TahunBerkurangGedungBangunanDisdikInline,
                    SKPDAsalGedungBangunanDisdikInline,
                    SKPDTujuanGedungBangunanDisdikInline,
                    FotoGedungBangunanDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Disdik
admin.site.register(GedungBangunanDisdik, GedungBangunanDisdikAdmin)
admin.site.register(KDPGedungBangunanDisdik, KDPGedungBangunanDisdikAdmin)
admin.site.register(GedungBangunanRuanganDisdik, GedungBangunanRuanganDisdikAdmin)
admin.site.register(GedungBangunanUsulHapusDisdik, GedungBangunanUsulHapusDisdikAdmin)
admin.site.register(KontrakGedungBangunanDisdik, KontrakGedungBangunanDisdikAdmin)
admin.site.register(HargaGedungBangunanDisdik, HargaGedungBangunanDisdikAdmin)
admin.site.register(GedungBangunanPenghapusanDisdik, GedungBangunanPenghapusanDisdikAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDisdikInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDisdik



class PenghapusanPeralatanMesinDisdikInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDisdik



class SKPDAsalPeralatanMesinDisdikInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDisdik



class SKPDTujuanPeralatanMesinDisdikInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDisdik



class FotoPeralatanMesinDisdikInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDisdik



class HargaPeralatanMesinDisdikInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdik

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDisdikInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDisdik


class PeralatanMesinDisdikAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikInline,
                    SKPDAsalPeralatanMesinDisdikInline,
                    FotoPeralatanMesinDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=7)
        return super(PeralatanMesinDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDisdikAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDisdikInline,
                    SKPDAsalPeralatanMesinDisdikInline,
                    FotoPeralatanMesinDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDisdikAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=7)
        return super(KontrakPeralatanMesinDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=7)



class HargaPeralatanMesinDisdikAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDisdikAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDisdikInline, TahunBerkurangPeralatanMesinDisdikInline,
                    SKPDAsalPeralatanMesinDisdikInline,
                    SKPDTujuanPeralatanMesinDisdikInline,
                    FotoPeralatanMesinDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Disdik
admin.site.register(PeralatanMesinDisdik, PeralatanMesinDisdikAdmin)
admin.site.register(PeralatanMesinUsulHapusDisdik, PeralatanMesinUsulHapusDisdikAdmin)
admin.site.register(KontrakPeralatanMesinDisdik, KontrakPeralatanMesinDisdikAdmin)
admin.site.register(HargaPeralatanMesinDisdik, HargaPeralatanMesinDisdikAdmin)
admin.site.register(PeralatanMesinPenghapusanDisdik, PeralatanMesinPenghapusanDisdikAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdik, KontrakJalanIrigasiJaringanDisdik, HargaJalanIrigasiJaringanDisdik, KDPJalanIrigasiJaringanDisdik, JalanIrigasiJaringanUsulHapusDisdik, TahunBerkurangUsulHapusJalanIrigasiJaringanDisdik

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDisdik, TahunBerkurangJalanIrigasiJaringanDisdik, PenghapusanJalanIrigasiJaringanDisdik

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDisdik, SKPDTujuanJalanIrigasiJaringanDisdik, FotoJalanIrigasiJaringanDisdik

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDisdikInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDisdik



class PenghapusanJalanIrigasiJaringanDisdikInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDisdik



class SKPDAsalJalanIrigasiJaringanDisdikInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDisdik



class SKPDTujuanJalanIrigasiJaringanDisdikInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDisdik



class FotoJalanIrigasiJaringanDisdikInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDisdik





class HargaJalanIrigasiJaringanDisdikInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdik

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDisdikInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDisdik


class JalanIrigasiJaringanDisdikAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikInline,
                    SKPDAsalJalanIrigasiJaringanDisdikInline,
                    FotoJalanIrigasiJaringanDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        return super(JalanIrigasiJaringanDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDisdikAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDisdikInline,
                    SKPDAsalJalanIrigasiJaringanDisdikInline,
                    FotoJalanIrigasiJaringanDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDisdikAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikInline,
                    SKPDAsalJalanIrigasiJaringanDisdikInline,
                    FotoJalanIrigasiJaringanDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        return super(KDPJalanIrigasiJaringanDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDisdikAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=7)
        return super(KontrakJalanIrigasiJaringanDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=7)



class HargaJalanIrigasiJaringanDisdikAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDisdikAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDisdikInline, TahunBerkurangJalanIrigasiJaringanDisdikInline,
                    SKPDAsalJalanIrigasiJaringanDisdikInline,
                    SKPDTujuanJalanIrigasiJaringanDisdikInline,
                    FotoJalanIrigasiJaringanDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Disdik
admin.site.register(JalanIrigasiJaringanDisdik, JalanIrigasiJaringanDisdikAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDisdik, JalanIrigasiJaringanUsulHapusDisdikAdmin)
admin.site.register(KDPJalanIrigasiJaringanDisdik, KDPJalanIrigasiJaringanDisdikAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDisdik, KontrakJalanIrigasiJaringanDisdikAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdik, HargaJalanIrigasiJaringanDisdikAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDisdik, JalanIrigasiJaringanPenghapusanDisdikAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDisdik, KontrakATLDisdik, HargaATLDisdik, ATLUsulHapusDisdik, TahunBerkurangUsulHapusATLDisdik

from atl.models import ATLPenghapusanDisdik, TahunBerkurangATLDisdik, PenghapusanATLDisdik

from atl.models import SKPDAsalATLDisdik, SKPDTujuanATLDisdik, FotoATLDisdik

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDisdikInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDisdik



class PenghapusanATLDisdikInline(PenghapusanATLInline):
    model = PenghapusanATLDisdik



class SKPDAsalATLDisdikInline(SKPDAsalATLInline):
    model = SKPDAsalATLDisdik



class SKPDTujuanATLDisdikInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDisdik



class FotoATLDisdikInline(FotoATLInline):
    model = FotoATLDisdik



class HargaATLDisdikInline(HargaATLInline):
    model = HargaATLDisdik

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDisdikInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDisdik


class ATLDisdikAdmin(ATLAdmin):
    inlines = [HargaATLDisdikInline,
                    SKPDAsalATLDisdikInline,
                    FotoATLDisdikInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=7)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=7)
        return super(ATLDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDisdikAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDisdikInline,
                    SKPDAsalATLDisdikInline,
                    FotoATLDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDisdikAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=7)
        return super(KontrakATLDisdikAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=7)



class HargaATLDisdikAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDisdikAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDisdikInline, TahunBerkurangATLDisdikInline,
                    SKPDAsalATLDisdikInline,
                    SKPDTujuanATLDisdikInline,
                    FotoATLDisdikInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=7)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Disdik
admin.site.register(ATLDisdik, ATLDisdikAdmin)
admin.site.register(ATLUsulHapusDisdik, ATLUsulHapusDisdikAdmin)
admin.site.register(KontrakATLDisdik, KontrakATLDisdikAdmin)
admin.site.register(HargaATLDisdik, HargaATLDisdikAdmin)
admin.site.register(ATLPenghapusanDisdik, ATLPenghapusanDisdikAdmin)
