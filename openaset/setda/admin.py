### $Id: admin.py,v 1.32 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahSetda, KontrakTanahSetda, HargaTanahSetda, TanahUsulHapusSetda, TahunBerkurangUsulHapusTanahSetda

from umum.models import TanahPenghapusanSetda, TahunBerkurangTanahSetda, PenghapusanTanahSetda

from umum.models import SKPDAsalTanahSetda, SKPDTujuanTanahSetda, FotoTanahSetda

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanSetda, KontrakGedungBangunanSetda, HargaGedungBangunanSetda, GedungBangunanRuanganSetda, GedungBangunanUsulHapusSetda, TahunBerkurangUsulHapusGedungSetda

from gedungbangunan.models import GedungBangunanPenghapusanSetda, TahunBerkurangGedungBangunanSetda, PenghapusanGedungBangunanSetda

from gedungbangunan.models import SKPDAsalGedungBangunanSetda, SKPDTujuanGedungBangunanSetda, FotoGedungBangunanSetda

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinSetda, KontrakPeralatanMesinSetda, HargaPeralatanMesinSetda, PeralatanMesinUsulHapusSetda, TahunBerkurangUsulHapusPeralatanMesinSetda

from peralatanmesin.models import PeralatanMesinPenghapusanSetda, TahunBerkurangPeralatanMesinSetda, PenghapusanPeralatanMesinSetda

from peralatanmesin.models import SKPDAsalPeralatanMesinSetda, SKPDTujuanPeralatanMesinSetda, FotoPeralatanMesinSetda

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahSetdaInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahSetda



class PenghapusanTanahSetdaInline(PenghapusanTanahInline):
    model = PenghapusanTanahSetda



class SKPDAsalTanahSetdaInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahSetda



class SKPDTujuanTanahSetdaInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahSetda



class FotoTanahSetdaInline(FotoTanahInline):
    model = FotoTanahSetda



class GedungBangunanSetdaInline(GedungBangunanInline):
    model = GedungBangunanSetda



class HargaTanahSetdaInline(HargaTanahInline):
    model = HargaTanahSetda

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=2)
        return super(HargaTanahSetdaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahSetdaInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahSetda


class TanahSetdaAdmin(TanahAdmin):
    inlines = [HargaTanahSetdaInline,
                SKPDAsalTanahSetdaInline,
                FotoTanahSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        return super(TanahSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusSetdaAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahSetdaInline,
                SKPDAsalTanahSetdaInline,
                FotoTanahSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahSetdaAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=2)
        return super(KontrakTanahSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=2)



class HargaTanahSetdaAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanSetdaAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahSetdaInline, TahunBerkurangTanahSetdaInline,
                    SKPDAsalTanahSetdaInline,
                    SKPDTujuanTanahSetdaInline,
                    FotoTanahSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Setda
admin.site.register(TanahSetda, TanahSetdaAdmin)
admin.site.register(TanahUsulHapusSetda, TanahUsulHapusSetdaAdmin)
admin.site.register(KontrakTanahSetda, KontrakTanahSetdaAdmin)
admin.site.register(HargaTanahSetda, HargaTanahSetdaAdmin)
admin.site.register(TanahPenghapusanSetda, TanahPenghapusanSetdaAdmin)



from gedungbangunan.models import KDPGedungBangunanSetda


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanSetdaInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanSetda



class PenghapusanGedungBangunanSetdaInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanSetda



class SKPDAsalGedungBangunanSetdaInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanSetda



class SKPDTujuanGedungBangunanSetdaInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanSetda



class FotoGedungBangunanSetdaInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanSetda



class HargaGedungBangunanSetdaInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanSetda

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=2)
        return super(HargaGedungBangunanSetdaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungSetdaInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungSetda


class GedungBangunanSetdaAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanSetdaInline,
                SKPDAsalGedungBangunanSetdaInline,
                FotoGedungBangunanSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        return super(GedungBangunanSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanSetdaAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanSetdaInline,
                SKPDAsalGedungBangunanSetdaInline,
                FotoGedungBangunanSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        return super(KDPGedungBangunanSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganSetdaAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusSetdaAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungSetdaInline,
                    SKPDAsalGedungBangunanSetdaInline,
                    FotoGedungBangunanSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanSetdaAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=2)
        return super(KontrakGedungBangunanSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=2)



class HargaGedungBangunanSetdaAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanSetdaAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanSetdaInline, TahunBerkurangGedungBangunanSetdaInline,
                    SKPDAsalGedungBangunanSetdaInline,
                    SKPDTujuanGedungBangunanSetdaInline,
                    FotoGedungBangunanSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Setda
admin.site.register(GedungBangunanSetda, GedungBangunanSetdaAdmin)
admin.site.register(KDPGedungBangunanSetda, KDPGedungBangunanSetdaAdmin)
admin.site.register(GedungBangunanRuanganSetda, GedungBangunanRuanganSetdaAdmin)
admin.site.register(GedungBangunanUsulHapusSetda, GedungBangunanUsulHapusSetdaAdmin)
admin.site.register(KontrakGedungBangunanSetda, KontrakGedungBangunanSetdaAdmin)
admin.site.register(HargaGedungBangunanSetda, HargaGedungBangunanSetdaAdmin)
admin.site.register(GedungBangunanPenghapusanSetda, GedungBangunanPenghapusanSetdaAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinSetdaInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinSetda



class PenghapusanPeralatanMesinSetdaInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinSetda



class SKPDAsalPeralatanMesinSetdaInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinSetda



class SKPDTujuanPeralatanMesinSetdaInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinSetda



class FotoPeralatanMesinSetdaInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinSetda



class HargaPeralatanMesinSetdaInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinSetda

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=2)
        return super(HargaPeralatanMesinSetdaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinSetdaInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinSetda


class PeralatanMesinSetdaAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinSetdaInline,
                    SKPDAsalPeralatanMesinSetdaInline,
                    FotoPeralatanMesinSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=2)
        return super(PeralatanMesinSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusSetdaAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinSetdaInline,
                    SKPDAsalPeralatanMesinSetdaInline,
                    FotoPeralatanMesinSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinSetdaAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=2)
        return super(KontrakPeralatanMesinSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=2)



class HargaPeralatanMesinSetdaAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanSetdaAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinSetdaInline, TahunBerkurangPeralatanMesinSetdaInline,
                    SKPDAsalPeralatanMesinSetdaInline,
                    SKPDTujuanPeralatanMesinSetdaInline,
                    FotoPeralatanMesinSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Setda
admin.site.register(PeralatanMesinSetda, PeralatanMesinSetdaAdmin)
admin.site.register(PeralatanMesinUsulHapusSetda, PeralatanMesinUsulHapusSetdaAdmin)
admin.site.register(KontrakPeralatanMesinSetda, KontrakPeralatanMesinSetdaAdmin)
admin.site.register(HargaPeralatanMesinSetda, HargaPeralatanMesinSetdaAdmin)
admin.site.register(PeralatanMesinPenghapusanSetda, PeralatanMesinPenghapusanSetdaAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanSetda, KontrakJalanIrigasiJaringanSetda, HargaJalanIrigasiJaringanSetda, KDPJalanIrigasiJaringanSetda, JalanIrigasiJaringanUsulHapusSetda, TahunBerkurangUsulHapusJalanIrigasiJaringanSetda

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanSetda, TahunBerkurangJalanIrigasiJaringanSetda, PenghapusanJalanIrigasiJaringanSetda

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanSetda, SKPDTujuanJalanIrigasiJaringanSetda, FotoJalanIrigasiJaringanSetda

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanSetdaInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanSetda



class PenghapusanJalanIrigasiJaringanSetdaInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanSetda



class SKPDAsalJalanIrigasiJaringanSetdaInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanSetda



class SKPDTujuanJalanIrigasiJaringanSetdaInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanSetda



class FotoJalanIrigasiJaringanSetdaInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanSetda





class HargaJalanIrigasiJaringanSetdaInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanSetda

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=2)
        return super(HargaJalanIrigasiJaringanSetdaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanSetdaInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanSetda


class JalanIrigasiJaringanSetdaAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSetdaInline,
                    SKPDAsalJalanIrigasiJaringanSetdaInline,
                    FotoJalanIrigasiJaringanSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        return super(JalanIrigasiJaringanSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusSetdaAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanSetdaInline,
                    SKPDAsalJalanIrigasiJaringanSetdaInline,
                    FotoJalanIrigasiJaringanSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanSetdaAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSetdaInline,
                    SKPDAsalJalanIrigasiJaringanSetdaInline,
                    FotoJalanIrigasiJaringanSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        return super(KDPJalanIrigasiJaringanSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanSetdaAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=2)
        return super(KontrakJalanIrigasiJaringanSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=2)



class HargaJalanIrigasiJaringanSetdaAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanSetdaAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanSetdaInline, TahunBerkurangJalanIrigasiJaringanSetdaInline,
                    SKPDAsalJalanIrigasiJaringanSetdaInline,
                    SKPDTujuanJalanIrigasiJaringanSetdaInline,
                    FotoJalanIrigasiJaringanSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Setda
admin.site.register(JalanIrigasiJaringanSetda, JalanIrigasiJaringanSetdaAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusSetda, JalanIrigasiJaringanUsulHapusSetdaAdmin)
admin.site.register(KDPJalanIrigasiJaringanSetda, KDPJalanIrigasiJaringanSetdaAdmin)
admin.site.register(KontrakJalanIrigasiJaringanSetda, KontrakJalanIrigasiJaringanSetdaAdmin)
admin.site.register(HargaJalanIrigasiJaringanSetda, HargaJalanIrigasiJaringanSetdaAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanSetda, JalanIrigasiJaringanPenghapusanSetdaAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLSetda, KontrakATLSetda, HargaATLSetda, ATLUsulHapusSetda, TahunBerkurangUsulHapusATLSetda

from atl.models import ATLPenghapusanSetda, TahunBerkurangATLSetda, PenghapusanATLSetda

from atl.models import SKPDAsalATLSetda, SKPDTujuanATLSetda, FotoATLSetda

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLSetdaInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLSetda



class PenghapusanATLSetdaInline(PenghapusanATLInline):
    model = PenghapusanATLSetda



class SKPDAsalATLSetdaInline(SKPDAsalATLInline):
    model = SKPDAsalATLSetda



class SKPDTujuanATLSetdaInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLSetda



class FotoATLSetdaInline(FotoATLInline):
    model = FotoATLSetda



class HargaATLSetdaInline(HargaATLInline):
    model = HargaATLSetda

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=2)
        return super(HargaATLSetdaInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLSetdaInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLSetda


class ATLSetdaAdmin(ATLAdmin):
    inlines = [HargaATLSetdaInline,
                    SKPDAsalATLSetdaInline,
                    FotoATLSetdaInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=2)
        return super(ATLSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusSetdaAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLSetdaInline,
                    SKPDAsalATLSetdaInline,
                    FotoATLSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLSetdaAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=2)
        return super(KontrakATLSetdaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=2)



class HargaATLSetdaAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanSetdaAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLSetdaInline, TahunBerkurangATLSetdaInline,
                    SKPDAsalATLSetdaInline,
                    SKPDTujuanATLSetdaInline,
                    FotoATLSetdaInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=2)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Setda
admin.site.register(ATLSetda, ATLSetdaAdmin)
admin.site.register(ATLUsulHapusSetda, ATLUsulHapusSetdaAdmin)
admin.site.register(KontrakATLSetda, KontrakATLSetdaAdmin)
admin.site.register(HargaATLSetda, HargaATLSetdaAdmin)
admin.site.register(ATLPenghapusanSetda, ATLPenghapusanSetdaAdmin)
