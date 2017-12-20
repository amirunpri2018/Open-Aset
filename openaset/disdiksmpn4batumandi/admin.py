### $Id: admin.py,v 1.15 2017/12/04 08:16:38 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikSMPN4Batumandi, HargaTanahDisdikSMPN4Batumandi
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikSMPN4Batumandi, HargaGedungBangunanDisdikSMPN4Batumandi, GedungBangunanRuanganDisdikSMPN4Batumandi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikSMPN4Batumandi, HargaPeralatanMesinDisdikSMPN4Batumandi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikSMPN4BatumandiInline(GedungBangunanInline):
    model = GedungBangunanDisdikSMPN4Batumandi



class HargaTanahDisdikSMPN4BatumandiInline(HargaTanahInline):
    model = HargaTanahDisdikSMPN4Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikSMPN4BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikSMPN4BatumandiAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikSMPN4BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=397
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDisdikSMPN4BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikSMPN4BatumandiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikSMPN4Batumandi
admin.site.register(TanahDisdikSMPN4Batumandi, TanahDisdikSMPN4BatumandiAdmin)
admin.site.register(HargaTanahDisdikSMPN4Batumandi, HargaTanahDisdikSMPN4BatumandiAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikSMPN4BatumandiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikSMPN4Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikSMPN4BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikSMPN4BatumandiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikSMPN4BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=397
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDisdikSMPN4BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikSMPN4BatumandiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 397
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikSMPN4BatumandiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikSMPN4Batumandi
admin.site.register(GedungBangunanDisdikSMPN4Batumandi, GedungBangunanDisdikSMPN4BatumandiAdmin)
admin.site.register(GedungBangunanRuanganDisdikSMPN4Batumandi, GedungBangunanRuanganDisdikSMPN4BatumandiAdmin)
admin.site.register(HargaGedungBangunanDisdikSMPN4Batumandi, HargaGedungBangunanDisdikSMPN4BatumandiAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikSMPN4BatumandiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikSMPN4Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikSMPN4BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikSMPN4BatumandiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikSMPN4BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=397
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=397
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikSMPN4BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikSMPN4BatumandiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikSMPN4Batumandi
admin.site.register(PeralatanMesinDisdikSMPN4Batumandi, PeralatanMesinDisdikSMPN4BatumandiAdmin)
admin.site.register(HargaPeralatanMesinDisdikSMPN4Batumandi, HargaPeralatanMesinDisdikSMPN4BatumandiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikSMPN4Batumandi, HargaJalanIrigasiJaringanDisdikSMPN4Batumandi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikSMPN4BatumandiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikSMPN4Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikSMPN4BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikSMPN4BatumandiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikSMPN4BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=397
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikSMPN4BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikSMPN4BatumandiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikSMPN4Batumandi
admin.site.register(JalanIrigasiJaringanDisdikSMPN4Batumandi, JalanIrigasiJaringanDisdikSMPN4BatumandiAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikSMPN4Batumandi, HargaJalanIrigasiJaringanDisdikSMPN4BatumandiAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikSMPN4Batumandi, HargaATLDisdikSMPN4Batumandi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikSMPN4BatumandiInline(HargaATLInline):
    model = HargaATLDisdikSMPN4Batumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikSMPN4BatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikSMPN4BatumandiAdmin(ATLAdmin):
    inlines = [HargaATLDisdikSMPN4BatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=397
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=397
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDisdikSMPN4BatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikSMPN4BatumandiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=397
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikSMPN4Batumandi
admin.site.register(ATLDisdikSMPN4Batumandi, ATLDisdikSMPN4BatumandiAdmin)
admin.site.register(HargaATLDisdikSMPN4Batumandi, HargaATLDisdikSMPN4BatumandiAdmin)
