### $Id: admin.py,v 1.15 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikSMPN2Batumandi, HargaTanahDisdikSMPN2Batumandi
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikSMPN2Batumandi, HargaGedungBangunanDisdikSMPN2Batumandi, GedungBangunanRuanganDisdikSMPN2Batumandi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikSMPN2Batumandi, HargaPeralatanMesinDisdikSMPN2Batumandi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikSMPN2BatumandiInline(GedungBangunanInline):
    model = GedungBangunanDisdikSMPN2Batumandi



class HargaTanahDisdikSMPN2BatumandiInline(HargaTanahInline):
    model = HargaTanahDisdikSMPN2Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikSMPN2BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikSMPN2BatumandiAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikSMPN2BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=104
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDisdikSMPN2BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikSMPN2BatumandiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikSMPN2Batumandi
admin.site.register(TanahDisdikSMPN2Batumandi, TanahDisdikSMPN2BatumandiAdmin)
admin.site.register(HargaTanahDisdikSMPN2Batumandi, HargaTanahDisdikSMPN2BatumandiAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikSMPN2BatumandiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikSMPN2Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikSMPN2BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikSMPN2BatumandiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikSMPN2BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=104
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDisdikSMPN2BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikSMPN2BatumandiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 104
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikSMPN2BatumandiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikSMPN2Batumandi
admin.site.register(GedungBangunanDisdikSMPN2Batumandi, GedungBangunanDisdikSMPN2BatumandiAdmin)
admin.site.register(GedungBangunanRuanganDisdikSMPN2Batumandi, GedungBangunanRuanganDisdikSMPN2BatumandiAdmin)
admin.site.register(HargaGedungBangunanDisdikSMPN2Batumandi, HargaGedungBangunanDisdikSMPN2BatumandiAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikSMPN2BatumandiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikSMPN2Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikSMPN2BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikSMPN2BatumandiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikSMPN2BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=104
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=104
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikSMPN2BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikSMPN2BatumandiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikSMPN2Batumandi
admin.site.register(PeralatanMesinDisdikSMPN2Batumandi, PeralatanMesinDisdikSMPN2BatumandiAdmin)
admin.site.register(HargaPeralatanMesinDisdikSMPN2Batumandi, HargaPeralatanMesinDisdikSMPN2BatumandiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikSMPN2Batumandi, HargaJalanIrigasiJaringanDisdikSMPN2Batumandi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikSMPN2BatumandiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikSMPN2Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikSMPN2BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikSMPN2BatumandiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikSMPN2BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=104
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikSMPN2BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikSMPN2BatumandiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikSMPN2Batumandi
admin.site.register(JalanIrigasiJaringanDisdikSMPN2Batumandi, JalanIrigasiJaringanDisdikSMPN2BatumandiAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikSMPN2Batumandi, HargaJalanIrigasiJaringanDisdikSMPN2BatumandiAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikSMPN2Batumandi, HargaATLDisdikSMPN2Batumandi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikSMPN2BatumandiInline(HargaATLInline):
    model = HargaATLDisdikSMPN2Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikSMPN2BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikSMPN2BatumandiAdmin(ATLAdmin):
    inlines = [HargaATLDisdikSMPN2BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=104
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=104
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDisdikSMPN2BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikSMPN2BatumandiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=104
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikSMPN2Batumandi
admin.site.register(ATLDisdikSMPN2Batumandi, ATLDisdikSMPN2BatumandiAdmin)
admin.site.register(HargaATLDisdikSMPN2Batumandi, HargaATLDisdikSMPN2BatumandiAdmin)
