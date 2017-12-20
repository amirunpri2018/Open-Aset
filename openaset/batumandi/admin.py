### $Id: admin.py,v 1.30 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahBatumandi, KontrakTanahBatumandi, HargaTanahBatumandi, TanahUsulHapusBatumandi, TahunBerkurangUsulHapusTanahBatumandi

from umum.models import TanahPenghapusanBatumandi, TahunBerkurangTanahBatumandi, PenghapusanTanahBatumandi

from umum.models import SKPDAsalTanahBatumandi, SKPDTujuanTanahBatumandi, FotoTanahBatumandi

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanBatumandi, KontrakGedungBangunanBatumandi, HargaGedungBangunanBatumandi, GedungBangunanRuanganBatumandi, GedungBangunanUsulHapusBatumandi, TahunBerkurangUsulHapusGedungBatumandi

from gedungbangunan.models import GedungBangunanPenghapusanBatumandi, TahunBerkurangGedungBangunanBatumandi, PenghapusanGedungBangunanBatumandi

from gedungbangunan.models import SKPDAsalGedungBangunanBatumandi, SKPDTujuanGedungBangunanBatumandi, FotoGedungBangunanBatumandi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinBatumandi, KontrakPeralatanMesinBatumandi, HargaPeralatanMesinBatumandi, PeralatanMesinUsulHapusBatumandi, TahunBerkurangUsulHapusPeralatanMesinBatumandi

from peralatanmesin.models import PeralatanMesinPenghapusanBatumandi, TahunBerkurangPeralatanMesinBatumandi, PenghapusanPeralatanMesinBatumandi

from peralatanmesin.models import SKPDAsalPeralatanMesinBatumandi, SKPDTujuanPeralatanMesinBatumandi, FotoPeralatanMesinBatumandi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahBatumandiInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahBatumandi



class PenghapusanTanahBatumandiInline(PenghapusanTanahInline):
    model = PenghapusanTanahBatumandi



class SKPDAsalTanahBatumandiInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahBatumandi



class SKPDTujuanTanahBatumandiInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahBatumandi



class FotoTanahBatumandiInline(FotoTanahInline):
    model = FotoTanahBatumandi



class GedungBangunanBatumandiInline(GedungBangunanInline):
    model = GedungBangunanBatumandi



class HargaTanahBatumandiInline(HargaTanahInline):
    model = HargaTanahBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=32)
        return super(HargaTanahBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahBatumandiInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahBatumandi


class TanahBatumandiAdmin(TanahAdmin):
    inlines = [HargaTanahBatumandiInline,
                SKPDAsalTanahBatumandiInline,
                FotoTanahBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        return super(TanahBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusBatumandiAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahBatumandiInline,
                SKPDAsalTanahBatumandiInline,
                FotoTanahBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahBatumandiAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=32)
        return super(KontrakTanahBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=32)



class HargaTanahBatumandiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanBatumandiAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahBatumandiInline, TahunBerkurangTanahBatumandiInline,
                    SKPDAsalTanahBatumandiInline,
                    SKPDTujuanTanahBatumandiInline,
                    FotoTanahBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah Batumandi
admin.site.register(TanahBatumandi, TanahBatumandiAdmin)
admin.site.register(TanahUsulHapusBatumandi, TanahUsulHapusBatumandiAdmin)
admin.site.register(KontrakTanahBatumandi, KontrakTanahBatumandiAdmin)
admin.site.register(HargaTanahBatumandi, HargaTanahBatumandiAdmin)
admin.site.register(TanahPenghapusanBatumandi, TanahPenghapusanBatumandiAdmin)



from gedungbangunan.models import KDPGedungBangunanBatumandi


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanBatumandiInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanBatumandi



class PenghapusanGedungBangunanBatumandiInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanBatumandi



class SKPDAsalGedungBangunanBatumandiInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanBatumandi



class SKPDTujuanGedungBangunanBatumandiInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanBatumandi



class FotoGedungBangunanBatumandiInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanBatumandi



class HargaGedungBangunanBatumandiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=32)
        return super(HargaGedungBangunanBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungBatumandiInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungBatumandi


class GedungBangunanBatumandiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanBatumandiInline,
                SKPDAsalGedungBangunanBatumandiInline,
                FotoGedungBangunanBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        return super(GedungBangunanBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanBatumandiAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanBatumandiInline,
                SKPDAsalGedungBangunanBatumandiInline,
                FotoGedungBangunanBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        return super(KDPGedungBangunanBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganBatumandiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusBatumandiAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungBatumandiInline,
                    SKPDAsalGedungBangunanBatumandiInline,
                    FotoGedungBangunanBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanBatumandiAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=32)
        return super(KontrakGedungBangunanBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=32)



class HargaGedungBangunanBatumandiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanBatumandiAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanBatumandiInline, TahunBerkurangGedungBangunanBatumandiInline,
                    SKPDAsalGedungBangunanBatumandiInline,
                    SKPDTujuanGedungBangunanBatumandiInline,
                    FotoGedungBangunanBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan Batumandi
admin.site.register(GedungBangunanBatumandi, GedungBangunanBatumandiAdmin)
admin.site.register(KDPGedungBangunanBatumandi, KDPGedungBangunanBatumandiAdmin)
admin.site.register(GedungBangunanRuanganBatumandi, GedungBangunanRuanganBatumandiAdmin)
admin.site.register(GedungBangunanUsulHapusBatumandi, GedungBangunanUsulHapusBatumandiAdmin)
admin.site.register(KontrakGedungBangunanBatumandi, KontrakGedungBangunanBatumandiAdmin)
admin.site.register(HargaGedungBangunanBatumandi, HargaGedungBangunanBatumandiAdmin)
admin.site.register(GedungBangunanPenghapusanBatumandi, GedungBangunanPenghapusanBatumandiAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinBatumandiInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinBatumandi



class PenghapusanPeralatanMesinBatumandiInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinBatumandi



class SKPDAsalPeralatanMesinBatumandiInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinBatumandi



class SKPDTujuanPeralatanMesinBatumandiInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinBatumandi



class FotoPeralatanMesinBatumandiInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinBatumandi



class HargaPeralatanMesinBatumandiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=32)
        return super(HargaPeralatanMesinBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinBatumandiInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinBatumandi


class PeralatanMesinBatumandiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinBatumandiInline,
                    SKPDAsalPeralatanMesinBatumandiInline,
                    FotoPeralatanMesinBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=32)
        return super(PeralatanMesinBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusBatumandiAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinBatumandiInline,
                    SKPDAsalPeralatanMesinBatumandiInline,
                    FotoPeralatanMesinBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinBatumandiAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=32)
        return super(KontrakPeralatanMesinBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=32)



class HargaPeralatanMesinBatumandiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanBatumandiAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinBatumandiInline, TahunBerkurangPeralatanMesinBatumandiInline,
                    SKPDAsalPeralatanMesinBatumandiInline,
                    SKPDTujuanPeralatanMesinBatumandiInline,
                    FotoPeralatanMesinBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin Batumandi
admin.site.register(PeralatanMesinBatumandi, PeralatanMesinBatumandiAdmin)
admin.site.register(PeralatanMesinUsulHapusBatumandi, PeralatanMesinUsulHapusBatumandiAdmin)
admin.site.register(KontrakPeralatanMesinBatumandi, KontrakPeralatanMesinBatumandiAdmin)
admin.site.register(HargaPeralatanMesinBatumandi, HargaPeralatanMesinBatumandiAdmin)
admin.site.register(PeralatanMesinPenghapusanBatumandi, PeralatanMesinPenghapusanBatumandiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanBatumandi, KontrakJalanIrigasiJaringanBatumandi, HargaJalanIrigasiJaringanBatumandi, KDPJalanIrigasiJaringanBatumandi, JalanIrigasiJaringanUsulHapusBatumandi, TahunBerkurangUsulHapusJalanIrigasiJaringanBatumandi

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanBatumandi, TahunBerkurangJalanIrigasiJaringanBatumandi, PenghapusanJalanIrigasiJaringanBatumandi

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanBatumandi, SKPDTujuanJalanIrigasiJaringanBatumandi, FotoJalanIrigasiJaringanBatumandi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanBatumandiInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanBatumandi



class PenghapusanJalanIrigasiJaringanBatumandiInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanBatumandi



class SKPDAsalJalanIrigasiJaringanBatumandiInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanBatumandi



class SKPDTujuanJalanIrigasiJaringanBatumandiInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanBatumandi



class FotoJalanIrigasiJaringanBatumandiInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanBatumandi





class HargaJalanIrigasiJaringanBatumandiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=32)
        return super(HargaJalanIrigasiJaringanBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanBatumandiInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanBatumandi


class JalanIrigasiJaringanBatumandiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBatumandiInline,
                    SKPDAsalJalanIrigasiJaringanBatumandiInline,
                    FotoJalanIrigasiJaringanBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        return super(JalanIrigasiJaringanBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusBatumandiAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanBatumandiInline,
                    SKPDAsalJalanIrigasiJaringanBatumandiInline,
                    FotoJalanIrigasiJaringanBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanBatumandiAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanBatumandiInline,
                    SKPDAsalJalanIrigasiJaringanBatumandiInline,
                    FotoJalanIrigasiJaringanBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        return super(KDPJalanIrigasiJaringanBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanBatumandiAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=32)
        return super(KontrakJalanIrigasiJaringanBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=32)



class HargaJalanIrigasiJaringanBatumandiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanBatumandiAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanBatumandiInline, TahunBerkurangJalanIrigasiJaringanBatumandiInline,
                    SKPDAsalJalanIrigasiJaringanBatumandiInline,
                    SKPDTujuanJalanIrigasiJaringanBatumandiInline,
                    FotoJalanIrigasiJaringanBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan Batumandi
admin.site.register(JalanIrigasiJaringanBatumandi, JalanIrigasiJaringanBatumandiAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusBatumandi, JalanIrigasiJaringanUsulHapusBatumandiAdmin)
admin.site.register(KDPJalanIrigasiJaringanBatumandi, KDPJalanIrigasiJaringanBatumandiAdmin)
admin.site.register(KontrakJalanIrigasiJaringanBatumandi, KontrakJalanIrigasiJaringanBatumandiAdmin)
admin.site.register(HargaJalanIrigasiJaringanBatumandi, HargaJalanIrigasiJaringanBatumandiAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanBatumandi, JalanIrigasiJaringanPenghapusanBatumandiAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLBatumandi, KontrakATLBatumandi, HargaATLBatumandi, ATLUsulHapusBatumandi, TahunBerkurangUsulHapusATLBatumandi

from atl.models import ATLPenghapusanBatumandi, TahunBerkurangATLBatumandi, PenghapusanATLBatumandi

from atl.models import SKPDAsalATLBatumandi, SKPDTujuanATLBatumandi, FotoATLBatumandi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLBatumandiInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLBatumandi



class PenghapusanATLBatumandiInline(PenghapusanATLInline):
    model = PenghapusanATLBatumandi



class SKPDAsalATLBatumandiInline(SKPDAsalATLInline):
    model = SKPDAsalATLBatumandi



class SKPDTujuanATLBatumandiInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLBatumandi



class FotoATLBatumandiInline(FotoATLInline):
    model = FotoATLBatumandi



class HargaATLBatumandiInline(HargaATLInline):
    model = HargaATLBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=32)
        return super(HargaATLBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLBatumandiInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLBatumandi


class ATLBatumandiAdmin(ATLAdmin):
    inlines = [HargaATLBatumandiInline,
                    SKPDAsalATLBatumandiInline,
                    FotoATLBatumandiInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=32)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=32)
        return super(ATLBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusBatumandiAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLBatumandiInline,
                    SKPDAsalATLBatumandiInline,
                    FotoATLBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLBatumandiAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=32)
        return super(KontrakATLBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=32)



class HargaATLBatumandiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanBatumandiAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLBatumandiInline, TahunBerkurangATLBatumandiInline,
                    SKPDAsalATLBatumandiInline,
                    SKPDTujuanATLBatumandiInline,
                    FotoATLBatumandiInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=32)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL Batumandi
admin.site.register(ATLBatumandi, ATLBatumandiAdmin)
admin.site.register(ATLUsulHapusBatumandi, ATLUsulHapusBatumandiAdmin)
admin.site.register(KontrakATLBatumandi, KontrakATLBatumandiAdmin)
admin.site.register(HargaATLBatumandi, HargaATLBatumandiAdmin)
admin.site.register(ATLPenghapusanBatumandi, ATLPenghapusanBatumandiAdmin)
