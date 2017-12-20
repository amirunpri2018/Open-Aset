### $Id: admin.py,v 1.13 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikAwayan, HargaTanahDisdikAwayan
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikAwayan, HargaGedungBangunanDisdikAwayan, GedungBangunanRuanganDisdikAwayan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikAwayan, HargaPeralatanMesinDisdikAwayan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikAwayanInline(GedungBangunanInline):
    model = GedungBangunanDisdikAwayan



class HargaTanahDisdikAwayanInline(HargaTanahInline):
    model = HargaTanahDisdikAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikAwayanAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikAwayanInline]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(TanahDisdikAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikAwayanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikAwayan
admin.site.register(TanahDisdikAwayan, TanahDisdikAwayanAdmin)
admin.site.register(HargaTanahDisdikAwayan, HargaTanahDisdikAwayanAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikAwayanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikAwayanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(GedungBangunanDisdikAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikAwayanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikAwayanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikAwayan
admin.site.register(GedungBangunanDisdikAwayan, GedungBangunanDisdikAwayanAdmin)
admin.site.register(GedungBangunanRuanganDisdikAwayan, GedungBangunanRuanganDisdikAwayanAdmin)
admin.site.register(HargaGedungBangunanDisdikAwayan, HargaGedungBangunanDisdikAwayanAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikAwayanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikAwayanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikAwayanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikAwayan
admin.site.register(PeralatanMesinDisdikAwayan, PeralatanMesinDisdikAwayanAdmin)
admin.site.register(HargaPeralatanMesinDisdikAwayan, HargaPeralatanMesinDisdikAwayanAdmin)






#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikAwayan,  HargaJalanIrigasiJaringanDisdikAwayan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikAwayanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikAwayanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikAwayanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikAwayan
admin.site.register(JalanIrigasiJaringanDisdikAwayan, JalanIrigasiJaringanDisdikAwayanAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikAwayan, HargaJalanIrigasiJaringanDisdikAwayanAdmin)




#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikAwayan, HargaATLDisdikAwayan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikAwayanInline(HargaATLInline):
    model = HargaATLDisdikAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikAwayanAdmin(ATLAdmin):
    inlines = [HargaATLDisdikAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(193,227)
            qs_id_sub_skpd.append(84)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(ATLDisdikAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikAwayanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(193,227)
        qs_id_sub_skpd.append(84)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikAwayan
admin.site.register(ATLDisdikAwayan, ATLDisdikAwayanAdmin)
admin.site.register(HargaATLDisdikAwayan, HargaATLDisdikAwayanAdmin)
