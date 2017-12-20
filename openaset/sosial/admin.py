### $Id: admin.py,v 1.5 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahSosial, KontrakTanahSosial, HargaTanahSosial, TanahUsulHapusSosial, TahunBerkurangUsulHapusTanahSosial

from umum.models import TanahPenghapusanSosial, TahunBerkurangTanahSosial, PenghapusanTanahSosial

from umum.models import SKPDAsalTanahSosial, SKPDTujuanTanahSosial, FotoTanahSosial

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanSosial, KontrakGedungBangunanSosial, HargaGedungBangunanSosial, GedungBangunanRuanganSosial, GedungBangunanUsulHapusSosial, TahunBerkurangUsulHapusGedungSosial

from gedungbangunan.models import GedungBangunanPenghapusanSosial, TahunBerkurangGedungBangunanSosial, PenghapusanGedungBangunanSosial

from gedungbangunan.models import SKPDAsalGedungBangunanSosial, SKPDTujuanGedungBangunanSosial, FotoGedungBangunanSosial

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinSosial, KontrakPeralatanMesinSosial, HargaPeralatanMesinSosial, PeralatanMesinUsulHapusSosial, TahunBerkurangUsulHapusPeralatanMesinSosial

from peralatanmesin.models import PeralatanMesinPenghapusanSosial, TahunBerkurangPeralatanMesinSosial, PenghapusanPeralatanMesinSosial

from peralatanmesin.models import SKPDAsalPeralatanMesinSosial, SKPDTujuanPeralatanMesinSosial, FotoPeralatanMesinSosial

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahSosialInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahSosial



class PenghapusanTanahSosialInline(PenghapusanTanahInline):
    model = PenghapusanTanahSosial



class SKPDAsalTanahSosialInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahSosial



class SKPDTujuanTanahSosialInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahSosial



class FotoTanahSosialInline(FotoTanahInline):
    model = FotoTanahSosial



class GedungBangunanSosialInline(GedungBangunanInline):
    model = GedungBangunanSosial



class HargaTanahSosialInline(HargaTanahInline):
    model = HargaTanahSosial

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=9)
        return super(HargaTanahSosialInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahSosialInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahSosial


class TanahSosialAdmin(TanahAdmin):
    inlines = [HargaTanahSosialInline,
                SKPDAsalTanahSosialInline,
                FotoTanahSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        return super(TanahSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusSosialAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahSosialInline,
                SKPDAsalTanahSosialInline,
                FotoTanahSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahSosialAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=9)
        return super(KontrakTanahSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=9)



class HargaTanahSosialAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanSosialAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahSosialInline, TahunBerkurangTanahSosialInline,
                    SKPDAsalTanahSosialInline,
                    SKPDTujuanTanahSosialInline,
                    FotoTanahSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Sosial
admin.site.register(TanahSosial, TanahSosialAdmin)
admin.site.register(TanahUsulHapusSosial, TanahUsulHapusSosialAdmin)
admin.site.register(KontrakTanahSosial, KontrakTanahSosialAdmin)
admin.site.register(HargaTanahSosial, HargaTanahSosialAdmin)
admin.site.register(TanahPenghapusanSosial, TanahPenghapusanSosialAdmin)



from gedungbangunan.models import KDPGedungBangunanSosial


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanSosialInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanSosial



class PenghapusanGedungBangunanSosialInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanSosial



class SKPDAsalGedungBangunanSosialInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanSosial



class SKPDTujuanGedungBangunanSosialInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanSosial



class FotoGedungBangunanSosialInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanSosial



class HargaGedungBangunanSosialInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanSosial

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=9)
        return super(HargaGedungBangunanSosialInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungSosialInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungSosial


class GedungBangunanSosialAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanSosialInline,
                SKPDAsalGedungBangunanSosialInline,
                FotoGedungBangunanSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        return super(GedungBangunanSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanSosialAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanSosialInline,
                SKPDAsalGedungBangunanSosialInline,
                FotoGedungBangunanSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        return super(KDPGedungBangunanSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganSosialAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusSosialAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungSosialInline,
                    SKPDAsalGedungBangunanSosialInline,
                    FotoGedungBangunanSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanSosialAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=9)
        return super(KontrakGedungBangunanSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=9)



class HargaGedungBangunanSosialAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanSosialAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanSosialInline, TahunBerkurangGedungBangunanSosialInline,
                    SKPDAsalGedungBangunanSosialInline,
                    SKPDTujuanGedungBangunanSosialInline,
                    FotoGedungBangunanSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Sosial
admin.site.register(GedungBangunanSosial, GedungBangunanSosialAdmin)
admin.site.register(KDPGedungBangunanSosial, KDPGedungBangunanSosialAdmin)
admin.site.register(GedungBangunanRuanganSosial, GedungBangunanRuanganSosialAdmin)
admin.site.register(GedungBangunanUsulHapusSosial, GedungBangunanUsulHapusSosialAdmin)
admin.site.register(KontrakGedungBangunanSosial, KontrakGedungBangunanSosialAdmin)
admin.site.register(HargaGedungBangunanSosial, HargaGedungBangunanSosialAdmin)
admin.site.register(GedungBangunanPenghapusanSosial, GedungBangunanPenghapusanSosialAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinSosialInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinSosial



class PenghapusanPeralatanMesinSosialInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinSosial



class SKPDAsalPeralatanMesinSosialInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinSosial



class SKPDTujuanPeralatanMesinSosialInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinSosial



class FotoPeralatanMesinSosialInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinSosial



class HargaPeralatanMesinSosialInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinSosial

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=9)
        return super(HargaPeralatanMesinSosialInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinSosialInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinSosial


class PeralatanMesinSosialAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinSosialInline,
                    SKPDAsalPeralatanMesinSosialInline,
                    FotoPeralatanMesinSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=9)
        return super(PeralatanMesinSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusSosialAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinSosialInline,
                    SKPDAsalPeralatanMesinSosialInline,
                    FotoPeralatanMesinSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinSosialAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=9)
        return super(KontrakPeralatanMesinSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=9)



class HargaPeralatanMesinSosialAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanSosialAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinSosialInline, TahunBerkurangPeralatanMesinSosialInline,
                    SKPDAsalPeralatanMesinSosialInline,
                    SKPDTujuanPeralatanMesinSosialInline,
                    FotoPeralatanMesinSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Sosial
admin.site.register(PeralatanMesinSosial, PeralatanMesinSosialAdmin)
admin.site.register(PeralatanMesinUsulHapusSosial, PeralatanMesinUsulHapusSosialAdmin)
admin.site.register(KontrakPeralatanMesinSosial, KontrakPeralatanMesinSosialAdmin)
admin.site.register(HargaPeralatanMesinSosial, HargaPeralatanMesinSosialAdmin)
admin.site.register(PeralatanMesinPenghapusanSosial, PeralatanMesinPenghapusanSosialAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanSosial, KontrakJalanIrigasiJaringanSosial, HargaJalanIrigasiJaringanSosial, KDPJalanIrigasiJaringanSosial, JalanIrigasiJaringanUsulHapusSosial, TahunBerkurangUsulHapusJalanIrigasiJaringanSosial

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanSosial, TahunBerkurangJalanIrigasiJaringanSosial, PenghapusanJalanIrigasiJaringanSosial

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanSosial, SKPDTujuanJalanIrigasiJaringanSosial, FotoJalanIrigasiJaringanSosial

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanSosialInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanSosial



class PenghapusanJalanIrigasiJaringanSosialInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanSosial



class SKPDAsalJalanIrigasiJaringanSosialInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanSosial



class SKPDTujuanJalanIrigasiJaringanSosialInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanSosial



class FotoJalanIrigasiJaringanSosialInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanSosial





class HargaJalanIrigasiJaringanSosialInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanSosial

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=9)
        return super(HargaJalanIrigasiJaringanSosialInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanSosialInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanSosial


class JalanIrigasiJaringanSosialAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSosialInline,
                    SKPDAsalJalanIrigasiJaringanSosialInline,
                    FotoJalanIrigasiJaringanSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        return super(JalanIrigasiJaringanSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusSosialAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanSosialInline,
                    SKPDAsalJalanIrigasiJaringanSosialInline,
                    FotoJalanIrigasiJaringanSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanSosialAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSosialInline,
                    SKPDAsalJalanIrigasiJaringanSosialInline,
                    FotoJalanIrigasiJaringanSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        return super(KDPJalanIrigasiJaringanSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanSosialAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=9)
        return super(KontrakJalanIrigasiJaringanSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=9)



class HargaJalanIrigasiJaringanSosialAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanSosialAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanSosialInline, TahunBerkurangJalanIrigasiJaringanSosialInline,
                    SKPDAsalJalanIrigasiJaringanSosialInline,
                    SKPDTujuanJalanIrigasiJaringanSosialInline,
                    FotoJalanIrigasiJaringanSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Sosial
admin.site.register(JalanIrigasiJaringanSosial, JalanIrigasiJaringanSosialAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusSosial, JalanIrigasiJaringanUsulHapusSosialAdmin)
admin.site.register(KDPJalanIrigasiJaringanSosial, KDPJalanIrigasiJaringanSosialAdmin)
admin.site.register(KontrakJalanIrigasiJaringanSosial, KontrakJalanIrigasiJaringanSosialAdmin)
admin.site.register(HargaJalanIrigasiJaringanSosial, HargaJalanIrigasiJaringanSosialAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanSosial, JalanIrigasiJaringanPenghapusanSosialAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLSosial, KontrakATLSosial, HargaATLSosial, ATLUsulHapusSosial, TahunBerkurangUsulHapusATLSosial

from atl.models import ATLPenghapusanSosial, TahunBerkurangATLSosial, PenghapusanATLSosial

from atl.models import SKPDAsalATLSosial, SKPDTujuanATLSosial, FotoATLSosial

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLSosialInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLSosial



class PenghapusanATLSosialInline(PenghapusanATLInline):
    model = PenghapusanATLSosial



class SKPDAsalATLSosialInline(SKPDAsalATLInline):
    model = SKPDAsalATLSosial



class SKPDTujuanATLSosialInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLSosial



class FotoATLSosialInline(FotoATLInline):
    model = FotoATLSosial



class HargaATLSosialInline(HargaATLInline):
    model = HargaATLSosial

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=9)
        return super(HargaATLSosialInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLSosialInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLSosial


class ATLSosialAdmin(ATLAdmin):
    inlines = [HargaATLSosialInline,
                    SKPDAsalATLSosialInline,
                    FotoATLSosialInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=9)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=9)
        return super(ATLSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusSosialAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLSosialInline,
                    SKPDAsalATLSosialInline,
                    FotoATLSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLSosialAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=9)
        return super(KontrakATLSosialAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=9)



class HargaATLSosialAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanSosialAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLSosialInline, TahunBerkurangATLSosialInline,
                    SKPDAsalATLSosialInline,
                    SKPDTujuanATLSosialInline,
                    FotoATLSosialInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=9)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Sosial
admin.site.register(ATLSosial, ATLSosialAdmin)
admin.site.register(ATLUsulHapusSosial, ATLUsulHapusSosialAdmin)
admin.site.register(KontrakATLSosial, KontrakATLSosialAdmin)
admin.site.register(HargaATLSosial, HargaATLSosialAdmin)
admin.site.register(ATLPenghapusanSosial, ATLPenghapusanSosialAdmin)
