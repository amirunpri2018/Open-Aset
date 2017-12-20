### $Id: admin.py,v 1.15 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikSMPN2Halong, HargaTanahDisdikSMPN2Halong
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikSMPN2Halong, HargaGedungBangunanDisdikSMPN2Halong, GedungBangunanRuanganDisdikSMPN2Halong

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikSMPN2Halong, HargaPeralatanMesinDisdikSMPN2Halong

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikSMPN2HalongInline(GedungBangunanInline):
    model = GedungBangunanDisdikSMPN2Halong



class HargaTanahDisdikSMPN2HalongInline(HargaTanahInline):
    model = HargaTanahDisdikSMPN2Halong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikSMPN2HalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikSMPN2HalongAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikSMPN2HalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=105
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDisdikSMPN2HalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikSMPN2HalongAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikSMPN2Halong
admin.site.register(TanahDisdikSMPN2Halong, TanahDisdikSMPN2HalongAdmin)
admin.site.register(HargaTanahDisdikSMPN2Halong, HargaTanahDisdikSMPN2HalongAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikSMPN2HalongInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikSMPN2Halong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikSMPN2HalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikSMPN2HalongAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikSMPN2HalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=105
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDisdikSMPN2HalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikSMPN2HalongAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 105
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikSMPN2HalongAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikSMPN2Halong
admin.site.register(GedungBangunanDisdikSMPN2Halong, GedungBangunanDisdikSMPN2HalongAdmin)
admin.site.register(GedungBangunanRuanganDisdikSMPN2Halong, GedungBangunanRuanganDisdikSMPN2HalongAdmin)
admin.site.register(HargaGedungBangunanDisdikSMPN2Halong, HargaGedungBangunanDisdikSMPN2HalongAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikSMPN2HalongInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikSMPN2Halong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikSMPN2HalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikSMPN2HalongAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikSMPN2HalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=105
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=105
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikSMPN2HalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikSMPN2HalongAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikSMPN2Halong
admin.site.register(PeralatanMesinDisdikSMPN2Halong, PeralatanMesinDisdikSMPN2HalongAdmin)
admin.site.register(HargaPeralatanMesinDisdikSMPN2Halong, HargaPeralatanMesinDisdikSMPN2HalongAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikSMPN2Halong, HargaJalanIrigasiJaringanDisdikSMPN2Halong

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikSMPN2HalongInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikSMPN2Halong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikSMPN2HalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikSMPN2HalongAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikSMPN2HalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=105
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikSMPN2HalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikSMPN2HalongAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikSMPN2Halong
admin.site.register(JalanIrigasiJaringanDisdikSMPN2Halong, JalanIrigasiJaringanDisdikSMPN2HalongAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikSMPN2Halong, HargaJalanIrigasiJaringanDisdikSMPN2HalongAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikSMPN2Halong, HargaATLDisdikSMPN2Halong

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikSMPN2HalongInline(HargaATLInline):
    model = HargaATLDisdikSMPN2Halong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikSMPN2HalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikSMPN2HalongAdmin(ATLAdmin):
    inlines = [HargaATLDisdikSMPN2HalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=105
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=105
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDisdikSMPN2HalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikSMPN2HalongAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=105
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikSMPN2Halong
admin.site.register(ATLDisdikSMPN2Halong, ATLDisdikSMPN2HalongAdmin)
admin.site.register(HargaATLDisdikSMPN2Halong, HargaATLDisdikSMPN2HalongAdmin)
