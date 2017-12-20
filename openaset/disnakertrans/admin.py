### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDisnakertrans, KontrakTanahDisnakertrans, HargaTanahDisnakertrans, TanahUsulHapusDisnakertrans, TahunBerkurangUsulHapusTanahDisnakertrans

from umum.models import TanahPenghapusanDisnakertrans, TahunBerkurangTanahDisnakertrans, PenghapusanTanahDisnakertrans

from umum.models import SKPDAsalTanahDisnakertrans, SKPDTujuanTanahDisnakertrans, FotoTanahDisnakertrans

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDisnakertrans, KontrakGedungBangunanDisnakertrans, HargaGedungBangunanDisnakertrans, GedungBangunanRuanganDisnakertrans, GedungBangunanUsulHapusDisnakertrans, TahunBerkurangUsulHapusGedungDisnakertrans

from gedungbangunan.models import GedungBangunanPenghapusanDisnakertrans, TahunBerkurangGedungBangunanDisnakertrans, PenghapusanGedungBangunanDisnakertrans

from gedungbangunan.models import SKPDAsalGedungBangunanDisnakertrans, SKPDTujuanGedungBangunanDisnakertrans, FotoGedungBangunanDisnakertrans

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDisnakertrans, KontrakPeralatanMesinDisnakertrans, HargaPeralatanMesinDisnakertrans, PeralatanMesinUsulHapusDisnakertrans, TahunBerkurangUsulHapusPeralatanMesinDisnakertrans

from peralatanmesin.models import PeralatanMesinPenghapusanDisnakertrans, TahunBerkurangPeralatanMesinDisnakertrans, PenghapusanPeralatanMesinDisnakertrans

from peralatanmesin.models import SKPDAsalPeralatanMesinDisnakertrans, SKPDTujuanPeralatanMesinDisnakertrans, FotoPeralatanMesinDisnakertrans

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDisnakertransInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDisnakertrans



class PenghapusanTanahDisnakertransInline(PenghapusanTanahInline):
    model = PenghapusanTanahDisnakertrans



class SKPDAsalTanahDisnakertransInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDisnakertrans



class SKPDTujuanTanahDisnakertransInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDisnakertrans



class FotoTanahDisnakertransInline(FotoTanahInline):
    model = FotoTanahDisnakertrans



class GedungBangunanDisnakertransInline(GedungBangunanInline):
    model = GedungBangunanDisnakertrans



class HargaTanahDisnakertransInline(HargaTanahInline):
    model = HargaTanahDisnakertrans

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=41)
        return super(HargaTanahDisnakertransInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDisnakertransInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDisnakertrans


class TanahDisnakertransAdmin(TanahAdmin):
    inlines = [HargaTanahDisnakertransInline,
                SKPDAsalTanahDisnakertransInline,
                FotoTanahDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        return super(TanahDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDisnakertransAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDisnakertransInline,
                SKPDAsalTanahDisnakertransInline,
                FotoTanahDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDisnakertransAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=41)
        return super(KontrakTanahDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=41)



class HargaTanahDisnakertransAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDisnakertransAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDisnakertransInline, TahunBerkurangTanahDisnakertransInline,
                    SKPDAsalTanahDisnakertransInline,
                    SKPDTujuanTanahDisnakertransInline,
                    FotoTanahDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Disnakertrans
admin.site.register(TanahDisnakertrans, TanahDisnakertransAdmin)
admin.site.register(TanahUsulHapusDisnakertrans, TanahUsulHapusDisnakertransAdmin)
admin.site.register(KontrakTanahDisnakertrans, KontrakTanahDisnakertransAdmin)
admin.site.register(HargaTanahDisnakertrans, HargaTanahDisnakertransAdmin)
admin.site.register(TanahPenghapusanDisnakertrans, TanahPenghapusanDisnakertransAdmin)



from gedungbangunan.models import KDPGedungBangunanDisnakertrans


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDisnakertransInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDisnakertrans



class PenghapusanGedungBangunanDisnakertransInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDisnakertrans



class SKPDAsalGedungBangunanDisnakertransInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDisnakertrans



class SKPDTujuanGedungBangunanDisnakertransInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDisnakertrans



class FotoGedungBangunanDisnakertransInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDisnakertrans



class HargaGedungBangunanDisnakertransInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisnakertrans

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=41)
        return super(HargaGedungBangunanDisnakertransInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDisnakertransInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDisnakertrans


class GedungBangunanDisnakertransAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisnakertransInline,
                SKPDAsalGedungBangunanDisnakertransInline,
                FotoGedungBangunanDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        return super(GedungBangunanDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDisnakertransAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisnakertransInline,
                SKPDAsalGedungBangunanDisnakertransInline,
                FotoGedungBangunanDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        return super(KDPGedungBangunanDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisnakertransAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDisnakertransAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDisnakertransInline,
                    SKPDAsalGedungBangunanDisnakertransInline,
                    FotoGedungBangunanDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDisnakertransAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=41)
        return super(KontrakGedungBangunanDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=41)



class HargaGedungBangunanDisnakertransAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDisnakertransAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDisnakertransInline, TahunBerkurangGedungBangunanDisnakertransInline,
                    SKPDAsalGedungBangunanDisnakertransInline,
                    SKPDTujuanGedungBangunanDisnakertransInline,
                    FotoGedungBangunanDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Disnakertrans
admin.site.register(GedungBangunanDisnakertrans, GedungBangunanDisnakertransAdmin)
admin.site.register(KDPGedungBangunanDisnakertrans, KDPGedungBangunanDisnakertransAdmin)
admin.site.register(GedungBangunanRuanganDisnakertrans, GedungBangunanRuanganDisnakertransAdmin)
admin.site.register(GedungBangunanUsulHapusDisnakertrans, GedungBangunanUsulHapusDisnakertransAdmin)
admin.site.register(KontrakGedungBangunanDisnakertrans, KontrakGedungBangunanDisnakertransAdmin)
admin.site.register(HargaGedungBangunanDisnakertrans, HargaGedungBangunanDisnakertransAdmin)
admin.site.register(GedungBangunanPenghapusanDisnakertrans, GedungBangunanPenghapusanDisnakertransAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDisnakertransInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDisnakertrans



class PenghapusanPeralatanMesinDisnakertransInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDisnakertrans



class SKPDAsalPeralatanMesinDisnakertransInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDisnakertrans



class SKPDTujuanPeralatanMesinDisnakertransInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDisnakertrans



class FotoPeralatanMesinDisnakertransInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDisnakertrans



class HargaPeralatanMesinDisnakertransInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisnakertrans

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=41)
        return super(HargaPeralatanMesinDisnakertransInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDisnakertransInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDisnakertrans


class PeralatanMesinDisnakertransAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisnakertransInline,
                    SKPDAsalPeralatanMesinDisnakertransInline,
                    FotoPeralatanMesinDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=41)
        return super(PeralatanMesinDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDisnakertransAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDisnakertransInline,
                    SKPDAsalPeralatanMesinDisnakertransInline,
                    FotoPeralatanMesinDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDisnakertransAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=41)
        return super(KontrakPeralatanMesinDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=41)



class HargaPeralatanMesinDisnakertransAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDisnakertransAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDisnakertransInline, TahunBerkurangPeralatanMesinDisnakertransInline,
                    SKPDAsalPeralatanMesinDisnakertransInline,
                    SKPDTujuanPeralatanMesinDisnakertransInline,
                    FotoPeralatanMesinDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Disnakertrans
admin.site.register(PeralatanMesinDisnakertrans, PeralatanMesinDisnakertransAdmin)
admin.site.register(PeralatanMesinUsulHapusDisnakertrans, PeralatanMesinUsulHapusDisnakertransAdmin)
admin.site.register(KontrakPeralatanMesinDisnakertrans, KontrakPeralatanMesinDisnakertransAdmin)
admin.site.register(HargaPeralatanMesinDisnakertrans, HargaPeralatanMesinDisnakertransAdmin)
admin.site.register(PeralatanMesinPenghapusanDisnakertrans, PeralatanMesinPenghapusanDisnakertransAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDisnakertrans, KontrakJalanIrigasiJaringanDisnakertrans, HargaJalanIrigasiJaringanDisnakertrans, KDPJalanIrigasiJaringanDisnakertrans, JalanIrigasiJaringanUsulHapusDisnakertrans, TahunBerkurangUsulHapusJalanIrigasiJaringanDisnakertrans

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDisnakertrans, TahunBerkurangJalanIrigasiJaringanDisnakertrans, PenghapusanJalanIrigasiJaringanDisnakertrans

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDisnakertrans, SKPDTujuanJalanIrigasiJaringanDisnakertrans, FotoJalanIrigasiJaringanDisnakertrans

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDisnakertransInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDisnakertrans



class PenghapusanJalanIrigasiJaringanDisnakertransInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDisnakertrans



class SKPDAsalJalanIrigasiJaringanDisnakertransInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDisnakertrans



class SKPDTujuanJalanIrigasiJaringanDisnakertransInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDisnakertrans



class FotoJalanIrigasiJaringanDisnakertransInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDisnakertrans





class HargaJalanIrigasiJaringanDisnakertransInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisnakertrans

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=41)
        return super(HargaJalanIrigasiJaringanDisnakertransInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDisnakertransInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDisnakertrans


class JalanIrigasiJaringanDisnakertransAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisnakertransInline,
                    SKPDAsalJalanIrigasiJaringanDisnakertransInline,
                    FotoJalanIrigasiJaringanDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        return super(JalanIrigasiJaringanDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDisnakertransAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDisnakertransInline,
                    SKPDAsalJalanIrigasiJaringanDisnakertransInline,
                    FotoJalanIrigasiJaringanDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDisnakertransAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisnakertransInline,
                    SKPDAsalJalanIrigasiJaringanDisnakertransInline,
                    FotoJalanIrigasiJaringanDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        return super(KDPJalanIrigasiJaringanDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDisnakertransAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=41)
        return super(KontrakJalanIrigasiJaringanDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=41)



class HargaJalanIrigasiJaringanDisnakertransAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDisnakertransAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDisnakertransInline, TahunBerkurangJalanIrigasiJaringanDisnakertransInline,
                    SKPDAsalJalanIrigasiJaringanDisnakertransInline,
                    SKPDTujuanJalanIrigasiJaringanDisnakertransInline,
                    FotoJalanIrigasiJaringanDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Disnakertrans
admin.site.register(JalanIrigasiJaringanDisnakertrans, JalanIrigasiJaringanDisnakertransAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDisnakertrans, JalanIrigasiJaringanUsulHapusDisnakertransAdmin)
admin.site.register(KDPJalanIrigasiJaringanDisnakertrans, KDPJalanIrigasiJaringanDisnakertransAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDisnakertrans, KontrakJalanIrigasiJaringanDisnakertransAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisnakertrans, HargaJalanIrigasiJaringanDisnakertransAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDisnakertrans, JalanIrigasiJaringanPenghapusanDisnakertransAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDisnakertrans, KontrakATLDisnakertrans, HargaATLDisnakertrans, ATLUsulHapusDisnakertrans, TahunBerkurangUsulHapusATLDisnakertrans

from atl.models import ATLPenghapusanDisnakertrans, TahunBerkurangATLDisnakertrans, PenghapusanATLDisnakertrans

from atl.models import SKPDAsalATLDisnakertrans, SKPDTujuanATLDisnakertrans, FotoATLDisnakertrans

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDisnakertransInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDisnakertrans



class PenghapusanATLDisnakertransInline(PenghapusanATLInline):
    model = PenghapusanATLDisnakertrans



class SKPDAsalATLDisnakertransInline(SKPDAsalATLInline):
    model = SKPDAsalATLDisnakertrans



class SKPDTujuanATLDisnakertransInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDisnakertrans



class FotoATLDisnakertransInline(FotoATLInline):
    model = FotoATLDisnakertrans



class HargaATLDisnakertransInline(HargaATLInline):
    model = HargaATLDisnakertrans

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=41)
        return super(HargaATLDisnakertransInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDisnakertransInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDisnakertrans


class ATLDisnakertransAdmin(ATLAdmin):
    inlines = [HargaATLDisnakertransInline,
                    SKPDAsalATLDisnakertransInline,
                    FotoATLDisnakertransInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=41)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=41)
        return super(ATLDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDisnakertransAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDisnakertransInline,
                    SKPDAsalATLDisnakertransInline,
                    FotoATLDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDisnakertransAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=41)
        return super(KontrakATLDisnakertransAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=41)



class HargaATLDisnakertransAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDisnakertransAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDisnakertransInline, TahunBerkurangATLDisnakertransInline,
                    SKPDAsalATLDisnakertransInline,
                    SKPDTujuanATLDisnakertransInline,
                    FotoATLDisnakertransInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=41)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Disnakertrans
admin.site.register(ATLDisnakertrans, ATLDisnakertransAdmin)
admin.site.register(ATLUsulHapusDisnakertrans, ATLUsulHapusDisnakertransAdmin)
admin.site.register(KontrakATLDisnakertrans, KontrakATLDisnakertransAdmin)
admin.site.register(HargaATLDisnakertrans, HargaATLDisnakertransAdmin)
admin.site.register(ATLPenghapusanDisnakertrans, ATLPenghapusanDisnakertransAdmin)
