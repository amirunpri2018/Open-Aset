### $Id: admin.py,v 1.13 2017/12/04 08:16:38 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikTebingTinggi, HargaTanahDisdikTebingTinggi
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikTebingTinggi, HargaGedungBangunanDisdikTebingTinggi, GedungBangunanRuanganDisdikTebingTinggi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikTebingTinggi, HargaPeralatanMesinDisdikTebingTinggi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikTebingTinggiInline(GedungBangunanInline):
    model = GedungBangunanDisdikTebingTinggi



class HargaTanahDisdikTebingTinggiInline(HargaTanahInline):
    model = HargaTanahDisdikTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikTebingTinggiAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikTebingTinggiInline]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(TanahDisdikTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikTebingTinggiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikTebingTinggi
admin.site.register(TanahDisdikTebingTinggi, TanahDisdikTebingTinggiAdmin)
admin.site.register(HargaTanahDisdikTebingTinggi, HargaTanahDisdikTebingTinggiAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikTebingTinggiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikTebingTinggiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikTebingTinggiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(GedungBangunanDisdikTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikTebingTinggiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikTebingTinggiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikTebingTinggi
admin.site.register(GedungBangunanDisdikTebingTinggi, GedungBangunanDisdikTebingTinggiAdmin)
admin.site.register(GedungBangunanRuanganDisdikTebingTinggi, GedungBangunanRuanganDisdikTebingTinggiAdmin)
admin.site.register(HargaGedungBangunanDisdikTebingTinggi, HargaGedungBangunanDisdikTebingTinggiAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikTebingTinggiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikTebingTinggiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikTebingTinggiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikTebingTinggiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikTebingTinggi
admin.site.register(PeralatanMesinDisdikTebingTinggi, PeralatanMesinDisdikTebingTinggiAdmin)
admin.site.register(HargaPeralatanMesinDisdikTebingTinggi, HargaPeralatanMesinDisdikTebingTinggiAdmin)






#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikTebingTinggi,  HargaJalanIrigasiJaringanDisdikTebingTinggi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikTebingTinggiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikTebingTinggiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikTebingTinggiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikTebingTinggiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikTebingTinggi
admin.site.register(JalanIrigasiJaringanDisdikTebingTinggi, JalanIrigasiJaringanDisdikTebingTinggiAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikTebingTinggi, HargaJalanIrigasiJaringanDisdikTebingTinggiAdmin)




#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikTebingTinggi, HargaATLDisdikTebingTinggi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikTebingTinggiInline(HargaATLInline):
    model = HargaATLDisdikTebingTinggi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikTebingTinggiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikTebingTinggiAdmin(ATLAdmin):
    inlines = [HargaATLDisdikTebingTinggiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(355,371)
            qs_id_sub_skpd.append(87)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(ATLDisdikTebingTinggiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikTebingTinggiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(355,371)
        qs_id_sub_skpd.append(87)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikTebingTinggi
admin.site.register(ATLDisdikTebingTinggi, ATLDisdikTebingTinggiAdmin)
admin.site.register(HargaATLDisdikTebingTinggi, HargaATLDisdikTebingTinggiAdmin)
