### $Id: admin.py,v 1.29 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahKESBANGPOL, KontrakTanahKESBANGPOL, HargaTanahKESBANGPOL, TanahUsulHapusKESBANGPOL, TahunBerkurangUsulHapusTanahKESBANGPOL

from umum.models import TanahPenghapusanKESBANGPOL, TahunBerkurangTanahKESBANGPOL, PenghapusanTanahKESBANGPOL

from umum.models import SKPDAsalTanahKESBANGPOL, SKPDTujuanTanahKESBANGPOL, FotoTanahKESBANGPOL

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanKESBANGPOL, KontrakGedungBangunanKESBANGPOL, HargaGedungBangunanKESBANGPOL, GedungBangunanRuanganKESBANGPOL, GedungBangunanUsulHapusKESBANGPOL, TahunBerkurangUsulHapusGedungKESBANGPOL

from gedungbangunan.models import GedungBangunanPenghapusanKESBANGPOL, TahunBerkurangGedungBangunanKESBANGPOL, PenghapusanGedungBangunanKESBANGPOL

from gedungbangunan.models import SKPDAsalGedungBangunanKESBANGPOL, SKPDTujuanGedungBangunanKESBANGPOL, FotoGedungBangunanKESBANGPOL

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinKESBANGPOL, KontrakPeralatanMesinKESBANGPOL, HargaPeralatanMesinKESBANGPOL, PeralatanMesinUsulHapusKESBANGPOL, TahunBerkurangUsulHapusPeralatanMesinKESBANGPOL

from peralatanmesin.models import PeralatanMesinPenghapusanKESBANGPOL, TahunBerkurangPeralatanMesinKESBANGPOL, PenghapusanPeralatanMesinKESBANGPOL

from peralatanmesin.models import SKPDAsalPeralatanMesinKESBANGPOL, SKPDTujuanPeralatanMesinKESBANGPOL, FotoPeralatanMesinKESBANGPOL

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahKESBANGPOLInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahKESBANGPOL



class PenghapusanTanahKESBANGPOLInline(PenghapusanTanahInline):
    model = PenghapusanTanahKESBANGPOL



class SKPDAsalTanahKESBANGPOLInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahKESBANGPOL



class SKPDTujuanTanahKESBANGPOLInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahKESBANGPOL



class FotoTanahKESBANGPOLInline(FotoTanahInline):
    model = FotoTanahKESBANGPOL



class GedungBangunanKESBANGPOLInline(GedungBangunanInline):
    model = GedungBangunanKESBANGPOL



class HargaTanahKESBANGPOLInline(HargaTanahInline):
    model = HargaTanahKESBANGPOL

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=24)
        return super(HargaTanahKESBANGPOLInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahKESBANGPOLInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahKESBANGPOL


class TanahKESBANGPOLAdmin(TanahAdmin):
    inlines = [HargaTanahKESBANGPOLInline,
                SKPDAsalTanahKESBANGPOLInline,
                FotoTanahKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        return super(TanahKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusKESBANGPOLAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahKESBANGPOLInline,
                SKPDAsalTanahKESBANGPOLInline,
                FotoTanahKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahKESBANGPOLAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=24)
        return super(KontrakTanahKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=24)



class HargaTanahKESBANGPOLAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanKESBANGPOLAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahKESBANGPOLInline, TahunBerkurangTanahKESBANGPOLInline,
                    SKPDAsalTanahKESBANGPOLInline,
                    SKPDTujuanTanahKESBANGPOLInline,
                    FotoTanahKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah KESBANGPOL
admin.site.register(TanahKESBANGPOL, TanahKESBANGPOLAdmin)
admin.site.register(TanahUsulHapusKESBANGPOL, TanahUsulHapusKESBANGPOLAdmin)
admin.site.register(KontrakTanahKESBANGPOL, KontrakTanahKESBANGPOLAdmin)
admin.site.register(HargaTanahKESBANGPOL, HargaTanahKESBANGPOLAdmin)
admin.site.register(TanahPenghapusanKESBANGPOL, TanahPenghapusanKESBANGPOLAdmin)



from gedungbangunan.models import KDPGedungBangunanKESBANGPOL


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanKESBANGPOLInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanKESBANGPOL



class PenghapusanGedungBangunanKESBANGPOLInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanKESBANGPOL



class SKPDAsalGedungBangunanKESBANGPOLInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanKESBANGPOL



class SKPDTujuanGedungBangunanKESBANGPOLInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanKESBANGPOL



class FotoGedungBangunanKESBANGPOLInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanKESBANGPOL



class HargaGedungBangunanKESBANGPOLInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanKESBANGPOL

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=24)
        return super(HargaGedungBangunanKESBANGPOLInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungKESBANGPOLInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungKESBANGPOL


class GedungBangunanKESBANGPOLAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanKESBANGPOLInline,
                SKPDAsalGedungBangunanKESBANGPOLInline,
                FotoGedungBangunanKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        return super(GedungBangunanKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanKESBANGPOLAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanKESBANGPOLInline,
                SKPDAsalGedungBangunanKESBANGPOLInline,
                FotoGedungBangunanKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        return super(KDPGedungBangunanKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganKESBANGPOLAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusKESBANGPOLAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungKESBANGPOLInline,
                    SKPDAsalGedungBangunanKESBANGPOLInline,
                    FotoGedungBangunanKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanKESBANGPOLAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=24)
        return super(KontrakGedungBangunanKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=24)



class HargaGedungBangunanKESBANGPOLAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanKESBANGPOLAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanKESBANGPOLInline, TahunBerkurangGedungBangunanKESBANGPOLInline,
                    SKPDAsalGedungBangunanKESBANGPOLInline,
                    SKPDTujuanGedungBangunanKESBANGPOLInline,
                    FotoGedungBangunanKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan KESBANGPOL
admin.site.register(GedungBangunanKESBANGPOL, GedungBangunanKESBANGPOLAdmin)
admin.site.register(KDPGedungBangunanKESBANGPOL, KDPGedungBangunanKESBANGPOLAdmin)
admin.site.register(GedungBangunanRuanganKESBANGPOL, GedungBangunanRuanganKESBANGPOLAdmin)
admin.site.register(GedungBangunanUsulHapusKESBANGPOL, GedungBangunanUsulHapusKESBANGPOLAdmin)
admin.site.register(KontrakGedungBangunanKESBANGPOL, KontrakGedungBangunanKESBANGPOLAdmin)
admin.site.register(HargaGedungBangunanKESBANGPOL, HargaGedungBangunanKESBANGPOLAdmin)
admin.site.register(GedungBangunanPenghapusanKESBANGPOL, GedungBangunanPenghapusanKESBANGPOLAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinKESBANGPOLInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinKESBANGPOL



class PenghapusanPeralatanMesinKESBANGPOLInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinKESBANGPOL



class SKPDAsalPeralatanMesinKESBANGPOLInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinKESBANGPOL



class SKPDTujuanPeralatanMesinKESBANGPOLInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinKESBANGPOL



class FotoPeralatanMesinKESBANGPOLInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinKESBANGPOL



class HargaPeralatanMesinKESBANGPOLInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinKESBANGPOL

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=24)
        return super(HargaPeralatanMesinKESBANGPOLInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinKESBANGPOLInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinKESBANGPOL


class PeralatanMesinKESBANGPOLAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinKESBANGPOLInline,
                    SKPDAsalPeralatanMesinKESBANGPOLInline,
                    FotoPeralatanMesinKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=24)
        return super(PeralatanMesinKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusKESBANGPOLAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinKESBANGPOLInline,
                    SKPDAsalPeralatanMesinKESBANGPOLInline,
                    FotoPeralatanMesinKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinKESBANGPOLAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=24)
        return super(KontrakPeralatanMesinKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=24)



class HargaPeralatanMesinKESBANGPOLAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanKESBANGPOLAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinKESBANGPOLInline, TahunBerkurangPeralatanMesinKESBANGPOLInline,
                    SKPDAsalPeralatanMesinKESBANGPOLInline,
                    SKPDTujuanPeralatanMesinKESBANGPOLInline,
                    FotoPeralatanMesinKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin KESBANGPOL
admin.site.register(PeralatanMesinKESBANGPOL, PeralatanMesinKESBANGPOLAdmin)
admin.site.register(PeralatanMesinUsulHapusKESBANGPOL, PeralatanMesinUsulHapusKESBANGPOLAdmin)
admin.site.register(KontrakPeralatanMesinKESBANGPOL, KontrakPeralatanMesinKESBANGPOLAdmin)
admin.site.register(HargaPeralatanMesinKESBANGPOL, HargaPeralatanMesinKESBANGPOLAdmin)
admin.site.register(PeralatanMesinPenghapusanKESBANGPOL, PeralatanMesinPenghapusanKESBANGPOLAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanKESBANGPOL, KontrakJalanIrigasiJaringanKESBANGPOL, HargaJalanIrigasiJaringanKESBANGPOL, KDPJalanIrigasiJaringanKESBANGPOL, JalanIrigasiJaringanUsulHapusKESBANGPOL, TahunBerkurangUsulHapusJalanIrigasiJaringanKESBANGPOL

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanKESBANGPOL, TahunBerkurangJalanIrigasiJaringanKESBANGPOL, PenghapusanJalanIrigasiJaringanKESBANGPOL

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanKESBANGPOL, SKPDTujuanJalanIrigasiJaringanKESBANGPOL, FotoJalanIrigasiJaringanKESBANGPOL

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanKESBANGPOLInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanKESBANGPOL



class PenghapusanJalanIrigasiJaringanKESBANGPOLInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanKESBANGPOL



class SKPDAsalJalanIrigasiJaringanKESBANGPOLInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanKESBANGPOL



class SKPDTujuanJalanIrigasiJaringanKESBANGPOLInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanKESBANGPOL



class FotoJalanIrigasiJaringanKESBANGPOLInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanKESBANGPOL





class HargaJalanIrigasiJaringanKESBANGPOLInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanKESBANGPOL

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=24)
        return super(HargaJalanIrigasiJaringanKESBANGPOLInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanKESBANGPOLInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanKESBANGPOL


class JalanIrigasiJaringanKESBANGPOLAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKESBANGPOLInline,
                    SKPDAsalJalanIrigasiJaringanKESBANGPOLInline,
                    FotoJalanIrigasiJaringanKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        return super(JalanIrigasiJaringanKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusKESBANGPOLAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanKESBANGPOLInline,
                    SKPDAsalJalanIrigasiJaringanKESBANGPOLInline,
                    FotoJalanIrigasiJaringanKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanKESBANGPOLAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanKESBANGPOLInline,
                    SKPDAsalJalanIrigasiJaringanKESBANGPOLInline,
                    FotoJalanIrigasiJaringanKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        return super(KDPJalanIrigasiJaringanKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanKESBANGPOLAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=24)
        return super(KontrakJalanIrigasiJaringanKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=24)



class HargaJalanIrigasiJaringanKESBANGPOLAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanKESBANGPOLAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanKESBANGPOLInline, TahunBerkurangJalanIrigasiJaringanKESBANGPOLInline,
                    SKPDAsalJalanIrigasiJaringanKESBANGPOLInline,
                    SKPDTujuanJalanIrigasiJaringanKESBANGPOLInline,
                    FotoJalanIrigasiJaringanKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan KESBANGPOL
admin.site.register(JalanIrigasiJaringanKESBANGPOL, JalanIrigasiJaringanKESBANGPOLAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusKESBANGPOL, JalanIrigasiJaringanUsulHapusKESBANGPOLAdmin)
admin.site.register(KDPJalanIrigasiJaringanKESBANGPOL, KDPJalanIrigasiJaringanKESBANGPOLAdmin)
admin.site.register(KontrakJalanIrigasiJaringanKESBANGPOL, KontrakJalanIrigasiJaringanKESBANGPOLAdmin)
admin.site.register(HargaJalanIrigasiJaringanKESBANGPOL, HargaJalanIrigasiJaringanKESBANGPOLAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanKESBANGPOL, JalanIrigasiJaringanPenghapusanKESBANGPOLAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLKESBANGPOL, KontrakATLKESBANGPOL, HargaATLKESBANGPOL, ATLUsulHapusKESBANGPOL, TahunBerkurangUsulHapusATLKESBANGPOL

from atl.models import ATLPenghapusanKESBANGPOL, TahunBerkurangATLKESBANGPOL, PenghapusanATLKESBANGPOL

from atl.models import SKPDAsalATLKESBANGPOL, SKPDTujuanATLKESBANGPOL, FotoATLKESBANGPOL

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLKESBANGPOLInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLKESBANGPOL



class PenghapusanATLKESBANGPOLInline(PenghapusanATLInline):
    model = PenghapusanATLKESBANGPOL



class SKPDAsalATLKESBANGPOLInline(SKPDAsalATLInline):
    model = SKPDAsalATLKESBANGPOL



class SKPDTujuanATLKESBANGPOLInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLKESBANGPOL



class FotoATLKESBANGPOLInline(FotoATLInline):
    model = FotoATLKESBANGPOL



class HargaATLKESBANGPOLInline(HargaATLInline):
    model = HargaATLKESBANGPOL

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=24)
        return super(HargaATLKESBANGPOLInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLKESBANGPOLInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLKESBANGPOL


class ATLKESBANGPOLAdmin(ATLAdmin):
    inlines = [HargaATLKESBANGPOLInline,
                    SKPDAsalATLKESBANGPOLInline,
                    FotoATLKESBANGPOLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=24)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=24)
        return super(ATLKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusKESBANGPOLAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLKESBANGPOLInline,
                    SKPDAsalATLKESBANGPOLInline,
                    FotoATLKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLKESBANGPOLAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=24)
        return super(KontrakATLKESBANGPOLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=24)



class HargaATLKESBANGPOLAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanKESBANGPOLAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLKESBANGPOLInline, TahunBerkurangATLKESBANGPOLInline,
                    SKPDAsalATLKESBANGPOLInline,
                    SKPDTujuanATLKESBANGPOLInline,
                    FotoATLKESBANGPOLInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=24)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL KESBANGPOL
admin.site.register(ATLKESBANGPOL, ATLKESBANGPOLAdmin)
admin.site.register(ATLUsulHapusKESBANGPOL, ATLUsulHapusKESBANGPOLAdmin)
admin.site.register(KontrakATLKESBANGPOL, KontrakATLKESBANGPOLAdmin)
admin.site.register(HargaATLKESBANGPOL, HargaATLKESBANGPOLAdmin)
admin.site.register(ATLPenghapusanKESBANGPOL, ATLPenghapusanKESBANGPOLAdmin)
