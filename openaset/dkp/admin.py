### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDKP, KontrakTanahDKP, HargaTanahDKP, TanahUsulHapusDKP, TahunBerkurangUsulHapusTanahDKP

from umum.models import TanahPenghapusanDKP, TahunBerkurangTanahDKP, PenghapusanTanahDKP

from umum.models import SKPDAsalTanahDKP, SKPDTujuanTanahDKP, FotoTanahDKP

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDKP, KontrakGedungBangunanDKP, HargaGedungBangunanDKP, GedungBangunanRuanganDKP, GedungBangunanUsulHapusDKP, TahunBerkurangUsulHapusGedungDKP

from gedungbangunan.models import GedungBangunanPenghapusanDKP, TahunBerkurangGedungBangunanDKP, PenghapusanGedungBangunanDKP

from gedungbangunan.models import SKPDAsalGedungBangunanDKP, SKPDTujuanGedungBangunanDKP, FotoGedungBangunanDKP

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDKP, KontrakPeralatanMesinDKP, HargaPeralatanMesinDKP, PeralatanMesinUsulHapusDKP, TahunBerkurangUsulHapusPeralatanMesinDKP

from peralatanmesin.models import PeralatanMesinPenghapusanDKP, TahunBerkurangPeralatanMesinDKP, PenghapusanPeralatanMesinDKP

from peralatanmesin.models import SKPDAsalPeralatanMesinDKP, SKPDTujuanPeralatanMesinDKP, FotoPeralatanMesinDKP

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDKPInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDKP



class PenghapusanTanahDKPInline(PenghapusanTanahInline):
    model = PenghapusanTanahDKP



class SKPDAsalTanahDKPInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDKP



class SKPDTujuanTanahDKPInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDKP



class FotoTanahDKPInline(FotoTanahInline):
    model = FotoTanahDKP



class GedungBangunanDKPInline(GedungBangunanInline):
    model = GedungBangunanDKP



class HargaTanahDKPInline(HargaTanahInline):
    model = HargaTanahDKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=15)
        return super(HargaTanahDKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDKPInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDKP


class TanahDKPAdmin(TanahAdmin):
    inlines = [HargaTanahDKPInline,
                SKPDAsalTanahDKPInline,
                FotoTanahDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        return super(TanahDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDKPAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDKPInline,
                SKPDAsalTanahDKPInline,
                FotoTanahDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDKPAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=15)
        return super(KontrakTanahDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=15)



class HargaTanahDKPAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDKPAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDKPInline, TahunBerkurangTanahDKPInline,
                    SKPDAsalTanahDKPInline,
                    SKPDTujuanTanahDKPInline,
                    FotoTanahDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DKP
admin.site.register(TanahDKP, TanahDKPAdmin)
admin.site.register(TanahUsulHapusDKP, TanahUsulHapusDKPAdmin)
admin.site.register(KontrakTanahDKP, KontrakTanahDKPAdmin)
admin.site.register(HargaTanahDKP, HargaTanahDKPAdmin)
admin.site.register(TanahPenghapusanDKP, TanahPenghapusanDKPAdmin)



from gedungbangunan.models import KDPGedungBangunanDKP


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDKPInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDKP



class PenghapusanGedungBangunanDKPInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDKP



class SKPDAsalGedungBangunanDKPInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDKP



class SKPDTujuanGedungBangunanDKPInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDKP



class FotoGedungBangunanDKPInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDKP



class HargaGedungBangunanDKPInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=15)
        return super(HargaGedungBangunanDKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDKPInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDKP


class GedungBangunanDKPAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDKPInline,
                SKPDAsalGedungBangunanDKPInline,
                FotoGedungBangunanDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        return super(GedungBangunanDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDKPAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDKPInline,
                SKPDAsalGedungBangunanDKPInline,
                FotoGedungBangunanDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        return super(KDPGedungBangunanDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDKPAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDKPAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDKPInline,
                    SKPDAsalGedungBangunanDKPInline,
                    FotoGedungBangunanDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDKPAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=15)
        return super(KontrakGedungBangunanDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=15)



class HargaGedungBangunanDKPAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDKPAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDKPInline, TahunBerkurangGedungBangunanDKPInline,
                    SKPDAsalGedungBangunanDKPInline,
                    SKPDTujuanGedungBangunanDKPInline,
                    FotoGedungBangunanDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DKP
admin.site.register(GedungBangunanDKP, GedungBangunanDKPAdmin)
admin.site.register(KDPGedungBangunanDKP, KDPGedungBangunanDKPAdmin)
admin.site.register(GedungBangunanRuanganDKP, GedungBangunanRuanganDKPAdmin)
admin.site.register(GedungBangunanUsulHapusDKP, GedungBangunanUsulHapusDKPAdmin)
admin.site.register(KontrakGedungBangunanDKP, KontrakGedungBangunanDKPAdmin)
admin.site.register(HargaGedungBangunanDKP, HargaGedungBangunanDKPAdmin)
admin.site.register(GedungBangunanPenghapusanDKP, GedungBangunanPenghapusanDKPAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDKPInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDKP



class PenghapusanPeralatanMesinDKPInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDKP



class SKPDAsalPeralatanMesinDKPInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDKP



class SKPDTujuanPeralatanMesinDKPInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDKP



class FotoPeralatanMesinDKPInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDKP



class HargaPeralatanMesinDKPInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=15)
        return super(HargaPeralatanMesinDKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDKPInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDKP


class PeralatanMesinDKPAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDKPInline,
                    SKPDAsalPeralatanMesinDKPInline,
                    FotoPeralatanMesinDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=15)
        return super(PeralatanMesinDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDKPAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDKPInline,
                    SKPDAsalPeralatanMesinDKPInline,
                    FotoPeralatanMesinDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDKPAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=15)
        return super(KontrakPeralatanMesinDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=15)



class HargaPeralatanMesinDKPAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDKPAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDKPInline, TahunBerkurangPeralatanMesinDKPInline,
                    SKPDAsalPeralatanMesinDKPInline,
                    SKPDTujuanPeralatanMesinDKPInline,
                    FotoPeralatanMesinDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DKP
admin.site.register(PeralatanMesinDKP, PeralatanMesinDKPAdmin)
admin.site.register(PeralatanMesinUsulHapusDKP, PeralatanMesinUsulHapusDKPAdmin)
admin.site.register(KontrakPeralatanMesinDKP, KontrakPeralatanMesinDKPAdmin)
admin.site.register(HargaPeralatanMesinDKP, HargaPeralatanMesinDKPAdmin)
admin.site.register(PeralatanMesinPenghapusanDKP, PeralatanMesinPenghapusanDKPAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDKP, KontrakJalanIrigasiJaringanDKP, HargaJalanIrigasiJaringanDKP, KDPJalanIrigasiJaringanDKP, JalanIrigasiJaringanUsulHapusDKP, TahunBerkurangUsulHapusJalanIrigasiJaringanDKP

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDKP, TahunBerkurangJalanIrigasiJaringanDKP, PenghapusanJalanIrigasiJaringanDKP

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDKP, SKPDTujuanJalanIrigasiJaringanDKP, FotoJalanIrigasiJaringanDKP

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDKPInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDKP



class PenghapusanJalanIrigasiJaringanDKPInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDKP



class SKPDAsalJalanIrigasiJaringanDKPInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDKP



class SKPDTujuanJalanIrigasiJaringanDKPInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDKP



class FotoJalanIrigasiJaringanDKPInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDKP





class HargaJalanIrigasiJaringanDKPInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=15)
        return super(HargaJalanIrigasiJaringanDKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDKPInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDKP


class JalanIrigasiJaringanDKPAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDKPInline,
                    SKPDAsalJalanIrigasiJaringanDKPInline,
                    FotoJalanIrigasiJaringanDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        return super(JalanIrigasiJaringanDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDKPAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDKPInline,
                    SKPDAsalJalanIrigasiJaringanDKPInline,
                    FotoJalanIrigasiJaringanDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDKPAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDKPInline,
                    SKPDAsalJalanIrigasiJaringanDKPInline,
                    FotoJalanIrigasiJaringanDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        return super(KDPJalanIrigasiJaringanDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDKPAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=15)
        return super(KontrakJalanIrigasiJaringanDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=15)



class HargaJalanIrigasiJaringanDKPAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDKPAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDKPInline, TahunBerkurangJalanIrigasiJaringanDKPInline,
                    SKPDAsalJalanIrigasiJaringanDKPInline,
                    SKPDTujuanJalanIrigasiJaringanDKPInline,
                    FotoJalanIrigasiJaringanDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DKP
admin.site.register(JalanIrigasiJaringanDKP, JalanIrigasiJaringanDKPAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDKP, JalanIrigasiJaringanUsulHapusDKPAdmin)
admin.site.register(KDPJalanIrigasiJaringanDKP, KDPJalanIrigasiJaringanDKPAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDKP, KontrakJalanIrigasiJaringanDKPAdmin)
admin.site.register(HargaJalanIrigasiJaringanDKP, HargaJalanIrigasiJaringanDKPAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDKP, JalanIrigasiJaringanPenghapusanDKPAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDKP, KontrakATLDKP, HargaATLDKP, ATLUsulHapusDKP, TahunBerkurangUsulHapusATLDKP

from atl.models import ATLPenghapusanDKP, TahunBerkurangATLDKP, PenghapusanATLDKP

from atl.models import SKPDAsalATLDKP, SKPDTujuanATLDKP, FotoATLDKP

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDKPInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDKP



class PenghapusanATLDKPInline(PenghapusanATLInline):
    model = PenghapusanATLDKP



class SKPDAsalATLDKPInline(SKPDAsalATLInline):
    model = SKPDAsalATLDKP



class SKPDTujuanATLDKPInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDKP



class FotoATLDKPInline(FotoATLInline):
    model = FotoATLDKP



class HargaATLDKPInline(HargaATLInline):
    model = HargaATLDKP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=15)
        return super(HargaATLDKPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDKPInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDKP


class ATLDKPAdmin(ATLAdmin):
    inlines = [HargaATLDKPInline,
                    SKPDAsalATLDKPInline,
                    FotoATLDKPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=15)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=15)
        return super(ATLDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDKPAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDKPInline,
                    SKPDAsalATLDKPInline,
                    FotoATLDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDKPAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=15)
        return super(KontrakATLDKPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=15)



class HargaATLDKPAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDKPAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDKPInline, TahunBerkurangATLDKPInline,
                    SKPDAsalATLDKPInline,
                    SKPDTujuanATLDKPInline,
                    FotoATLDKPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=15)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DKP
admin.site.register(ATLDKP, ATLDKPAdmin)
admin.site.register(ATLUsulHapusDKP, ATLUsulHapusDKPAdmin)
admin.site.register(KontrakATLDKP, KontrakATLDKPAdmin)
admin.site.register(HargaATLDKP, HargaATLDKPAdmin)
admin.site.register(ATLPenghapusanDKP, ATLPenghapusanDKPAdmin)
