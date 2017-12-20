### $Id: admin.py,v 1.32 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDinkes, KontrakTanahDinkes, HargaTanahDinkes, TanahUsulHapusDinkes, TahunBerkurangUsulHapusTanahDinkes

from umum.models import TanahPenghapusanDinkes, TahunBerkurangTanahDinkes, PenghapusanTanahDinkes

from umum.models import SKPDAsalTanahDinkes, SKPDTujuanTanahDinkes, FotoTanahDinkes

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDinkes, KontrakGedungBangunanDinkes, HargaGedungBangunanDinkes, GedungBangunanRuanganDinkes, GedungBangunanUsulHapusDinkes, TahunBerkurangUsulHapusGedungDinkes

from gedungbangunan.models import GedungBangunanPenghapusanDinkes, TahunBerkurangGedungBangunanDinkes, PenghapusanGedungBangunanDinkes

from gedungbangunan.models import SKPDAsalGedungBangunanDinkes, SKPDTujuanGedungBangunanDinkes, FotoGedungBangunanDinkes

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDinkes, KontrakPeralatanMesinDinkes, HargaPeralatanMesinDinkes, PeralatanMesinUsulHapusDinkes, TahunBerkurangUsulHapusPeralatanMesinDinkes

from peralatanmesin.models import PeralatanMesinPenghapusanDinkes, TahunBerkurangPeralatanMesinDinkes, PenghapusanPeralatanMesinDinkes

from peralatanmesin.models import SKPDAsalPeralatanMesinDinkes, SKPDTujuanPeralatanMesinDinkes, FotoPeralatanMesinDinkes

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDinkesInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDinkes



class PenghapusanTanahDinkesInline(PenghapusanTanahInline):
    model = PenghapusanTanahDinkes



class SKPDAsalTanahDinkesInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDinkes



class SKPDTujuanTanahDinkesInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDinkes



class FotoTanahDinkesInline(FotoTanahInline):
    model = FotoTanahDinkes



class GedungBangunanDinkesInline(GedungBangunanInline):
    model = GedungBangunanDinkes



class HargaTanahDinkesInline(HargaTanahInline):
    model = HargaTanahDinkes

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=5)
        return super(HargaTanahDinkesInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDinkesInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDinkes


class TanahDinkesAdmin(TanahAdmin):
    inlines = [HargaTanahDinkesInline,
                SKPDAsalTanahDinkesInline,
                FotoTanahDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        return super(TanahDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDinkesAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDinkesInline,
                SKPDAsalTanahDinkesInline,
                FotoTanahDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDinkesAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=5)
        return super(KontrakTanahDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=5)



class HargaTanahDinkesAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDinkesAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDinkesInline, TahunBerkurangTanahDinkesInline,
                    SKPDAsalTanahDinkesInline,
                    SKPDTujuanTanahDinkesInline,
                    FotoTanahDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Dinkes
admin.site.register(TanahDinkes, TanahDinkesAdmin)
admin.site.register(TanahUsulHapusDinkes, TanahUsulHapusDinkesAdmin)
admin.site.register(KontrakTanahDinkes, KontrakTanahDinkesAdmin)
admin.site.register(HargaTanahDinkes, HargaTanahDinkesAdmin)
admin.site.register(TanahPenghapusanDinkes, TanahPenghapusanDinkesAdmin)



from gedungbangunan.models import KDPGedungBangunanDinkes


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDinkesInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDinkes



class PenghapusanGedungBangunanDinkesInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDinkes



class SKPDAsalGedungBangunanDinkesInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDinkes



class SKPDTujuanGedungBangunanDinkesInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDinkes



class FotoGedungBangunanDinkesInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDinkes



class HargaGedungBangunanDinkesInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDinkes

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=5)
        return super(HargaGedungBangunanDinkesInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDinkesInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDinkes


class GedungBangunanDinkesAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDinkesInline,
                SKPDAsalGedungBangunanDinkesInline,
                FotoGedungBangunanDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        return super(GedungBangunanDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDinkesAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDinkesInline,
                SKPDAsalGedungBangunanDinkesInline,
                FotoGedungBangunanDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        return super(KDPGedungBangunanDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDinkesAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDinkesAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDinkesInline,
                    SKPDAsalGedungBangunanDinkesInline,
                    FotoGedungBangunanDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDinkesAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=5)
        return super(KontrakGedungBangunanDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=5)



class HargaGedungBangunanDinkesAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDinkesAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDinkesInline, TahunBerkurangGedungBangunanDinkesInline,
                    SKPDAsalGedungBangunanDinkesInline,
                    SKPDTujuanGedungBangunanDinkesInline,
                    FotoGedungBangunanDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Dinkes
admin.site.register(GedungBangunanDinkes, GedungBangunanDinkesAdmin)
admin.site.register(KDPGedungBangunanDinkes, KDPGedungBangunanDinkesAdmin)
admin.site.register(GedungBangunanRuanganDinkes, GedungBangunanRuanganDinkesAdmin)
admin.site.register(GedungBangunanUsulHapusDinkes, GedungBangunanUsulHapusDinkesAdmin)
admin.site.register(KontrakGedungBangunanDinkes, KontrakGedungBangunanDinkesAdmin)
admin.site.register(HargaGedungBangunanDinkes, HargaGedungBangunanDinkesAdmin)
admin.site.register(GedungBangunanPenghapusanDinkes, GedungBangunanPenghapusanDinkesAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDinkesInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDinkes



class PenghapusanPeralatanMesinDinkesInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDinkes



class SKPDAsalPeralatanMesinDinkesInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDinkes



class SKPDTujuanPeralatanMesinDinkesInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDinkes



class FotoPeralatanMesinDinkesInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDinkes



class HargaPeralatanMesinDinkesInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDinkes

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=5)
        return super(HargaPeralatanMesinDinkesInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDinkesInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDinkes


class PeralatanMesinDinkesAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDinkesInline,
                    SKPDAsalPeralatanMesinDinkesInline,
                    FotoPeralatanMesinDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=5)
        return super(PeralatanMesinDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDinkesAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDinkesInline,
                    SKPDAsalPeralatanMesinDinkesInline,
                    FotoPeralatanMesinDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDinkesAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=5)
        return super(KontrakPeralatanMesinDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=5)



class HargaPeralatanMesinDinkesAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDinkesAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDinkesInline, TahunBerkurangPeralatanMesinDinkesInline,
                    SKPDAsalPeralatanMesinDinkesInline,
                    SKPDTujuanPeralatanMesinDinkesInline,
                    FotoPeralatanMesinDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Dinkes
admin.site.register(PeralatanMesinDinkes, PeralatanMesinDinkesAdmin)
admin.site.register(PeralatanMesinUsulHapusDinkes, PeralatanMesinUsulHapusDinkesAdmin)
admin.site.register(KontrakPeralatanMesinDinkes, KontrakPeralatanMesinDinkesAdmin)
admin.site.register(HargaPeralatanMesinDinkes, HargaPeralatanMesinDinkesAdmin)
admin.site.register(PeralatanMesinPenghapusanDinkes, PeralatanMesinPenghapusanDinkesAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDinkes, KontrakJalanIrigasiJaringanDinkes, HargaJalanIrigasiJaringanDinkes, KDPJalanIrigasiJaringanDinkes, JalanIrigasiJaringanUsulHapusDinkes, TahunBerkurangUsulHapusJalanIrigasiJaringanDinkes

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDinkes, TahunBerkurangJalanIrigasiJaringanDinkes, PenghapusanJalanIrigasiJaringanDinkes

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDinkes, SKPDTujuanJalanIrigasiJaringanDinkes, FotoJalanIrigasiJaringanDinkes

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDinkesInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDinkes



class PenghapusanJalanIrigasiJaringanDinkesInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDinkes



class SKPDAsalJalanIrigasiJaringanDinkesInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDinkes



class SKPDTujuanJalanIrigasiJaringanDinkesInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDinkes



class FotoJalanIrigasiJaringanDinkesInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDinkes





class HargaJalanIrigasiJaringanDinkesInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDinkes

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=5)
        return super(HargaJalanIrigasiJaringanDinkesInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDinkesInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDinkes


class JalanIrigasiJaringanDinkesAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDinkesInline,
                    SKPDAsalJalanIrigasiJaringanDinkesInline,
                    FotoJalanIrigasiJaringanDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        return super(JalanIrigasiJaringanDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDinkesAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDinkesInline,
                    SKPDAsalJalanIrigasiJaringanDinkesInline,
                    FotoJalanIrigasiJaringanDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDinkesAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDinkesInline,
                    SKPDAsalJalanIrigasiJaringanDinkesInline,
                    FotoJalanIrigasiJaringanDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        return super(KDPJalanIrigasiJaringanDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDinkesAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=5)
        return super(KontrakJalanIrigasiJaringanDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=5)



class HargaJalanIrigasiJaringanDinkesAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDinkesAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDinkesInline, TahunBerkurangJalanIrigasiJaringanDinkesInline,
                    SKPDAsalJalanIrigasiJaringanDinkesInline,
                    SKPDTujuanJalanIrigasiJaringanDinkesInline,
                    FotoJalanIrigasiJaringanDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Dinkes
admin.site.register(JalanIrigasiJaringanDinkes, JalanIrigasiJaringanDinkesAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDinkes, JalanIrigasiJaringanUsulHapusDinkesAdmin)
admin.site.register(KDPJalanIrigasiJaringanDinkes, KDPJalanIrigasiJaringanDinkesAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDinkes, KontrakJalanIrigasiJaringanDinkesAdmin)
admin.site.register(HargaJalanIrigasiJaringanDinkes, HargaJalanIrigasiJaringanDinkesAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDinkes, JalanIrigasiJaringanPenghapusanDinkesAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDinkes, KontrakATLDinkes, HargaATLDinkes, ATLUsulHapusDinkes, TahunBerkurangUsulHapusATLDinkes

from atl.models import ATLPenghapusanDinkes, TahunBerkurangATLDinkes, PenghapusanATLDinkes

from atl.models import SKPDAsalATLDinkes, SKPDTujuanATLDinkes, FotoATLDinkes

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDinkesInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDinkes



class PenghapusanATLDinkesInline(PenghapusanATLInline):
    model = PenghapusanATLDinkes



class SKPDAsalATLDinkesInline(SKPDAsalATLInline):
    model = SKPDAsalATLDinkes



class SKPDTujuanATLDinkesInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDinkes



class FotoATLDinkesInline(FotoATLInline):
    model = FotoATLDinkes



class HargaATLDinkesInline(HargaATLInline):
    model = HargaATLDinkes

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=5)
        return super(HargaATLDinkesInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDinkesInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDinkes


class ATLDinkesAdmin(ATLAdmin):
    inlines = [HargaATLDinkesInline,
                    SKPDAsalATLDinkesInline,
                    FotoATLDinkesInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=5)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=5)
        return super(ATLDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDinkesAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDinkesInline,
                    SKPDAsalATLDinkesInline,
                    FotoATLDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDinkesAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=5)
        return super(KontrakATLDinkesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=5)



class HargaATLDinkesAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDinkesAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDinkesInline, TahunBerkurangATLDinkesInline,
                    SKPDAsalATLDinkesInline,
                    SKPDTujuanATLDinkesInline,
                    FotoATLDinkesInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=5)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Dinkes
admin.site.register(ATLDinkes, ATLDinkesAdmin)
admin.site.register(ATLUsulHapusDinkes, ATLUsulHapusDinkesAdmin)
admin.site.register(KontrakATLDinkes, KontrakATLDinkesAdmin)
admin.site.register(HargaATLDinkes, HargaATLDinkesAdmin)
admin.site.register(ATLPenghapusanDinkes, ATLPenghapusanDinkesAdmin)
