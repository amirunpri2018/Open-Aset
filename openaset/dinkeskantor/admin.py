### $Id: admin.py,v 1.9 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDinkesKantor, HargaTanahDinkesKantor
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDinkesKantor, HargaGedungBangunanDinkesKantor, GedungBangunanRuanganDinkesKantor

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDinkesKantor, HargaPeralatanMesinDinkesKantor

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDinkesKantorInline(GedungBangunanInline):
    model = GedungBangunanDinkesKantor



class HargaTanahDinkesKantorInline(HargaTanahInline):
    model = HargaTanahDinkesKantor

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=5)
        return super(HargaTanahDinkesKantorInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDinkesKantorAdmin(TanahAdmin):
    inlines = [HargaTanahDinkesKantorInline]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(TanahDinkesKantorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDinkesKantorAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DinkesKantor
admin.site.register(TanahDinkesKantor, TanahDinkesKantorAdmin)
admin.site.register(HargaTanahDinkesKantor, HargaTanahDinkesKantorAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDinkesKantorInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDinkesKantor

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=5)
        return super(HargaGedungBangunanDinkesKantorInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDinkesKantorAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDinkesKantorInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(GedungBangunanDinkesKantorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDinkesKantorAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDinkesKantorAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DinkesKantor
admin.site.register(GedungBangunanDinkesKantor, GedungBangunanDinkesKantorAdmin)
admin.site.register(GedungBangunanRuanganDinkesKantor, GedungBangunanRuanganDinkesKantorAdmin)
admin.site.register(HargaGedungBangunanDinkesKantor, HargaGedungBangunanDinkesKantorAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDinkesKantorInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDinkesKantor

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=5)
        return super(HargaPeralatanMesinDinkesKantorInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDinkesKantorAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDinkesKantorInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(PeralatanMesinDinkesKantorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDinkesKantorAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DinkesKantor
admin.site.register(PeralatanMesinDinkesKantor, PeralatanMesinDinkesKantorAdmin)
admin.site.register(HargaPeralatanMesinDinkesKantor, HargaPeralatanMesinDinkesKantorAdmin)






#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDinkesKantor,  HargaJalanIrigasiJaringanDinkesKantor

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDinkesKantorInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDinkesKantor

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=5)
        return super(HargaJalanIrigasiJaringanDinkesKantorInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDinkesKantorAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDinkesKantorInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDinkesKantorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDinkesKantorAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DinkesKantor
admin.site.register(JalanIrigasiJaringanDinkesKantor, JalanIrigasiJaringanDinkesKantorAdmin)
admin.site.register(HargaJalanIrigasiJaringanDinkesKantor, HargaJalanIrigasiJaringanDinkesKantorAdmin)




#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDinkesKantor, HargaATLDinkesKantor

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDinkesKantorInline(HargaATLInline):
    model = HargaATLDinkesKantor

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=5)
        return super(HargaATLDinkesKantorInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDinkesKantorAdmin(ATLAdmin):
    inlines = [HargaATLDinkesKantorInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(22,28)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(ATLDinkesKantorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDinkesKantorAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(22,28)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DinkesKantor
admin.site.register(ATLDinkesKantor, ATLDinkesKantorAdmin)
admin.site.register(HargaATLDinkesKantor, HargaATLDinkesKantorAdmin)
