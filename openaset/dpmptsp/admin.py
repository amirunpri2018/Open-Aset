### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDPMPTSP, KontrakTanahDPMPTSP, HargaTanahDPMPTSP, TanahUsulHapusDPMPTSP, TahunBerkurangUsulHapusTanahDPMPTSP

from umum.models import TanahPenghapusanDPMPTSP, TahunBerkurangTanahDPMPTSP, PenghapusanTanahDPMPTSP

from umum.models import SKPDAsalTanahDPMPTSP, SKPDTujuanTanahDPMPTSP, FotoTanahDPMPTSP

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDPMPTSP, KontrakGedungBangunanDPMPTSP, HargaGedungBangunanDPMPTSP, GedungBangunanRuanganDPMPTSP, GedungBangunanUsulHapusDPMPTSP, TahunBerkurangUsulHapusGedungDPMPTSP

from gedungbangunan.models import GedungBangunanPenghapusanDPMPTSP, TahunBerkurangGedungBangunanDPMPTSP, PenghapusanGedungBangunanDPMPTSP

from gedungbangunan.models import SKPDAsalGedungBangunanDPMPTSP, SKPDTujuanGedungBangunanDPMPTSP, FotoGedungBangunanDPMPTSP

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDPMPTSP, KontrakPeralatanMesinDPMPTSP, HargaPeralatanMesinDPMPTSP, PeralatanMesinUsulHapusDPMPTSP, TahunBerkurangUsulHapusPeralatanMesinDPMPTSP

from peralatanmesin.models import PeralatanMesinPenghapusanDPMPTSP, TahunBerkurangPeralatanMesinDPMPTSP, PenghapusanPeralatanMesinDPMPTSP

from peralatanmesin.models import SKPDAsalPeralatanMesinDPMPTSP, SKPDTujuanPeralatanMesinDPMPTSP, FotoPeralatanMesinDPMPTSP

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDPMPTSPInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDPMPTSP



class PenghapusanTanahDPMPTSPInline(PenghapusanTanahInline):
    model = PenghapusanTanahDPMPTSP



class SKPDAsalTanahDPMPTSPInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDPMPTSP



class SKPDTujuanTanahDPMPTSPInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDPMPTSP



class FotoTanahDPMPTSPInline(FotoTanahInline):
    model = FotoTanahDPMPTSP



class GedungBangunanDPMPTSPInline(GedungBangunanInline):
    model = GedungBangunanDPMPTSP



class HargaTanahDPMPTSPInline(HargaTanahInline):
    model = HargaTanahDPMPTSP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=18)
        return super(HargaTanahDPMPTSPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDPMPTSPInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDPMPTSP


class TanahDPMPTSPAdmin(TanahAdmin):
    inlines = [HargaTanahDPMPTSPInline,
                SKPDAsalTanahDPMPTSPInline,
                FotoTanahDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        return super(TanahDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDPMPTSPAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDPMPTSPInline,
                SKPDAsalTanahDPMPTSPInline,
                FotoTanahDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDPMPTSPAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=18)
        return super(KontrakTanahDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=18)



class HargaTanahDPMPTSPAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDPMPTSPAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDPMPTSPInline, TahunBerkurangTanahDPMPTSPInline,
                    SKPDAsalTanahDPMPTSPInline,
                    SKPDTujuanTanahDPMPTSPInline,
                    FotoTanahDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DPMPTSP
admin.site.register(TanahDPMPTSP, TanahDPMPTSPAdmin)
admin.site.register(TanahUsulHapusDPMPTSP, TanahUsulHapusDPMPTSPAdmin)
admin.site.register(KontrakTanahDPMPTSP, KontrakTanahDPMPTSPAdmin)
admin.site.register(HargaTanahDPMPTSP, HargaTanahDPMPTSPAdmin)
admin.site.register(TanahPenghapusanDPMPTSP, TanahPenghapusanDPMPTSPAdmin)



from gedungbangunan.models import KDPGedungBangunanDPMPTSP


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDPMPTSPInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDPMPTSP



class PenghapusanGedungBangunanDPMPTSPInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDPMPTSP



class SKPDAsalGedungBangunanDPMPTSPInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDPMPTSP



class SKPDTujuanGedungBangunanDPMPTSPInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDPMPTSP



class FotoGedungBangunanDPMPTSPInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDPMPTSP



class HargaGedungBangunanDPMPTSPInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDPMPTSP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=18)
        return super(HargaGedungBangunanDPMPTSPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDPMPTSPInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDPMPTSP


class GedungBangunanDPMPTSPAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPMPTSPInline,
                SKPDAsalGedungBangunanDPMPTSPInline,
                FotoGedungBangunanDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        return super(GedungBangunanDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDPMPTSPAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPMPTSPInline,
                SKPDAsalGedungBangunanDPMPTSPInline,
                FotoGedungBangunanDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        return super(KDPGedungBangunanDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDPMPTSPAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDPMPTSPAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDPMPTSPInline,
                    SKPDAsalGedungBangunanDPMPTSPInline,
                    FotoGedungBangunanDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDPMPTSPAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=18)
        return super(KontrakGedungBangunanDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=18)



class HargaGedungBangunanDPMPTSPAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDPMPTSPAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDPMPTSPInline, TahunBerkurangGedungBangunanDPMPTSPInline,
                    SKPDAsalGedungBangunanDPMPTSPInline,
                    SKPDTujuanGedungBangunanDPMPTSPInline,
                    FotoGedungBangunanDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DPMPTSP
admin.site.register(GedungBangunanDPMPTSP, GedungBangunanDPMPTSPAdmin)
admin.site.register(KDPGedungBangunanDPMPTSP, KDPGedungBangunanDPMPTSPAdmin)
admin.site.register(GedungBangunanRuanganDPMPTSP, GedungBangunanRuanganDPMPTSPAdmin)
admin.site.register(GedungBangunanUsulHapusDPMPTSP, GedungBangunanUsulHapusDPMPTSPAdmin)
admin.site.register(KontrakGedungBangunanDPMPTSP, KontrakGedungBangunanDPMPTSPAdmin)
admin.site.register(HargaGedungBangunanDPMPTSP, HargaGedungBangunanDPMPTSPAdmin)
admin.site.register(GedungBangunanPenghapusanDPMPTSP, GedungBangunanPenghapusanDPMPTSPAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDPMPTSPInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDPMPTSP



class PenghapusanPeralatanMesinDPMPTSPInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDPMPTSP



class SKPDAsalPeralatanMesinDPMPTSPInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDPMPTSP



class SKPDTujuanPeralatanMesinDPMPTSPInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDPMPTSP



class FotoPeralatanMesinDPMPTSPInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDPMPTSP



class HargaPeralatanMesinDPMPTSPInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDPMPTSP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=18)
        return super(HargaPeralatanMesinDPMPTSPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDPMPTSPInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDPMPTSP


class PeralatanMesinDPMPTSPAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDPMPTSPInline,
                    SKPDAsalPeralatanMesinDPMPTSPInline,
                    FotoPeralatanMesinDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=18)
        return super(PeralatanMesinDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDPMPTSPAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDPMPTSPInline,
                    SKPDAsalPeralatanMesinDPMPTSPInline,
                    FotoPeralatanMesinDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDPMPTSPAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=18)
        return super(KontrakPeralatanMesinDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=18)



class HargaPeralatanMesinDPMPTSPAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDPMPTSPAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDPMPTSPInline, TahunBerkurangPeralatanMesinDPMPTSPInline,
                    SKPDAsalPeralatanMesinDPMPTSPInline,
                    SKPDTujuanPeralatanMesinDPMPTSPInline,
                    FotoPeralatanMesinDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DPMPTSP
admin.site.register(PeralatanMesinDPMPTSP, PeralatanMesinDPMPTSPAdmin)
admin.site.register(PeralatanMesinUsulHapusDPMPTSP, PeralatanMesinUsulHapusDPMPTSPAdmin)
admin.site.register(KontrakPeralatanMesinDPMPTSP, KontrakPeralatanMesinDPMPTSPAdmin)
admin.site.register(HargaPeralatanMesinDPMPTSP, HargaPeralatanMesinDPMPTSPAdmin)
admin.site.register(PeralatanMesinPenghapusanDPMPTSP, PeralatanMesinPenghapusanDPMPTSPAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDPMPTSP, KontrakJalanIrigasiJaringanDPMPTSP, HargaJalanIrigasiJaringanDPMPTSP, KDPJalanIrigasiJaringanDPMPTSP, JalanIrigasiJaringanUsulHapusDPMPTSP, TahunBerkurangUsulHapusJalanIrigasiJaringanDPMPTSP

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDPMPTSP, TahunBerkurangJalanIrigasiJaringanDPMPTSP, PenghapusanJalanIrigasiJaringanDPMPTSP

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDPMPTSP, SKPDTujuanJalanIrigasiJaringanDPMPTSP, FotoJalanIrigasiJaringanDPMPTSP

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDPMPTSPInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDPMPTSP



class PenghapusanJalanIrigasiJaringanDPMPTSPInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDPMPTSP



class SKPDAsalJalanIrigasiJaringanDPMPTSPInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDPMPTSP



class SKPDTujuanJalanIrigasiJaringanDPMPTSPInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDPMPTSP



class FotoJalanIrigasiJaringanDPMPTSPInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDPMPTSP





class HargaJalanIrigasiJaringanDPMPTSPInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDPMPTSP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=18)
        return super(HargaJalanIrigasiJaringanDPMPTSPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPMPTSPInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDPMPTSP


class JalanIrigasiJaringanDPMPTSPAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPMPTSPInline,
                    SKPDAsalJalanIrigasiJaringanDPMPTSPInline,
                    FotoJalanIrigasiJaringanDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        return super(JalanIrigasiJaringanDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDPMPTSPAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDPMPTSPInline,
                    SKPDAsalJalanIrigasiJaringanDPMPTSPInline,
                    FotoJalanIrigasiJaringanDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDPMPTSPAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPMPTSPInline,
                    SKPDAsalJalanIrigasiJaringanDPMPTSPInline,
                    FotoJalanIrigasiJaringanDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        return super(KDPJalanIrigasiJaringanDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDPMPTSPAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=18)
        return super(KontrakJalanIrigasiJaringanDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=18)



class HargaJalanIrigasiJaringanDPMPTSPAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDPMPTSPAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDPMPTSPInline, TahunBerkurangJalanIrigasiJaringanDPMPTSPInline,
                    SKPDAsalJalanIrigasiJaringanDPMPTSPInline,
                    SKPDTujuanJalanIrigasiJaringanDPMPTSPInline,
                    FotoJalanIrigasiJaringanDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DPMPTSP
admin.site.register(JalanIrigasiJaringanDPMPTSP, JalanIrigasiJaringanDPMPTSPAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDPMPTSP, JalanIrigasiJaringanUsulHapusDPMPTSPAdmin)
admin.site.register(KDPJalanIrigasiJaringanDPMPTSP, KDPJalanIrigasiJaringanDPMPTSPAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDPMPTSP, KontrakJalanIrigasiJaringanDPMPTSPAdmin)
admin.site.register(HargaJalanIrigasiJaringanDPMPTSP, HargaJalanIrigasiJaringanDPMPTSPAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDPMPTSP, JalanIrigasiJaringanPenghapusanDPMPTSPAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDPMPTSP, KontrakATLDPMPTSP, HargaATLDPMPTSP, ATLUsulHapusDPMPTSP, TahunBerkurangUsulHapusATLDPMPTSP

from atl.models import ATLPenghapusanDPMPTSP, TahunBerkurangATLDPMPTSP, PenghapusanATLDPMPTSP

from atl.models import SKPDAsalATLDPMPTSP, SKPDTujuanATLDPMPTSP, FotoATLDPMPTSP

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDPMPTSPInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDPMPTSP



class PenghapusanATLDPMPTSPInline(PenghapusanATLInline):
    model = PenghapusanATLDPMPTSP



class SKPDAsalATLDPMPTSPInline(SKPDAsalATLInline):
    model = SKPDAsalATLDPMPTSP



class SKPDTujuanATLDPMPTSPInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDPMPTSP



class FotoATLDPMPTSPInline(FotoATLInline):
    model = FotoATLDPMPTSP



class HargaATLDPMPTSPInline(HargaATLInline):
    model = HargaATLDPMPTSP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=18)
        return super(HargaATLDPMPTSPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDPMPTSPInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDPMPTSP


class ATLDPMPTSPAdmin(ATLAdmin):
    inlines = [HargaATLDPMPTSPInline,
                    SKPDAsalATLDPMPTSPInline,
                    FotoATLDPMPTSPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=18)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=18)
        return super(ATLDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDPMPTSPAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDPMPTSPInline,
                    SKPDAsalATLDPMPTSPInline,
                    FotoATLDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDPMPTSPAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=18)
        return super(KontrakATLDPMPTSPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=18)



class HargaATLDPMPTSPAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDPMPTSPAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDPMPTSPInline, TahunBerkurangATLDPMPTSPInline,
                    SKPDAsalATLDPMPTSPInline,
                    SKPDTujuanATLDPMPTSPInline,
                    FotoATLDPMPTSPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=18)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DPMPTSP
admin.site.register(ATLDPMPTSP, ATLDPMPTSPAdmin)
admin.site.register(ATLUsulHapusDPMPTSP, ATLUsulHapusDPMPTSPAdmin)
admin.site.register(KontrakATLDPMPTSP, KontrakATLDPMPTSPAdmin)
admin.site.register(HargaATLDPMPTSP, HargaATLDPMPTSPAdmin)
admin.site.register(ATLPenghapusanDPMPTSP, ATLPenghapusanDPMPTSPAdmin)
