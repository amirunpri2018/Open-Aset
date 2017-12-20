### $Id: admin.py,v 1.17 2017/12/18 03:15:44 muntaza Exp $



from django.contrib import admin

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah

from gedungbangunan.models import Ruangan

from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus, PeralatanMesinReklas

from peralatanmesin.models import SKPDAsalPeralatanMesin, SKPDTujuanPeralatanMesin, FotoPeralatanMesin

from umum.forms import HargaTanahForm


### class Peralatan Mesin
class SKPDAsalPeralatanMesinInline(admin.TabularInline):
    model = SKPDAsalPeralatanMesin
    extra = 0

class SKPDTujuanPeralatanMesinInline(admin.TabularInline):
    model = SKPDTujuanPeralatanMesin
    extra = 0


class HargaPeralatanMesinInline(admin.TabularInline):
    model = HargaPeralatanMesin
    form = HargaTanahForm
    extra = 0
    fields = ['id_peralatan_mesin', 'id_asal_usul',
                    'tahun', 'id_kontrak_peralatan_mesin', 'harga_bertambah',
                    'harga_berkurang',
                    'catatan', 'tahun_mutasi']
    raw_id_fields = ['id_kontrak_peralatan_mesin']



class FotoPeralatanMesinInline(admin.TabularInline):
    model = FotoPeralatanMesin
    extra = 0
    fields = ['id_peralatan_mesin', 'foto', 'tanggal',
                    'catatan', ]



class PeralatanMesinAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'merk_type', 'ukuran_cc', 'bahan', 'tahun',
                    'nomor_pabrik', 'nomor_rangka', 'nomor_mesin',
                    'nomor_polisi', 'nomor_bpkb',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'id_ruangan', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang',]
    list_per_page = 10
    radio_fields = {"id_golongan_barang" : admin.HORIZONTAL}
    raw_id_fields = ['id_kode_barang', ]
    inlines = [HargaPeralatanMesinInline, SKPDAsalPeralatanMesinInline,
                    FotoPeralatanMesinInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=1)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=2)
        return super(PeralatanMesinAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PenghapusanPeralatanMesinInline(admin.TabularInline):
    model = PenghapusanPeralatanMesin
    extra = 0

class PemanfaatanPeralatanMesinInline(admin.TabularInline):
    model = PemanfaatanPeralatanMesin
    extra = 0

class TahunBerkurangPeralatanMesinInline(admin.TabularInline):
    model = TahunBerkurangPeralatanMesin
    extra = 0


class TahunBerkurangUsulHapusPeralatanMesinInline(admin.TabularInline):
    model = TahunBerkurangUsulHapusPeralatanMesin
    extra = 0


class KontrakPeralatanMesinAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga')
    search_fields = ['nomor_sp2d']
    date_hierarchy = 'tanggal_sp2d'
    list_per_page = 10
    list_filter = ['id_skpd']



class KontrakPeralatanMesinUmumAdmin(KontrakPeralatanMesinAdmin):
    readonly_fields = ['nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga']


class PeralatanMesinPenghapusanAdmin(PeralatanMesinAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'merk_type', 'ukuran_cc', 'bahan', 'tahun',
                    'nomor_pabrik', 'nomor_rangka', 'nomor_mesin',
                    'nomor_polisi', 'nomor_bpkb',
                    'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', 'keterangan']
    save_as = False
    inlines = [PenghapusanPeralatanMesinInline,
                    TahunBerkurangPeralatanMesinInline,
                    SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline,
                    FotoPeralatanMesinInline, ]

class PeralatanMesinUsulHapusAdmin(PeralatanMesinAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'merk_type', 'ukuran_cc', 'bahan', 'tahun',
                    'nomor_pabrik', 'nomor_rangka', 'nomor_mesin',
                    'nomor_polisi', 'nomor_bpkb',
                    'banyak_barang',
                    'id_satuan_barang', 'id_ruangan']
    save_as = False
    inlines = [TahunBerkurangUsulHapusPeralatanMesinInline,
                    SKPDAsalPeralatanMesinInline,
                    FotoPeralatanMesinInline, ]



class PeralatanMesinReklasAdmin(PeralatanMesinAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'merk_type', 'ukuran_cc', 'bahan', 'tahun',
                    'nomor_pabrik', 'nomor_rangka', 'nomor_mesin',
                    'nomor_polisi', 'nomor_bpkb',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'id_ruangan', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang',]
    list_per_page = 10
    raw_id_fields = ['id_kode_barang', 'id_sub_skpd', ]
    inlines = [HargaPeralatanMesinInline, PenghapusanPeralatanMesinInline,
                    TahunBerkurangPeralatanMesinInline,
                    SKPDAsalPeralatanMesinInline,
                    FotoPeralatanMesinInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=1)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=2)
        return super(PeralatanMesinReklasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_mutasi_berkurang__exact=9)


class PeralatanMesinPemanfaatanAdmin(PeralatanMesinAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'merk_type', 'ukuran_cc', 'bahan', 'tahun',
                    'nomor_pabrik', 'nomor_rangka', 'nomor_mesin',
                    'nomor_polisi', 'nomor_bpkb',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', 'keterangan']
    save_as = False
    inlines = [PemanfaatanPeralatanMesinInline]


class HargaPeralatanMesinAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_peralatan_mesin', 'id_asal_usul',
                    'tahun', 'id_kontrak_peralatan_mesin',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    list_display = ('id_peralatan_mesin', 'id_asal_usul',
                    'tahun', 'id_kontrak_peralatan_mesin',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan')
    readonly_fields = ['id_peralatan_mesin', 'id_asal_usul',
                    'tahun', 'id_kontrak_peralatan_mesin',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    #search_fields = ['id_ruangan']
    list_filter = ['tahun', 'id_asal_usul']
    list_per_page = 10
    raw_id_fields = ['id_kontrak_peralatan_mesin']




###Register UMUM Peralatan Mesin


###Register Peralatan Mesin
admin.site.register(PeralatanMesin, PeralatanMesinAdmin)
admin.site.register(KontrakPeralatanMesin, KontrakPeralatanMesinUmumAdmin)
admin.site.register(PeralatanMesinPenghapusan, PeralatanMesinPenghapusanAdmin)
admin.site.register(PeralatanMesinUsulHapus, PeralatanMesinUsulHapusAdmin)
admin.site.register(PeralatanMesinPemanfaatan, PeralatanMesinPemanfaatanAdmin)
admin.site.register(HargaPeralatanMesin, HargaPeralatanMesinAdmin)
admin.site.register(PeralatanMesinReklas, PeralatanMesinReklasAdmin)
