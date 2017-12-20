### $Id: admin.py,v 1.5 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahPerikanan, KontrakTanahPerikanan, HargaTanahPerikanan, TanahUsulHapusPerikanan, TahunBerkurangUsulHapusTanahPerikanan

from umum.models import TanahPenghapusanPerikanan, TahunBerkurangTanahPerikanan, PenghapusanTanahPerikanan

from umum.models import SKPDAsalTanahPerikanan, SKPDTujuanTanahPerikanan, FotoTanahPerikanan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanPerikanan, KontrakGedungBangunanPerikanan, HargaGedungBangunanPerikanan, GedungBangunanRuanganPerikanan, GedungBangunanUsulHapusPerikanan, TahunBerkurangUsulHapusGedungPerikanan

from gedungbangunan.models import GedungBangunanPenghapusanPerikanan, TahunBerkurangGedungBangunanPerikanan, PenghapusanGedungBangunanPerikanan

from gedungbangunan.models import SKPDAsalGedungBangunanPerikanan, SKPDTujuanGedungBangunanPerikanan, FotoGedungBangunanPerikanan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinPerikanan, KontrakPeralatanMesinPerikanan, HargaPeralatanMesinPerikanan, PeralatanMesinUsulHapusPerikanan, TahunBerkurangUsulHapusPeralatanMesinPerikanan

from peralatanmesin.models import PeralatanMesinPenghapusanPerikanan, TahunBerkurangPeralatanMesinPerikanan, PenghapusanPeralatanMesinPerikanan

from peralatanmesin.models import SKPDAsalPeralatanMesinPerikanan, SKPDTujuanPeralatanMesinPerikanan, FotoPeralatanMesinPerikanan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahPerikananInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahPerikanan



class PenghapusanTanahPerikananInline(PenghapusanTanahInline):
    model = PenghapusanTanahPerikanan



class SKPDAsalTanahPerikananInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahPerikanan



class SKPDTujuanTanahPerikananInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahPerikanan



class FotoTanahPerikananInline(FotoTanahInline):
    model = FotoTanahPerikanan



class GedungBangunanPerikananInline(GedungBangunanInline):
    model = GedungBangunanPerikanan



class HargaTanahPerikananInline(HargaTanahInline):
    model = HargaTanahPerikanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=45)
        return super(HargaTanahPerikananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahPerikananInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahPerikanan


class TanahPerikananAdmin(TanahAdmin):
    inlines = [HargaTanahPerikananInline,
                SKPDAsalTanahPerikananInline,
                FotoTanahPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        return super(TanahPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusPerikananAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahPerikananInline,
                SKPDAsalTanahPerikananInline,
                FotoTanahPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahPerikananAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=45)
        return super(KontrakTanahPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=45)



class HargaTanahPerikananAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanPerikananAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahPerikananInline, TahunBerkurangTanahPerikananInline,
                    SKPDAsalTanahPerikananInline,
                    SKPDTujuanTanahPerikananInline,
                    FotoTanahPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Perikanan
admin.site.register(TanahPerikanan, TanahPerikananAdmin)
admin.site.register(TanahUsulHapusPerikanan, TanahUsulHapusPerikananAdmin)
admin.site.register(KontrakTanahPerikanan, KontrakTanahPerikananAdmin)
admin.site.register(HargaTanahPerikanan, HargaTanahPerikananAdmin)
admin.site.register(TanahPenghapusanPerikanan, TanahPenghapusanPerikananAdmin)



from gedungbangunan.models import KDPGedungBangunanPerikanan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanPerikananInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanPerikanan



class PenghapusanGedungBangunanPerikananInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanPerikanan



class SKPDAsalGedungBangunanPerikananInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanPerikanan



class SKPDTujuanGedungBangunanPerikananInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanPerikanan



class FotoGedungBangunanPerikananInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanPerikanan



class HargaGedungBangunanPerikananInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanPerikanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=45)
        return super(HargaGedungBangunanPerikananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungPerikananInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungPerikanan


class GedungBangunanPerikananAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanPerikananInline,
                SKPDAsalGedungBangunanPerikananInline,
                FotoGedungBangunanPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        return super(GedungBangunanPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanPerikananAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanPerikananInline,
                SKPDAsalGedungBangunanPerikananInline,
                FotoGedungBangunanPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        return super(KDPGedungBangunanPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganPerikananAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusPerikananAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungPerikananInline,
                    SKPDAsalGedungBangunanPerikananInline,
                    FotoGedungBangunanPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanPerikananAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=45)
        return super(KontrakGedungBangunanPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=45)



class HargaGedungBangunanPerikananAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanPerikananAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanPerikananInline, TahunBerkurangGedungBangunanPerikananInline,
                    SKPDAsalGedungBangunanPerikananInline,
                    SKPDTujuanGedungBangunanPerikananInline,
                    FotoGedungBangunanPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Perikanan
admin.site.register(GedungBangunanPerikanan, GedungBangunanPerikananAdmin)
admin.site.register(KDPGedungBangunanPerikanan, KDPGedungBangunanPerikananAdmin)
admin.site.register(GedungBangunanRuanganPerikanan, GedungBangunanRuanganPerikananAdmin)
admin.site.register(GedungBangunanUsulHapusPerikanan, GedungBangunanUsulHapusPerikananAdmin)
admin.site.register(KontrakGedungBangunanPerikanan, KontrakGedungBangunanPerikananAdmin)
admin.site.register(HargaGedungBangunanPerikanan, HargaGedungBangunanPerikananAdmin)
admin.site.register(GedungBangunanPenghapusanPerikanan, GedungBangunanPenghapusanPerikananAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinPerikananInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinPerikanan



class PenghapusanPeralatanMesinPerikananInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinPerikanan



class SKPDAsalPeralatanMesinPerikananInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinPerikanan



class SKPDTujuanPeralatanMesinPerikananInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinPerikanan



class FotoPeralatanMesinPerikananInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinPerikanan



class HargaPeralatanMesinPerikananInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinPerikanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=45)
        return super(HargaPeralatanMesinPerikananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinPerikananInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinPerikanan


class PeralatanMesinPerikananAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinPerikananInline,
                    SKPDAsalPeralatanMesinPerikananInline,
                    FotoPeralatanMesinPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=45)
        return super(PeralatanMesinPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusPerikananAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinPerikananInline,
                    SKPDAsalPeralatanMesinPerikananInline,
                    FotoPeralatanMesinPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinPerikananAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=45)
        return super(KontrakPeralatanMesinPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=45)



class HargaPeralatanMesinPerikananAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanPerikananAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinPerikananInline, TahunBerkurangPeralatanMesinPerikananInline,
                    SKPDAsalPeralatanMesinPerikananInline,
                    SKPDTujuanPeralatanMesinPerikananInline,
                    FotoPeralatanMesinPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Perikanan
admin.site.register(PeralatanMesinPerikanan, PeralatanMesinPerikananAdmin)
admin.site.register(PeralatanMesinUsulHapusPerikanan, PeralatanMesinUsulHapusPerikananAdmin)
admin.site.register(KontrakPeralatanMesinPerikanan, KontrakPeralatanMesinPerikananAdmin)
admin.site.register(HargaPeralatanMesinPerikanan, HargaPeralatanMesinPerikananAdmin)
admin.site.register(PeralatanMesinPenghapusanPerikanan, PeralatanMesinPenghapusanPerikananAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanPerikanan, KontrakJalanIrigasiJaringanPerikanan, HargaJalanIrigasiJaringanPerikanan, KDPJalanIrigasiJaringanPerikanan, JalanIrigasiJaringanUsulHapusPerikanan, TahunBerkurangUsulHapusJalanIrigasiJaringanPerikanan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanPerikanan, TahunBerkurangJalanIrigasiJaringanPerikanan, PenghapusanJalanIrigasiJaringanPerikanan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanPerikanan, SKPDTujuanJalanIrigasiJaringanPerikanan, FotoJalanIrigasiJaringanPerikanan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanPerikananInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanPerikanan



class PenghapusanJalanIrigasiJaringanPerikananInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanPerikanan



class SKPDAsalJalanIrigasiJaringanPerikananInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanPerikanan



class SKPDTujuanJalanIrigasiJaringanPerikananInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanPerikanan



class FotoJalanIrigasiJaringanPerikananInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanPerikanan





class HargaJalanIrigasiJaringanPerikananInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanPerikanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=45)
        return super(HargaJalanIrigasiJaringanPerikananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanPerikananInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanPerikanan


class JalanIrigasiJaringanPerikananAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPerikananInline,
                    SKPDAsalJalanIrigasiJaringanPerikananInline,
                    FotoJalanIrigasiJaringanPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        return super(JalanIrigasiJaringanPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusPerikananAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanPerikananInline,
                    SKPDAsalJalanIrigasiJaringanPerikananInline,
                    FotoJalanIrigasiJaringanPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanPerikananAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPerikananInline,
                    SKPDAsalJalanIrigasiJaringanPerikananInline,
                    FotoJalanIrigasiJaringanPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        return super(KDPJalanIrigasiJaringanPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanPerikananAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=45)
        return super(KontrakJalanIrigasiJaringanPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=45)



class HargaJalanIrigasiJaringanPerikananAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanPerikananAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanPerikananInline, TahunBerkurangJalanIrigasiJaringanPerikananInline,
                    SKPDAsalJalanIrigasiJaringanPerikananInline,
                    SKPDTujuanJalanIrigasiJaringanPerikananInline,
                    FotoJalanIrigasiJaringanPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Perikanan
admin.site.register(JalanIrigasiJaringanPerikanan, JalanIrigasiJaringanPerikananAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusPerikanan, JalanIrigasiJaringanUsulHapusPerikananAdmin)
admin.site.register(KDPJalanIrigasiJaringanPerikanan, KDPJalanIrigasiJaringanPerikananAdmin)
admin.site.register(KontrakJalanIrigasiJaringanPerikanan, KontrakJalanIrigasiJaringanPerikananAdmin)
admin.site.register(HargaJalanIrigasiJaringanPerikanan, HargaJalanIrigasiJaringanPerikananAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanPerikanan, JalanIrigasiJaringanPenghapusanPerikananAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLPerikanan, KontrakATLPerikanan, HargaATLPerikanan, ATLUsulHapusPerikanan, TahunBerkurangUsulHapusATLPerikanan

from atl.models import ATLPenghapusanPerikanan, TahunBerkurangATLPerikanan, PenghapusanATLPerikanan

from atl.models import SKPDAsalATLPerikanan, SKPDTujuanATLPerikanan, FotoATLPerikanan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLPerikananInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLPerikanan



class PenghapusanATLPerikananInline(PenghapusanATLInline):
    model = PenghapusanATLPerikanan



class SKPDAsalATLPerikananInline(SKPDAsalATLInline):
    model = SKPDAsalATLPerikanan



class SKPDTujuanATLPerikananInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLPerikanan



class FotoATLPerikananInline(FotoATLInline):
    model = FotoATLPerikanan



class HargaATLPerikananInline(HargaATLInline):
    model = HargaATLPerikanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=45)
        return super(HargaATLPerikananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLPerikananInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLPerikanan


class ATLPerikananAdmin(ATLAdmin):
    inlines = [HargaATLPerikananInline,
                    SKPDAsalATLPerikananInline,
                    FotoATLPerikananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=45)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=45)
        return super(ATLPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusPerikananAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLPerikananInline,
                    SKPDAsalATLPerikananInline,
                    FotoATLPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLPerikananAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=45)
        return super(KontrakATLPerikananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=45)



class HargaATLPerikananAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanPerikananAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLPerikananInline, TahunBerkurangATLPerikananInline,
                    SKPDAsalATLPerikananInline,
                    SKPDTujuanATLPerikananInline,
                    FotoATLPerikananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=45)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Perikanan
admin.site.register(ATLPerikanan, ATLPerikananAdmin)
admin.site.register(ATLUsulHapusPerikanan, ATLUsulHapusPerikananAdmin)
admin.site.register(KontrakATLPerikanan, KontrakATLPerikananAdmin)
admin.site.register(HargaATLPerikanan, HargaATLPerikananAdmin)
admin.site.register(ATLPenghapusanPerikanan, ATLPenghapusanPerikananAdmin)
