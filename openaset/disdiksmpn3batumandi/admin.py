### $Id: admin.py,v 1.15 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikSMPN3Batumandi, HargaTanahDisdikSMPN3Batumandi
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikSMPN3Batumandi, HargaGedungBangunanDisdikSMPN3Batumandi, GedungBangunanRuanganDisdikSMPN3Batumandi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikSMPN3Batumandi, HargaPeralatanMesinDisdikSMPN3Batumandi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikSMPN3BatumandiInline(GedungBangunanInline):
    model = GedungBangunanDisdikSMPN3Batumandi



class HargaTanahDisdikSMPN3BatumandiInline(HargaTanahInline):
    model = HargaTanahDisdikSMPN3Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikSMPN3BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikSMPN3BatumandiAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikSMPN3BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=110
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDisdikSMPN3BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikSMPN3BatumandiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikSMPN3Batumandi
admin.site.register(TanahDisdikSMPN3Batumandi, TanahDisdikSMPN3BatumandiAdmin)
admin.site.register(HargaTanahDisdikSMPN3Batumandi, HargaTanahDisdikSMPN3BatumandiAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikSMPN3BatumandiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikSMPN3Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikSMPN3BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikSMPN3BatumandiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikSMPN3BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=110
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDisdikSMPN3BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikSMPN3BatumandiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 110
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikSMPN3BatumandiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikSMPN3Batumandi
admin.site.register(GedungBangunanDisdikSMPN3Batumandi, GedungBangunanDisdikSMPN3BatumandiAdmin)
admin.site.register(GedungBangunanRuanganDisdikSMPN3Batumandi, GedungBangunanRuanganDisdikSMPN3BatumandiAdmin)
admin.site.register(HargaGedungBangunanDisdikSMPN3Batumandi, HargaGedungBangunanDisdikSMPN3BatumandiAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikSMPN3BatumandiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikSMPN3Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikSMPN3BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikSMPN3BatumandiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikSMPN3BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=110
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=110
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikSMPN3BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikSMPN3BatumandiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikSMPN3Batumandi
admin.site.register(PeralatanMesinDisdikSMPN3Batumandi, PeralatanMesinDisdikSMPN3BatumandiAdmin)
admin.site.register(HargaPeralatanMesinDisdikSMPN3Batumandi, HargaPeralatanMesinDisdikSMPN3BatumandiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikSMPN3Batumandi, HargaJalanIrigasiJaringanDisdikSMPN3Batumandi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikSMPN3BatumandiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikSMPN3Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikSMPN3BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikSMPN3BatumandiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikSMPN3BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=110
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikSMPN3BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikSMPN3BatumandiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikSMPN3Batumandi
admin.site.register(JalanIrigasiJaringanDisdikSMPN3Batumandi, JalanIrigasiJaringanDisdikSMPN3BatumandiAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikSMPN3Batumandi, HargaJalanIrigasiJaringanDisdikSMPN3BatumandiAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikSMPN3Batumandi, HargaATLDisdikSMPN3Batumandi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikSMPN3BatumandiInline(HargaATLInline):
    model = HargaATLDisdikSMPN3Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikSMPN3BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikSMPN3BatumandiAdmin(ATLAdmin):
    inlines = [HargaATLDisdikSMPN3BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=110
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=110
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDisdikSMPN3BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikSMPN3BatumandiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=110
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikSMPN3Batumandi
admin.site.register(ATLDisdikSMPN3Batumandi, ATLDisdikSMPN3BatumandiAdmin)
admin.site.register(HargaATLDisdikSMPN3Batumandi, HargaATLDisdikSMPN3BatumandiAdmin)
