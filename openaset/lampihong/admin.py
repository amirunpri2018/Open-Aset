### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahLampihong, KontrakTanahLampihong, HargaTanahLampihong, TanahUsulHapusLampihong, TahunBerkurangUsulHapusTanahLampihong

from umum.models import TanahPenghapusanLampihong, TahunBerkurangTanahLampihong, PenghapusanTanahLampihong

from umum.models import SKPDAsalTanahLampihong, SKPDTujuanTanahLampihong, FotoTanahLampihong

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanLampihong, KontrakGedungBangunanLampihong, HargaGedungBangunanLampihong, GedungBangunanRuanganLampihong, GedungBangunanUsulHapusLampihong, TahunBerkurangUsulHapusGedungLampihong

from gedungbangunan.models import GedungBangunanPenghapusanLampihong, TahunBerkurangGedungBangunanLampihong, PenghapusanGedungBangunanLampihong

from gedungbangunan.models import SKPDAsalGedungBangunanLampihong, SKPDTujuanGedungBangunanLampihong, FotoGedungBangunanLampihong

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinLampihong, KontrakPeralatanMesinLampihong, HargaPeralatanMesinLampihong, PeralatanMesinUsulHapusLampihong, TahunBerkurangUsulHapusPeralatanMesinLampihong

from peralatanmesin.models import PeralatanMesinPenghapusanLampihong, TahunBerkurangPeralatanMesinLampihong, PenghapusanPeralatanMesinLampihong

from peralatanmesin.models import SKPDAsalPeralatanMesinLampihong, SKPDTujuanPeralatanMesinLampihong, FotoPeralatanMesinLampihong

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahLampihongInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahLampihong



class PenghapusanTanahLampihongInline(PenghapusanTanahInline):
    model = PenghapusanTanahLampihong



class SKPDAsalTanahLampihongInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahLampihong



class SKPDTujuanTanahLampihongInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahLampihong



class FotoTanahLampihongInline(FotoTanahInline):
    model = FotoTanahLampihong



class GedungBangunanLampihongInline(GedungBangunanInline):
    model = GedungBangunanLampihong



class HargaTanahLampihongInline(HargaTanahInline):
    model = HargaTanahLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=31)
        return super(HargaTanahLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahLampihongInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahLampihong


class TanahLampihongAdmin(TanahAdmin):
    inlines = [HargaTanahLampihongInline,
                SKPDAsalTanahLampihongInline,
                FotoTanahLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        return super(TanahLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusLampihongAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahLampihongInline,
                SKPDAsalTanahLampihongInline,
                FotoTanahLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahLampihongAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=31)
        return super(KontrakTanahLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=31)



class HargaTanahLampihongAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanLampihongAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahLampihongInline, TahunBerkurangTanahLampihongInline,
                    SKPDAsalTanahLampihongInline,
                    SKPDTujuanTanahLampihongInline,
                    FotoTanahLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Lampihong
admin.site.register(TanahLampihong, TanahLampihongAdmin)
admin.site.register(TanahUsulHapusLampihong, TanahUsulHapusLampihongAdmin)
admin.site.register(KontrakTanahLampihong, KontrakTanahLampihongAdmin)
admin.site.register(HargaTanahLampihong, HargaTanahLampihongAdmin)
admin.site.register(TanahPenghapusanLampihong, TanahPenghapusanLampihongAdmin)



from gedungbangunan.models import KDPGedungBangunanLampihong


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanLampihongInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanLampihong



class PenghapusanGedungBangunanLampihongInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanLampihong



class SKPDAsalGedungBangunanLampihongInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanLampihong



class SKPDTujuanGedungBangunanLampihongInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanLampihong



class FotoGedungBangunanLampihongInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanLampihong



class HargaGedungBangunanLampihongInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=31)
        return super(HargaGedungBangunanLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungLampihongInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungLampihong


class GedungBangunanLampihongAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanLampihongInline,
                SKPDAsalGedungBangunanLampihongInline,
                FotoGedungBangunanLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        return super(GedungBangunanLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanLampihongAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanLampihongInline,
                SKPDAsalGedungBangunanLampihongInline,
                FotoGedungBangunanLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        return super(KDPGedungBangunanLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganLampihongAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusLampihongAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungLampihongInline,
                    SKPDAsalGedungBangunanLampihongInline,
                    FotoGedungBangunanLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanLampihongAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=31)
        return super(KontrakGedungBangunanLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=31)



class HargaGedungBangunanLampihongAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanLampihongAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanLampihongInline, TahunBerkurangGedungBangunanLampihongInline,
                    SKPDAsalGedungBangunanLampihongInline,
                    SKPDTujuanGedungBangunanLampihongInline,
                    FotoGedungBangunanLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Lampihong
admin.site.register(GedungBangunanLampihong, GedungBangunanLampihongAdmin)
admin.site.register(KDPGedungBangunanLampihong, KDPGedungBangunanLampihongAdmin)
admin.site.register(GedungBangunanRuanganLampihong, GedungBangunanRuanganLampihongAdmin)
admin.site.register(GedungBangunanUsulHapusLampihong, GedungBangunanUsulHapusLampihongAdmin)
admin.site.register(KontrakGedungBangunanLampihong, KontrakGedungBangunanLampihongAdmin)
admin.site.register(HargaGedungBangunanLampihong, HargaGedungBangunanLampihongAdmin)
admin.site.register(GedungBangunanPenghapusanLampihong, GedungBangunanPenghapusanLampihongAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinLampihongInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinLampihong



class PenghapusanPeralatanMesinLampihongInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinLampihong



class SKPDAsalPeralatanMesinLampihongInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinLampihong



class SKPDTujuanPeralatanMesinLampihongInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinLampihong



class FotoPeralatanMesinLampihongInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinLampihong



class HargaPeralatanMesinLampihongInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=31)
        return super(HargaPeralatanMesinLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinLampihongInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinLampihong


class PeralatanMesinLampihongAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinLampihongInline,
                    SKPDAsalPeralatanMesinLampihongInline,
                    FotoPeralatanMesinLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=31)
        return super(PeralatanMesinLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusLampihongAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinLampihongInline,
                    SKPDAsalPeralatanMesinLampihongInline,
                    FotoPeralatanMesinLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinLampihongAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=31)
        return super(KontrakPeralatanMesinLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=31)



class HargaPeralatanMesinLampihongAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanLampihongAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinLampihongInline, TahunBerkurangPeralatanMesinLampihongInline,
                    SKPDAsalPeralatanMesinLampihongInline,
                    SKPDTujuanPeralatanMesinLampihongInline,
                    FotoPeralatanMesinLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Lampihong
admin.site.register(PeralatanMesinLampihong, PeralatanMesinLampihongAdmin)
admin.site.register(PeralatanMesinUsulHapusLampihong, PeralatanMesinUsulHapusLampihongAdmin)
admin.site.register(KontrakPeralatanMesinLampihong, KontrakPeralatanMesinLampihongAdmin)
admin.site.register(HargaPeralatanMesinLampihong, HargaPeralatanMesinLampihongAdmin)
admin.site.register(PeralatanMesinPenghapusanLampihong, PeralatanMesinPenghapusanLampihongAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanLampihong, KontrakJalanIrigasiJaringanLampihong, HargaJalanIrigasiJaringanLampihong, KDPJalanIrigasiJaringanLampihong, JalanIrigasiJaringanUsulHapusLampihong, TahunBerkurangUsulHapusJalanIrigasiJaringanLampihong

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanLampihong, TahunBerkurangJalanIrigasiJaringanLampihong, PenghapusanJalanIrigasiJaringanLampihong

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanLampihong, SKPDTujuanJalanIrigasiJaringanLampihong, FotoJalanIrigasiJaringanLampihong

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanLampihongInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanLampihong



class PenghapusanJalanIrigasiJaringanLampihongInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanLampihong



class SKPDAsalJalanIrigasiJaringanLampihongInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanLampihong



class SKPDTujuanJalanIrigasiJaringanLampihongInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanLampihong



class FotoJalanIrigasiJaringanLampihongInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanLampihong





class HargaJalanIrigasiJaringanLampihongInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=31)
        return super(HargaJalanIrigasiJaringanLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanLampihongInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanLampihong


class JalanIrigasiJaringanLampihongAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanLampihongInline,
                    SKPDAsalJalanIrigasiJaringanLampihongInline,
                    FotoJalanIrigasiJaringanLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        return super(JalanIrigasiJaringanLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusLampihongAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanLampihongInline,
                    SKPDAsalJalanIrigasiJaringanLampihongInline,
                    FotoJalanIrigasiJaringanLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanLampihongAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanLampihongInline,
                    SKPDAsalJalanIrigasiJaringanLampihongInline,
                    FotoJalanIrigasiJaringanLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        return super(KDPJalanIrigasiJaringanLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanLampihongAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=31)
        return super(KontrakJalanIrigasiJaringanLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=31)



class HargaJalanIrigasiJaringanLampihongAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanLampihongAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanLampihongInline, TahunBerkurangJalanIrigasiJaringanLampihongInline,
                    SKPDAsalJalanIrigasiJaringanLampihongInline,
                    SKPDTujuanJalanIrigasiJaringanLampihongInline,
                    FotoJalanIrigasiJaringanLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Lampihong
admin.site.register(JalanIrigasiJaringanLampihong, JalanIrigasiJaringanLampihongAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusLampihong, JalanIrigasiJaringanUsulHapusLampihongAdmin)
admin.site.register(KDPJalanIrigasiJaringanLampihong, KDPJalanIrigasiJaringanLampihongAdmin)
admin.site.register(KontrakJalanIrigasiJaringanLampihong, KontrakJalanIrigasiJaringanLampihongAdmin)
admin.site.register(HargaJalanIrigasiJaringanLampihong, HargaJalanIrigasiJaringanLampihongAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanLampihong, JalanIrigasiJaringanPenghapusanLampihongAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLLampihong, KontrakATLLampihong, HargaATLLampihong, ATLUsulHapusLampihong, TahunBerkurangUsulHapusATLLampihong

from atl.models import ATLPenghapusanLampihong, TahunBerkurangATLLampihong, PenghapusanATLLampihong

from atl.models import SKPDAsalATLLampihong, SKPDTujuanATLLampihong, FotoATLLampihong

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLLampihongInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLLampihong



class PenghapusanATLLampihongInline(PenghapusanATLInline):
    model = PenghapusanATLLampihong



class SKPDAsalATLLampihongInline(SKPDAsalATLInline):
    model = SKPDAsalATLLampihong



class SKPDTujuanATLLampihongInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLLampihong



class FotoATLLampihongInline(FotoATLInline):
    model = FotoATLLampihong



class HargaATLLampihongInline(HargaATLInline):
    model = HargaATLLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=31)
        return super(HargaATLLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLLampihongInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLLampihong


class ATLLampihongAdmin(ATLAdmin):
    inlines = [HargaATLLampihongInline,
                    SKPDAsalATLLampihongInline,
                    FotoATLLampihongInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=31)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=31)
        return super(ATLLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusLampihongAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLLampihongInline,
                    SKPDAsalATLLampihongInline,
                    FotoATLLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLLampihongAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=31)
        return super(KontrakATLLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=31)



class HargaATLLampihongAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanLampihongAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLLampihongInline, TahunBerkurangATLLampihongInline,
                    SKPDAsalATLLampihongInline,
                    SKPDTujuanATLLampihongInline,
                    FotoATLLampihongInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=31)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Lampihong
admin.site.register(ATLLampihong, ATLLampihongAdmin)
admin.site.register(ATLUsulHapusLampihong, ATLUsulHapusLampihongAdmin)
admin.site.register(KontrakATLLampihong, KontrakATLLampihongAdmin)
admin.site.register(HargaATLLampihong, HargaATLLampihongAdmin)
admin.site.register(ATLPenghapusanLampihong, ATLPenghapusanLampihongAdmin)
