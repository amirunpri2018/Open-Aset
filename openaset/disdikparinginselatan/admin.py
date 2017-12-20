### $Id: admin.py,v 1.13 2017/12/04 08:16:37 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah

#### Tanah
from umum.models import TanahDisdikParinginSelatan, HargaTanahDisdikParinginSelatan
from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan

from gedungbangunan.models import GedungBangunanDisdikParinginSelatan, HargaGedungBangunanDisdikParinginSelatan, GedungBangunanRuanganDisdikParinginSelatan

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin



#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan

from peralatanmesin.models import PeralatanMesinDisdikParinginSelatan, HargaPeralatanMesinDisdikParinginSelatan

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin




#### Class Tanah
class GedungBangunanDisdikParinginSelatanInline(GedungBangunanInline):
    model = GedungBangunanDisdikParinginSelatan



class HargaTanahDisdikParinginSelatanInline(HargaTanahInline):
    model = HargaTanahDisdikParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=7)
        return super(HargaTanahDisdikParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TanahDisdikParinginSelatanAdmin(TanahAdmin):
    inlines = [HargaTanahDisdikParinginSelatanInline]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(TanahDisdikParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaTanahDisdikParinginSelatanAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



### Register Tanah DisdikParinginSelatan
admin.site.register(TanahDisdikParinginSelatan, TanahDisdikParinginSelatanAdmin)
admin.site.register(HargaTanahDisdikParinginSelatan, HargaTanahDisdikParinginSelatanAdmin)





#### Class Gedung dan Bangunan
class HargaGedungBangunanDisdikParinginSelatanInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDisdikParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=7)
        return super(HargaGedungBangunanDisdikParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class GedungBangunanDisdikParinginSelatanAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDisdikParinginSelatanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(GedungBangunanDisdikParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDisdikParinginSelatanAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class HargaGedungBangunanDisdikParinginSelatanAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



###Register GedungBangunan DisdikParinginSelatan
admin.site.register(GedungBangunanDisdikParinginSelatan, GedungBangunanDisdikParinginSelatanAdmin)
admin.site.register(GedungBangunanRuanganDisdikParinginSelatan, GedungBangunanRuanganDisdikParinginSelatanAdmin)
admin.site.register(HargaGedungBangunanDisdikParinginSelatan, HargaGedungBangunanDisdikParinginSelatanAdmin)




#### Class Peralatan Mesin
class HargaPeralatanMesinDisdikParinginSelatanInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDisdikParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=7)
        return super(HargaPeralatanMesinDisdikParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PeralatanMesinDisdikParinginSelatanAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDisdikParinginSelatanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(PeralatanMesinDisdikParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaPeralatanMesinDisdikParinginSelatanAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



###Register PeralatanMesin DisdikParinginSelatan
admin.site.register(PeralatanMesinDisdikParinginSelatan, PeralatanMesinDisdikParinginSelatanAdmin)
admin.site.register(HargaPeralatanMesinDisdikParinginSelatan, HargaPeralatanMesinDisdikParinginSelatanAdmin)






#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan

from jalanirigasijaringan.models import JalanIrigasiJaringanDisdikParinginSelatan,  HargaJalanIrigasiJaringanDisdikParinginSelatan

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin




#### Class Jalan, Irigasi dan Jaringan


class HargaJalanIrigasiJaringanDisdikParinginSelatanInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDisdikParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=7)
        return super(HargaJalanIrigasiJaringanDisdikParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class JalanIrigasiJaringanDisdikParinginSelatanAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDisdikParinginSelatanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        return super(JalanIrigasiJaringanDisdikParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class HargaJalanIrigasiJaringanDisdikParinginSelatanAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



###Register JalanIrigasiJaringan DisdikParinginSelatan
admin.site.register(JalanIrigasiJaringanDisdikParinginSelatan, JalanIrigasiJaringanDisdikParinginSelatanAdmin)
admin.site.register(HargaJalanIrigasiJaringanDisdikParinginSelatan, HargaJalanIrigasiJaringanDisdikParinginSelatanAdmin)




#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan

from atl.models import ATLDisdikParinginSelatan, HargaATLDisdikParinginSelatan

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin




#### Class Aset Tetap Lainnya
class HargaATLDisdikParinginSelatanInline(HargaATLInline):
    model = HargaATLDisdikParinginSelatan

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=7)
        return super(HargaATLDisdikParinginSelatanInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ATLDisdikParinginSelatanAdmin(ATLAdmin):
    inlines = [HargaATLDisdikParinginSelatanInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = SUBSKPD.objects.filter(id__in=qs_id_sub_skpd)
        if db_field.name == "id_ruangan":
            qs_id_sub_skpd=range(371,396)
            qs_id_sub_skpd.append(88)
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__in=qs_id_sub_skpd)
        return super(ATLDisdikParinginSelatanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        return self.model.objects.filter(id_sub_skpd__in=qs_id_sub_skpd).filter(id_mutasi_berkurang__exact=5)



class HargaATLDisdikParinginSelatanAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        qs_id_sub_skpd=range(371,396)
        qs_id_sub_skpd.append(88)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=qs_id_sub_skpd)
        return self.model.objects.filter(id_atl__in=atl_qs)



###Register ATL DisdikParinginSelatan
admin.site.register(ATLDisdikParinginSelatan, ATLDisdikParinginSelatanAdmin)
admin.site.register(HargaATLDisdikParinginSelatan, HargaATLDisdikParinginSelatanAdmin)
