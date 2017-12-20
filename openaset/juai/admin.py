### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahJuai, KontrakTanahJuai, HargaTanahJuai, TanahUsulHapusJuai, TahunBerkurangUsulHapusTanahJuai

from umum.models import TanahPenghapusanJuai, TahunBerkurangTanahJuai, PenghapusanTanahJuai

from umum.models import SKPDAsalTanahJuai, SKPDTujuanTanahJuai, FotoTanahJuai

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanJuai, KontrakGedungBangunanJuai, HargaGedungBangunanJuai, GedungBangunanRuanganJuai, GedungBangunanUsulHapusJuai, TahunBerkurangUsulHapusGedungJuai

from gedungbangunan.models import GedungBangunanPenghapusanJuai, TahunBerkurangGedungBangunanJuai, PenghapusanGedungBangunanJuai

from gedungbangunan.models import SKPDAsalGedungBangunanJuai, SKPDTujuanGedungBangunanJuai, FotoGedungBangunanJuai

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinJuai, KontrakPeralatanMesinJuai, HargaPeralatanMesinJuai, PeralatanMesinUsulHapusJuai, TahunBerkurangUsulHapusPeralatanMesinJuai

from peralatanmesin.models import PeralatanMesinPenghapusanJuai, TahunBerkurangPeralatanMesinJuai, PenghapusanPeralatanMesinJuai

from peralatanmesin.models import SKPDAsalPeralatanMesinJuai, SKPDTujuanPeralatanMesinJuai, FotoPeralatanMesinJuai

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahJuaiInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahJuai



class PenghapusanTanahJuaiInline(PenghapusanTanahInline):
    model = PenghapusanTanahJuai



class SKPDAsalTanahJuaiInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahJuai



class SKPDTujuanTanahJuaiInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahJuai



class FotoTanahJuaiInline(FotoTanahInline):
    model = FotoTanahJuai



class GedungBangunanJuaiInline(GedungBangunanInline):
    model = GedungBangunanJuai



class HargaTanahJuaiInline(HargaTanahInline):
    model = HargaTanahJuai

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=33)
        return super(HargaTanahJuaiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahJuaiInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahJuai


class TanahJuaiAdmin(TanahAdmin):
    inlines = [HargaTanahJuaiInline,
                SKPDAsalTanahJuaiInline,
                FotoTanahJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        return super(TanahJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusJuaiAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahJuaiInline,
                SKPDAsalTanahJuaiInline,
                FotoTanahJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahJuaiAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=33)
        return super(KontrakTanahJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=33)



class HargaTanahJuaiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanJuaiAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahJuaiInline, TahunBerkurangTanahJuaiInline,
                    SKPDAsalTanahJuaiInline,
                    SKPDTujuanTanahJuaiInline,
                    FotoTanahJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Juai
admin.site.register(TanahJuai, TanahJuaiAdmin)
admin.site.register(TanahUsulHapusJuai, TanahUsulHapusJuaiAdmin)
admin.site.register(KontrakTanahJuai, KontrakTanahJuaiAdmin)
admin.site.register(HargaTanahJuai, HargaTanahJuaiAdmin)
admin.site.register(TanahPenghapusanJuai, TanahPenghapusanJuaiAdmin)



from gedungbangunan.models import KDPGedungBangunanJuai


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanJuaiInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanJuai



class PenghapusanGedungBangunanJuaiInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanJuai



class SKPDAsalGedungBangunanJuaiInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanJuai



class SKPDTujuanGedungBangunanJuaiInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanJuai



class FotoGedungBangunanJuaiInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanJuai



class HargaGedungBangunanJuaiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanJuai

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=33)
        return super(HargaGedungBangunanJuaiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungJuaiInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungJuai


class GedungBangunanJuaiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanJuaiInline,
                SKPDAsalGedungBangunanJuaiInline,
                FotoGedungBangunanJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        return super(GedungBangunanJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanJuaiAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanJuaiInline,
                SKPDAsalGedungBangunanJuaiInline,
                FotoGedungBangunanJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        return super(KDPGedungBangunanJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganJuaiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusJuaiAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungJuaiInline,
                    SKPDAsalGedungBangunanJuaiInline,
                    FotoGedungBangunanJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanJuaiAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=33)
        return super(KontrakGedungBangunanJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=33)



class HargaGedungBangunanJuaiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanJuaiAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanJuaiInline, TahunBerkurangGedungBangunanJuaiInline,
                    SKPDAsalGedungBangunanJuaiInline,
                    SKPDTujuanGedungBangunanJuaiInline,
                    FotoGedungBangunanJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Juai
admin.site.register(GedungBangunanJuai, GedungBangunanJuaiAdmin)
admin.site.register(KDPGedungBangunanJuai, KDPGedungBangunanJuaiAdmin)
admin.site.register(GedungBangunanRuanganJuai, GedungBangunanRuanganJuaiAdmin)
admin.site.register(GedungBangunanUsulHapusJuai, GedungBangunanUsulHapusJuaiAdmin)
admin.site.register(KontrakGedungBangunanJuai, KontrakGedungBangunanJuaiAdmin)
admin.site.register(HargaGedungBangunanJuai, HargaGedungBangunanJuaiAdmin)
admin.site.register(GedungBangunanPenghapusanJuai, GedungBangunanPenghapusanJuaiAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinJuaiInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinJuai



class PenghapusanPeralatanMesinJuaiInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinJuai



class SKPDAsalPeralatanMesinJuaiInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinJuai



class SKPDTujuanPeralatanMesinJuaiInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinJuai



class FotoPeralatanMesinJuaiInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinJuai



class HargaPeralatanMesinJuaiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinJuai

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=33)
        return super(HargaPeralatanMesinJuaiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinJuaiInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinJuai


class PeralatanMesinJuaiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinJuaiInline,
                    SKPDAsalPeralatanMesinJuaiInline,
                    FotoPeralatanMesinJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=33)
        return super(PeralatanMesinJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusJuaiAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinJuaiInline,
                    SKPDAsalPeralatanMesinJuaiInline,
                    FotoPeralatanMesinJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinJuaiAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=33)
        return super(KontrakPeralatanMesinJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=33)



class HargaPeralatanMesinJuaiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanJuaiAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinJuaiInline, TahunBerkurangPeralatanMesinJuaiInline,
                    SKPDAsalPeralatanMesinJuaiInline,
                    SKPDTujuanPeralatanMesinJuaiInline,
                    FotoPeralatanMesinJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Juai
admin.site.register(PeralatanMesinJuai, PeralatanMesinJuaiAdmin)
admin.site.register(PeralatanMesinUsulHapusJuai, PeralatanMesinUsulHapusJuaiAdmin)
admin.site.register(KontrakPeralatanMesinJuai, KontrakPeralatanMesinJuaiAdmin)
admin.site.register(HargaPeralatanMesinJuai, HargaPeralatanMesinJuaiAdmin)
admin.site.register(PeralatanMesinPenghapusanJuai, PeralatanMesinPenghapusanJuaiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanJuai, KontrakJalanIrigasiJaringanJuai, HargaJalanIrigasiJaringanJuai, KDPJalanIrigasiJaringanJuai, JalanIrigasiJaringanUsulHapusJuai, TahunBerkurangUsulHapusJalanIrigasiJaringanJuai

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanJuai, TahunBerkurangJalanIrigasiJaringanJuai, PenghapusanJalanIrigasiJaringanJuai

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanJuai, SKPDTujuanJalanIrigasiJaringanJuai, FotoJalanIrigasiJaringanJuai

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanJuaiInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanJuai



class PenghapusanJalanIrigasiJaringanJuaiInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanJuai



class SKPDAsalJalanIrigasiJaringanJuaiInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanJuai



class SKPDTujuanJalanIrigasiJaringanJuaiInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanJuai



class FotoJalanIrigasiJaringanJuaiInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanJuai





class HargaJalanIrigasiJaringanJuaiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanJuai

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=33)
        return super(HargaJalanIrigasiJaringanJuaiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanJuaiInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanJuai


class JalanIrigasiJaringanJuaiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanJuaiInline,
                    SKPDAsalJalanIrigasiJaringanJuaiInline,
                    FotoJalanIrigasiJaringanJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        return super(JalanIrigasiJaringanJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusJuaiAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanJuaiInline,
                    SKPDAsalJalanIrigasiJaringanJuaiInline,
                    FotoJalanIrigasiJaringanJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanJuaiAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanJuaiInline,
                    SKPDAsalJalanIrigasiJaringanJuaiInline,
                    FotoJalanIrigasiJaringanJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        return super(KDPJalanIrigasiJaringanJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanJuaiAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=33)
        return super(KontrakJalanIrigasiJaringanJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=33)



class HargaJalanIrigasiJaringanJuaiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanJuaiAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanJuaiInline, TahunBerkurangJalanIrigasiJaringanJuaiInline,
                    SKPDAsalJalanIrigasiJaringanJuaiInline,
                    SKPDTujuanJalanIrigasiJaringanJuaiInline,
                    FotoJalanIrigasiJaringanJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Juai
admin.site.register(JalanIrigasiJaringanJuai, JalanIrigasiJaringanJuaiAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusJuai, JalanIrigasiJaringanUsulHapusJuaiAdmin)
admin.site.register(KDPJalanIrigasiJaringanJuai, KDPJalanIrigasiJaringanJuaiAdmin)
admin.site.register(KontrakJalanIrigasiJaringanJuai, KontrakJalanIrigasiJaringanJuaiAdmin)
admin.site.register(HargaJalanIrigasiJaringanJuai, HargaJalanIrigasiJaringanJuaiAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanJuai, JalanIrigasiJaringanPenghapusanJuaiAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLJuai, KontrakATLJuai, HargaATLJuai, ATLUsulHapusJuai, TahunBerkurangUsulHapusATLJuai

from atl.models import ATLPenghapusanJuai, TahunBerkurangATLJuai, PenghapusanATLJuai

from atl.models import SKPDAsalATLJuai, SKPDTujuanATLJuai, FotoATLJuai

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLJuaiInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLJuai



class PenghapusanATLJuaiInline(PenghapusanATLInline):
    model = PenghapusanATLJuai



class SKPDAsalATLJuaiInline(SKPDAsalATLInline):
    model = SKPDAsalATLJuai



class SKPDTujuanATLJuaiInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLJuai



class FotoATLJuaiInline(FotoATLInline):
    model = FotoATLJuai



class HargaATLJuaiInline(HargaATLInline):
    model = HargaATLJuai

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=33)
        return super(HargaATLJuaiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLJuaiInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLJuai


class ATLJuaiAdmin(ATLAdmin):
    inlines = [HargaATLJuaiInline,
                    SKPDAsalATLJuaiInline,
                    FotoATLJuaiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=33)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=33)
        return super(ATLJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusJuaiAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLJuaiInline,
                    SKPDAsalATLJuaiInline,
                    FotoATLJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLJuaiAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=33)
        return super(KontrakATLJuaiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=33)



class HargaATLJuaiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanJuaiAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLJuaiInline, TahunBerkurangATLJuaiInline,
                    SKPDAsalATLJuaiInline,
                    SKPDTujuanATLJuaiInline,
                    FotoATLJuaiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=33)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Juai
admin.site.register(ATLJuai, ATLJuaiAdmin)
admin.site.register(ATLUsulHapusJuai, ATLUsulHapusJuaiAdmin)
admin.site.register(KontrakATLJuai, KontrakATLJuaiAdmin)
admin.site.register(HargaATLJuai, HargaATLJuaiAdmin)
admin.site.register(ATLPenghapusanJuai, ATLPenghapusanJuaiAdmin)
