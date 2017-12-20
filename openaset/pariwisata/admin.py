### $Id: admin.py,v 1.5 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahPariwisata, KontrakTanahPariwisata, HargaTanahPariwisata, TanahUsulHapusPariwisata, TahunBerkurangUsulHapusTanahPariwisata

from umum.models import TanahPenghapusanPariwisata, TahunBerkurangTanahPariwisata, PenghapusanTanahPariwisata

from umum.models import SKPDAsalTanahPariwisata, SKPDTujuanTanahPariwisata, FotoTanahPariwisata

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanPariwisata, KontrakGedungBangunanPariwisata, HargaGedungBangunanPariwisata, GedungBangunanRuanganPariwisata, GedungBangunanUsulHapusPariwisata, TahunBerkurangUsulHapusGedungPariwisata

from gedungbangunan.models import GedungBangunanPenghapusanPariwisata, TahunBerkurangGedungBangunanPariwisata, PenghapusanGedungBangunanPariwisata

from gedungbangunan.models import SKPDAsalGedungBangunanPariwisata, SKPDTujuanGedungBangunanPariwisata, FotoGedungBangunanPariwisata

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinPariwisata, KontrakPeralatanMesinPariwisata, HargaPeralatanMesinPariwisata, PeralatanMesinUsulHapusPariwisata, TahunBerkurangUsulHapusPeralatanMesinPariwisata

from peralatanmesin.models import PeralatanMesinPenghapusanPariwisata, TahunBerkurangPeralatanMesinPariwisata, PenghapusanPeralatanMesinPariwisata

from peralatanmesin.models import SKPDAsalPeralatanMesinPariwisata, SKPDTujuanPeralatanMesinPariwisata, FotoPeralatanMesinPariwisata

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahPariwisataInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahPariwisata



class PenghapusanTanahPariwisataInline(PenghapusanTanahInline):
    model = PenghapusanTanahPariwisata



class SKPDAsalTanahPariwisataInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahPariwisata



class SKPDTujuanTanahPariwisataInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahPariwisata



class FotoTanahPariwisataInline(FotoTanahInline):
    model = FotoTanahPariwisata



class GedungBangunanPariwisataInline(GedungBangunanInline):
    model = GedungBangunanPariwisata



class HargaTanahPariwisataInline(HargaTanahInline):
    model = HargaTanahPariwisata

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=46)
        return super(HargaTanahPariwisataInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahPariwisataInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahPariwisata


class TanahPariwisataAdmin(TanahAdmin):
    inlines = [HargaTanahPariwisataInline,
                SKPDAsalTanahPariwisataInline,
                FotoTanahPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        return super(TanahPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusPariwisataAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahPariwisataInline,
                SKPDAsalTanahPariwisataInline,
                FotoTanahPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahPariwisataAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=46)
        return super(KontrakTanahPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=46)



class HargaTanahPariwisataAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanPariwisataAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahPariwisataInline, TahunBerkurangTanahPariwisataInline,
                    SKPDAsalTanahPariwisataInline,
                    SKPDTujuanTanahPariwisataInline,
                    FotoTanahPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Pariwisata
admin.site.register(TanahPariwisata, TanahPariwisataAdmin)
admin.site.register(TanahUsulHapusPariwisata, TanahUsulHapusPariwisataAdmin)
admin.site.register(KontrakTanahPariwisata, KontrakTanahPariwisataAdmin)
admin.site.register(HargaTanahPariwisata, HargaTanahPariwisataAdmin)
admin.site.register(TanahPenghapusanPariwisata, TanahPenghapusanPariwisataAdmin)



from gedungbangunan.models import KDPGedungBangunanPariwisata


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanPariwisataInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanPariwisata



class PenghapusanGedungBangunanPariwisataInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanPariwisata



class SKPDAsalGedungBangunanPariwisataInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanPariwisata



class SKPDTujuanGedungBangunanPariwisataInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanPariwisata



class FotoGedungBangunanPariwisataInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanPariwisata



class HargaGedungBangunanPariwisataInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanPariwisata

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=46)
        return super(HargaGedungBangunanPariwisataInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungPariwisataInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungPariwisata


class GedungBangunanPariwisataAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanPariwisataInline,
                SKPDAsalGedungBangunanPariwisataInline,
                FotoGedungBangunanPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        return super(GedungBangunanPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanPariwisataAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanPariwisataInline,
                SKPDAsalGedungBangunanPariwisataInline,
                FotoGedungBangunanPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        return super(KDPGedungBangunanPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganPariwisataAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusPariwisataAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungPariwisataInline,
                    SKPDAsalGedungBangunanPariwisataInline,
                    FotoGedungBangunanPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanPariwisataAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=46)
        return super(KontrakGedungBangunanPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=46)



class HargaGedungBangunanPariwisataAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanPariwisataAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanPariwisataInline, TahunBerkurangGedungBangunanPariwisataInline,
                    SKPDAsalGedungBangunanPariwisataInline,
                    SKPDTujuanGedungBangunanPariwisataInline,
                    FotoGedungBangunanPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Pariwisata
admin.site.register(GedungBangunanPariwisata, GedungBangunanPariwisataAdmin)
admin.site.register(KDPGedungBangunanPariwisata, KDPGedungBangunanPariwisataAdmin)
admin.site.register(GedungBangunanRuanganPariwisata, GedungBangunanRuanganPariwisataAdmin)
admin.site.register(GedungBangunanUsulHapusPariwisata, GedungBangunanUsulHapusPariwisataAdmin)
admin.site.register(KontrakGedungBangunanPariwisata, KontrakGedungBangunanPariwisataAdmin)
admin.site.register(HargaGedungBangunanPariwisata, HargaGedungBangunanPariwisataAdmin)
admin.site.register(GedungBangunanPenghapusanPariwisata, GedungBangunanPenghapusanPariwisataAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinPariwisataInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinPariwisata



class PenghapusanPeralatanMesinPariwisataInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinPariwisata



class SKPDAsalPeralatanMesinPariwisataInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinPariwisata



class SKPDTujuanPeralatanMesinPariwisataInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinPariwisata



class FotoPeralatanMesinPariwisataInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinPariwisata



class HargaPeralatanMesinPariwisataInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinPariwisata

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=46)
        return super(HargaPeralatanMesinPariwisataInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinPariwisataInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinPariwisata


class PeralatanMesinPariwisataAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinPariwisataInline,
                    SKPDAsalPeralatanMesinPariwisataInline,
                    FotoPeralatanMesinPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=46)
        return super(PeralatanMesinPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusPariwisataAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinPariwisataInline,
                    SKPDAsalPeralatanMesinPariwisataInline,
                    FotoPeralatanMesinPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinPariwisataAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=46)
        return super(KontrakPeralatanMesinPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=46)



class HargaPeralatanMesinPariwisataAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanPariwisataAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinPariwisataInline, TahunBerkurangPeralatanMesinPariwisataInline,
                    SKPDAsalPeralatanMesinPariwisataInline,
                    SKPDTujuanPeralatanMesinPariwisataInline,
                    FotoPeralatanMesinPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Pariwisata
admin.site.register(PeralatanMesinPariwisata, PeralatanMesinPariwisataAdmin)
admin.site.register(PeralatanMesinUsulHapusPariwisata, PeralatanMesinUsulHapusPariwisataAdmin)
admin.site.register(KontrakPeralatanMesinPariwisata, KontrakPeralatanMesinPariwisataAdmin)
admin.site.register(HargaPeralatanMesinPariwisata, HargaPeralatanMesinPariwisataAdmin)
admin.site.register(PeralatanMesinPenghapusanPariwisata, PeralatanMesinPenghapusanPariwisataAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanPariwisata, KontrakJalanIrigasiJaringanPariwisata, HargaJalanIrigasiJaringanPariwisata, KDPJalanIrigasiJaringanPariwisata, JalanIrigasiJaringanUsulHapusPariwisata, TahunBerkurangUsulHapusJalanIrigasiJaringanPariwisata

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanPariwisata, TahunBerkurangJalanIrigasiJaringanPariwisata, PenghapusanJalanIrigasiJaringanPariwisata

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanPariwisata, SKPDTujuanJalanIrigasiJaringanPariwisata, FotoJalanIrigasiJaringanPariwisata

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanPariwisataInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanPariwisata



class PenghapusanJalanIrigasiJaringanPariwisataInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanPariwisata



class SKPDAsalJalanIrigasiJaringanPariwisataInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanPariwisata



class SKPDTujuanJalanIrigasiJaringanPariwisataInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanPariwisata



class FotoJalanIrigasiJaringanPariwisataInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanPariwisata





class HargaJalanIrigasiJaringanPariwisataInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanPariwisata

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=46)
        return super(HargaJalanIrigasiJaringanPariwisataInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanPariwisataInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanPariwisata


class JalanIrigasiJaringanPariwisataAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPariwisataInline,
                    SKPDAsalJalanIrigasiJaringanPariwisataInline,
                    FotoJalanIrigasiJaringanPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        return super(JalanIrigasiJaringanPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusPariwisataAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanPariwisataInline,
                    SKPDAsalJalanIrigasiJaringanPariwisataInline,
                    FotoJalanIrigasiJaringanPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanPariwisataAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanPariwisataInline,
                    SKPDAsalJalanIrigasiJaringanPariwisataInline,
                    FotoJalanIrigasiJaringanPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        return super(KDPJalanIrigasiJaringanPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanPariwisataAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=46)
        return super(KontrakJalanIrigasiJaringanPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=46)



class HargaJalanIrigasiJaringanPariwisataAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanPariwisataAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanPariwisataInline, TahunBerkurangJalanIrigasiJaringanPariwisataInline,
                    SKPDAsalJalanIrigasiJaringanPariwisataInline,
                    SKPDTujuanJalanIrigasiJaringanPariwisataInline,
                    FotoJalanIrigasiJaringanPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Pariwisata
admin.site.register(JalanIrigasiJaringanPariwisata, JalanIrigasiJaringanPariwisataAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusPariwisata, JalanIrigasiJaringanUsulHapusPariwisataAdmin)
admin.site.register(KDPJalanIrigasiJaringanPariwisata, KDPJalanIrigasiJaringanPariwisataAdmin)
admin.site.register(KontrakJalanIrigasiJaringanPariwisata, KontrakJalanIrigasiJaringanPariwisataAdmin)
admin.site.register(HargaJalanIrigasiJaringanPariwisata, HargaJalanIrigasiJaringanPariwisataAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanPariwisata, JalanIrigasiJaringanPenghapusanPariwisataAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLPariwisata, KontrakATLPariwisata, HargaATLPariwisata, ATLUsulHapusPariwisata, TahunBerkurangUsulHapusATLPariwisata

from atl.models import ATLPenghapusanPariwisata, TahunBerkurangATLPariwisata, PenghapusanATLPariwisata

from atl.models import SKPDAsalATLPariwisata, SKPDTujuanATLPariwisata, FotoATLPariwisata

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLPariwisataInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLPariwisata



class PenghapusanATLPariwisataInline(PenghapusanATLInline):
    model = PenghapusanATLPariwisata



class SKPDAsalATLPariwisataInline(SKPDAsalATLInline):
    model = SKPDAsalATLPariwisata



class SKPDTujuanATLPariwisataInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLPariwisata



class FotoATLPariwisataInline(FotoATLInline):
    model = FotoATLPariwisata



class HargaATLPariwisataInline(HargaATLInline):
    model = HargaATLPariwisata

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=46)
        return super(HargaATLPariwisataInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLPariwisataInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLPariwisata


class ATLPariwisataAdmin(ATLAdmin):
    inlines = [HargaATLPariwisataInline,
                    SKPDAsalATLPariwisataInline,
                    FotoATLPariwisataInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=46)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=46)
        return super(ATLPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusPariwisataAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLPariwisataInline,
                    SKPDAsalATLPariwisataInline,
                    FotoATLPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLPariwisataAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=46)
        return super(KontrakATLPariwisataAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=46)



class HargaATLPariwisataAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanPariwisataAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLPariwisataInline, TahunBerkurangATLPariwisataInline,
                    SKPDAsalATLPariwisataInline,
                    SKPDTujuanATLPariwisataInline,
                    FotoATLPariwisataInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=46)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Pariwisata
admin.site.register(ATLPariwisata, ATLPariwisataAdmin)
admin.site.register(ATLUsulHapusPariwisata, ATLUsulHapusPariwisataAdmin)
admin.site.register(KontrakATLPariwisata, KontrakATLPariwisataAdmin)
admin.site.register(HargaATLPariwisata, HargaATLPariwisataAdmin)
admin.site.register(ATLPenghapusanPariwisata, ATLPenghapusanPariwisataAdmin)
