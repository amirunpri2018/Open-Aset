### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDPPPA, KontrakTanahDPPPA, HargaTanahDPPPA, TanahUsulHapusDPPPA, TahunBerkurangUsulHapusTanahDPPPA

from umum.models import TanahPenghapusanDPPPA, TahunBerkurangTanahDPPPA, PenghapusanTanahDPPPA

from umum.models import SKPDAsalTanahDPPPA, SKPDTujuanTanahDPPPA, FotoTanahDPPPA

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDPPPA, KontrakGedungBangunanDPPPA, HargaGedungBangunanDPPPA, GedungBangunanRuanganDPPPA, GedungBangunanUsulHapusDPPPA, TahunBerkurangUsulHapusGedungDPPPA

from gedungbangunan.models import GedungBangunanPenghapusanDPPPA, TahunBerkurangGedungBangunanDPPPA, PenghapusanGedungBangunanDPPPA

from gedungbangunan.models import SKPDAsalGedungBangunanDPPPA, SKPDTujuanGedungBangunanDPPPA, FotoGedungBangunanDPPPA

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDPPPA, KontrakPeralatanMesinDPPPA, HargaPeralatanMesinDPPPA, PeralatanMesinUsulHapusDPPPA, TahunBerkurangUsulHapusPeralatanMesinDPPPA

from peralatanmesin.models import PeralatanMesinPenghapusanDPPPA, TahunBerkurangPeralatanMesinDPPPA, PenghapusanPeralatanMesinDPPPA

from peralatanmesin.models import SKPDAsalPeralatanMesinDPPPA, SKPDTujuanPeralatanMesinDPPPA, FotoPeralatanMesinDPPPA

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDPPPAInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDPPPA



class PenghapusanTanahDPPPAInline(PenghapusanTanahInline):
    model = PenghapusanTanahDPPPA



class SKPDAsalTanahDPPPAInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDPPPA



class SKPDTujuanTanahDPPPAInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDPPPA



class FotoTanahDPPPAInline(FotoTanahInline):
    model = FotoTanahDPPPA



class GedungBangunanDPPPAInline(GedungBangunanInline):
    model = GedungBangunanDPPPA



class HargaTanahDPPPAInline(HargaTanahInline):
    model = HargaTanahDPPPA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=11)
        return super(HargaTanahDPPPAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDPPPAInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDPPPA


class TanahDPPPAAdmin(TanahAdmin):
    inlines = [HargaTanahDPPPAInline,
                SKPDAsalTanahDPPPAInline,
                FotoTanahDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        return super(TanahDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDPPPAAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDPPPAInline,
                SKPDAsalTanahDPPPAInline,
                FotoTanahDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDPPPAAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=11)
        return super(KontrakTanahDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=11)



class HargaTanahDPPPAAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDPPPAAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDPPPAInline, TahunBerkurangTanahDPPPAInline,
                    SKPDAsalTanahDPPPAInline,
                    SKPDTujuanTanahDPPPAInline,
                    FotoTanahDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DPPPA
admin.site.register(TanahDPPPA, TanahDPPPAAdmin)
admin.site.register(TanahUsulHapusDPPPA, TanahUsulHapusDPPPAAdmin)
admin.site.register(KontrakTanahDPPPA, KontrakTanahDPPPAAdmin)
admin.site.register(HargaTanahDPPPA, HargaTanahDPPPAAdmin)
admin.site.register(TanahPenghapusanDPPPA, TanahPenghapusanDPPPAAdmin)



from gedungbangunan.models import KDPGedungBangunanDPPPA


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDPPPAInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDPPPA



class PenghapusanGedungBangunanDPPPAInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDPPPA



class SKPDAsalGedungBangunanDPPPAInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDPPPA



class SKPDTujuanGedungBangunanDPPPAInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDPPPA



class FotoGedungBangunanDPPPAInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDPPPA



class HargaGedungBangunanDPPPAInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDPPPA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=11)
        return super(HargaGedungBangunanDPPPAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDPPPAInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDPPPA


class GedungBangunanDPPPAAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPPPAInline,
                SKPDAsalGedungBangunanDPPPAInline,
                FotoGedungBangunanDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        return super(GedungBangunanDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDPPPAAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPPPAInline,
                SKPDAsalGedungBangunanDPPPAInline,
                FotoGedungBangunanDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        return super(KDPGedungBangunanDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDPPPAAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDPPPAAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDPPPAInline,
                    SKPDAsalGedungBangunanDPPPAInline,
                    FotoGedungBangunanDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDPPPAAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=11)
        return super(KontrakGedungBangunanDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=11)



class HargaGedungBangunanDPPPAAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDPPPAAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDPPPAInline, TahunBerkurangGedungBangunanDPPPAInline,
                    SKPDAsalGedungBangunanDPPPAInline,
                    SKPDTujuanGedungBangunanDPPPAInline,
                    FotoGedungBangunanDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DPPPA
admin.site.register(GedungBangunanDPPPA, GedungBangunanDPPPAAdmin)
admin.site.register(KDPGedungBangunanDPPPA, KDPGedungBangunanDPPPAAdmin)
admin.site.register(GedungBangunanRuanganDPPPA, GedungBangunanRuanganDPPPAAdmin)
admin.site.register(GedungBangunanUsulHapusDPPPA, GedungBangunanUsulHapusDPPPAAdmin)
admin.site.register(KontrakGedungBangunanDPPPA, KontrakGedungBangunanDPPPAAdmin)
admin.site.register(HargaGedungBangunanDPPPA, HargaGedungBangunanDPPPAAdmin)
admin.site.register(GedungBangunanPenghapusanDPPPA, GedungBangunanPenghapusanDPPPAAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDPPPAInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDPPPA



class PenghapusanPeralatanMesinDPPPAInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDPPPA



class SKPDAsalPeralatanMesinDPPPAInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDPPPA



class SKPDTujuanPeralatanMesinDPPPAInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDPPPA



class FotoPeralatanMesinDPPPAInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDPPPA



class HargaPeralatanMesinDPPPAInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDPPPA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=11)
        return super(HargaPeralatanMesinDPPPAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDPPPAInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDPPPA


class PeralatanMesinDPPPAAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDPPPAInline,
                    SKPDAsalPeralatanMesinDPPPAInline,
                    FotoPeralatanMesinDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=11)
        return super(PeralatanMesinDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDPPPAAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDPPPAInline,
                    SKPDAsalPeralatanMesinDPPPAInline,
                    FotoPeralatanMesinDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDPPPAAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=11)
        return super(KontrakPeralatanMesinDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=11)



class HargaPeralatanMesinDPPPAAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDPPPAAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDPPPAInline, TahunBerkurangPeralatanMesinDPPPAInline,
                    SKPDAsalPeralatanMesinDPPPAInline,
                    SKPDTujuanPeralatanMesinDPPPAInline,
                    FotoPeralatanMesinDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DPPPA
admin.site.register(PeralatanMesinDPPPA, PeralatanMesinDPPPAAdmin)
admin.site.register(PeralatanMesinUsulHapusDPPPA, PeralatanMesinUsulHapusDPPPAAdmin)
admin.site.register(KontrakPeralatanMesinDPPPA, KontrakPeralatanMesinDPPPAAdmin)
admin.site.register(HargaPeralatanMesinDPPPA, HargaPeralatanMesinDPPPAAdmin)
admin.site.register(PeralatanMesinPenghapusanDPPPA, PeralatanMesinPenghapusanDPPPAAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDPPPA, KontrakJalanIrigasiJaringanDPPPA, HargaJalanIrigasiJaringanDPPPA, KDPJalanIrigasiJaringanDPPPA, JalanIrigasiJaringanUsulHapusDPPPA, TahunBerkurangUsulHapusJalanIrigasiJaringanDPPPA

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDPPPA, TahunBerkurangJalanIrigasiJaringanDPPPA, PenghapusanJalanIrigasiJaringanDPPPA

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDPPPA, SKPDTujuanJalanIrigasiJaringanDPPPA, FotoJalanIrigasiJaringanDPPPA

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDPPPAInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDPPPA



class PenghapusanJalanIrigasiJaringanDPPPAInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDPPPA



class SKPDAsalJalanIrigasiJaringanDPPPAInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDPPPA



class SKPDTujuanJalanIrigasiJaringanDPPPAInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDPPPA



class FotoJalanIrigasiJaringanDPPPAInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDPPPA





class HargaJalanIrigasiJaringanDPPPAInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDPPPA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=11)
        return super(HargaJalanIrigasiJaringanDPPPAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPPPAInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDPPPA


class JalanIrigasiJaringanDPPPAAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPPPAInline,
                    SKPDAsalJalanIrigasiJaringanDPPPAInline,
                    FotoJalanIrigasiJaringanDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        return super(JalanIrigasiJaringanDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDPPPAAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDPPPAInline,
                    SKPDAsalJalanIrigasiJaringanDPPPAInline,
                    FotoJalanIrigasiJaringanDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDPPPAAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPPPAInline,
                    SKPDAsalJalanIrigasiJaringanDPPPAInline,
                    FotoJalanIrigasiJaringanDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        return super(KDPJalanIrigasiJaringanDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDPPPAAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=11)
        return super(KontrakJalanIrigasiJaringanDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=11)



class HargaJalanIrigasiJaringanDPPPAAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDPPPAAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDPPPAInline, TahunBerkurangJalanIrigasiJaringanDPPPAInline,
                    SKPDAsalJalanIrigasiJaringanDPPPAInline,
                    SKPDTujuanJalanIrigasiJaringanDPPPAInline,
                    FotoJalanIrigasiJaringanDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DPPPA
admin.site.register(JalanIrigasiJaringanDPPPA, JalanIrigasiJaringanDPPPAAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDPPPA, JalanIrigasiJaringanUsulHapusDPPPAAdmin)
admin.site.register(KDPJalanIrigasiJaringanDPPPA, KDPJalanIrigasiJaringanDPPPAAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDPPPA, KontrakJalanIrigasiJaringanDPPPAAdmin)
admin.site.register(HargaJalanIrigasiJaringanDPPPA, HargaJalanIrigasiJaringanDPPPAAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDPPPA, JalanIrigasiJaringanPenghapusanDPPPAAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDPPPA, KontrakATLDPPPA, HargaATLDPPPA, ATLUsulHapusDPPPA, TahunBerkurangUsulHapusATLDPPPA

from atl.models import ATLPenghapusanDPPPA, TahunBerkurangATLDPPPA, PenghapusanATLDPPPA

from atl.models import SKPDAsalATLDPPPA, SKPDTujuanATLDPPPA, FotoATLDPPPA

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDPPPAInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDPPPA



class PenghapusanATLDPPPAInline(PenghapusanATLInline):
    model = PenghapusanATLDPPPA



class SKPDAsalATLDPPPAInline(SKPDAsalATLInline):
    model = SKPDAsalATLDPPPA



class SKPDTujuanATLDPPPAInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDPPPA



class FotoATLDPPPAInline(FotoATLInline):
    model = FotoATLDPPPA



class HargaATLDPPPAInline(HargaATLInline):
    model = HargaATLDPPPA

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=11)
        return super(HargaATLDPPPAInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDPPPAInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDPPPA


class ATLDPPPAAdmin(ATLAdmin):
    inlines = [HargaATLDPPPAInline,
                    SKPDAsalATLDPPPAInline,
                    FotoATLDPPPAInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=11)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=11)
        return super(ATLDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDPPPAAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDPPPAInline,
                    SKPDAsalATLDPPPAInline,
                    FotoATLDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDPPPAAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=11)
        return super(KontrakATLDPPPAAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=11)



class HargaATLDPPPAAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDPPPAAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDPPPAInline, TahunBerkurangATLDPPPAInline,
                    SKPDAsalATLDPPPAInline,
                    SKPDTujuanATLDPPPAInline,
                    FotoATLDPPPAInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=11)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DPPPA
admin.site.register(ATLDPPPA, ATLDPPPAAdmin)
admin.site.register(ATLUsulHapusDPPPA, ATLUsulHapusDPPPAAdmin)
admin.site.register(KontrakATLDPPPA, KontrakATLDPPPAAdmin)
admin.site.register(HargaATLDPPPA, HargaATLDPPPAAdmin)
admin.site.register(ATLPenghapusanDPPPA, ATLPenghapusanDPPPAAdmin)
