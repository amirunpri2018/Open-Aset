### $Id: admin.py,v 1.13 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDinkesBatumandi, HargaTanahDinkesBatumandi
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDinkesBatumandi, HargaGedungBangunanDinkesBatumandi, GedungBangunanRuanganDinkesBatumandi

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDinkesBatumandi, HargaPeralatanMesinDinkesBatumandi

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDinkesBatumandiInline(GedungBangunanInline):
    model = GedungBangunanDinkesBatumandi



class HargaTanahDinkesBatumandiInline(HargaTanahInline):
    model = HargaTanahDinkesBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=5)
        return super(HargaTanahDinkesBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDinkesBatumandiAdmin(TanahAdmin):
    inlines = [HargaTanahDinkesBatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=30
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(TanahDinkesBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDinkesBatumandiAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        tanah_qs = Tanah.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DinkesBatumandi
admin.site.register(TanahDinkesBatumandi, TanahDinkesBatumandiAdmin)
admin.site.register(HargaTanahDinkesBatumandi, HargaTanahDinkesBatumandiAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDinkesBatumandiInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDinkesBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=5)
        return super(HargaGedungBangunanDinkesBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDinkesBatumandiAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDinkesBatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=30
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(GedungBangunanDinkesBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDinkesBatumandiAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = 30
        return self.model.objects.filter(id_sub_skpd__exact=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDinkesBatumandiAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DinkesBatumandi
admin.site.register(GedungBangunanDinkesBatumandi, GedungBangunanDinkesBatumandiAdmin)
admin.site.register(GedungBangunanRuanganDinkesBatumandi, GedungBangunanRuanganDinkesBatumandiAdmin)
admin.site.register(HargaGedungBangunanDinkesBatumandi, HargaGedungBangunanDinkesBatumandiAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDinkesBatumandiInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDinkesBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=5)
        return super(HargaPeralatanMesinDinkesBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDinkesBatumandiAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDinkesBatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=30
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=30
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(PeralatanMesinDinkesBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDinkesBatumandiAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DinkesBatumandi
admin.site.register(PeralatanMesinDinkesBatumandi, PeralatanMesinDinkesBatumandiAdmin)
admin.site.register(HargaPeralatanMesinDinkesBatumandi, HargaPeralatanMesinDinkesBatumandiAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDinkesBatumandi, HargaJalanIrigasiJaringanDinkesBatumandi

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDinkesBatumandiInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDinkesBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=5)
        return super(HargaJalanIrigasiJaringanDinkesBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDinkesBatumandiAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDinkesBatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=30
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDinkesBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDinkesBatumandiAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DinkesBatumandi
admin.site.register(JalanIrigasiJaringanDinkesBatumandi, JalanIrigasiJaringanDinkesBatumandiAdmin)
admin.site.register(HargaJalanIrigasiJaringanDinkesBatumandi, HargaJalanIrigasiJaringanDinkesBatumandiAdmin)



#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDinkesBatumandi, HargaATLDinkesBatumandi

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDinkesBatumandiInline(HargaATLInline):
    model = HargaATLDinkesBatumandi

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=5)
        return super(HargaATLDinkesBatumandiInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDinkesBatumandiAdmin(ATLAdmin):
    inlines = [HargaATLDinkesBatumandiInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=30
            kwargs["queryset"] = SUBSKPD.objects.filter(id__exact=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=30
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__exact=qs_id_sub_skpd)
        return super(ATLDinkesBatumandiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        return self.model.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDinkesBatumandiAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=30
        atl_qs = ATL.objects.filter(id_sub_skpd__exact=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DinkesBatumandi
admin.site.register(ATLDinkesBatumandi, ATLDinkesBatumandiAdmin)
admin.site.register(HargaATLDinkesBatumandi, HargaATLDinkesBatumandiAdmin)
