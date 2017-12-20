### $Id: admin.py,v 1.14 2017/12/04 08:16:32 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDinkesAwayan, HargaTanahDinkesAwayan
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDinkesAwayan, HargaGedungBangunanDinkesAwayan, GedungBangunanRuanganDinkesAwayan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDinkesAwayan, HargaPeralatanMesinDinkesAwayan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDinkesAwayanInline(GedungBangunanInline):
    model = GedungBangunanDinkesAwayan



class HargaTanahDinkesAwayanInline(HargaTanahInline):
    model = HargaTanahDinkesAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=5)
        return super(HargaTanahDinkesAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDinkesAwayanAdmin(TanahAdmin):
    inlines = [HargaTanahDinkesAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=31
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDinkesAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDinkesAwayanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DinkesAwayan
admin.site.register(TanahDinkesAwayan, TanahDinkesAwayanAdmin)
admin.site.register(HargaTanahDinkesAwayan, HargaTanahDinkesAwayanAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDinkesAwayanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDinkesAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=5)
        return super(HargaGedungBangunanDinkesAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDinkesAwayanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDinkesAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=31
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDinkesAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDinkesAwayanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 31
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDinkesAwayanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DinkesAwayan
admin.site.register(GedungBangunanDinkesAwayan, GedungBangunanDinkesAwayanAdmin)
admin.site.register(GedungBangunanRuanganDinkesAwayan, GedungBangunanRuanganDinkesAwayanAdmin)
admin.site.register(HargaGedungBangunanDinkesAwayan, HargaGedungBangunanDinkesAwayanAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDinkesAwayanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDinkesAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=5)
        return super(HargaPeralatanMesinDinkesAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDinkesAwayanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDinkesAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=31
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=31
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDinkesAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDinkesAwayanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DinkesAwayan
admin.site.register(PeralatanMesinDinkesAwayan, PeralatanMesinDinkesAwayanAdmin)
admin.site.register(HargaPeralatanMesinDinkesAwayan, HargaPeralatanMesinDinkesAwayanAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDinkesAwayan, HargaJalanIrigasiJaringanDinkesAwayan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDinkesAwayanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDinkesAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=5)
        return super(HargaJalanIrigasiJaringanDinkesAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDinkesAwayanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDinkesAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=31
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDinkesAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDinkesAwayanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DinkesAwayan
admin.site.register(JalanIrigasiJaringanDinkesAwayan, JalanIrigasiJaringanDinkesAwayanAdmin)
admin.site.register(HargaJalanIrigasiJaringanDinkesAwayan, HargaJalanIrigasiJaringanDinkesAwayanAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDinkesAwayan, HargaATLDinkesAwayan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDinkesAwayanInline(HargaATLInline):
    model = HargaATLDinkesAwayan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=5)
        return super(HargaATLDinkesAwayanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDinkesAwayanAdmin(ATLAdmin):
    inlines = [HargaATLDinkesAwayanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=31
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=31
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDinkesAwayanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDinkesAwayanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=31
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DinkesAwayan
admin.site.register(ATLDinkesAwayan, ATLDinkesAwayanAdmin)
admin.site.register(HargaATLDinkesAwayan, HargaATLDinkesAwayanAdmin)
