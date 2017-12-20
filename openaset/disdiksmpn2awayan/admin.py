### $Id: admin.py,v 1.15 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikSMPN2Awayan, HargaTanahDisdikSMPN2Awayan
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikSMPN2Awayan, HargaGedungBangunanDisdikSMPN2Awayan, GedungBangunanRuanganDisdikSMPN2Awayan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikSMPN2Awayan, HargaPeralatanMesinDisdikSMPN2Awayan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikSMPN2AwayanInline(GedungBangunanInline):
    model = GedungBangunanDisdikSMPN2Awayan



class HargaTanahDisdikSMPN2AwayanInline(HargaTanahInline):
    model = HargaTanahDisdikSMPN2Awayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikSMPN2AwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikSMPN2AwayanAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikSMPN2AwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=103
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDisdikSMPN2AwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikSMPN2AwayanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikSMPN2Awayan
admin.site.register(TanahDisdikSMPN2Awayan, TanahDisdikSMPN2AwayanAdmin)
admin.site.register(HargaTanahDisdikSMPN2Awayan, HargaTanahDisdikSMPN2AwayanAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikSMPN2AwayanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikSMPN2Awayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikSMPN2AwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikSMPN2AwayanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikSMPN2AwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=103
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDisdikSMPN2AwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikSMPN2AwayanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 103
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikSMPN2AwayanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikSMPN2Awayan
admin.site.register(GedungBangunanDisdikSMPN2Awayan, GedungBangunanDisdikSMPN2AwayanAdmin)
admin.site.register(GedungBangunanRuanganDisdikSMPN2Awayan, GedungBangunanRuanganDisdikSMPN2AwayanAdmin)
admin.site.register(HargaGedungBangunanDisdikSMPN2Awayan, HargaGedungBangunanDisdikSMPN2AwayanAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikSMPN2AwayanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikSMPN2Awayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikSMPN2AwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikSMPN2AwayanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikSMPN2AwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=103
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=103
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikSMPN2AwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikSMPN2AwayanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikSMPN2Awayan
admin.site.register(PeralatanMesinDisdikSMPN2Awayan, PeralatanMesinDisdikSMPN2AwayanAdmin)
admin.site.register(HargaPeralatanMesinDisdikSMPN2Awayan, HargaPeralatanMesinDisdikSMPN2AwayanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikSMPN2Awayan, HargaJalanIrigasiJaringanDisdikSMPN2Awayan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikSMPN2AwayanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikSMPN2Awayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikSMPN2AwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikSMPN2AwayanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikSMPN2AwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=103
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikSMPN2AwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikSMPN2AwayanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikSMPN2Awayan
admin.site.register(JalanIrigasiJaringanDisdikSMPN2Awayan, JalanIrigasiJaringanDisdikSMPN2AwayanAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikSMPN2Awayan, HargaJalanIrigasiJaringanDisdikSMPN2AwayanAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikSMPN2Awayan, HargaATLDisdikSMPN2Awayan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikSMPN2AwayanInline(HargaATLInline):
    model = HargaATLDisdikSMPN2Awayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikSMPN2AwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikSMPN2AwayanAdmin(ATLAdmin):
    inlines = [HargaATLDisdikSMPN2AwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=103
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=103
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDisdikSMPN2AwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikSMPN2AwayanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=103
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikSMPN2Awayan
admin.site.register(ATLDisdikSMPN2Awayan, ATLDisdikSMPN2AwayanAdmin)
admin.site.register(HargaATLDisdikSMPN2Awayan, HargaATLDisdikSMPN2AwayanAdmin)
