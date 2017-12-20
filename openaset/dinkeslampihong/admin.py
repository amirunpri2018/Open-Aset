### $Id: admin.py,v 1.13 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDinkesLampihong, HargaTanahDinkesLampihong
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDinkesLampihong, HargaGedungBangunanDinkesLampihong, GedungBangunanRuanganDinkesLampihong

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDinkesLampihong, HargaPeralatanMesinDinkesLampihong

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDinkesLampihongInline(GedungBangunanInline):
    model = GedungBangunanDinkesLampihong



class HargaTanahDinkesLampihongInline(HargaTanahInline):
    model = HargaTanahDinkesLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=5)
        return super(HargaTanahDinkesLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDinkesLampihongAdmin(TanahAdmin):
    inlines = [HargaTanahDinkesLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=29
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDinkesLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDinkesLampihongAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DinkesLampihong
admin.site.register(TanahDinkesLampihong, TanahDinkesLampihongAdmin)
admin.site.register(HargaTanahDinkesLampihong, HargaTanahDinkesLampihongAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDinkesLampihongInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDinkesLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=5)
        return super(HargaGedungBangunanDinkesLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDinkesLampihongAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDinkesLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=29
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDinkesLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDinkesLampihongAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 29
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDinkesLampihongAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DinkesLampihong
admin.site.register(GedungBangunanDinkesLampihong, GedungBangunanDinkesLampihongAdmin)
admin.site.register(GedungBangunanRuanganDinkesLampihong, GedungBangunanRuanganDinkesLampihongAdmin)
admin.site.register(HargaGedungBangunanDinkesLampihong, HargaGedungBangunanDinkesLampihongAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDinkesLampihongInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDinkesLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=5)
        return super(HargaPeralatanMesinDinkesLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDinkesLampihongAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDinkesLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=29
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=29
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDinkesLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDinkesLampihongAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DinkesLampihong
admin.site.register(PeralatanMesinDinkesLampihong, PeralatanMesinDinkesLampihongAdmin)
admin.site.register(HargaPeralatanMesinDinkesLampihong, HargaPeralatanMesinDinkesLampihongAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDinkesLampihong, HargaJalanIrigasiJaringanDinkesLampihong

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDinkesLampihongInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDinkesLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=5)
        return super(HargaJalanIrigasiJaringanDinkesLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDinkesLampihongAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDinkesLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=29
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDinkesLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDinkesLampihongAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DinkesLampihong
admin.site.register(JalanIrigasiJaringanDinkesLampihong, JalanIrigasiJaringanDinkesLampihongAdmin)
admin.site.register(HargaJalanIrigasiJaringanDinkesLampihong, HargaJalanIrigasiJaringanDinkesLampihongAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDinkesLampihong, HargaATLDinkesLampihong

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDinkesLampihongInline(HargaATLInline):
    model = HargaATLDinkesLampihong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=5)
        return super(HargaATLDinkesLampihongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDinkesLampihongAdmin(ATLAdmin):
    inlines = [HargaATLDinkesLampihongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=29
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=29
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDinkesLampihongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDinkesLampihongAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=29
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DinkesLampihong
admin.site.register(ATLDinkesLampihong, ATLDinkesLampihongAdmin)
admin.site.register(HargaATLDinkesLampihong, HargaATLDinkesLampihongAdmin)
