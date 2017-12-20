### $Id: admin.py,v 1.29 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahSATPOLPP, KontrakTanahSATPOLPP, HargaTanahSATPOLPP, TanahUsulHapusSATPOLPP, TahunBerkurangUsulHapusTanahSATPOLPP

from umum.models import TanahPenghapusanSATPOLPP, TahunBerkurangTanahSATPOLPP, PenghapusanTanahSATPOLPP

from umum.models import SKPDAsalTanahSATPOLPP, SKPDTujuanTanahSATPOLPP, FotoTanahSATPOLPP

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanSATPOLPP, KontrakGedungBangunanSATPOLPP, HargaGedungBangunanSATPOLPP, GedungBangunanRuanganSATPOLPP, GedungBangunanUsulHapusSATPOLPP, TahunBerkurangUsulHapusGedungSATPOLPP

from gedungbangunan.models import GedungBangunanPenghapusanSATPOLPP, TahunBerkurangGedungBangunanSATPOLPP, PenghapusanGedungBangunanSATPOLPP

from gedungbangunan.models import SKPDAsalGedungBangunanSATPOLPP, SKPDTujuanGedungBangunanSATPOLPP, FotoGedungBangunanSATPOLPP

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinSATPOLPP, KontrakPeralatanMesinSATPOLPP, HargaPeralatanMesinSATPOLPP, PeralatanMesinUsulHapusSATPOLPP, TahunBerkurangUsulHapusPeralatanMesinSATPOLPP

from peralatanmesin.models import PeralatanMesinPenghapusanSATPOLPP, TahunBerkurangPeralatanMesinSATPOLPP, PenghapusanPeralatanMesinSATPOLPP

from peralatanmesin.models import SKPDAsalPeralatanMesinSATPOLPP, SKPDTujuanPeralatanMesinSATPOLPP, FotoPeralatanMesinSATPOLPP

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahSATPOLPPInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahSATPOLPP



class PenghapusanTanahSATPOLPPInline(PenghapusanTanahInline):
    model = PenghapusanTanahSATPOLPP



class SKPDAsalTanahSATPOLPPInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahSATPOLPP



class SKPDTujuanTanahSATPOLPPInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahSATPOLPP



class FotoTanahSATPOLPPInline(FotoTanahInline):
    model = FotoTanahSATPOLPP



class GedungBangunanSATPOLPPInline(GedungBangunanInline):
    model = GedungBangunanSATPOLPP



class HargaTanahSATPOLPPInline(HargaTanahInline):
    model = HargaTanahSATPOLPP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=25)
        return super(HargaTanahSATPOLPPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahSATPOLPPInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahSATPOLPP


class TanahSATPOLPPAdmin(TanahAdmin):
    inlines = [HargaTanahSATPOLPPInline,
                SKPDAsalTanahSATPOLPPInline,
                FotoTanahSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        return super(TanahSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusSATPOLPPAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahSATPOLPPInline,
                SKPDAsalTanahSATPOLPPInline,
                FotoTanahSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahSATPOLPPAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=25)
        return super(KontrakTanahSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=25)



class HargaTanahSATPOLPPAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanSATPOLPPAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahSATPOLPPInline, TahunBerkurangTanahSATPOLPPInline,
                    SKPDAsalTanahSATPOLPPInline,
                    SKPDTujuanTanahSATPOLPPInline,
                    FotoTanahSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah SATPOLPP
admin.site.register(TanahSATPOLPP, TanahSATPOLPPAdmin)
admin.site.register(TanahUsulHapusSATPOLPP, TanahUsulHapusSATPOLPPAdmin)
admin.site.register(KontrakTanahSATPOLPP, KontrakTanahSATPOLPPAdmin)
admin.site.register(HargaTanahSATPOLPP, HargaTanahSATPOLPPAdmin)
admin.site.register(TanahPenghapusanSATPOLPP, TanahPenghapusanSATPOLPPAdmin)



from gedungbangunan.models import KDPGedungBangunanSATPOLPP


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanSATPOLPPInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanSATPOLPP



class PenghapusanGedungBangunanSATPOLPPInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanSATPOLPP



class SKPDAsalGedungBangunanSATPOLPPInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanSATPOLPP



class SKPDTujuanGedungBangunanSATPOLPPInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanSATPOLPP



class FotoGedungBangunanSATPOLPPInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanSATPOLPP



class HargaGedungBangunanSATPOLPPInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanSATPOLPP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=25)
        return super(HargaGedungBangunanSATPOLPPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungSATPOLPPInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungSATPOLPP


class GedungBangunanSATPOLPPAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanSATPOLPPInline,
                SKPDAsalGedungBangunanSATPOLPPInline,
                FotoGedungBangunanSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        return super(GedungBangunanSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanSATPOLPPAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanSATPOLPPInline,
                SKPDAsalGedungBangunanSATPOLPPInline,
                FotoGedungBangunanSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        return super(KDPGedungBangunanSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganSATPOLPPAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusSATPOLPPAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungSATPOLPPInline,
                    SKPDAsalGedungBangunanSATPOLPPInline,
                    FotoGedungBangunanSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanSATPOLPPAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=25)
        return super(KontrakGedungBangunanSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=25)



class HargaGedungBangunanSATPOLPPAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanSATPOLPPAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanSATPOLPPInline, TahunBerkurangGedungBangunanSATPOLPPInline,
                    SKPDAsalGedungBangunanSATPOLPPInline,
                    SKPDTujuanGedungBangunanSATPOLPPInline,
                    FotoGedungBangunanSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan SATPOLPP
admin.site.register(GedungBangunanSATPOLPP, GedungBangunanSATPOLPPAdmin)
admin.site.register(KDPGedungBangunanSATPOLPP, KDPGedungBangunanSATPOLPPAdmin)
admin.site.register(GedungBangunanRuanganSATPOLPP, GedungBangunanRuanganSATPOLPPAdmin)
admin.site.register(GedungBangunanUsulHapusSATPOLPP, GedungBangunanUsulHapusSATPOLPPAdmin)
admin.site.register(KontrakGedungBangunanSATPOLPP, KontrakGedungBangunanSATPOLPPAdmin)
admin.site.register(HargaGedungBangunanSATPOLPP, HargaGedungBangunanSATPOLPPAdmin)
admin.site.register(GedungBangunanPenghapusanSATPOLPP, GedungBangunanPenghapusanSATPOLPPAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinSATPOLPPInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinSATPOLPP



class PenghapusanPeralatanMesinSATPOLPPInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinSATPOLPP



class SKPDAsalPeralatanMesinSATPOLPPInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinSATPOLPP



class SKPDTujuanPeralatanMesinSATPOLPPInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinSATPOLPP



class FotoPeralatanMesinSATPOLPPInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinSATPOLPP



class HargaPeralatanMesinSATPOLPPInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinSATPOLPP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=25)
        return super(HargaPeralatanMesinSATPOLPPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinSATPOLPPInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinSATPOLPP


class PeralatanMesinSATPOLPPAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinSATPOLPPInline,
                    SKPDAsalPeralatanMesinSATPOLPPInline,
                    FotoPeralatanMesinSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=25)
        return super(PeralatanMesinSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusSATPOLPPAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinSATPOLPPInline,
                    SKPDAsalPeralatanMesinSATPOLPPInline,
                    FotoPeralatanMesinSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinSATPOLPPAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=25)
        return super(KontrakPeralatanMesinSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=25)



class HargaPeralatanMesinSATPOLPPAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanSATPOLPPAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinSATPOLPPInline, TahunBerkurangPeralatanMesinSATPOLPPInline,
                    SKPDAsalPeralatanMesinSATPOLPPInline,
                    SKPDTujuanPeralatanMesinSATPOLPPInline,
                    FotoPeralatanMesinSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin SATPOLPP
admin.site.register(PeralatanMesinSATPOLPP, PeralatanMesinSATPOLPPAdmin)
admin.site.register(PeralatanMesinUsulHapusSATPOLPP, PeralatanMesinUsulHapusSATPOLPPAdmin)
admin.site.register(KontrakPeralatanMesinSATPOLPP, KontrakPeralatanMesinSATPOLPPAdmin)
admin.site.register(HargaPeralatanMesinSATPOLPP, HargaPeralatanMesinSATPOLPPAdmin)
admin.site.register(PeralatanMesinPenghapusanSATPOLPP, PeralatanMesinPenghapusanSATPOLPPAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanSATPOLPP, KontrakJalanIrigasiJaringanSATPOLPP, HargaJalanIrigasiJaringanSATPOLPP, KDPJalanIrigasiJaringanSATPOLPP, JalanIrigasiJaringanUsulHapusSATPOLPP, TahunBerkurangUsulHapusJalanIrigasiJaringanSATPOLPP

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanSATPOLPP, TahunBerkurangJalanIrigasiJaringanSATPOLPP, PenghapusanJalanIrigasiJaringanSATPOLPP

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanSATPOLPP, SKPDTujuanJalanIrigasiJaringanSATPOLPP, FotoJalanIrigasiJaringanSATPOLPP

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanSATPOLPPInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanSATPOLPP



class PenghapusanJalanIrigasiJaringanSATPOLPPInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanSATPOLPP



class SKPDAsalJalanIrigasiJaringanSATPOLPPInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanSATPOLPP



class SKPDTujuanJalanIrigasiJaringanSATPOLPPInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanSATPOLPP



class FotoJalanIrigasiJaringanSATPOLPPInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanSATPOLPP





class HargaJalanIrigasiJaringanSATPOLPPInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanSATPOLPP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=25)
        return super(HargaJalanIrigasiJaringanSATPOLPPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanSATPOLPPInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanSATPOLPP


class JalanIrigasiJaringanSATPOLPPAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSATPOLPPInline,
                    SKPDAsalJalanIrigasiJaringanSATPOLPPInline,
                    FotoJalanIrigasiJaringanSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        return super(JalanIrigasiJaringanSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusSATPOLPPAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanSATPOLPPInline,
                    SKPDAsalJalanIrigasiJaringanSATPOLPPInline,
                    FotoJalanIrigasiJaringanSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanSATPOLPPAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSATPOLPPInline,
                    SKPDAsalJalanIrigasiJaringanSATPOLPPInline,
                    FotoJalanIrigasiJaringanSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        return super(KDPJalanIrigasiJaringanSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanSATPOLPPAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=25)
        return super(KontrakJalanIrigasiJaringanSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=25)



class HargaJalanIrigasiJaringanSATPOLPPAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanSATPOLPPAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanSATPOLPPInline, TahunBerkurangJalanIrigasiJaringanSATPOLPPInline,
                    SKPDAsalJalanIrigasiJaringanSATPOLPPInline,
                    SKPDTujuanJalanIrigasiJaringanSATPOLPPInline,
                    FotoJalanIrigasiJaringanSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan SATPOLPP
admin.site.register(JalanIrigasiJaringanSATPOLPP, JalanIrigasiJaringanSATPOLPPAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusSATPOLPP, JalanIrigasiJaringanUsulHapusSATPOLPPAdmin)
admin.site.register(KDPJalanIrigasiJaringanSATPOLPP, KDPJalanIrigasiJaringanSATPOLPPAdmin)
admin.site.register(KontrakJalanIrigasiJaringanSATPOLPP, KontrakJalanIrigasiJaringanSATPOLPPAdmin)
admin.site.register(HargaJalanIrigasiJaringanSATPOLPP, HargaJalanIrigasiJaringanSATPOLPPAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanSATPOLPP, JalanIrigasiJaringanPenghapusanSATPOLPPAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLSATPOLPP, KontrakATLSATPOLPP, HargaATLSATPOLPP, ATLUsulHapusSATPOLPP, TahunBerkurangUsulHapusATLSATPOLPP

from atl.models import ATLPenghapusanSATPOLPP, TahunBerkurangATLSATPOLPP, PenghapusanATLSATPOLPP

from atl.models import SKPDAsalATLSATPOLPP, SKPDTujuanATLSATPOLPP, FotoATLSATPOLPP

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLSATPOLPPInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLSATPOLPP



class PenghapusanATLSATPOLPPInline(PenghapusanATLInline):
    model = PenghapusanATLSATPOLPP



class SKPDAsalATLSATPOLPPInline(SKPDAsalATLInline):
    model = SKPDAsalATLSATPOLPP



class SKPDTujuanATLSATPOLPPInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLSATPOLPP



class FotoATLSATPOLPPInline(FotoATLInline):
    model = FotoATLSATPOLPP



class HargaATLSATPOLPPInline(HargaATLInline):
    model = HargaATLSATPOLPP

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=25)
        return super(HargaATLSATPOLPPInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLSATPOLPPInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLSATPOLPP


class ATLSATPOLPPAdmin(ATLAdmin):
    inlines = [HargaATLSATPOLPPInline,
                    SKPDAsalATLSATPOLPPInline,
                    FotoATLSATPOLPPInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=25)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=25)
        return super(ATLSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusSATPOLPPAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLSATPOLPPInline,
                    SKPDAsalATLSATPOLPPInline,
                    FotoATLSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLSATPOLPPAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=25)
        return super(KontrakATLSATPOLPPAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=25)



class HargaATLSATPOLPPAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanSATPOLPPAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLSATPOLPPInline, TahunBerkurangATLSATPOLPPInline,
                    SKPDAsalATLSATPOLPPInline,
                    SKPDTujuanATLSATPOLPPInline,
                    FotoATLSATPOLPPInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=25)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL SATPOLPP
admin.site.register(ATLSATPOLPP, ATLSATPOLPPAdmin)
admin.site.register(ATLUsulHapusSATPOLPP, ATLUsulHapusSATPOLPPAdmin)
admin.site.register(KontrakATLSATPOLPP, KontrakATLSATPOLPPAdmin)
admin.site.register(HargaATLSATPOLPP, HargaATLSATPOLPPAdmin)
admin.site.register(ATLPenghapusanSATPOLPP, ATLPenghapusanSATPOLPPAdmin)
