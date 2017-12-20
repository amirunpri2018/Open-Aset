### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahInspektorat, KontrakTanahInspektorat, HargaTanahInspektorat, TanahUsulHapusInspektorat, TahunBerkurangUsulHapusTanahInspektorat

from umum.models import TanahPenghapusanInspektorat, TahunBerkurangTanahInspektorat, PenghapusanTanahInspektorat

from umum.models import SKPDAsalTanahInspektorat, SKPDTujuanTanahInspektorat, FotoTanahInspektorat

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanInspektorat, KontrakGedungBangunanInspektorat, HargaGedungBangunanInspektorat, GedungBangunanRuanganInspektorat, GedungBangunanUsulHapusInspektorat, TahunBerkurangUsulHapusGedungInspektorat

from gedungbangunan.models import GedungBangunanPenghapusanInspektorat, TahunBerkurangGedungBangunanInspektorat, PenghapusanGedungBangunanInspektorat

from gedungbangunan.models import SKPDAsalGedungBangunanInspektorat, SKPDTujuanGedungBangunanInspektorat, FotoGedungBangunanInspektorat

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinInspektorat, KontrakPeralatanMesinInspektorat, HargaPeralatanMesinInspektorat, PeralatanMesinUsulHapusInspektorat, TahunBerkurangUsulHapusPeralatanMesinInspektorat

from peralatanmesin.models import PeralatanMesinPenghapusanInspektorat, TahunBerkurangPeralatanMesinInspektorat, PenghapusanPeralatanMesinInspektorat

from peralatanmesin.models import SKPDAsalPeralatanMesinInspektorat, SKPDTujuanPeralatanMesinInspektorat, FotoPeralatanMesinInspektorat

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahInspektoratInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahInspektorat



class PenghapusanTanahInspektoratInline(PenghapusanTanahInline):
    model = PenghapusanTanahInspektorat



class SKPDAsalTanahInspektoratInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahInspektorat



class SKPDTujuanTanahInspektoratInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahInspektorat



class FotoTanahInspektoratInline(FotoTanahInline):
    model = FotoTanahInspektorat



class GedungBangunanInspektoratInline(GedungBangunanInline):
    model = GedungBangunanInspektorat



class HargaTanahInspektoratInline(HargaTanahInline):
    model = HargaTanahInspektorat

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=20)
        return super(HargaTanahInspektoratInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahInspektoratInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahInspektorat


class TanahInspektoratAdmin(TanahAdmin):
    inlines = [HargaTanahInspektoratInline,
                SKPDAsalTanahInspektoratInline,
                FotoTanahInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        return super(TanahInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusInspektoratAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahInspektoratInline,
                SKPDAsalTanahInspektoratInline,
                FotoTanahInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahInspektoratAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=20)
        return super(KontrakTanahInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=20)



class HargaTanahInspektoratAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanInspektoratAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahInspektoratInline, TahunBerkurangTanahInspektoratInline,
                    SKPDAsalTanahInspektoratInline,
                    SKPDTujuanTanahInspektoratInline,
                    FotoTanahInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Inspektorat
admin.site.register(TanahInspektorat, TanahInspektoratAdmin)
admin.site.register(TanahUsulHapusInspektorat, TanahUsulHapusInspektoratAdmin)
admin.site.register(KontrakTanahInspektorat, KontrakTanahInspektoratAdmin)
admin.site.register(HargaTanahInspektorat, HargaTanahInspektoratAdmin)
admin.site.register(TanahPenghapusanInspektorat, TanahPenghapusanInspektoratAdmin)



from gedungbangunan.models import KDPGedungBangunanInspektorat


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanInspektoratInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanInspektorat



class PenghapusanGedungBangunanInspektoratInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanInspektorat



class SKPDAsalGedungBangunanInspektoratInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanInspektorat



class SKPDTujuanGedungBangunanInspektoratInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanInspektorat



class FotoGedungBangunanInspektoratInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanInspektorat



class HargaGedungBangunanInspektoratInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanInspektorat

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=20)
        return super(HargaGedungBangunanInspektoratInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungInspektoratInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungInspektorat


class GedungBangunanInspektoratAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanInspektoratInline,
                SKPDAsalGedungBangunanInspektoratInline,
                FotoGedungBangunanInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        return super(GedungBangunanInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanInspektoratAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanInspektoratInline,
                SKPDAsalGedungBangunanInspektoratInline,
                FotoGedungBangunanInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        return super(KDPGedungBangunanInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganInspektoratAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusInspektoratAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungInspektoratInline,
                    SKPDAsalGedungBangunanInspektoratInline,
                    FotoGedungBangunanInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanInspektoratAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=20)
        return super(KontrakGedungBangunanInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=20)



class HargaGedungBangunanInspektoratAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanInspektoratAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanInspektoratInline, TahunBerkurangGedungBangunanInspektoratInline,
                    SKPDAsalGedungBangunanInspektoratInline,
                    SKPDTujuanGedungBangunanInspektoratInline,
                    FotoGedungBangunanInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Inspektorat
admin.site.register(GedungBangunanInspektorat, GedungBangunanInspektoratAdmin)
admin.site.register(KDPGedungBangunanInspektorat, KDPGedungBangunanInspektoratAdmin)
admin.site.register(GedungBangunanRuanganInspektorat, GedungBangunanRuanganInspektoratAdmin)
admin.site.register(GedungBangunanUsulHapusInspektorat, GedungBangunanUsulHapusInspektoratAdmin)
admin.site.register(KontrakGedungBangunanInspektorat, KontrakGedungBangunanInspektoratAdmin)
admin.site.register(HargaGedungBangunanInspektorat, HargaGedungBangunanInspektoratAdmin)
admin.site.register(GedungBangunanPenghapusanInspektorat, GedungBangunanPenghapusanInspektoratAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinInspektoratInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinInspektorat



class PenghapusanPeralatanMesinInspektoratInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinInspektorat



class SKPDAsalPeralatanMesinInspektoratInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinInspektorat



class SKPDTujuanPeralatanMesinInspektoratInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinInspektorat



class FotoPeralatanMesinInspektoratInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinInspektorat



class HargaPeralatanMesinInspektoratInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinInspektorat

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=20)
        return super(HargaPeralatanMesinInspektoratInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinInspektoratInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinInspektorat


class PeralatanMesinInspektoratAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinInspektoratInline,
                    SKPDAsalPeralatanMesinInspektoratInline,
                    FotoPeralatanMesinInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=20)
        return super(PeralatanMesinInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusInspektoratAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinInspektoratInline,
                    SKPDAsalPeralatanMesinInspektoratInline,
                    FotoPeralatanMesinInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinInspektoratAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=20)
        return super(KontrakPeralatanMesinInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=20)



class HargaPeralatanMesinInspektoratAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanInspektoratAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinInspektoratInline, TahunBerkurangPeralatanMesinInspektoratInline,
                    SKPDAsalPeralatanMesinInspektoratInline,
                    SKPDTujuanPeralatanMesinInspektoratInline,
                    FotoPeralatanMesinInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Inspektorat
admin.site.register(PeralatanMesinInspektorat, PeralatanMesinInspektoratAdmin)
admin.site.register(PeralatanMesinUsulHapusInspektorat, PeralatanMesinUsulHapusInspektoratAdmin)
admin.site.register(KontrakPeralatanMesinInspektorat, KontrakPeralatanMesinInspektoratAdmin)
admin.site.register(HargaPeralatanMesinInspektorat, HargaPeralatanMesinInspektoratAdmin)
admin.site.register(PeralatanMesinPenghapusanInspektorat, PeralatanMesinPenghapusanInspektoratAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanInspektorat, KontrakJalanIrigasiJaringanInspektorat, HargaJalanIrigasiJaringanInspektorat, KDPJalanIrigasiJaringanInspektorat, JalanIrigasiJaringanUsulHapusInspektorat, TahunBerkurangUsulHapusJalanIrigasiJaringanInspektorat

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanInspektorat, TahunBerkurangJalanIrigasiJaringanInspektorat, PenghapusanJalanIrigasiJaringanInspektorat

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanInspektorat, SKPDTujuanJalanIrigasiJaringanInspektorat, FotoJalanIrigasiJaringanInspektorat

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanInspektoratInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanInspektorat



class PenghapusanJalanIrigasiJaringanInspektoratInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanInspektorat



class SKPDAsalJalanIrigasiJaringanInspektoratInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanInspektorat



class SKPDTujuanJalanIrigasiJaringanInspektoratInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanInspektorat



class FotoJalanIrigasiJaringanInspektoratInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanInspektorat





class HargaJalanIrigasiJaringanInspektoratInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanInspektorat

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=20)
        return super(HargaJalanIrigasiJaringanInspektoratInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanInspektoratInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanInspektorat


class JalanIrigasiJaringanInspektoratAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanInspektoratInline,
                    SKPDAsalJalanIrigasiJaringanInspektoratInline,
                    FotoJalanIrigasiJaringanInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        return super(JalanIrigasiJaringanInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusInspektoratAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanInspektoratInline,
                    SKPDAsalJalanIrigasiJaringanInspektoratInline,
                    FotoJalanIrigasiJaringanInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanInspektoratAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanInspektoratInline,
                    SKPDAsalJalanIrigasiJaringanInspektoratInline,
                    FotoJalanIrigasiJaringanInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        return super(KDPJalanIrigasiJaringanInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanInspektoratAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=20)
        return super(KontrakJalanIrigasiJaringanInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=20)



class HargaJalanIrigasiJaringanInspektoratAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanInspektoratAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanInspektoratInline, TahunBerkurangJalanIrigasiJaringanInspektoratInline,
                    SKPDAsalJalanIrigasiJaringanInspektoratInline,
                    SKPDTujuanJalanIrigasiJaringanInspektoratInline,
                    FotoJalanIrigasiJaringanInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Inspektorat
admin.site.register(JalanIrigasiJaringanInspektorat, JalanIrigasiJaringanInspektoratAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusInspektorat, JalanIrigasiJaringanUsulHapusInspektoratAdmin)
admin.site.register(KDPJalanIrigasiJaringanInspektorat, KDPJalanIrigasiJaringanInspektoratAdmin)
admin.site.register(KontrakJalanIrigasiJaringanInspektorat, KontrakJalanIrigasiJaringanInspektoratAdmin)
admin.site.register(HargaJalanIrigasiJaringanInspektorat, HargaJalanIrigasiJaringanInspektoratAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanInspektorat, JalanIrigasiJaringanPenghapusanInspektoratAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLInspektorat, KontrakATLInspektorat, HargaATLInspektorat, ATLUsulHapusInspektorat, TahunBerkurangUsulHapusATLInspektorat

from atl.models import ATLPenghapusanInspektorat, TahunBerkurangATLInspektorat, PenghapusanATLInspektorat

from atl.models import SKPDAsalATLInspektorat, SKPDTujuanATLInspektorat, FotoATLInspektorat

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLInspektoratInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLInspektorat



class PenghapusanATLInspektoratInline(PenghapusanATLInline):
    model = PenghapusanATLInspektorat



class SKPDAsalATLInspektoratInline(SKPDAsalATLInline):
    model = SKPDAsalATLInspektorat



class SKPDTujuanATLInspektoratInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLInspektorat



class FotoATLInspektoratInline(FotoATLInline):
    model = FotoATLInspektorat



class HargaATLInspektoratInline(HargaATLInline):
    model = HargaATLInspektorat

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=20)
        return super(HargaATLInspektoratInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLInspektoratInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLInspektorat


class ATLInspektoratAdmin(ATLAdmin):
    inlines = [HargaATLInspektoratInline,
                    SKPDAsalATLInspektoratInline,
                    FotoATLInspektoratInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=20)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=20)
        return super(ATLInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusInspektoratAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLInspektoratInline,
                    SKPDAsalATLInspektoratInline,
                    FotoATLInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLInspektoratAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=20)
        return super(KontrakATLInspektoratAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=20)



class HargaATLInspektoratAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanInspektoratAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLInspektoratInline, TahunBerkurangATLInspektoratInline,
                    SKPDAsalATLInspektoratInline,
                    SKPDTujuanATLInspektoratInline,
                    FotoATLInspektoratInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=20)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Inspektorat
admin.site.register(ATLInspektorat, ATLInspektoratAdmin)
admin.site.register(ATLUsulHapusInspektorat, ATLUsulHapusInspektoratAdmin)
admin.site.register(KontrakATLInspektorat, KontrakATLInspektoratAdmin)
admin.site.register(HargaATLInspektorat, HargaATLInspektoratAdmin)
admin.site.register(ATLPenghapusanInspektorat, ATLPenghapusanInspektoratAdmin)
