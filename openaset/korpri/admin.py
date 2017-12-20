### $Id: admin.py,v 1.33 2017/12/18 09:12:52 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahSekretariatKorpri, KontrakTanahSekretariatKorpri, HargaTanahSekretariatKorpri, TanahUsulHapusSekretariatKorpri, TahunBerkurangUsulHapusTanahSekretariatKorpri

from umum.models import TanahPenghapusanSekretariatKorpri, TahunBerkurangTanahSekretariatKorpri, PenghapusanTanahSekretariatKorpri

from umum.models import SKPDAsalTanahSekretariatKorpri, SKPDTujuanTanahSekretariatKorpri, FotoTanahSekretariatKorpri

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanSekretariatKorpri, KontrakGedungBangunanSekretariatKorpri, HargaGedungBangunanSekretariatKorpri, GedungBangunanRuanganSekretariatKorpri, GedungBangunanUsulHapusSekretariatKorpri, TahunBerkurangUsulHapusGedungSekretariatKorpri

from gedungbangunan.models import GedungBangunanPenghapusanSekretariatKorpri, TahunBerkurangGedungBangunanSekretariatKorpri, PenghapusanGedungBangunanSekretariatKorpri

from gedungbangunan.models import SKPDAsalGedungBangunanSekretariatKorpri, SKPDTujuanGedungBangunanSekretariatKorpri, FotoGedungBangunanSekretariatKorpri

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinSekretariatKorpri, KontrakPeralatanMesinSekretariatKorpri, HargaPeralatanMesinSekretariatKorpri, PeralatanMesinUsulHapusSekretariatKorpri, TahunBerkurangUsulHapusPeralatanMesinSekretariatKorpri

from peralatanmesin.models import PeralatanMesinPenghapusanSekretariatKorpri, TahunBerkurangPeralatanMesinSekretariatKorpri, PenghapusanPeralatanMesinSekretariatKorpri

from peralatanmesin.models import SKPDAsalPeralatanMesinSekretariatKorpri, SKPDTujuanPeralatanMesinSekretariatKorpri, FotoPeralatanMesinSekretariatKorpri

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahSekretariatKorpriInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahSekretariatKorpri



class PenghapusanTanahSekretariatKorpriInline(PenghapusanTanahInline):
    model = PenghapusanTanahSekretariatKorpri



class SKPDAsalTanahSekretariatKorpriInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahSekretariatKorpri



class SKPDTujuanTanahSekretariatKorpriInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahSekretariatKorpri



class FotoTanahSekretariatKorpriInline(FotoTanahInline):
    model = FotoTanahSekretariatKorpri



class GedungBangunanSekretariatKorpriInline(GedungBangunanInline):
    model = GedungBangunanSekretariatKorpri



class HargaTanahSekretariatKorpriInline(HargaTanahInline):
    model = HargaTanahSekretariatKorpri

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=27)
        return super(HargaTanahSekretariatKorpriInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahSekretariatKorpriInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahSekretariatKorpri


class TanahSekretariatKorpriAdmin(TanahAdmin):
    inlines = [HargaTanahSekretariatKorpriInline,
                SKPDAsalTanahSekretariatKorpriInline,
                FotoTanahSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        return super(TanahSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusSekretariatKorpriAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahSekretariatKorpriInline,
                SKPDAsalTanahSekretariatKorpriInline,
                FotoTanahSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahSekretariatKorpriAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=27)
        return super(KontrakTanahSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=27)



class HargaTanahSekretariatKorpriAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanSekretariatKorpriAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahSekretariatKorpriInline, TahunBerkurangTanahSekretariatKorpriInline,
                    SKPDAsalTanahSekretariatKorpriInline,
                    SKPDTujuanTanahSekretariatKorpriInline,
                    FotoTanahSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah SekretariatKorpri
admin.site.register(TanahSekretariatKorpri, TanahSekretariatKorpriAdmin)
admin.site.register(TanahUsulHapusSekretariatKorpri, TanahUsulHapusSekretariatKorpriAdmin)
admin.site.register(KontrakTanahSekretariatKorpri, KontrakTanahSekretariatKorpriAdmin)
admin.site.register(HargaTanahSekretariatKorpri, HargaTanahSekretariatKorpriAdmin)
admin.site.register(TanahPenghapusanSekretariatKorpri, TanahPenghapusanSekretariatKorpriAdmin)



from gedungbangunan.models import KDPGedungBangunanSekretariatKorpri


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanSekretariatKorpriInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanSekretariatKorpri



class PenghapusanGedungBangunanSekretariatKorpriInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanSekretariatKorpri



class SKPDAsalGedungBangunanSekretariatKorpriInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanSekretariatKorpri



class SKPDTujuanGedungBangunanSekretariatKorpriInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanSekretariatKorpri



class FotoGedungBangunanSekretariatKorpriInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanSekretariatKorpri



class HargaGedungBangunanSekretariatKorpriInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanSekretariatKorpri

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=27)
        return super(HargaGedungBangunanSekretariatKorpriInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungSekretariatKorpriInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungSekretariatKorpri


class GedungBangunanSekretariatKorpriAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanSekretariatKorpriInline,
                SKPDAsalGedungBangunanSekretariatKorpriInline,
                FotoGedungBangunanSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        return super(GedungBangunanSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanSekretariatKorpriAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanSekretariatKorpriInline,
                SKPDAsalGedungBangunanSekretariatKorpriInline,
                FotoGedungBangunanSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        return super(KDPGedungBangunanSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganSekretariatKorpriAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusSekretariatKorpriAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungSekretariatKorpriInline,
                    SKPDAsalGedungBangunanSekretariatKorpriInline,
                    FotoGedungBangunanSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanSekretariatKorpriAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=27)
        return super(KontrakGedungBangunanSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=27)



class HargaGedungBangunanSekretariatKorpriAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanSekretariatKorpriAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanSekretariatKorpriInline, TahunBerkurangGedungBangunanSekretariatKorpriInline,
                    SKPDAsalGedungBangunanSekretariatKorpriInline,
                    SKPDTujuanGedungBangunanSekretariatKorpriInline,
                    FotoGedungBangunanSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan SekretariatKorpri
admin.site.register(GedungBangunanSekretariatKorpri, GedungBangunanSekretariatKorpriAdmin)
admin.site.register(KDPGedungBangunanSekretariatKorpri, KDPGedungBangunanSekretariatKorpriAdmin)
admin.site.register(GedungBangunanRuanganSekretariatKorpri, GedungBangunanRuanganSekretariatKorpriAdmin)
admin.site.register(GedungBangunanUsulHapusSekretariatKorpri, GedungBangunanUsulHapusSekretariatKorpriAdmin)
admin.site.register(KontrakGedungBangunanSekretariatKorpri, KontrakGedungBangunanSekretariatKorpriAdmin)
admin.site.register(HargaGedungBangunanSekretariatKorpri, HargaGedungBangunanSekretariatKorpriAdmin)
admin.site.register(GedungBangunanPenghapusanSekretariatKorpri, GedungBangunanPenghapusanSekretariatKorpriAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinSekretariatKorpriInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinSekretariatKorpri



class PenghapusanPeralatanMesinSekretariatKorpriInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinSekretariatKorpri



class SKPDAsalPeralatanMesinSekretariatKorpriInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinSekretariatKorpri



class SKPDTujuanPeralatanMesinSekretariatKorpriInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinSekretariatKorpri



class FotoPeralatanMesinSekretariatKorpriInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinSekretariatKorpri



class HargaPeralatanMesinSekretariatKorpriInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinSekretariatKorpri

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=27)
        return super(HargaPeralatanMesinSekretariatKorpriInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinSekretariatKorpriInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinSekretariatKorpri


class PeralatanMesinSekretariatKorpriAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinSekretariatKorpriInline,
                    SKPDAsalPeralatanMesinSekretariatKorpriInline,
                    FotoPeralatanMesinSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=27)
        return super(PeralatanMesinSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusSekretariatKorpriAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinSekretariatKorpriInline,
                    SKPDAsalPeralatanMesinSekretariatKorpriInline,
                    FotoPeralatanMesinSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinSekretariatKorpriAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=27)
        return super(KontrakPeralatanMesinSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=27)



class HargaPeralatanMesinSekretariatKorpriAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanSekretariatKorpriAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinSekretariatKorpriInline, TahunBerkurangPeralatanMesinSekretariatKorpriInline,
                    SKPDAsalPeralatanMesinSekretariatKorpriInline,
                    SKPDTujuanPeralatanMesinSekretariatKorpriInline,
                    FotoPeralatanMesinSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin SekretariatKorpri
admin.site.register(PeralatanMesinSekretariatKorpri, PeralatanMesinSekretariatKorpriAdmin)
admin.site.register(PeralatanMesinUsulHapusSekretariatKorpri, PeralatanMesinUsulHapusSekretariatKorpriAdmin)
admin.site.register(KontrakPeralatanMesinSekretariatKorpri, KontrakPeralatanMesinSekretariatKorpriAdmin)
admin.site.register(HargaPeralatanMesinSekretariatKorpri, HargaPeralatanMesinSekretariatKorpriAdmin)
admin.site.register(PeralatanMesinPenghapusanSekretariatKorpri, PeralatanMesinPenghapusanSekretariatKorpriAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanSekretariatKorpri, KontrakJalanIrigasiJaringanSekretariatKorpri, HargaJalanIrigasiJaringanSekretariatKorpri, KDPJalanIrigasiJaringanSekretariatKorpri, JalanIrigasiJaringanUsulHapusSekretariatKorpri, TahunBerkurangUsulHapusJalanIrigasiJaringanSekretariatKorpri

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanSekretariatKorpri, TahunBerkurangJalanIrigasiJaringanSekretariatKorpri, PenghapusanJalanIrigasiJaringanSekretariatKorpri

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanSekretariatKorpri, SKPDTujuanJalanIrigasiJaringanSekretariatKorpri, FotoJalanIrigasiJaringanSekretariatKorpri

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanSekretariatKorpriInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanSekretariatKorpri



class PenghapusanJalanIrigasiJaringanSekretariatKorpriInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanSekretariatKorpri



class SKPDAsalJalanIrigasiJaringanSekretariatKorpriInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanSekretariatKorpri



class SKPDTujuanJalanIrigasiJaringanSekretariatKorpriInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanSekretariatKorpri



class FotoJalanIrigasiJaringanSekretariatKorpriInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanSekretariatKorpri





class HargaJalanIrigasiJaringanSekretariatKorpriInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanSekretariatKorpri

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=27)
        return super(HargaJalanIrigasiJaringanSekretariatKorpriInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanSekretariatKorpriInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanSekretariatKorpri


class JalanIrigasiJaringanSekretariatKorpriAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSekretariatKorpriInline,
                    SKPDAsalJalanIrigasiJaringanSekretariatKorpriInline,
                    FotoJalanIrigasiJaringanSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        return super(JalanIrigasiJaringanSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusSekretariatKorpriAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanSekretariatKorpriInline,
                    SKPDAsalJalanIrigasiJaringanSekretariatKorpriInline,
                    FotoJalanIrigasiJaringanSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanSekretariatKorpriAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanSekretariatKorpriInline,
                    SKPDAsalJalanIrigasiJaringanSekretariatKorpriInline,
                    FotoJalanIrigasiJaringanSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        return super(KDPJalanIrigasiJaringanSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanSekretariatKorpriAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=27)
        return super(KontrakJalanIrigasiJaringanSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=27)



class HargaJalanIrigasiJaringanSekretariatKorpriAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanSekretariatKorpriAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanSekretariatKorpriInline, TahunBerkurangJalanIrigasiJaringanSekretariatKorpriInline,
                    SKPDAsalJalanIrigasiJaringanSekretariatKorpriInline,
                    SKPDTujuanJalanIrigasiJaringanSekretariatKorpriInline,
                    FotoJalanIrigasiJaringanSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan SekretariatKorpri
admin.site.register(JalanIrigasiJaringanSekretariatKorpri, JalanIrigasiJaringanSekretariatKorpriAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusSekretariatKorpri, JalanIrigasiJaringanUsulHapusSekretariatKorpriAdmin)
admin.site.register(KDPJalanIrigasiJaringanSekretariatKorpri, KDPJalanIrigasiJaringanSekretariatKorpriAdmin)
admin.site.register(KontrakJalanIrigasiJaringanSekretariatKorpri, KontrakJalanIrigasiJaringanSekretariatKorpriAdmin)
admin.site.register(HargaJalanIrigasiJaringanSekretariatKorpri, HargaJalanIrigasiJaringanSekretariatKorpriAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanSekretariatKorpri, JalanIrigasiJaringanPenghapusanSekretariatKorpriAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLSekretariatKorpri, KontrakATLSekretariatKorpri, HargaATLSekretariatKorpri, ATLUsulHapusSekretariatKorpri, TahunBerkurangUsulHapusATLSekretariatKorpri

from atl.models import ATLPenghapusanSekretariatKorpri, TahunBerkurangATLSekretariatKorpri, PenghapusanATLSekretariatKorpri

from atl.models import SKPDAsalATLSekretariatKorpri, SKPDTujuanATLSekretariatKorpri, FotoATLSekretariatKorpri

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLSekretariatKorpriInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLSekretariatKorpri



class PenghapusanATLSekretariatKorpriInline(PenghapusanATLInline):
    model = PenghapusanATLSekretariatKorpri



class SKPDAsalATLSekretariatKorpriInline(SKPDAsalATLInline):
    model = SKPDAsalATLSekretariatKorpri



class SKPDTujuanATLSekretariatKorpriInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLSekretariatKorpri



class FotoATLSekretariatKorpriInline(FotoATLInline):
    model = FotoATLSekretariatKorpri



class HargaATLSekretariatKorpriInline(HargaATLInline):
    model = HargaATLSekretariatKorpri

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=27)
        return super(HargaATLSekretariatKorpriInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLSekretariatKorpriInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLSekretariatKorpri


class ATLSekretariatKorpriAdmin(ATLAdmin):
    inlines = [HargaATLSekretariatKorpriInline,
                    SKPDAsalATLSekretariatKorpriInline,
                    FotoATLSekretariatKorpriInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=27)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=27)
        return super(ATLSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusSekretariatKorpriAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLSekretariatKorpriInline,
                    SKPDAsalATLSekretariatKorpriInline,
                    FotoATLSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLSekretariatKorpriAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=27)
        return super(KontrakATLSekretariatKorpriAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=27)



class HargaATLSekretariatKorpriAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanSekretariatKorpriAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLSekretariatKorpriInline, TahunBerkurangATLSekretariatKorpriInline,
                    SKPDAsalATLSekretariatKorpriInline,
                    SKPDTujuanATLSekretariatKorpriInline,
                    FotoATLSekretariatKorpriInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=27)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL SekretariatKorpri
admin.site.register(ATLSekretariatKorpri, ATLSekretariatKorpriAdmin)
admin.site.register(ATLUsulHapusSekretariatKorpri, ATLUsulHapusSekretariatKorpriAdmin)
admin.site.register(KontrakATLSekretariatKorpri, KontrakATLSekretariatKorpriAdmin)
admin.site.register(HargaATLSekretariatKorpri, HargaATLSekretariatKorpriAdmin)
admin.site.register(ATLPenghapusanSekretariatKorpri, ATLPenghapusanSekretariatKorpriAdmin)
