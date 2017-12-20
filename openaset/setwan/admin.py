### $Id: admin.py,v 1.40 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahSetwan, KontrakTanahSetwan, HargaTanahSetwan, TanahUsulHapusSetwan, TahunBerkurangUsulHapusTanahSetwan

from umum.models import TanahPenghapusanSetwan, TahunBerkurangTanahSetwan, PenghapusanTanahSetwan

from umum.models import SKPDAsalTanahSetwan, SKPDTujuanTanahSetwan, FotoTanahSetwan

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanSetwan, KontrakGedungBangunanSetwan, HargaGedungBangunanSetwan, GedungBangunanRuanganSetwan, GedungBangunanUsulHapusSetwan, TahunBerkurangUsulHapusGedungSetwan

from gedungbangunan.models import GedungBangunanPenghapusanSetwan, TahunBerkurangGedungBangunanSetwan, PenghapusanGedungBangunanSetwan

from gedungbangunan.models import SKPDAsalGedungBangunanSetwan, SKPDTujuanGedungBangunanSetwan, FotoGedungBangunanSetwan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinSetwan, KontrakPeralatanMesinSetwan, HargaPeralatanMesinSetwan, PeralatanMesinUsulHapusSetwan, TahunBerkurangUsulHapusPeralatanMesinSetwan

from peralatanmesin.models import PeralatanMesinPenghapusanSetwan, TahunBerkurangPeralatanMesinSetwan, PenghapusanPeralatanMesinSetwan

from peralatanmesin.models import SKPDAsalPeralatanMesinSetwan, SKPDTujuanPeralatanMesinSetwan, FotoPeralatanMesinSetwan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahSetwanInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahSetwan



class PenghapusanTanahSetwanInline(PenghapusanTanahInline):
    model = PenghapusanTanahSetwan



class SKPDAsalTanahSetwanInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahSetwan



class SKPDTujuanTanahSetwanInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahSetwan



class FotoTanahSetwanInline(FotoTanahInline):
    model = FotoTanahSetwan



class GedungBangunanSetwanInline(GedungBangunanInline):
    model = GedungBangunanSetwan



class HargaTanahSetwanInline(HargaTanahInline):
    model = HargaTanahSetwan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=1)
        return super(HargaTanahSetwanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahSetwanInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahSetwan


class TanahSetwanAdmin(TanahAdmin):
    inlines = [HargaTanahSetwanInline,
                SKPDAsalTanahSetwanInline,
                FotoTanahSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        return super(TanahSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusSetwanAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahSetwanInline,
                SKPDAsalTanahSetwanInline,
                FotoTanahSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahSetwanAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=1)
        return super(KontrakTanahSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=1)



class HargaTanahSetwanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanSetwanAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahSetwanInline, TahunBerkurangTanahSetwanInline,
                    SKPDAsalTanahSetwanInline,
                    SKPDTujuanTanahSetwanInline,
                    FotoTanahSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Setwan
admin.site.register(TanahSetwan, TanahSetwanAdmin)
admin.site.register(TanahUsulHapusSetwan, TanahUsulHapusSetwanAdmin)
admin.site.register(KontrakTanahSetwan, KontrakTanahSetwanAdmin)
admin.site.register(HargaTanahSetwan, HargaTanahSetwanAdmin)
admin.site.register(TanahPenghapusanSetwan, TanahPenghapusanSetwanAdmin)



from gedungbangunan.models import KDPGedungBangunanSetwan


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanSetwanInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanSetwan



class PenghapusanGedungBangunanSetwanInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanSetwan



class SKPDAsalGedungBangunanSetwanInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanSetwan



class SKPDTujuanGedungBangunanSetwanInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanSetwan



class FotoGedungBangunanSetwanInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanSetwan



class HargaGedungBangunanSetwanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanSetwan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=1)
        return super(HargaGedungBangunanSetwanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungSetwanInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungSetwan


class GedungBangunanSetwanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanSetwanInline,
                SKPDAsalGedungBangunanSetwanInline,
                FotoGedungBangunanSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        return super(GedungBangunanSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanSetwanAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanSetwanInline,
                SKPDAsalGedungBangunanSetwanInline,
                FotoGedungBangunanSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        return super(KDPGedungBangunanSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganSetwanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusSetwanAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungSetwanInline,
                    SKPDAsalGedungBangunanSetwanInline,
                    FotoGedungBangunanSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanSetwanAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=1)
        return super(KontrakGedungBangunanSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=1)



class HargaGedungBangunanSetwanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanSetwanAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanSetwanInline, TahunBerkurangGedungBangunanSetwanInline,
                    SKPDAsalGedungBangunanSetwanInline,
                    SKPDTujuanGedungBangunanSetwanInline,
                    FotoGedungBangunanSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Setwan
admin.site.register(GedungBangunanSetwan, GedungBangunanSetwanAdmin)
admin.site.register(KDPGedungBangunanSetwan, KDPGedungBangunanSetwanAdmin)
admin.site.register(GedungBangunanRuanganSetwan, GedungBangunanRuanganSetwanAdmin)
admin.site.register(GedungBangunanUsulHapusSetwan, GedungBangunanUsulHapusSetwanAdmin)
admin.site.register(KontrakGedungBangunanSetwan, KontrakGedungBangunanSetwanAdmin)
admin.site.register(HargaGedungBangunanSetwan, HargaGedungBangunanSetwanAdmin)
admin.site.register(GedungBangunanPenghapusanSetwan, GedungBangunanPenghapusanSetwanAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinSetwanInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinSetwan



class PenghapusanPeralatanMesinSetwanInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinSetwan



class SKPDAsalPeralatanMesinSetwanInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinSetwan



class SKPDTujuanPeralatanMesinSetwanInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinSetwan



class FotoPeralatanMesinSetwanInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinSetwan



class HargaPeralatanMesinSetwanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinSetwan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=1)
        return super(HargaPeralatanMesinSetwanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinSetwanInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinSetwan


class PeralatanMesinSetwanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinSetwanInline,
                    SKPDAsalPeralatanMesinSetwanInline,
                    FotoPeralatanMesinSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=1)
        return super(PeralatanMesinSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusSetwanAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinSetwanInline,
                    SKPDAsalPeralatanMesinSetwanInline,
                    FotoPeralatanMesinSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinSetwanAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=1)
        return super(KontrakPeralatanMesinSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=1)



class HargaPeralatanMesinSetwanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanSetwanAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinSetwanInline, TahunBerkurangPeralatanMesinSetwanInline,
                    SKPDAsalPeralatanMesinSetwanInline,
                    SKPDTujuanPeralatanMesinSetwanInline,
                    FotoPeralatanMesinSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Setwan
admin.site.register(PeralatanMesinSetwan, PeralatanMesinSetwanAdmin)
admin.site.register(PeralatanMesinUsulHapusSetwan, PeralatanMesinUsulHapusSetwanAdmin)
admin.site.register(KontrakPeralatanMesinSetwan, KontrakPeralatanMesinSetwanAdmin)
admin.site.register(HargaPeralatanMesinSetwan, HargaPeralatanMesinSetwanAdmin)
admin.site.register(PeralatanMesinPenghapusanSetwan, PeralatanMesinPenghapusanSetwanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanSetwan, KontrakJalanIrigasiJaringanSetwan, HargaJalanIrigasiJaringanSetwan, KDPJalanIrigasiJaringanSetwan, JalanIrigasiJaringanUsulHapusSetwan, TahunBerkurangUsulHapusJalanIrigasiJaringanSetwan

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanSetwan, TahunBerkurangJalanIrigasiJaringanSetwan, PenghapusanJalanIrigasiJaringanSetwan

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanSetwan, SKPDTujuanJalanIrigasiJaringanSetwan, FotoJalanIrigasiJaringanSetwan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanSetwanInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanSetwan



class PenghapusanJalanIrigasiJaringanSetwanInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanSetwan



class SKPDAsalJalanIrigasiJaringanSetwanInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanSetwan



class SKPDTujuanJalanIrigasiJaringanSetwanInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanSetwan



class FotoJalanIrigasiJaringanSetwanInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanSetwan





class HargaJalanIrigasiJaringanSetwanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanSetwan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=1)
        return super(HargaJalanIrigasiJaringanSetwanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanSetwanInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanSetwan


class JalanIrigasiJaringanSetwanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSetwanInline,
                    SKPDAsalJalanIrigasiJaringanSetwanInline,
                    FotoJalanIrigasiJaringanSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        return super(JalanIrigasiJaringanSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusSetwanAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanSetwanInline,
                    SKPDAsalJalanIrigasiJaringanSetwanInline,
                    FotoJalanIrigasiJaringanSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanSetwanAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSetwanInline,
                    SKPDAsalJalanIrigasiJaringanSetwanInline,
                    FotoJalanIrigasiJaringanSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        return super(KDPJalanIrigasiJaringanSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanSetwanAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=1)
        return super(KontrakJalanIrigasiJaringanSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=1)



class HargaJalanIrigasiJaringanSetwanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanSetwanAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanSetwanInline, TahunBerkurangJalanIrigasiJaringanSetwanInline,
                    SKPDAsalJalanIrigasiJaringanSetwanInline,
                    SKPDTujuanJalanIrigasiJaringanSetwanInline,
                    FotoJalanIrigasiJaringanSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Setwan
admin.site.register(JalanIrigasiJaringanSetwan, JalanIrigasiJaringanSetwanAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusSetwan, JalanIrigasiJaringanUsulHapusSetwanAdmin)
admin.site.register(KDPJalanIrigasiJaringanSetwan, KDPJalanIrigasiJaringanSetwanAdmin)
admin.site.register(KontrakJalanIrigasiJaringanSetwan, KontrakJalanIrigasiJaringanSetwanAdmin)
admin.site.register(HargaJalanIrigasiJaringanSetwan, HargaJalanIrigasiJaringanSetwanAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanSetwan, JalanIrigasiJaringanPenghapusanSetwanAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLSetwan, KontrakATLSetwan, HargaATLSetwan, ATLUsulHapusSetwan, TahunBerkurangUsulHapusATLSetwan

from atl.models import ATLPenghapusanSetwan, TahunBerkurangATLSetwan, PenghapusanATLSetwan

from atl.models import SKPDAsalATLSetwan, SKPDTujuanATLSetwan, FotoATLSetwan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLSetwanInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLSetwan



class PenghapusanATLSetwanInline(PenghapusanATLInline):
    model = PenghapusanATLSetwan



class SKPDAsalATLSetwanInline(SKPDAsalATLInline):
    model = SKPDAsalATLSetwan



class SKPDTujuanATLSetwanInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLSetwan



class FotoATLSetwanInline(FotoATLInline):
    model = FotoATLSetwan



class HargaATLSetwanInline(HargaATLInline):
    model = HargaATLSetwan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=1)
        return super(HargaATLSetwanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLSetwanInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLSetwan


class ATLSetwanAdmin(ATLAdmin):
    inlines = [HargaATLSetwanInline,
                    SKPDAsalATLSetwanInline,
                    FotoATLSetwanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=1)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=1)
        return super(ATLSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusSetwanAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLSetwanInline,
                    SKPDAsalATLSetwanInline,
                    FotoATLSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLSetwanAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=1)
        return super(KontrakATLSetwanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=1)



class HargaATLSetwanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanSetwanAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLSetwanInline, TahunBerkurangATLSetwanInline,
                    SKPDAsalATLSetwanInline,
                    SKPDTujuanATLSetwanInline,
                    FotoATLSetwanInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=1)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Setwan
admin.site.register(ATLSetwan, ATLSetwanAdmin)
admin.site.register(ATLUsulHapusSetwan, ATLUsulHapusSetwanAdmin)
admin.site.register(KontrakATLSetwan, KontrakATLSetwanAdmin)
admin.site.register(HargaATLSetwan, HargaATLSetwanAdmin)
admin.site.register(ATLPenghapusanSetwan, ATLPenghapusanSetwanAdmin)
