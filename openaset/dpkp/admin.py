### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDPKP, KontrakTanahDPKP, HargaTanahDPKP, TanahUsulHapusDPKP, TahunBerkurangUsulHapusTanahDPKP

from umum.models import TanahPenghapusanDPKP, TahunBerkurangTanahDPKP, PenghapusanTanahDPKP

from umum.models import SKPDAsalTanahDPKP, SKPDTujuanTanahDPKP, FotoTanahDPKP

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDPKP, KontrakGedungBangunanDPKP, HargaGedungBangunanDPKP, GedungBangunanRuanganDPKP, GedungBangunanUsulHapusDPKP, TahunBerkurangUsulHapusGedungDPKP

from gedungbangunan.models import GedungBangunanPenghapusanDPKP, TahunBerkurangGedungBangunanDPKP, PenghapusanGedungBangunanDPKP

from gedungbangunan.models import SKPDAsalGedungBangunanDPKP, SKPDTujuanGedungBangunanDPKP, FotoGedungBangunanDPKP

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDPKP, KontrakPeralatanMesinDPKP, HargaPeralatanMesinDPKP, PeralatanMesinUsulHapusDPKP, TahunBerkurangUsulHapusPeralatanMesinDPKP

from peralatanmesin.models import PeralatanMesinPenghapusanDPKP, TahunBerkurangPeralatanMesinDPKP, PenghapusanPeralatanMesinDPKP

from peralatanmesin.models import SKPDAsalPeralatanMesinDPKP, SKPDTujuanPeralatanMesinDPKP, FotoPeralatanMesinDPKP

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDPKPInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDPKP



class PenghapusanTanahDPKPInline(PenghapusanTanahInline):
    model = PenghapusanTanahDPKP



class SKPDAsalTanahDPKPInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDPKP



class SKPDTujuanTanahDPKPInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDPKP



class FotoTanahDPKPInline(FotoTanahInline):
    model = FotoTanahDPKP



class GedungBangunanDPKPInline(GedungBangunanInline):
    model = GedungBangunanDPKP



class HargaTanahDPKPInline(HargaTanahInline):
    model = HargaTanahDPKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=40)
        return super(HargaTanahDPKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDPKPInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDPKP


class TanahDPKPAdmin(TanahAdmin):
    inlines = [HargaTanahDPKPInline,
                SKPDAsalTanahDPKPInline,
                FotoTanahDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        return super(TanahDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDPKPAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDPKPInline,
                SKPDAsalTanahDPKPInline,
                FotoTanahDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDPKPAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=40)
        return super(KontrakTanahDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=40)



class HargaTanahDPKPAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDPKPAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDPKPInline, TahunBerkurangTanahDPKPInline,
                    SKPDAsalTanahDPKPInline,
                    SKPDTujuanTanahDPKPInline,
                    FotoTanahDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DPKP
admin.site.register(TanahDPKP, TanahDPKPAdmin)
admin.site.register(TanahUsulHapusDPKP, TanahUsulHapusDPKPAdmin)
admin.site.register(KontrakTanahDPKP, KontrakTanahDPKPAdmin)
admin.site.register(HargaTanahDPKP, HargaTanahDPKPAdmin)
admin.site.register(TanahPenghapusanDPKP, TanahPenghapusanDPKPAdmin)



from gedungbangunan.models import KDPGedungBangunanDPKP


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDPKPInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDPKP



class PenghapusanGedungBangunanDPKPInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDPKP



class SKPDAsalGedungBangunanDPKPInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDPKP



class SKPDTujuanGedungBangunanDPKPInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDPKP



class FotoGedungBangunanDPKPInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDPKP



class HargaGedungBangunanDPKPInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDPKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=40)
        return super(HargaGedungBangunanDPKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDPKPInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDPKP


class GedungBangunanDPKPAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPKPInline,
                SKPDAsalGedungBangunanDPKPInline,
                FotoGedungBangunanDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        return super(GedungBangunanDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDPKPAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPKPInline,
                SKPDAsalGedungBangunanDPKPInline,
                FotoGedungBangunanDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        return super(KDPGedungBangunanDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDPKPAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDPKPAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDPKPInline,
                    SKPDAsalGedungBangunanDPKPInline,
                    FotoGedungBangunanDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDPKPAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=40)
        return super(KontrakGedungBangunanDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=40)



class HargaGedungBangunanDPKPAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDPKPAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDPKPInline, TahunBerkurangGedungBangunanDPKPInline,
                    SKPDAsalGedungBangunanDPKPInline,
                    SKPDTujuanGedungBangunanDPKPInline,
                    FotoGedungBangunanDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DPKP
admin.site.register(GedungBangunanDPKP, GedungBangunanDPKPAdmin)
admin.site.register(KDPGedungBangunanDPKP, KDPGedungBangunanDPKPAdmin)
admin.site.register(GedungBangunanRuanganDPKP, GedungBangunanRuanganDPKPAdmin)
admin.site.register(GedungBangunanUsulHapusDPKP, GedungBangunanUsulHapusDPKPAdmin)
admin.site.register(KontrakGedungBangunanDPKP, KontrakGedungBangunanDPKPAdmin)
admin.site.register(HargaGedungBangunanDPKP, HargaGedungBangunanDPKPAdmin)
admin.site.register(GedungBangunanPenghapusanDPKP, GedungBangunanPenghapusanDPKPAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDPKPInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDPKP



class PenghapusanPeralatanMesinDPKPInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDPKP



class SKPDAsalPeralatanMesinDPKPInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDPKP



class SKPDTujuanPeralatanMesinDPKPInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDPKP



class FotoPeralatanMesinDPKPInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDPKP



class HargaPeralatanMesinDPKPInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDPKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=40)
        return super(HargaPeralatanMesinDPKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDPKPInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDPKP


class PeralatanMesinDPKPAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDPKPInline,
                    SKPDAsalPeralatanMesinDPKPInline,
                    FotoPeralatanMesinDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=40)
        return super(PeralatanMesinDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDPKPAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDPKPInline,
                    SKPDAsalPeralatanMesinDPKPInline,
                    FotoPeralatanMesinDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDPKPAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=40)
        return super(KontrakPeralatanMesinDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=40)



class HargaPeralatanMesinDPKPAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDPKPAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDPKPInline, TahunBerkurangPeralatanMesinDPKPInline,
                    SKPDAsalPeralatanMesinDPKPInline,
                    SKPDTujuanPeralatanMesinDPKPInline,
                    FotoPeralatanMesinDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DPKP
admin.site.register(PeralatanMesinDPKP, PeralatanMesinDPKPAdmin)
admin.site.register(PeralatanMesinUsulHapusDPKP, PeralatanMesinUsulHapusDPKPAdmin)
admin.site.register(KontrakPeralatanMesinDPKP, KontrakPeralatanMesinDPKPAdmin)
admin.site.register(HargaPeralatanMesinDPKP, HargaPeralatanMesinDPKPAdmin)
admin.site.register(PeralatanMesinPenghapusanDPKP, PeralatanMesinPenghapusanDPKPAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDPKP, KontrakJalanIrigasiJaringanDPKP, HargaJalanIrigasiJaringanDPKP, KDPJalanIrigasiJaringanDPKP, JalanIrigasiJaringanUsulHapusDPKP, TahunBerkurangUsulHapusJalanIrigasiJaringanDPKP

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDPKP, TahunBerkurangJalanIrigasiJaringanDPKP, PenghapusanJalanIrigasiJaringanDPKP

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDPKP, SKPDTujuanJalanIrigasiJaringanDPKP, FotoJalanIrigasiJaringanDPKP

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDPKPInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDPKP



class PenghapusanJalanIrigasiJaringanDPKPInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDPKP



class SKPDAsalJalanIrigasiJaringanDPKPInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDPKP



class SKPDTujuanJalanIrigasiJaringanDPKPInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDPKP



class FotoJalanIrigasiJaringanDPKPInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDPKP





class HargaJalanIrigasiJaringanDPKPInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDPKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=40)
        return super(HargaJalanIrigasiJaringanDPKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPKPInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDPKP


class JalanIrigasiJaringanDPKPAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPKPInline,
                    SKPDAsalJalanIrigasiJaringanDPKPInline,
                    FotoJalanIrigasiJaringanDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        return super(JalanIrigasiJaringanDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDPKPAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDPKPInline,
                    SKPDAsalJalanIrigasiJaringanDPKPInline,
                    FotoJalanIrigasiJaringanDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDPKPAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPKPInline,
                    SKPDAsalJalanIrigasiJaringanDPKPInline,
                    FotoJalanIrigasiJaringanDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        return super(KDPJalanIrigasiJaringanDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDPKPAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=40)
        return super(KontrakJalanIrigasiJaringanDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=40)



class HargaJalanIrigasiJaringanDPKPAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDPKPAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDPKPInline, TahunBerkurangJalanIrigasiJaringanDPKPInline,
                    SKPDAsalJalanIrigasiJaringanDPKPInline,
                    SKPDTujuanJalanIrigasiJaringanDPKPInline,
                    FotoJalanIrigasiJaringanDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DPKP
admin.site.register(JalanIrigasiJaringanDPKP, JalanIrigasiJaringanDPKPAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDPKP, JalanIrigasiJaringanUsulHapusDPKPAdmin)
admin.site.register(KDPJalanIrigasiJaringanDPKP, KDPJalanIrigasiJaringanDPKPAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDPKP, KontrakJalanIrigasiJaringanDPKPAdmin)
admin.site.register(HargaJalanIrigasiJaringanDPKP, HargaJalanIrigasiJaringanDPKPAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDPKP, JalanIrigasiJaringanPenghapusanDPKPAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDPKP, KontrakATLDPKP, HargaATLDPKP, ATLUsulHapusDPKP, TahunBerkurangUsulHapusATLDPKP

from atl.models import ATLPenghapusanDPKP, TahunBerkurangATLDPKP, PenghapusanATLDPKP

from atl.models import SKPDAsalATLDPKP, SKPDTujuanATLDPKP, FotoATLDPKP

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDPKPInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDPKP



class PenghapusanATLDPKPInline(PenghapusanATLInline):
    model = PenghapusanATLDPKP



class SKPDAsalATLDPKPInline(SKPDAsalATLInline):
    model = SKPDAsalATLDPKP



class SKPDTujuanATLDPKPInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDPKP



class FotoATLDPKPInline(FotoATLInline):
    model = FotoATLDPKP



class HargaATLDPKPInline(HargaATLInline):
    model = HargaATLDPKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=40)
        return super(HargaATLDPKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDPKPInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDPKP


class ATLDPKPAdmin(ATLAdmin):
    inlines = [HargaATLDPKPInline,
                    SKPDAsalATLDPKPInline,
                    FotoATLDPKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=40)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=40)
        return super(ATLDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDPKPAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDPKPInline,
                    SKPDAsalATLDPKPInline,
                    FotoATLDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDPKPAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=40)
        return super(KontrakATLDPKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=40)



class HargaATLDPKPAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDPKPAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDPKPInline, TahunBerkurangATLDPKPInline,
                    SKPDAsalATLDPKPInline,
                    SKPDTujuanATLDPKPInline,
                    FotoATLDPKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=40)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DPKP
admin.site.register(ATLDPKP, ATLDPKPAdmin)
admin.site.register(ATLUsulHapusDPKP, ATLUsulHapusDPKPAdmin)
admin.site.register(KontrakATLDPKP, KontrakATLDPKPAdmin)
admin.site.register(HargaATLDPKP, HargaATLDPKPAdmin)
admin.site.register(ATLPenghapusanDPKP, ATLPenghapusanDPKPAdmin)
