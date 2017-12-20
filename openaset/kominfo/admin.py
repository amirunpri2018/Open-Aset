### $Id: admin.py,v 1.5 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahKominfo, KontrakTanahKominfo, HargaTanahKominfo, TanahUsulHapusKominfo, TahunBerkurangUsulHapusTanahKominfo

from umum.models import TanahPenghapusanKominfo, TahunBerkurangTanahKominfo, PenghapusanTanahKominfo

from umum.models import SKPDAsalTanahKominfo, SKPDTujuanTanahKominfo, FotoTanahKominfo

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanKominfo, KontrakGedungBangunanKominfo, HargaGedungBangunanKominfo, GedungBangunanRuanganKominfo, GedungBangunanUsulHapusKominfo, TahunBerkurangUsulHapusGedungKominfo

from gedungbangunan.models import GedungBangunanPenghapusanKominfo, TahunBerkurangGedungBangunanKominfo, PenghapusanGedungBangunanKominfo

from gedungbangunan.models import SKPDAsalGedungBangunanKominfo, SKPDTujuanGedungBangunanKominfo, FotoGedungBangunanKominfo

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinKominfo, KontrakPeralatanMesinKominfo, HargaPeralatanMesinKominfo, PeralatanMesinUsulHapusKominfo, TahunBerkurangUsulHapusPeralatanMesinKominfo

from peralatanmesin.models import PeralatanMesinPenghapusanKominfo, TahunBerkurangPeralatanMesinKominfo, PenghapusanPeralatanMesinKominfo

from peralatanmesin.models import SKPDAsalPeralatanMesinKominfo, SKPDTujuanPeralatanMesinKominfo, FotoPeralatanMesinKominfo

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahKominfoInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahKominfo



class PenghapusanTanahKominfoInline(PenghapusanTanahInline):
    model = PenghapusanTanahKominfo



class SKPDAsalTanahKominfoInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahKominfo



class SKPDTujuanTanahKominfoInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahKominfo



class FotoTanahKominfoInline(FotoTanahInline):
    model = FotoTanahKominfo



class GedungBangunanKominfoInline(GedungBangunanInline):
    model = GedungBangunanKominfo



class HargaTanahKominfoInline(HargaTanahInline):
    model = HargaTanahKominfo

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=43)
        return super(HargaTanahKominfoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahKominfoInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahKominfo


class TanahKominfoAdmin(TanahAdmin):
    inlines = [HargaTanahKominfoInline,
                SKPDAsalTanahKominfoInline,
                FotoTanahKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        return super(TanahKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusKominfoAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahKominfoInline,
                SKPDAsalTanahKominfoInline,
                FotoTanahKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahKominfoAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=43)
        return super(KontrakTanahKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=43)



class HargaTanahKominfoAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanKominfoAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahKominfoInline, TahunBerkurangTanahKominfoInline,
                    SKPDAsalTanahKominfoInline,
                    SKPDTujuanTanahKominfoInline,
                    FotoTanahKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Kominfo
admin.site.register(TanahKominfo, TanahKominfoAdmin)
admin.site.register(TanahUsulHapusKominfo, TanahUsulHapusKominfoAdmin)
admin.site.register(KontrakTanahKominfo, KontrakTanahKominfoAdmin)
admin.site.register(HargaTanahKominfo, HargaTanahKominfoAdmin)
admin.site.register(TanahPenghapusanKominfo, TanahPenghapusanKominfoAdmin)



from gedungbangunan.models import KDPGedungBangunanKominfo


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanKominfoInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanKominfo



class PenghapusanGedungBangunanKominfoInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanKominfo



class SKPDAsalGedungBangunanKominfoInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanKominfo



class SKPDTujuanGedungBangunanKominfoInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanKominfo



class FotoGedungBangunanKominfoInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanKominfo



class HargaGedungBangunanKominfoInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanKominfo

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=43)
        return super(HargaGedungBangunanKominfoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungKominfoInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungKominfo


class GedungBangunanKominfoAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanKominfoInline,
                SKPDAsalGedungBangunanKominfoInline,
                FotoGedungBangunanKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        return super(GedungBangunanKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanKominfoAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanKominfoInline,
                SKPDAsalGedungBangunanKominfoInline,
                FotoGedungBangunanKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        return super(KDPGedungBangunanKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganKominfoAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusKominfoAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungKominfoInline,
                    SKPDAsalGedungBangunanKominfoInline,
                    FotoGedungBangunanKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanKominfoAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=43)
        return super(KontrakGedungBangunanKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=43)



class HargaGedungBangunanKominfoAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanKominfoAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanKominfoInline, TahunBerkurangGedungBangunanKominfoInline,
                    SKPDAsalGedungBangunanKominfoInline,
                    SKPDTujuanGedungBangunanKominfoInline,
                    FotoGedungBangunanKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Kominfo
admin.site.register(GedungBangunanKominfo, GedungBangunanKominfoAdmin)
admin.site.register(KDPGedungBangunanKominfo, KDPGedungBangunanKominfoAdmin)
admin.site.register(GedungBangunanRuanganKominfo, GedungBangunanRuanganKominfoAdmin)
admin.site.register(GedungBangunanUsulHapusKominfo, GedungBangunanUsulHapusKominfoAdmin)
admin.site.register(KontrakGedungBangunanKominfo, KontrakGedungBangunanKominfoAdmin)
admin.site.register(HargaGedungBangunanKominfo, HargaGedungBangunanKominfoAdmin)
admin.site.register(GedungBangunanPenghapusanKominfo, GedungBangunanPenghapusanKominfoAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinKominfoInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinKominfo



class PenghapusanPeralatanMesinKominfoInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinKominfo



class SKPDAsalPeralatanMesinKominfoInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinKominfo



class SKPDTujuanPeralatanMesinKominfoInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinKominfo



class FotoPeralatanMesinKominfoInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinKominfo



class HargaPeralatanMesinKominfoInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinKominfo

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=43)
        return super(HargaPeralatanMesinKominfoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinKominfoInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinKominfo


class PeralatanMesinKominfoAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinKominfoInline,
                    SKPDAsalPeralatanMesinKominfoInline,
                    FotoPeralatanMesinKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=43)
        return super(PeralatanMesinKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusKominfoAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinKominfoInline,
                    SKPDAsalPeralatanMesinKominfoInline,
                    FotoPeralatanMesinKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinKominfoAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=43)
        return super(KontrakPeralatanMesinKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=43)



class HargaPeralatanMesinKominfoAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanKominfoAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinKominfoInline, TahunBerkurangPeralatanMesinKominfoInline,
                    SKPDAsalPeralatanMesinKominfoInline,
                    SKPDTujuanPeralatanMesinKominfoInline,
                    FotoPeralatanMesinKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Kominfo
admin.site.register(PeralatanMesinKominfo, PeralatanMesinKominfoAdmin)
admin.site.register(PeralatanMesinUsulHapusKominfo, PeralatanMesinUsulHapusKominfoAdmin)
admin.site.register(KontrakPeralatanMesinKominfo, KontrakPeralatanMesinKominfoAdmin)
admin.site.register(HargaPeralatanMesinKominfo, HargaPeralatanMesinKominfoAdmin)
admin.site.register(PeralatanMesinPenghapusanKominfo, PeralatanMesinPenghapusanKominfoAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanKominfo, KontrakJalanIrigasiJaringanKominfo, HargaJalanIrigasiJaringanKominfo, KDPJalanIrigasiJaringanKominfo, JalanIrigasiJaringanUsulHapusKominfo, TahunBerkurangUsulHapusJalanIrigasiJaringanKominfo

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanKominfo, TahunBerkurangJalanIrigasiJaringanKominfo, PenghapusanJalanIrigasiJaringanKominfo

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanKominfo, SKPDTujuanJalanIrigasiJaringanKominfo, FotoJalanIrigasiJaringanKominfo

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanKominfoInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanKominfo



class PenghapusanJalanIrigasiJaringanKominfoInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanKominfo



class SKPDAsalJalanIrigasiJaringanKominfoInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanKominfo



class SKPDTujuanJalanIrigasiJaringanKominfoInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanKominfo



class FotoJalanIrigasiJaringanKominfoInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanKominfo





class HargaJalanIrigasiJaringanKominfoInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanKominfo

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=43)
        return super(HargaJalanIrigasiJaringanKominfoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanKominfoInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanKominfo


class JalanIrigasiJaringanKominfoAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKominfoInline,
                    SKPDAsalJalanIrigasiJaringanKominfoInline,
                    FotoJalanIrigasiJaringanKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        return super(JalanIrigasiJaringanKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusKominfoAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanKominfoInline,
                    SKPDAsalJalanIrigasiJaringanKominfoInline,
                    FotoJalanIrigasiJaringanKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanKominfoAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKominfoInline,
                    SKPDAsalJalanIrigasiJaringanKominfoInline,
                    FotoJalanIrigasiJaringanKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        return super(KDPJalanIrigasiJaringanKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanKominfoAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=43)
        return super(KontrakJalanIrigasiJaringanKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=43)



class HargaJalanIrigasiJaringanKominfoAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanKominfoAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanKominfoInline, TahunBerkurangJalanIrigasiJaringanKominfoInline,
                    SKPDAsalJalanIrigasiJaringanKominfoInline,
                    SKPDTujuanJalanIrigasiJaringanKominfoInline,
                    FotoJalanIrigasiJaringanKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Kominfo
admin.site.register(JalanIrigasiJaringanKominfo, JalanIrigasiJaringanKominfoAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusKominfo, JalanIrigasiJaringanUsulHapusKominfoAdmin)
admin.site.register(KDPJalanIrigasiJaringanKominfo, KDPJalanIrigasiJaringanKominfoAdmin)
admin.site.register(KontrakJalanIrigasiJaringanKominfo, KontrakJalanIrigasiJaringanKominfoAdmin)
admin.site.register(HargaJalanIrigasiJaringanKominfo, HargaJalanIrigasiJaringanKominfoAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanKominfo, JalanIrigasiJaringanPenghapusanKominfoAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLKominfo, KontrakATLKominfo, HargaATLKominfo, ATLUsulHapusKominfo, TahunBerkurangUsulHapusATLKominfo

from atl.models import ATLPenghapusanKominfo, TahunBerkurangATLKominfo, PenghapusanATLKominfo

from atl.models import SKPDAsalATLKominfo, SKPDTujuanATLKominfo, FotoATLKominfo

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLKominfoInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLKominfo



class PenghapusanATLKominfoInline(PenghapusanATLInline):
    model = PenghapusanATLKominfo



class SKPDAsalATLKominfoInline(SKPDAsalATLInline):
    model = SKPDAsalATLKominfo



class SKPDTujuanATLKominfoInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLKominfo



class FotoATLKominfoInline(FotoATLInline):
    model = FotoATLKominfo



class HargaATLKominfoInline(HargaATLInline):
    model = HargaATLKominfo

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=43)
        return super(HargaATLKominfoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLKominfoInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLKominfo


class ATLKominfoAdmin(ATLAdmin):
    inlines = [HargaATLKominfoInline,
                    SKPDAsalATLKominfoInline,
                    FotoATLKominfoInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=43)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=43)
        return super(ATLKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusKominfoAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLKominfoInline,
                    SKPDAsalATLKominfoInline,
                    FotoATLKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLKominfoAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=43)
        return super(KontrakATLKominfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=43)



class HargaATLKominfoAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanKominfoAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLKominfoInline, TahunBerkurangATLKominfoInline,
                    SKPDAsalATLKominfoInline,
                    SKPDTujuanATLKominfoInline,
                    FotoATLKominfoInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=43)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Kominfo
admin.site.register(ATLKominfo, ATLKominfoAdmin)
admin.site.register(ATLUsulHapusKominfo, ATLUsulHapusKominfoAdmin)
admin.site.register(KontrakATLKominfo, KontrakATLKominfoAdmin)
admin.site.register(HargaATLKominfo, HargaATLKominfoAdmin)
admin.site.register(ATLPenghapusanKominfo, ATLPenghapusanKominfoAdmin)
