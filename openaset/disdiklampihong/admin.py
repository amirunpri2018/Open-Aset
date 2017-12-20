### $Id: admin.py,v 1.10 2015/12/05 12:51:26 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikLampihong, HargaTanahDisdikLampihong
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikLampihong, HargaGedungBangunanDisdikLampihong, GedungBangunanRuanganDisdikLampihong

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikLampihong, HargaPeralatanMesinDisdikLampihong

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikLampihongInline(GedungBangunanInline):
    model = GedungBangunanDisdikLampihong



class HargaTanahDisdikLampihongInline(HargaTanahInline):
    model = HargaTanahDisdikLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikLampihongAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikLampihongInline]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(TanahDisdikLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikLampihongAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikLampihong
admin.site.register(TanahDisdikLampihong, TanahDisdikLampihongAdmin)
admin.site.register(HargaTanahDisdikLampihong, HargaTanahDisdikLampihongAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikLampihongInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikLampihongAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(GedungBangunanDisdikLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikLampihongAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikLampihongAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikLampihong
admin.site.register(GedungBangunanDisdikLampihong, GedungBangunanDisdikLampihongAdmin)
admin.site.register(GedungBangunanRuanganDisdikLampihong, GedungBangunanRuanganDisdikLampihongAdmin)
admin.site.register(HargaGedungBangunanDisdikLampihong, HargaGedungBangunanDisdikLampihongAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikLampihongInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikLampihongAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikLampihongAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikLampihong
admin.site.register(PeralatanMesinDisdikLampihong, PeralatanMesinDisdikLampihongAdmin)
admin.site.register(HargaPeralatanMesinDisdikLampihong, HargaPeralatanMesinDisdikLampihongAdmin)






#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikLampihong,  HargaJalanIrigasiJaringanDisdikLampihong

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikLampihongInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikLampihongAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikLampihongAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikLampihong
admin.site.register(JalanIrigasiJaringanDisdikLampihong, JalanIrigasiJaringanDisdikLampihongAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikLampihong, HargaJalanIrigasiJaringanDisdikLampihongAdmin)




#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikLampihong, HargaATLDisdikLampihong

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikLampihongInline(HargaATLInline):
    model = HargaATLDisdikLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikLampihongAdmin(ATLAdmin):
    inlines = [HargaATLDisdikLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(118,160)
            qs_id_sub_skpd.append(81)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(ATLDisdikLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikLampihongAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(118,160)
        qs_id_sub_skpd.append(81)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikLampihong
admin.site.register(ATLDisdikLampihong, ATLDisdikLampihongAdmin)
admin.site.register(HargaATLDisdikLampihong, HargaATLDisdikLampihongAdmin)
