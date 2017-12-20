### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDistamben, KontrakTanahDistamben, HargaTanahDistamben, TanahUsulHapusDistamben, TahunBerkurangUsulHapusTanahDistamben

from umum.models import TanahPenghapusanDistamben, TahunBerkurangTanahDistamben, PenghapusanTanahDistamben

from umum.models import SKPDAsalTanahDistamben, SKPDTujuanTanahDistamben, FotoTanahDistamben

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDistamben, KontrakGedungBangunanDistamben, HargaGedungBangunanDistamben, GedungBangunanRuanganDistamben, GedungBangunanUsulHapusDistamben, TahunBerkurangUsulHapusGedungDistamben

from gedungbangunan.models import GedungBangunanPenghapusanDistamben, TahunBerkurangGedungBangunanDistamben, PenghapusanGedungBangunanDistamben

from gedungbangunan.models import SKPDAsalGedungBangunanDistamben, SKPDTujuanGedungBangunanDistamben, FotoGedungBangunanDistamben

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDistamben, KontrakPeralatanMesinDistamben, HargaPeralatanMesinDistamben, PeralatanMesinUsulHapusDistamben, TahunBerkurangUsulHapusPeralatanMesinDistamben

from peralatanmesin.models import PeralatanMesinPenghapusanDistamben, TahunBerkurangPeralatanMesinDistamben, PenghapusanPeralatanMesinDistamben

from peralatanmesin.models import SKPDAsalPeralatanMesinDistamben, SKPDTujuanPeralatanMesinDistamben, FotoPeralatanMesinDistamben

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDistambenInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDistamben



class PenghapusanTanahDistambenInline(PenghapusanTanahInline):
    model = PenghapusanTanahDistamben



class SKPDAsalTanahDistambenInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDistamben



class SKPDTujuanTanahDistambenInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDistamben



class FotoTanahDistambenInline(FotoTanahInline):
    model = FotoTanahDistamben



class GedungBangunanDistambenInline(GedungBangunanInline):
    model = GedungBangunanDistamben



class HargaTanahDistambenInline(HargaTanahInline):
    model = HargaTanahDistamben

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=17)
        return super(HargaTanahDistambenInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDistambenInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDistamben


class TanahDistambenAdmin(TanahAdmin):
    inlines = [HargaTanahDistambenInline,
                SKPDAsalTanahDistambenInline,
                FotoTanahDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        return super(TanahDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDistambenAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDistambenInline,
                SKPDAsalTanahDistambenInline,
                FotoTanahDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDistambenAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=17)
        return super(KontrakTanahDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=17)



class HargaTanahDistambenAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDistambenAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDistambenInline, TahunBerkurangTanahDistambenInline,
                    SKPDAsalTanahDistambenInline,
                    SKPDTujuanTanahDistambenInline,
                    FotoTanahDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Distamben
admin.site.register(TanahDistamben, TanahDistambenAdmin)
admin.site.register(TanahUsulHapusDistamben, TanahUsulHapusDistambenAdmin)
admin.site.register(KontrakTanahDistamben, KontrakTanahDistambenAdmin)
admin.site.register(HargaTanahDistamben, HargaTanahDistambenAdmin)
admin.site.register(TanahPenghapusanDistamben, TanahPenghapusanDistambenAdmin)



from gedungbangunan.models import KDPGedungBangunanDistamben


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDistambenInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDistamben



class PenghapusanGedungBangunanDistambenInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDistamben



class SKPDAsalGedungBangunanDistambenInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDistamben



class SKPDTujuanGedungBangunanDistambenInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDistamben



class FotoGedungBangunanDistambenInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDistamben



class HargaGedungBangunanDistambenInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDistamben

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=17)
        return super(HargaGedungBangunanDistambenInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDistambenInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDistamben


class GedungBangunanDistambenAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDistambenInline,
                SKPDAsalGedungBangunanDistambenInline,
                FotoGedungBangunanDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        return super(GedungBangunanDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDistambenAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDistambenInline,
                SKPDAsalGedungBangunanDistambenInline,
                FotoGedungBangunanDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        return super(KDPGedungBangunanDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDistambenAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDistambenAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDistambenInline,
                    SKPDAsalGedungBangunanDistambenInline,
                    FotoGedungBangunanDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDistambenAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=17)
        return super(KontrakGedungBangunanDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=17)



class HargaGedungBangunanDistambenAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDistambenAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDistambenInline, TahunBerkurangGedungBangunanDistambenInline,
                    SKPDAsalGedungBangunanDistambenInline,
                    SKPDTujuanGedungBangunanDistambenInline,
                    FotoGedungBangunanDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Distamben
admin.site.register(GedungBangunanDistamben, GedungBangunanDistambenAdmin)
admin.site.register(KDPGedungBangunanDistamben, KDPGedungBangunanDistambenAdmin)
admin.site.register(GedungBangunanRuanganDistamben, GedungBangunanRuanganDistambenAdmin)
admin.site.register(GedungBangunanUsulHapusDistamben, GedungBangunanUsulHapusDistambenAdmin)
admin.site.register(KontrakGedungBangunanDistamben, KontrakGedungBangunanDistambenAdmin)
admin.site.register(HargaGedungBangunanDistamben, HargaGedungBangunanDistambenAdmin)
admin.site.register(GedungBangunanPenghapusanDistamben, GedungBangunanPenghapusanDistambenAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDistambenInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDistamben



class PenghapusanPeralatanMesinDistambenInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDistamben



class SKPDAsalPeralatanMesinDistambenInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDistamben



class SKPDTujuanPeralatanMesinDistambenInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDistamben



class FotoPeralatanMesinDistambenInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDistamben



class HargaPeralatanMesinDistambenInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDistamben

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=17)
        return super(HargaPeralatanMesinDistambenInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDistambenInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDistamben


class PeralatanMesinDistambenAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDistambenInline,
                    SKPDAsalPeralatanMesinDistambenInline,
                    FotoPeralatanMesinDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=17)
        return super(PeralatanMesinDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDistambenAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDistambenInline,
                    SKPDAsalPeralatanMesinDistambenInline,
                    FotoPeralatanMesinDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDistambenAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=17)
        return super(KontrakPeralatanMesinDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=17)



class HargaPeralatanMesinDistambenAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDistambenAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDistambenInline, TahunBerkurangPeralatanMesinDistambenInline,
                    SKPDAsalPeralatanMesinDistambenInline,
                    SKPDTujuanPeralatanMesinDistambenInline,
                    FotoPeralatanMesinDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Distamben
admin.site.register(PeralatanMesinDistamben, PeralatanMesinDistambenAdmin)
admin.site.register(PeralatanMesinUsulHapusDistamben, PeralatanMesinUsulHapusDistambenAdmin)
admin.site.register(KontrakPeralatanMesinDistamben, KontrakPeralatanMesinDistambenAdmin)
admin.site.register(HargaPeralatanMesinDistamben, HargaPeralatanMesinDistambenAdmin)
admin.site.register(PeralatanMesinPenghapusanDistamben, PeralatanMesinPenghapusanDistambenAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDistamben, KontrakJalanIrigasiJaringanDistamben, HargaJalanIrigasiJaringanDistamben, KDPJalanIrigasiJaringanDistamben, JalanIrigasiJaringanUsulHapusDistamben, TahunBerkurangUsulHapusJalanIrigasiJaringanDistamben

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDistamben, TahunBerkurangJalanIrigasiJaringanDistamben, PenghapusanJalanIrigasiJaringanDistamben

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDistamben, SKPDTujuanJalanIrigasiJaringanDistamben, FotoJalanIrigasiJaringanDistamben

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDistambenInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDistamben



class PenghapusanJalanIrigasiJaringanDistambenInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDistamben



class SKPDAsalJalanIrigasiJaringanDistambenInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDistamben



class SKPDTujuanJalanIrigasiJaringanDistambenInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDistamben



class FotoJalanIrigasiJaringanDistambenInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDistamben





class HargaJalanIrigasiJaringanDistambenInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDistamben

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=17)
        return super(HargaJalanIrigasiJaringanDistambenInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDistambenInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDistamben


class JalanIrigasiJaringanDistambenAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDistambenInline,
                    SKPDAsalJalanIrigasiJaringanDistambenInline,
                    FotoJalanIrigasiJaringanDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        return super(JalanIrigasiJaringanDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDistambenAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDistambenInline,
                    SKPDAsalJalanIrigasiJaringanDistambenInline,
                    FotoJalanIrigasiJaringanDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDistambenAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDistambenInline,
                    SKPDAsalJalanIrigasiJaringanDistambenInline,
                    FotoJalanIrigasiJaringanDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        return super(KDPJalanIrigasiJaringanDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDistambenAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=17)
        return super(KontrakJalanIrigasiJaringanDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=17)



class HargaJalanIrigasiJaringanDistambenAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDistambenAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDistambenInline, TahunBerkurangJalanIrigasiJaringanDistambenInline,
                    SKPDAsalJalanIrigasiJaringanDistambenInline,
                    SKPDTujuanJalanIrigasiJaringanDistambenInline,
                    FotoJalanIrigasiJaringanDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Distamben
admin.site.register(JalanIrigasiJaringanDistamben, JalanIrigasiJaringanDistambenAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDistamben, JalanIrigasiJaringanUsulHapusDistambenAdmin)
admin.site.register(KDPJalanIrigasiJaringanDistamben, KDPJalanIrigasiJaringanDistambenAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDistamben, KontrakJalanIrigasiJaringanDistambenAdmin)
admin.site.register(HargaJalanIrigasiJaringanDistamben, HargaJalanIrigasiJaringanDistambenAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDistamben, JalanIrigasiJaringanPenghapusanDistambenAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDistamben, KontrakATLDistamben, HargaATLDistamben, ATLUsulHapusDistamben, TahunBerkurangUsulHapusATLDistamben

from atl.models import ATLPenghapusanDistamben, TahunBerkurangATLDistamben, PenghapusanATLDistamben

from atl.models import SKPDAsalATLDistamben, SKPDTujuanATLDistamben, FotoATLDistamben

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDistambenInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDistamben



class PenghapusanATLDistambenInline(PenghapusanATLInline):
    model = PenghapusanATLDistamben



class SKPDAsalATLDistambenInline(SKPDAsalATLInline):
    model = SKPDAsalATLDistamben



class SKPDTujuanATLDistambenInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDistamben



class FotoATLDistambenInline(FotoATLInline):
    model = FotoATLDistamben



class HargaATLDistambenInline(HargaATLInline):
    model = HargaATLDistamben

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=17)
        return super(HargaATLDistambenInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDistambenInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDistamben


class ATLDistambenAdmin(ATLAdmin):
    inlines = [HargaATLDistambenInline,
                    SKPDAsalATLDistambenInline,
                    FotoATLDistambenInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=17)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=17)
        return super(ATLDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDistambenAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDistambenInline,
                    SKPDAsalATLDistambenInline,
                    FotoATLDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDistambenAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=17)
        return super(KontrakATLDistambenAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=17)



class HargaATLDistambenAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDistambenAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDistambenInline, TahunBerkurangATLDistambenInline,
                    SKPDAsalATLDistambenInline,
                    SKPDTujuanATLDistambenInline,
                    FotoATLDistambenInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=17)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Distamben
admin.site.register(ATLDistamben, ATLDistambenAdmin)
admin.site.register(ATLUsulHapusDistamben, ATLUsulHapusDistambenAdmin)
admin.site.register(KontrakATLDistamben, KontrakATLDistambenAdmin)
admin.site.register(HargaATLDistamben, HargaATLDistambenAdmin)
admin.site.register(ATLPenghapusanDistamben, ATLPenghapusanDistambenAdmin)
