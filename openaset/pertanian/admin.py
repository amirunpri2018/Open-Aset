### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahPertanian, KontrakTanahPertanian, HargaTanahPertanian, TanahUsulHapusPertanian, TahunBerkurangUsulHapusTanahPertanian

from umum.models import TanahPenghapusanPertanian, TahunBerkurangTanahPertanian, PenghapusanTanahPertanian

from umum.models import SKPDAsalTanahPertanian, SKPDTujuanTanahPertanian, FotoTanahPertanian

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanPertanian, KontrakGedungBangunanPertanian, HargaGedungBangunanPertanian, GedungBangunanRuanganPertanian, GedungBangunanUsulHapusPertanian, TahunBerkurangUsulHapusGedungPertanian

from gedungbangunan.models import GedungBangunanPenghapusanPertanian, TahunBerkurangGedungBangunanPertanian, PenghapusanGedungBangunanPertanian

from gedungbangunan.models import SKPDAsalGedungBangunanPertanian, SKPDTujuanGedungBangunanPertanian, FotoGedungBangunanPertanian

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinPertanian, KontrakPeralatanMesinPertanian, HargaPeralatanMesinPertanian, PeralatanMesinUsulHapusPertanian, TahunBerkurangUsulHapusPeralatanMesinPertanian

from peralatanmesin.models import PeralatanMesinPenghapusanPertanian, TahunBerkurangPeralatanMesinPertanian, PenghapusanPeralatanMesinPertanian

from peralatanmesin.models import SKPDAsalPeralatanMesinPertanian, SKPDTujuanPeralatanMesinPertanian, FotoPeralatanMesinPertanian

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahPertanianInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahPertanian



class PenghapusanTanahPertanianInline(PenghapusanTanahInline):
    model = PenghapusanTanahPertanian



class SKPDAsalTanahPertanianInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahPertanian



class SKPDTujuanTanahPertanianInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahPertanian



class FotoTanahPertanianInline(FotoTanahInline):
    model = FotoTanahPertanian



class GedungBangunanPertanianInline(GedungBangunanInline):
    model = GedungBangunanPertanian



class HargaTanahPertanianInline(HargaTanahInline):
    model = HargaTanahPertanian

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=13)
        return super(HargaTanahPertanianInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahPertanianInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahPertanian


class TanahPertanianAdmin(TanahAdmin):
    inlines = [HargaTanahPertanianInline,
                SKPDAsalTanahPertanianInline,
                FotoTanahPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        return super(TanahPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusPertanianAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahPertanianInline,
                SKPDAsalTanahPertanianInline,
                FotoTanahPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahPertanianAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=13)
        return super(KontrakTanahPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=13)



class HargaTanahPertanianAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanPertanianAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahPertanianInline, TahunBerkurangTanahPertanianInline,
                    SKPDAsalTanahPertanianInline,
                    SKPDTujuanTanahPertanianInline,
                    FotoTanahPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Pertanian
admin.site.register(TanahPertanian, TanahPertanianAdmin)
admin.site.register(TanahUsulHapusPertanian, TanahUsulHapusPertanianAdmin)
admin.site.register(KontrakTanahPertanian, KontrakTanahPertanianAdmin)
admin.site.register(HargaTanahPertanian, HargaTanahPertanianAdmin)
admin.site.register(TanahPenghapusanPertanian, TanahPenghapusanPertanianAdmin)



from gedungbangunan.models import KDPGedungBangunanPertanian


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanPertanianInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanPertanian



class PenghapusanGedungBangunanPertanianInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanPertanian



class SKPDAsalGedungBangunanPertanianInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanPertanian



class SKPDTujuanGedungBangunanPertanianInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanPertanian



class FotoGedungBangunanPertanianInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanPertanian



class HargaGedungBangunanPertanianInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanPertanian

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=13)
        return super(HargaGedungBangunanPertanianInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungPertanianInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungPertanian


class GedungBangunanPertanianAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanPertanianInline,
                SKPDAsalGedungBangunanPertanianInline,
                FotoGedungBangunanPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        return super(GedungBangunanPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanPertanianAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanPertanianInline,
                SKPDAsalGedungBangunanPertanianInline,
                FotoGedungBangunanPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        return super(KDPGedungBangunanPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganPertanianAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusPertanianAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungPertanianInline,
                    SKPDAsalGedungBangunanPertanianInline,
                    FotoGedungBangunanPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanPertanianAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=13)
        return super(KontrakGedungBangunanPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=13)



class HargaGedungBangunanPertanianAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanPertanianAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanPertanianInline, TahunBerkurangGedungBangunanPertanianInline,
                    SKPDAsalGedungBangunanPertanianInline,
                    SKPDTujuanGedungBangunanPertanianInline,
                    FotoGedungBangunanPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Pertanian
admin.site.register(GedungBangunanPertanian, GedungBangunanPertanianAdmin)
admin.site.register(KDPGedungBangunanPertanian, KDPGedungBangunanPertanianAdmin)
admin.site.register(GedungBangunanRuanganPertanian, GedungBangunanRuanganPertanianAdmin)
admin.site.register(GedungBangunanUsulHapusPertanian, GedungBangunanUsulHapusPertanianAdmin)
admin.site.register(KontrakGedungBangunanPertanian, KontrakGedungBangunanPertanianAdmin)
admin.site.register(HargaGedungBangunanPertanian, HargaGedungBangunanPertanianAdmin)
admin.site.register(GedungBangunanPenghapusanPertanian, GedungBangunanPenghapusanPertanianAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinPertanianInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinPertanian



class PenghapusanPeralatanMesinPertanianInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinPertanian



class SKPDAsalPeralatanMesinPertanianInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinPertanian



class SKPDTujuanPeralatanMesinPertanianInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinPertanian



class FotoPeralatanMesinPertanianInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinPertanian



class HargaPeralatanMesinPertanianInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinPertanian

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=13)
        return super(HargaPeralatanMesinPertanianInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinPertanianInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinPertanian


class PeralatanMesinPertanianAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinPertanianInline,
                    SKPDAsalPeralatanMesinPertanianInline,
                    FotoPeralatanMesinPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=13)
        return super(PeralatanMesinPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusPertanianAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinPertanianInline,
                    SKPDAsalPeralatanMesinPertanianInline,
                    FotoPeralatanMesinPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinPertanianAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=13)
        return super(KontrakPeralatanMesinPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=13)



class HargaPeralatanMesinPertanianAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanPertanianAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinPertanianInline, TahunBerkurangPeralatanMesinPertanianInline,
                    SKPDAsalPeralatanMesinPertanianInline,
                    SKPDTujuanPeralatanMesinPertanianInline,
                    FotoPeralatanMesinPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Pertanian
admin.site.register(PeralatanMesinPertanian, PeralatanMesinPertanianAdmin)
admin.site.register(PeralatanMesinUsulHapusPertanian, PeralatanMesinUsulHapusPertanianAdmin)
admin.site.register(KontrakPeralatanMesinPertanian, KontrakPeralatanMesinPertanianAdmin)
admin.site.register(HargaPeralatanMesinPertanian, HargaPeralatanMesinPertanianAdmin)
admin.site.register(PeralatanMesinPenghapusanPertanian, PeralatanMesinPenghapusanPertanianAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanPertanian, KontrakJalanIrigasiJaringanPertanian, HargaJalanIrigasiJaringanPertanian, KDPJalanIrigasiJaringanPertanian, JalanIrigasiJaringanUsulHapusPertanian, TahunBerkurangUsulHapusJalanIrigasiJaringanPertanian

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanPertanian, TahunBerkurangJalanIrigasiJaringanPertanian, PenghapusanJalanIrigasiJaringanPertanian

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanPertanian, SKPDTujuanJalanIrigasiJaringanPertanian, FotoJalanIrigasiJaringanPertanian

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanPertanianInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanPertanian



class PenghapusanJalanIrigasiJaringanPertanianInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanPertanian



class SKPDAsalJalanIrigasiJaringanPertanianInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanPertanian



class SKPDTujuanJalanIrigasiJaringanPertanianInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanPertanian



class FotoJalanIrigasiJaringanPertanianInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanPertanian





class HargaJalanIrigasiJaringanPertanianInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanPertanian

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=13)
        return super(HargaJalanIrigasiJaringanPertanianInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanPertanianInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanPertanian


class JalanIrigasiJaringanPertanianAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPertanianInline,
                    SKPDAsalJalanIrigasiJaringanPertanianInline,
                    FotoJalanIrigasiJaringanPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        return super(JalanIrigasiJaringanPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusPertanianAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanPertanianInline,
                    SKPDAsalJalanIrigasiJaringanPertanianInline,
                    FotoJalanIrigasiJaringanPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanPertanianAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPertanianInline,
                    SKPDAsalJalanIrigasiJaringanPertanianInline,
                    FotoJalanIrigasiJaringanPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        return super(KDPJalanIrigasiJaringanPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanPertanianAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=13)
        return super(KontrakJalanIrigasiJaringanPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=13)



class HargaJalanIrigasiJaringanPertanianAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanPertanianAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanPertanianInline, TahunBerkurangJalanIrigasiJaringanPertanianInline,
                    SKPDAsalJalanIrigasiJaringanPertanianInline,
                    SKPDTujuanJalanIrigasiJaringanPertanianInline,
                    FotoJalanIrigasiJaringanPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Pertanian
admin.site.register(JalanIrigasiJaringanPertanian, JalanIrigasiJaringanPertanianAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusPertanian, JalanIrigasiJaringanUsulHapusPertanianAdmin)
admin.site.register(KDPJalanIrigasiJaringanPertanian, KDPJalanIrigasiJaringanPertanianAdmin)
admin.site.register(KontrakJalanIrigasiJaringanPertanian, KontrakJalanIrigasiJaringanPertanianAdmin)
admin.site.register(HargaJalanIrigasiJaringanPertanian, HargaJalanIrigasiJaringanPertanianAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanPertanian, JalanIrigasiJaringanPenghapusanPertanianAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLPertanian, KontrakATLPertanian, HargaATLPertanian, ATLUsulHapusPertanian, TahunBerkurangUsulHapusATLPertanian

from atl.models import ATLPenghapusanPertanian, TahunBerkurangATLPertanian, PenghapusanATLPertanian

from atl.models import SKPDAsalATLPertanian, SKPDTujuanATLPertanian, FotoATLPertanian

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLPertanianInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLPertanian



class PenghapusanATLPertanianInline(PenghapusanATLInline):
    model = PenghapusanATLPertanian



class SKPDAsalATLPertanianInline(SKPDAsalATLInline):
    model = SKPDAsalATLPertanian



class SKPDTujuanATLPertanianInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLPertanian



class FotoATLPertanianInline(FotoATLInline):
    model = FotoATLPertanian



class HargaATLPertanianInline(HargaATLInline):
    model = HargaATLPertanian

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=13)
        return super(HargaATLPertanianInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLPertanianInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLPertanian


class ATLPertanianAdmin(ATLAdmin):
    inlines = [HargaATLPertanianInline,
                    SKPDAsalATLPertanianInline,
                    FotoATLPertanianInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=13)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=13)
        return super(ATLPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusPertanianAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLPertanianInline,
                    SKPDAsalATLPertanianInline,
                    FotoATLPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLPertanianAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=13)
        return super(KontrakATLPertanianAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=13)



class HargaATLPertanianAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanPertanianAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLPertanianInline, TahunBerkurangATLPertanianInline,
                    SKPDAsalATLPertanianInline,
                    SKPDTujuanATLPertanianInline,
                    FotoATLPertanianInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=13)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Pertanian
admin.site.register(ATLPertanian, ATLPertanianAdmin)
admin.site.register(ATLUsulHapusPertanian, ATLUsulHapusPertanianAdmin)
admin.site.register(KontrakATLPertanian, KontrakATLPertanianAdmin)
admin.site.register(HargaATLPertanian, HargaATLPertanianAdmin)
admin.site.register(ATLPenghapusanPertanian, ATLPenghapusanPertanianAdmin)
