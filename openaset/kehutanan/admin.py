### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahKehutanan, KontrakTanahKehutanan, HargaTanahKehutanan, TanahUsulHapusKehutanan, TahunBerkurangUsulHapusTanahKehutanan

from umum.models import TanahPenghapusanKehutanan, TahunBerkurangTanahKehutanan, PenghapusanTanahKehutanan

from umum.models import SKPDAsalTanahKehutanan, SKPDTujuanTanahKehutanan, FotoTanahKehutanan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanKehutanan, KontrakGedungBangunanKehutanan, HargaGedungBangunanKehutanan, GedungBangunanRuanganKehutanan, GedungBangunanUsulHapusKehutanan, TahunBerkurangUsulHapusGedungKehutanan

from gedungbangunan.models import GedungBangunanPenghapusanKehutanan, TahunBerkurangGedungBangunanKehutanan, PenghapusanGedungBangunanKehutanan

from gedungbangunan.models import SKPDAsalGedungBangunanKehutanan, SKPDTujuanGedungBangunanKehutanan, FotoGedungBangunanKehutanan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinKehutanan, KontrakPeralatanMesinKehutanan, HargaPeralatanMesinKehutanan, PeralatanMesinUsulHapusKehutanan, TahunBerkurangUsulHapusPeralatanMesinKehutanan

from peralatanmesin.models import PeralatanMesinPenghapusanKehutanan, TahunBerkurangPeralatanMesinKehutanan, PenghapusanPeralatanMesinKehutanan

from peralatanmesin.models import SKPDAsalPeralatanMesinKehutanan, SKPDTujuanPeralatanMesinKehutanan, FotoPeralatanMesinKehutanan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahKehutananInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahKehutanan



class PenghapusanTanahKehutananInline(PenghapusanTanahInline):
    model = PenghapusanTanahKehutanan



class SKPDAsalTanahKehutananInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahKehutanan



class SKPDTujuanTanahKehutananInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahKehutanan



class FotoTanahKehutananInline(FotoTanahInline):
    model = FotoTanahKehutanan



class GedungBangunanKehutananInline(GedungBangunanInline):
    model = GedungBangunanKehutanan



class HargaTanahKehutananInline(HargaTanahInline):
    model = HargaTanahKehutanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=14)
        return super(HargaTanahKehutananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahKehutananInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahKehutanan


class TanahKehutananAdmin(TanahAdmin):
    inlines = [HargaTanahKehutananInline,
                SKPDAsalTanahKehutananInline,
                FotoTanahKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        return super(TanahKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusKehutananAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahKehutananInline,
                SKPDAsalTanahKehutananInline,
                FotoTanahKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahKehutananAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=14)
        return super(KontrakTanahKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=14)



class HargaTanahKehutananAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanKehutananAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahKehutananInline, TahunBerkurangTanahKehutananInline,
                    SKPDAsalTanahKehutananInline,
                    SKPDTujuanTanahKehutananInline,
                    FotoTanahKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Kehutanan
admin.site.register(TanahKehutanan, TanahKehutananAdmin)
admin.site.register(TanahUsulHapusKehutanan, TanahUsulHapusKehutananAdmin)
admin.site.register(KontrakTanahKehutanan, KontrakTanahKehutananAdmin)
admin.site.register(HargaTanahKehutanan, HargaTanahKehutananAdmin)
admin.site.register(TanahPenghapusanKehutanan, TanahPenghapusanKehutananAdmin)



from gedungbangunan.models import KDPGedungBangunanKehutanan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanKehutananInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanKehutanan



class PenghapusanGedungBangunanKehutananInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanKehutanan



class SKPDAsalGedungBangunanKehutananInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanKehutanan



class SKPDTujuanGedungBangunanKehutananInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanKehutanan



class FotoGedungBangunanKehutananInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanKehutanan



class HargaGedungBangunanKehutananInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanKehutanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=14)
        return super(HargaGedungBangunanKehutananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungKehutananInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungKehutanan


class GedungBangunanKehutananAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanKehutananInline,
                SKPDAsalGedungBangunanKehutananInline,
                FotoGedungBangunanKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        return super(GedungBangunanKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanKehutananAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanKehutananInline,
                SKPDAsalGedungBangunanKehutananInline,
                FotoGedungBangunanKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        return super(KDPGedungBangunanKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganKehutananAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusKehutananAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungKehutananInline,
                    SKPDAsalGedungBangunanKehutananInline,
                    FotoGedungBangunanKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanKehutananAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=14)
        return super(KontrakGedungBangunanKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=14)



class HargaGedungBangunanKehutananAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanKehutananAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanKehutananInline, TahunBerkurangGedungBangunanKehutananInline,
                    SKPDAsalGedungBangunanKehutananInline,
                    SKPDTujuanGedungBangunanKehutananInline,
                    FotoGedungBangunanKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Kehutanan
admin.site.register(GedungBangunanKehutanan, GedungBangunanKehutananAdmin)
admin.site.register(KDPGedungBangunanKehutanan, KDPGedungBangunanKehutananAdmin)
admin.site.register(GedungBangunanRuanganKehutanan, GedungBangunanRuanganKehutananAdmin)
admin.site.register(GedungBangunanUsulHapusKehutanan, GedungBangunanUsulHapusKehutananAdmin)
admin.site.register(KontrakGedungBangunanKehutanan, KontrakGedungBangunanKehutananAdmin)
admin.site.register(HargaGedungBangunanKehutanan, HargaGedungBangunanKehutananAdmin)
admin.site.register(GedungBangunanPenghapusanKehutanan, GedungBangunanPenghapusanKehutananAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinKehutananInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinKehutanan



class PenghapusanPeralatanMesinKehutananInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinKehutanan



class SKPDAsalPeralatanMesinKehutananInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinKehutanan



class SKPDTujuanPeralatanMesinKehutananInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinKehutanan



class FotoPeralatanMesinKehutananInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinKehutanan



class HargaPeralatanMesinKehutananInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinKehutanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=14)
        return super(HargaPeralatanMesinKehutananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinKehutananInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinKehutanan


class PeralatanMesinKehutananAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinKehutananInline,
                    SKPDAsalPeralatanMesinKehutananInline,
                    FotoPeralatanMesinKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=14)
        return super(PeralatanMesinKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusKehutananAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinKehutananInline,
                    SKPDAsalPeralatanMesinKehutananInline,
                    FotoPeralatanMesinKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinKehutananAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=14)
        return super(KontrakPeralatanMesinKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=14)



class HargaPeralatanMesinKehutananAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanKehutananAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinKehutananInline, TahunBerkurangPeralatanMesinKehutananInline,
                    SKPDAsalPeralatanMesinKehutananInline,
                    SKPDTujuanPeralatanMesinKehutananInline,
                    FotoPeralatanMesinKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Kehutanan
admin.site.register(PeralatanMesinKehutanan, PeralatanMesinKehutananAdmin)
admin.site.register(PeralatanMesinUsulHapusKehutanan, PeralatanMesinUsulHapusKehutananAdmin)
admin.site.register(KontrakPeralatanMesinKehutanan, KontrakPeralatanMesinKehutananAdmin)
admin.site.register(HargaPeralatanMesinKehutanan, HargaPeralatanMesinKehutananAdmin)
admin.site.register(PeralatanMesinPenghapusanKehutanan, PeralatanMesinPenghapusanKehutananAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanKehutanan, KontrakJalanIrigasiJaringanKehutanan, HargaJalanIrigasiJaringanKehutanan, KDPJalanIrigasiJaringanKehutanan, JalanIrigasiJaringanUsulHapusKehutanan, TahunBerkurangUsulHapusJalanIrigasiJaringanKehutanan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanKehutanan, TahunBerkurangJalanIrigasiJaringanKehutanan, PenghapusanJalanIrigasiJaringanKehutanan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanKehutanan, SKPDTujuanJalanIrigasiJaringanKehutanan, FotoJalanIrigasiJaringanKehutanan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanKehutananInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanKehutanan



class PenghapusanJalanIrigasiJaringanKehutananInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanKehutanan



class SKPDAsalJalanIrigasiJaringanKehutananInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanKehutanan



class SKPDTujuanJalanIrigasiJaringanKehutananInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanKehutanan



class FotoJalanIrigasiJaringanKehutananInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanKehutanan





class HargaJalanIrigasiJaringanKehutananInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanKehutanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=14)
        return super(HargaJalanIrigasiJaringanKehutananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanKehutananInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanKehutanan


class JalanIrigasiJaringanKehutananAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKehutananInline,
                    SKPDAsalJalanIrigasiJaringanKehutananInline,
                    FotoJalanIrigasiJaringanKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        return super(JalanIrigasiJaringanKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusKehutananAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanKehutananInline,
                    SKPDAsalJalanIrigasiJaringanKehutananInline,
                    FotoJalanIrigasiJaringanKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanKehutananAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKehutananInline,
                    SKPDAsalJalanIrigasiJaringanKehutananInline,
                    FotoJalanIrigasiJaringanKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        return super(KDPJalanIrigasiJaringanKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanKehutananAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=14)
        return super(KontrakJalanIrigasiJaringanKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=14)



class HargaJalanIrigasiJaringanKehutananAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanKehutananAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanKehutananInline, TahunBerkurangJalanIrigasiJaringanKehutananInline,
                    SKPDAsalJalanIrigasiJaringanKehutananInline,
                    SKPDTujuanJalanIrigasiJaringanKehutananInline,
                    FotoJalanIrigasiJaringanKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Kehutanan
admin.site.register(JalanIrigasiJaringanKehutanan, JalanIrigasiJaringanKehutananAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusKehutanan, JalanIrigasiJaringanUsulHapusKehutananAdmin)
admin.site.register(KDPJalanIrigasiJaringanKehutanan, KDPJalanIrigasiJaringanKehutananAdmin)
admin.site.register(KontrakJalanIrigasiJaringanKehutanan, KontrakJalanIrigasiJaringanKehutananAdmin)
admin.site.register(HargaJalanIrigasiJaringanKehutanan, HargaJalanIrigasiJaringanKehutananAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanKehutanan, JalanIrigasiJaringanPenghapusanKehutananAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLKehutanan, KontrakATLKehutanan, HargaATLKehutanan, ATLUsulHapusKehutanan, TahunBerkurangUsulHapusATLKehutanan

from atl.models import ATLPenghapusanKehutanan, TahunBerkurangATLKehutanan, PenghapusanATLKehutanan

from atl.models import SKPDAsalATLKehutanan, SKPDTujuanATLKehutanan, FotoATLKehutanan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLKehutananInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLKehutanan



class PenghapusanATLKehutananInline(PenghapusanATLInline):
    model = PenghapusanATLKehutanan



class SKPDAsalATLKehutananInline(SKPDAsalATLInline):
    model = SKPDAsalATLKehutanan



class SKPDTujuanATLKehutananInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLKehutanan



class FotoATLKehutananInline(FotoATLInline):
    model = FotoATLKehutanan



class HargaATLKehutananInline(HargaATLInline):
    model = HargaATLKehutanan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=14)
        return super(HargaATLKehutananInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLKehutananInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLKehutanan


class ATLKehutananAdmin(ATLAdmin):
    inlines = [HargaATLKehutananInline,
                    SKPDAsalATLKehutananInline,
                    FotoATLKehutananInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=14)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=14)
        return super(ATLKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusKehutananAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLKehutananInline,
                    SKPDAsalATLKehutananInline,
                    FotoATLKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLKehutananAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=14)
        return super(KontrakATLKehutananAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=14)



class HargaATLKehutananAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanKehutananAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLKehutananInline, TahunBerkurangATLKehutananInline,
                    SKPDAsalATLKehutananInline,
                    SKPDTujuanATLKehutananInline,
                    FotoATLKehutananInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=14)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Kehutanan
admin.site.register(ATLKehutanan, ATLKehutananAdmin)
admin.site.register(ATLUsulHapusKehutanan, ATLUsulHapusKehutananAdmin)
admin.site.register(KontrakATLKehutanan, KontrakATLKehutananAdmin)
admin.site.register(HargaATLKehutanan, HargaATLKehutananAdmin)
admin.site.register(ATLPenghapusanKehutanan, ATLPenghapusanKehutananAdmin)
