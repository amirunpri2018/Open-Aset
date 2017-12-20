### $Id: admin.py,v 1.13 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikHalong, HargaTanahDisdikHalong
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikHalong, HargaGedungBangunanDisdikHalong, GedungBangunanRuanganDisdikHalong

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikHalong, HargaPeralatanMesinDisdikHalong

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikHalongInline(GedungBangunanInline):
    model = GedungBangunanDisdikHalong



class HargaTanahDisdikHalongInline(HargaTanahInline):
    model = HargaTanahDisdikHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikHalongAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikHalongInline]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(TanahDisdikHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikHalongAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikHalong
admin.site.register(TanahDisdikHalong, TanahDisdikHalongAdmin)
admin.site.register(HargaTanahDisdikHalong, HargaTanahDisdikHalongAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikHalongInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikHalongAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikHalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(GedungBangunanDisdikHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikHalongAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikHalongAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikHalong
admin.site.register(GedungBangunanDisdikHalong, GedungBangunanDisdikHalongAdmin)
admin.site.register(GedungBangunanRuanganDisdikHalong, GedungBangunanRuanganDisdikHalongAdmin)
admin.site.register(HargaGedungBangunanDisdikHalong, HargaGedungBangunanDisdikHalongAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikHalongInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikHalongAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikHalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikHalongAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikHalong
admin.site.register(PeralatanMesinDisdikHalong, PeralatanMesinDisdikHalongAdmin)
admin.site.register(HargaPeralatanMesinDisdikHalong, HargaPeralatanMesinDisdikHalongAdmin)






#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikHalong,  HargaJalanIrigasiJaringanDisdikHalong

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikHalongInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikHalongAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikHalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikHalongAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikHalong
admin.site.register(JalanIrigasiJaringanDisdikHalong, JalanIrigasiJaringanDisdikHalongAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikHalong, HargaJalanIrigasiJaringanDisdikHalongAdmin)




#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikHalong, HargaATLDisdikHalong

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikHalongInline(HargaATLInline):
    model = HargaATLDisdikHalong

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikHalongInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikHalongAdmin(ATLAdmin):
    inlines = [HargaATLDisdikHalongInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(311,355)
            qs_id_sub_skpd.append(86)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(ATLDisdikHalongAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikHalongAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(311,355)
        qs_id_sub_skpd.append(86)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikHalong
admin.site.register(ATLDisdikHalong, ATLDisdikHalongAdmin)
admin.site.register(HargaATLDisdikHalong, HargaATLDisdikHalongAdmin)
