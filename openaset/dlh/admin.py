### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDLH, KontrakTanahDLH, HargaTanahDLH, TanahUsulHapusDLH, TahunBerkurangUsulHapusTanahDLH

from umum.models import TanahPenghapusanDLH, TahunBerkurangTanahDLH, PenghapusanTanahDLH

from umum.models import SKPDAsalTanahDLH, SKPDTujuanTanahDLH, FotoTanahDLH

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDLH, KontrakGedungBangunanDLH, HargaGedungBangunanDLH, GedungBangunanRuanganDLH, GedungBangunanUsulHapusDLH, TahunBerkurangUsulHapusGedungDLH

from gedungbangunan.models import GedungBangunanPenghapusanDLH, TahunBerkurangGedungBangunanDLH, PenghapusanGedungBangunanDLH

from gedungbangunan.models import SKPDAsalGedungBangunanDLH, SKPDTujuanGedungBangunanDLH, FotoGedungBangunanDLH

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDLH, KontrakPeralatanMesinDLH, HargaPeralatanMesinDLH, PeralatanMesinUsulHapusDLH, TahunBerkurangUsulHapusPeralatanMesinDLH

from peralatanmesin.models import PeralatanMesinPenghapusanDLH, TahunBerkurangPeralatanMesinDLH, PenghapusanPeralatanMesinDLH

from peralatanmesin.models import SKPDAsalPeralatanMesinDLH, SKPDTujuanPeralatanMesinDLH, FotoPeralatanMesinDLH

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDLHInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDLH



class PenghapusanTanahDLHInline(PenghapusanTanahInline):
    model = PenghapusanTanahDLH



class SKPDAsalTanahDLHInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDLH



class SKPDTujuanTanahDLHInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDLH



class FotoTanahDLHInline(FotoTanahInline):
    model = FotoTanahDLH



class GedungBangunanDLHInline(GedungBangunanInline):
    model = GedungBangunanDLH



class HargaTanahDLHInline(HargaTanahInline):
    model = HargaTanahDLH

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=22)
        return super(HargaTanahDLHInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDLHInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDLH


class TanahDLHAdmin(TanahAdmin):
    inlines = [HargaTanahDLHInline,
                SKPDAsalTanahDLHInline,
                FotoTanahDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        return super(TanahDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDLHAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDLHInline,
                SKPDAsalTanahDLHInline,
                FotoTanahDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDLHAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=22)
        return super(KontrakTanahDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=22)



class HargaTanahDLHAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDLHAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDLHInline, TahunBerkurangTanahDLHInline,
                    SKPDAsalTanahDLHInline,
                    SKPDTujuanTanahDLHInline,
                    FotoTanahDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DLH
admin.site.register(TanahDLH, TanahDLHAdmin)
admin.site.register(TanahUsulHapusDLH, TanahUsulHapusDLHAdmin)
admin.site.register(KontrakTanahDLH, KontrakTanahDLHAdmin)
admin.site.register(HargaTanahDLH, HargaTanahDLHAdmin)
admin.site.register(TanahPenghapusanDLH, TanahPenghapusanDLHAdmin)



from gedungbangunan.models import KDPGedungBangunanDLH


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDLHInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDLH



class PenghapusanGedungBangunanDLHInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDLH



class SKPDAsalGedungBangunanDLHInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDLH



class SKPDTujuanGedungBangunanDLHInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDLH



class FotoGedungBangunanDLHInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDLH



class HargaGedungBangunanDLHInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDLH

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=22)
        return super(HargaGedungBangunanDLHInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDLHInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDLH


class GedungBangunanDLHAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDLHInline,
                SKPDAsalGedungBangunanDLHInline,
                FotoGedungBangunanDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        return super(GedungBangunanDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDLHAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDLHInline,
                SKPDAsalGedungBangunanDLHInline,
                FotoGedungBangunanDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        return super(KDPGedungBangunanDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDLHAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDLHAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDLHInline,
                    SKPDAsalGedungBangunanDLHInline,
                    FotoGedungBangunanDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDLHAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=22)
        return super(KontrakGedungBangunanDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=22)



class HargaGedungBangunanDLHAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDLHAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDLHInline, TahunBerkurangGedungBangunanDLHInline,
                    SKPDAsalGedungBangunanDLHInline,
                    SKPDTujuanGedungBangunanDLHInline,
                    FotoGedungBangunanDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DLH
admin.site.register(GedungBangunanDLH, GedungBangunanDLHAdmin)
admin.site.register(KDPGedungBangunanDLH, KDPGedungBangunanDLHAdmin)
admin.site.register(GedungBangunanRuanganDLH, GedungBangunanRuanganDLHAdmin)
admin.site.register(GedungBangunanUsulHapusDLH, GedungBangunanUsulHapusDLHAdmin)
admin.site.register(KontrakGedungBangunanDLH, KontrakGedungBangunanDLHAdmin)
admin.site.register(HargaGedungBangunanDLH, HargaGedungBangunanDLHAdmin)
admin.site.register(GedungBangunanPenghapusanDLH, GedungBangunanPenghapusanDLHAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDLHInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDLH



class PenghapusanPeralatanMesinDLHInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDLH



class SKPDAsalPeralatanMesinDLHInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDLH



class SKPDTujuanPeralatanMesinDLHInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDLH



class FotoPeralatanMesinDLHInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDLH



class HargaPeralatanMesinDLHInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDLH

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=22)
        return super(HargaPeralatanMesinDLHInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDLHInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDLH


class PeralatanMesinDLHAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDLHInline,
                    SKPDAsalPeralatanMesinDLHInline,
                    FotoPeralatanMesinDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=22)
        return super(PeralatanMesinDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDLHAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDLHInline,
                    SKPDAsalPeralatanMesinDLHInline,
                    FotoPeralatanMesinDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDLHAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=22)
        return super(KontrakPeralatanMesinDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=22)



class HargaPeralatanMesinDLHAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDLHAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDLHInline, TahunBerkurangPeralatanMesinDLHInline,
                    SKPDAsalPeralatanMesinDLHInline,
                    SKPDTujuanPeralatanMesinDLHInline,
                    FotoPeralatanMesinDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DLH
admin.site.register(PeralatanMesinDLH, PeralatanMesinDLHAdmin)
admin.site.register(PeralatanMesinUsulHapusDLH, PeralatanMesinUsulHapusDLHAdmin)
admin.site.register(KontrakPeralatanMesinDLH, KontrakPeralatanMesinDLHAdmin)
admin.site.register(HargaPeralatanMesinDLH, HargaPeralatanMesinDLHAdmin)
admin.site.register(PeralatanMesinPenghapusanDLH, PeralatanMesinPenghapusanDLHAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDLH, KontrakJalanIrigasiJaringanDLH, HargaJalanIrigasiJaringanDLH, KDPJalanIrigasiJaringanDLH, JalanIrigasiJaringanUsulHapusDLH, TahunBerkurangUsulHapusJalanIrigasiJaringanDLH

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDLH, TahunBerkurangJalanIrigasiJaringanDLH, PenghapusanJalanIrigasiJaringanDLH

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDLH, SKPDTujuanJalanIrigasiJaringanDLH, FotoJalanIrigasiJaringanDLH

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDLHInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDLH



class PenghapusanJalanIrigasiJaringanDLHInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDLH



class SKPDAsalJalanIrigasiJaringanDLHInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDLH



class SKPDTujuanJalanIrigasiJaringanDLHInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDLH



class FotoJalanIrigasiJaringanDLHInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDLH





class HargaJalanIrigasiJaringanDLHInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDLH

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=22)
        return super(HargaJalanIrigasiJaringanDLHInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDLHInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDLH


class JalanIrigasiJaringanDLHAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDLHInline,
                    SKPDAsalJalanIrigasiJaringanDLHInline,
                    FotoJalanIrigasiJaringanDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        return super(JalanIrigasiJaringanDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDLHAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDLHInline,
                    SKPDAsalJalanIrigasiJaringanDLHInline,
                    FotoJalanIrigasiJaringanDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDLHAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDLHInline,
                    SKPDAsalJalanIrigasiJaringanDLHInline,
                    FotoJalanIrigasiJaringanDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        return super(KDPJalanIrigasiJaringanDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDLHAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=22)
        return super(KontrakJalanIrigasiJaringanDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=22)



class HargaJalanIrigasiJaringanDLHAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDLHAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDLHInline, TahunBerkurangJalanIrigasiJaringanDLHInline,
                    SKPDAsalJalanIrigasiJaringanDLHInline,
                    SKPDTujuanJalanIrigasiJaringanDLHInline,
                    FotoJalanIrigasiJaringanDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DLH
admin.site.register(JalanIrigasiJaringanDLH, JalanIrigasiJaringanDLHAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDLH, JalanIrigasiJaringanUsulHapusDLHAdmin)
admin.site.register(KDPJalanIrigasiJaringanDLH, KDPJalanIrigasiJaringanDLHAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDLH, KontrakJalanIrigasiJaringanDLHAdmin)
admin.site.register(HargaJalanIrigasiJaringanDLH, HargaJalanIrigasiJaringanDLHAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDLH, JalanIrigasiJaringanPenghapusanDLHAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDLH, KontrakATLDLH, HargaATLDLH, ATLUsulHapusDLH, TahunBerkurangUsulHapusATLDLH

from atl.models import ATLPenghapusanDLH, TahunBerkurangATLDLH, PenghapusanATLDLH

from atl.models import SKPDAsalATLDLH, SKPDTujuanATLDLH, FotoATLDLH

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDLHInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDLH



class PenghapusanATLDLHInline(PenghapusanATLInline):
    model = PenghapusanATLDLH



class SKPDAsalATLDLHInline(SKPDAsalATLInline):
    model = SKPDAsalATLDLH



class SKPDTujuanATLDLHInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDLH



class FotoATLDLHInline(FotoATLInline):
    model = FotoATLDLH



class HargaATLDLHInline(HargaATLInline):
    model = HargaATLDLH

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=22)
        return super(HargaATLDLHInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDLHInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDLH


class ATLDLHAdmin(ATLAdmin):
    inlines = [HargaATLDLHInline,
                    SKPDAsalATLDLHInline,
                    FotoATLDLHInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=22)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=22)
        return super(ATLDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDLHAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDLHInline,
                    SKPDAsalATLDLHInline,
                    FotoATLDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDLHAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=22)
        return super(KontrakATLDLHAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=22)



class HargaATLDLHAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDLHAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDLHInline, TahunBerkurangATLDLHInline,
                    SKPDAsalATLDLHInline,
                    SKPDTujuanATLDLHInline,
                    FotoATLDLHInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=22)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DLH
admin.site.register(ATLDLH, ATLDLHAdmin)
admin.site.register(ATLUsulHapusDLH, ATLUsulHapusDLHAdmin)
admin.site.register(KontrakATLDLH, KontrakATLDLHAdmin)
admin.site.register(HargaATLDLH, HargaATLDLHAdmin)
admin.site.register(ATLPenghapusanDLH, ATLPenghapusanDLHAdmin)
