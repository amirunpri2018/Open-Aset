### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDKUKMP, KontrakTanahDKUKMP, HargaTanahDKUKMP, TanahUsulHapusDKUKMP, TahunBerkurangUsulHapusTanahDKUKMP

from umum.models import TanahPenghapusanDKUKMP, TahunBerkurangTanahDKUKMP, PenghapusanTanahDKUKMP

from umum.models import SKPDAsalTanahDKUKMP, SKPDTujuanTanahDKUKMP, FotoTanahDKUKMP

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDKUKMP, KontrakGedungBangunanDKUKMP, HargaGedungBangunanDKUKMP, GedungBangunanRuanganDKUKMP, GedungBangunanUsulHapusDKUKMP, TahunBerkurangUsulHapusGedungDKUKMP

from gedungbangunan.models import GedungBangunanPenghapusanDKUKMP, TahunBerkurangGedungBangunanDKUKMP, PenghapusanGedungBangunanDKUKMP

from gedungbangunan.models import SKPDAsalGedungBangunanDKUKMP, SKPDTujuanGedungBangunanDKUKMP, FotoGedungBangunanDKUKMP

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDKUKMP, KontrakPeralatanMesinDKUKMP, HargaPeralatanMesinDKUKMP, PeralatanMesinUsulHapusDKUKMP, TahunBerkurangUsulHapusPeralatanMesinDKUKMP

from peralatanmesin.models import PeralatanMesinPenghapusanDKUKMP, TahunBerkurangPeralatanMesinDKUKMP, PenghapusanPeralatanMesinDKUKMP

from peralatanmesin.models import SKPDAsalPeralatanMesinDKUKMP, SKPDTujuanPeralatanMesinDKUKMP, FotoPeralatanMesinDKUKMP

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDKUKMPInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDKUKMP



class PenghapusanTanahDKUKMPInline(PenghapusanTanahInline):
    model = PenghapusanTanahDKUKMP



class SKPDAsalTanahDKUKMPInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDKUKMP



class SKPDTujuanTanahDKUKMPInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDKUKMP



class FotoTanahDKUKMPInline(FotoTanahInline):
    model = FotoTanahDKUKMP



class GedungBangunanDKUKMPInline(GedungBangunanInline):
    model = GedungBangunanDKUKMP



class HargaTanahDKUKMPInline(HargaTanahInline):
    model = HargaTanahDKUKMP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=16)
        return super(HargaTanahDKUKMPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDKUKMPInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDKUKMP


class TanahDKUKMPAdmin(TanahAdmin):
    inlines = [HargaTanahDKUKMPInline,
                SKPDAsalTanahDKUKMPInline,
                FotoTanahDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        return super(TanahDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDKUKMPAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDKUKMPInline,
                SKPDAsalTanahDKUKMPInline,
                FotoTanahDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDKUKMPAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=16)
        return super(KontrakTanahDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=16)



class HargaTanahDKUKMPAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDKUKMPAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDKUKMPInline, TahunBerkurangTanahDKUKMPInline,
                    SKPDAsalTanahDKUKMPInline,
                    SKPDTujuanTanahDKUKMPInline,
                    FotoTanahDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DKUKMP
admin.site.register(TanahDKUKMP, TanahDKUKMPAdmin)
admin.site.register(TanahUsulHapusDKUKMP, TanahUsulHapusDKUKMPAdmin)
admin.site.register(KontrakTanahDKUKMP, KontrakTanahDKUKMPAdmin)
admin.site.register(HargaTanahDKUKMP, HargaTanahDKUKMPAdmin)
admin.site.register(TanahPenghapusanDKUKMP, TanahPenghapusanDKUKMPAdmin)



from gedungbangunan.models import KDPGedungBangunanDKUKMP


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDKUKMPInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDKUKMP



class PenghapusanGedungBangunanDKUKMPInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDKUKMP



class SKPDAsalGedungBangunanDKUKMPInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDKUKMP



class SKPDTujuanGedungBangunanDKUKMPInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDKUKMP



class FotoGedungBangunanDKUKMPInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDKUKMP



class HargaGedungBangunanDKUKMPInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDKUKMP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=16)
        return super(HargaGedungBangunanDKUKMPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDKUKMPInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDKUKMP


class GedungBangunanDKUKMPAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDKUKMPInline,
                SKPDAsalGedungBangunanDKUKMPInline,
                FotoGedungBangunanDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        return super(GedungBangunanDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDKUKMPAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDKUKMPInline,
                SKPDAsalGedungBangunanDKUKMPInline,
                FotoGedungBangunanDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        return super(KDPGedungBangunanDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDKUKMPAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDKUKMPAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDKUKMPInline,
                    SKPDAsalGedungBangunanDKUKMPInline,
                    FotoGedungBangunanDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDKUKMPAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=16)
        return super(KontrakGedungBangunanDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=16)



class HargaGedungBangunanDKUKMPAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDKUKMPAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDKUKMPInline, TahunBerkurangGedungBangunanDKUKMPInline,
                    SKPDAsalGedungBangunanDKUKMPInline,
                    SKPDTujuanGedungBangunanDKUKMPInline,
                    FotoGedungBangunanDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DKUKMP
admin.site.register(GedungBangunanDKUKMP, GedungBangunanDKUKMPAdmin)
admin.site.register(KDPGedungBangunanDKUKMP, KDPGedungBangunanDKUKMPAdmin)
admin.site.register(GedungBangunanRuanganDKUKMP, GedungBangunanRuanganDKUKMPAdmin)
admin.site.register(GedungBangunanUsulHapusDKUKMP, GedungBangunanUsulHapusDKUKMPAdmin)
admin.site.register(KontrakGedungBangunanDKUKMP, KontrakGedungBangunanDKUKMPAdmin)
admin.site.register(HargaGedungBangunanDKUKMP, HargaGedungBangunanDKUKMPAdmin)
admin.site.register(GedungBangunanPenghapusanDKUKMP, GedungBangunanPenghapusanDKUKMPAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDKUKMPInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDKUKMP



class PenghapusanPeralatanMesinDKUKMPInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDKUKMP



class SKPDAsalPeralatanMesinDKUKMPInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDKUKMP



class SKPDTujuanPeralatanMesinDKUKMPInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDKUKMP



class FotoPeralatanMesinDKUKMPInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDKUKMP



class HargaPeralatanMesinDKUKMPInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDKUKMP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=16)
        return super(HargaPeralatanMesinDKUKMPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDKUKMPInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDKUKMP


class PeralatanMesinDKUKMPAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDKUKMPInline,
                    SKPDAsalPeralatanMesinDKUKMPInline,
                    FotoPeralatanMesinDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=16)
        return super(PeralatanMesinDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDKUKMPAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDKUKMPInline,
                    SKPDAsalPeralatanMesinDKUKMPInline,
                    FotoPeralatanMesinDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDKUKMPAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=16)
        return super(KontrakPeralatanMesinDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=16)



class HargaPeralatanMesinDKUKMPAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDKUKMPAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDKUKMPInline, TahunBerkurangPeralatanMesinDKUKMPInline,
                    SKPDAsalPeralatanMesinDKUKMPInline,
                    SKPDTujuanPeralatanMesinDKUKMPInline,
                    FotoPeralatanMesinDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DKUKMP
admin.site.register(PeralatanMesinDKUKMP, PeralatanMesinDKUKMPAdmin)
admin.site.register(PeralatanMesinUsulHapusDKUKMP, PeralatanMesinUsulHapusDKUKMPAdmin)
admin.site.register(KontrakPeralatanMesinDKUKMP, KontrakPeralatanMesinDKUKMPAdmin)
admin.site.register(HargaPeralatanMesinDKUKMP, HargaPeralatanMesinDKUKMPAdmin)
admin.site.register(PeralatanMesinPenghapusanDKUKMP, PeralatanMesinPenghapusanDKUKMPAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDKUKMP, KontrakJalanIrigasiJaringanDKUKMP, HargaJalanIrigasiJaringanDKUKMP, KDPJalanIrigasiJaringanDKUKMP, JalanIrigasiJaringanUsulHapusDKUKMP, TahunBerkurangUsulHapusJalanIrigasiJaringanDKUKMP

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDKUKMP, TahunBerkurangJalanIrigasiJaringanDKUKMP, PenghapusanJalanIrigasiJaringanDKUKMP

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDKUKMP, SKPDTujuanJalanIrigasiJaringanDKUKMP, FotoJalanIrigasiJaringanDKUKMP

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDKUKMPInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDKUKMP



class PenghapusanJalanIrigasiJaringanDKUKMPInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDKUKMP



class SKPDAsalJalanIrigasiJaringanDKUKMPInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDKUKMP



class SKPDTujuanJalanIrigasiJaringanDKUKMPInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDKUKMP



class FotoJalanIrigasiJaringanDKUKMPInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDKUKMP





class HargaJalanIrigasiJaringanDKUKMPInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDKUKMP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=16)
        return super(HargaJalanIrigasiJaringanDKUKMPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDKUKMPInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDKUKMP


class JalanIrigasiJaringanDKUKMPAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDKUKMPInline,
                    SKPDAsalJalanIrigasiJaringanDKUKMPInline,
                    FotoJalanIrigasiJaringanDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        return super(JalanIrigasiJaringanDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDKUKMPAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDKUKMPInline,
                    SKPDAsalJalanIrigasiJaringanDKUKMPInline,
                    FotoJalanIrigasiJaringanDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDKUKMPAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDKUKMPInline,
                    SKPDAsalJalanIrigasiJaringanDKUKMPInline,
                    FotoJalanIrigasiJaringanDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        return super(KDPJalanIrigasiJaringanDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDKUKMPAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=16)
        return super(KontrakJalanIrigasiJaringanDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=16)



class HargaJalanIrigasiJaringanDKUKMPAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDKUKMPAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDKUKMPInline, TahunBerkurangJalanIrigasiJaringanDKUKMPInline,
                    SKPDAsalJalanIrigasiJaringanDKUKMPInline,
                    SKPDTujuanJalanIrigasiJaringanDKUKMPInline,
                    FotoJalanIrigasiJaringanDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DKUKMP
admin.site.register(JalanIrigasiJaringanDKUKMP, JalanIrigasiJaringanDKUKMPAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDKUKMP, JalanIrigasiJaringanUsulHapusDKUKMPAdmin)
admin.site.register(KDPJalanIrigasiJaringanDKUKMP, KDPJalanIrigasiJaringanDKUKMPAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDKUKMP, KontrakJalanIrigasiJaringanDKUKMPAdmin)
admin.site.register(HargaJalanIrigasiJaringanDKUKMP, HargaJalanIrigasiJaringanDKUKMPAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDKUKMP, JalanIrigasiJaringanPenghapusanDKUKMPAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDKUKMP, KontrakATLDKUKMP, HargaATLDKUKMP, ATLUsulHapusDKUKMP, TahunBerkurangUsulHapusATLDKUKMP

from atl.models import ATLPenghapusanDKUKMP, TahunBerkurangATLDKUKMP, PenghapusanATLDKUKMP

from atl.models import SKPDAsalATLDKUKMP, SKPDTujuanATLDKUKMP, FotoATLDKUKMP

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDKUKMPInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDKUKMP



class PenghapusanATLDKUKMPInline(PenghapusanATLInline):
    model = PenghapusanATLDKUKMP



class SKPDAsalATLDKUKMPInline(SKPDAsalATLInline):
    model = SKPDAsalATLDKUKMP



class SKPDTujuanATLDKUKMPInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDKUKMP



class FotoATLDKUKMPInline(FotoATLInline):
    model = FotoATLDKUKMP



class HargaATLDKUKMPInline(HargaATLInline):
    model = HargaATLDKUKMP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=16)
        return super(HargaATLDKUKMPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDKUKMPInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDKUKMP


class ATLDKUKMPAdmin(ATLAdmin):
    inlines = [HargaATLDKUKMPInline,
                    SKPDAsalATLDKUKMPInline,
                    FotoATLDKUKMPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=16)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=16)
        return super(ATLDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDKUKMPAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDKUKMPInline,
                    SKPDAsalATLDKUKMPInline,
                    FotoATLDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDKUKMPAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=16)
        return super(KontrakATLDKUKMPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=16)



class HargaATLDKUKMPAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDKUKMPAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDKUKMPInline, TahunBerkurangATLDKUKMPInline,
                    SKPDAsalATLDKUKMPInline,
                    SKPDTujuanATLDKUKMPInline,
                    FotoATLDKUKMPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=16)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DKUKMP
admin.site.register(ATLDKUKMP, ATLDKUKMPAdmin)
admin.site.register(ATLUsulHapusDKUKMP, ATLUsulHapusDKUKMPAdmin)
admin.site.register(KontrakATLDKUKMP, KontrakATLDKUKMPAdmin)
admin.site.register(HargaATLDKUKMP, HargaATLDKUKMPAdmin)
admin.site.register(ATLPenghapusanDKUKMP, ATLPenghapusanDKUKMPAdmin)
