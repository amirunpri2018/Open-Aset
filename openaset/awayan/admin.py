### $Id: admin.py,v 1.30 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahAwayan, KontrakTanahAwayan, HargaTanahAwayan, TanahUsulHapusAwayan, TahunBerkurangUsulHapusTanahAwayan

from umum.models import TanahPenghapusanAwayan, TahunBerkurangTanahAwayan, PenghapusanTanahAwayan

from umum.models import SKPDAsalTanahAwayan, SKPDTujuanTanahAwayan, FotoTanahAwayan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanAwayan, KontrakGedungBangunanAwayan, HargaGedungBangunanAwayan, GedungBangunanRuanganAwayan, GedungBangunanUsulHapusAwayan, TahunBerkurangUsulHapusGedungAwayan

from gedungbangunan.models import GedungBangunanPenghapusanAwayan, TahunBerkurangGedungBangunanAwayan, PenghapusanGedungBangunanAwayan

from gedungbangunan.models import SKPDAsalGedungBangunanAwayan, SKPDTujuanGedungBangunanAwayan, FotoGedungBangunanAwayan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinAwayan, KontrakPeralatanMesinAwayan, HargaPeralatanMesinAwayan, PeralatanMesinUsulHapusAwayan, TahunBerkurangUsulHapusPeralatanMesinAwayan

from peralatanmesin.models import PeralatanMesinPenghapusanAwayan, TahunBerkurangPeralatanMesinAwayan, PenghapusanPeralatanMesinAwayan

from peralatanmesin.models import SKPDAsalPeralatanMesinAwayan, SKPDTujuanPeralatanMesinAwayan, FotoPeralatanMesinAwayan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahAwayanInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahAwayan



class PenghapusanTanahAwayanInline(PenghapusanTanahInline):
    model = PenghapusanTanahAwayan



class SKPDAsalTanahAwayanInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahAwayan



class SKPDTujuanTanahAwayanInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahAwayan



class FotoTanahAwayanInline(FotoTanahInline):
    model = FotoTanahAwayan



class GedungBangunanAwayanInline(GedungBangunanInline):
    model = GedungBangunanAwayan



class HargaTanahAwayanInline(HargaTanahInline):
    model = HargaTanahAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=34)
        return super(HargaTanahAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahAwayanInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahAwayan


class TanahAwayanAdmin(TanahAdmin):
    inlines = [HargaTanahAwayanInline,
                SKPDAsalTanahAwayanInline,
                FotoTanahAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        return super(TanahAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusAwayanAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahAwayanInline,
                SKPDAsalTanahAwayanInline,
                FotoTanahAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahAwayanAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=34)
        return super(KontrakTanahAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=34)



class HargaTanahAwayanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanAwayanAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahAwayanInline, TahunBerkurangTanahAwayanInline,
                    SKPDAsalTanahAwayanInline,
                    SKPDTujuanTanahAwayanInline,
                    FotoTanahAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Awayan
admin.site.register(TanahAwayan, TanahAwayanAdmin)
admin.site.register(TanahUsulHapusAwayan, TanahUsulHapusAwayanAdmin)
admin.site.register(KontrakTanahAwayan, KontrakTanahAwayanAdmin)
admin.site.register(HargaTanahAwayan, HargaTanahAwayanAdmin)
admin.site.register(TanahPenghapusanAwayan, TanahPenghapusanAwayanAdmin)



from gedungbangunan.models import KDPGedungBangunanAwayan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanAwayanInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanAwayan



class PenghapusanGedungBangunanAwayanInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanAwayan



class SKPDAsalGedungBangunanAwayanInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanAwayan



class SKPDTujuanGedungBangunanAwayanInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanAwayan



class FotoGedungBangunanAwayanInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanAwayan



class HargaGedungBangunanAwayanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=34)
        return super(HargaGedungBangunanAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungAwayanInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungAwayan


class GedungBangunanAwayanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanAwayanInline,
                SKPDAsalGedungBangunanAwayanInline,
                FotoGedungBangunanAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        return super(GedungBangunanAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanAwayanAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanAwayanInline,
                SKPDAsalGedungBangunanAwayanInline,
                FotoGedungBangunanAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        return super(KDPGedungBangunanAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganAwayanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusAwayanAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungAwayanInline,
                    SKPDAsalGedungBangunanAwayanInline,
                    FotoGedungBangunanAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanAwayanAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=34)
        return super(KontrakGedungBangunanAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=34)



class HargaGedungBangunanAwayanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanAwayanAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanAwayanInline, TahunBerkurangGedungBangunanAwayanInline,
                    SKPDAsalGedungBangunanAwayanInline,
                    SKPDTujuanGedungBangunanAwayanInline,
                    FotoGedungBangunanAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Awayan
admin.site.register(GedungBangunanAwayan, GedungBangunanAwayanAdmin)
admin.site.register(KDPGedungBangunanAwayan, KDPGedungBangunanAwayanAdmin)
admin.site.register(GedungBangunanRuanganAwayan, GedungBangunanRuanganAwayanAdmin)
admin.site.register(GedungBangunanUsulHapusAwayan, GedungBangunanUsulHapusAwayanAdmin)
admin.site.register(KontrakGedungBangunanAwayan, KontrakGedungBangunanAwayanAdmin)
admin.site.register(HargaGedungBangunanAwayan, HargaGedungBangunanAwayanAdmin)
admin.site.register(GedungBangunanPenghapusanAwayan, GedungBangunanPenghapusanAwayanAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinAwayanInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinAwayan



class PenghapusanPeralatanMesinAwayanInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinAwayan



class SKPDAsalPeralatanMesinAwayanInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinAwayan



class SKPDTujuanPeralatanMesinAwayanInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinAwayan



class FotoPeralatanMesinAwayanInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinAwayan



class HargaPeralatanMesinAwayanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=34)
        return super(HargaPeralatanMesinAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinAwayanInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinAwayan


class PeralatanMesinAwayanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinAwayanInline,
                    SKPDAsalPeralatanMesinAwayanInline,
                    FotoPeralatanMesinAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=34)
        return super(PeralatanMesinAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusAwayanAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinAwayanInline,
                    SKPDAsalPeralatanMesinAwayanInline,
                    FotoPeralatanMesinAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinAwayanAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=34)
        return super(KontrakPeralatanMesinAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=34)



class HargaPeralatanMesinAwayanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanAwayanAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinAwayanInline, TahunBerkurangPeralatanMesinAwayanInline,
                    SKPDAsalPeralatanMesinAwayanInline,
                    SKPDTujuanPeralatanMesinAwayanInline,
                    FotoPeralatanMesinAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Awayan
admin.site.register(PeralatanMesinAwayan, PeralatanMesinAwayanAdmin)
admin.site.register(PeralatanMesinUsulHapusAwayan, PeralatanMesinUsulHapusAwayanAdmin)
admin.site.register(KontrakPeralatanMesinAwayan, KontrakPeralatanMesinAwayanAdmin)
admin.site.register(HargaPeralatanMesinAwayan, HargaPeralatanMesinAwayanAdmin)
admin.site.register(PeralatanMesinPenghapusanAwayan, PeralatanMesinPenghapusanAwayanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanAwayan, KontrakJalanIrigasiJaringanAwayan, HargaJalanIrigasiJaringanAwayan, KDPJalanIrigasiJaringanAwayan, JalanIrigasiJaringanUsulHapusAwayan, TahunBerkurangUsulHapusJalanIrigasiJaringanAwayan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanAwayan, TahunBerkurangJalanIrigasiJaringanAwayan, PenghapusanJalanIrigasiJaringanAwayan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanAwayan, SKPDTujuanJalanIrigasiJaringanAwayan, FotoJalanIrigasiJaringanAwayan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanAwayanInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanAwayan



class PenghapusanJalanIrigasiJaringanAwayanInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanAwayan



class SKPDAsalJalanIrigasiJaringanAwayanInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanAwayan



class SKPDTujuanJalanIrigasiJaringanAwayanInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanAwayan



class FotoJalanIrigasiJaringanAwayanInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanAwayan





class HargaJalanIrigasiJaringanAwayanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=34)
        return super(HargaJalanIrigasiJaringanAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanAwayanInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanAwayan


class JalanIrigasiJaringanAwayanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanAwayanInline,
                    SKPDAsalJalanIrigasiJaringanAwayanInline,
                    FotoJalanIrigasiJaringanAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        return super(JalanIrigasiJaringanAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusAwayanAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanAwayanInline,
                    SKPDAsalJalanIrigasiJaringanAwayanInline,
                    FotoJalanIrigasiJaringanAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanAwayanAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanAwayanInline,
                    SKPDAsalJalanIrigasiJaringanAwayanInline,
                    FotoJalanIrigasiJaringanAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        return super(KDPJalanIrigasiJaringanAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanAwayanAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=34)
        return super(KontrakJalanIrigasiJaringanAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=34)



class HargaJalanIrigasiJaringanAwayanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanAwayanAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanAwayanInline, TahunBerkurangJalanIrigasiJaringanAwayanInline,
                    SKPDAsalJalanIrigasiJaringanAwayanInline,
                    SKPDTujuanJalanIrigasiJaringanAwayanInline,
                    FotoJalanIrigasiJaringanAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Awayan
admin.site.register(JalanIrigasiJaringanAwayan, JalanIrigasiJaringanAwayanAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusAwayan, JalanIrigasiJaringanUsulHapusAwayanAdmin)
admin.site.register(KDPJalanIrigasiJaringanAwayan, KDPJalanIrigasiJaringanAwayanAdmin)
admin.site.register(KontrakJalanIrigasiJaringanAwayan, KontrakJalanIrigasiJaringanAwayanAdmin)
admin.site.register(HargaJalanIrigasiJaringanAwayan, HargaJalanIrigasiJaringanAwayanAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanAwayan, JalanIrigasiJaringanPenghapusanAwayanAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLAwayan, KontrakATLAwayan, HargaATLAwayan, ATLUsulHapusAwayan, TahunBerkurangUsulHapusATLAwayan

from atl.models import ATLPenghapusanAwayan, TahunBerkurangATLAwayan, PenghapusanATLAwayan

from atl.models import SKPDAsalATLAwayan, SKPDTujuanATLAwayan, FotoATLAwayan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLAwayanInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLAwayan



class PenghapusanATLAwayanInline(PenghapusanATLInline):
    model = PenghapusanATLAwayan



class SKPDAsalATLAwayanInline(SKPDAsalATLInline):
    model = SKPDAsalATLAwayan



class SKPDTujuanATLAwayanInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLAwayan



class FotoATLAwayanInline(FotoATLInline):
    model = FotoATLAwayan



class HargaATLAwayanInline(HargaATLInline):
    model = HargaATLAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=34)
        return super(HargaATLAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLAwayanInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLAwayan


class ATLAwayanAdmin(ATLAdmin):
    inlines = [HargaATLAwayanInline,
                    SKPDAsalATLAwayanInline,
                    FotoATLAwayanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=34)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=34)
        return super(ATLAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusAwayanAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLAwayanInline,
                    SKPDAsalATLAwayanInline,
                    FotoATLAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLAwayanAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=34)
        return super(KontrakATLAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=34)



class HargaATLAwayanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanAwayanAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLAwayanInline, TahunBerkurangATLAwayanInline,
                    SKPDAsalATLAwayanInline,
                    SKPDTujuanATLAwayanInline,
                    FotoATLAwayanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=34)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Awayan
admin.site.register(ATLAwayan, ATLAwayanAdmin)
admin.site.register(ATLUsulHapusAwayan, ATLUsulHapusAwayanAdmin)
admin.site.register(KontrakATLAwayan, KontrakATLAwayanAdmin)
admin.site.register(HargaATLAwayan, HargaATLAwayanAdmin)
admin.site.register(ATLPenghapusanAwayan, ATLPenghapusanAwayanAdmin)
