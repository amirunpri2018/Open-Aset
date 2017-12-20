### $Id: admin.py,v 1.14 2017/12/18 03:41:28 muntaza Exp $



from django.contrib import admin

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah

from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, KDPJalanIrigasiJaringan, KDPJalanIrigasiJaringanReklas, TahunBerkurangUsulHapusJalanIrigasiJaringan


#untuk menampung inline
from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringan, SKPDTujuanJalanIrigasiJaringan, FotoJalanIrigasiJaringan

from umum.forms import HargaTanahForm


### class Jalan Irigasi Jaringan
class SKPDAsalJalanIrigasiJaringanInline(admin.TabularInline):
    model = SKPDAsalJalanIrigasiJaringan
    extra = 0

class SKPDTujuanJalanIrigasiJaringanInline(admin.TabularInline):
    model = SKPDTujuanJalanIrigasiJaringan
    extra = 0

class HargaJalanIrigasiJaringanInline(admin.TabularInline):
    model = HargaJalanIrigasiJaringan
    form = HargaTanahForm
    extra = 0
    fields = ['id_jalan_irigasi_jaringan', 'id_asal_usul',
                    'tahun', 'id_kontrak_jalan_irigasi_jaringan',
                    'harga_bertambah',
                    'harga_berkurang',
                    'catatan', 'tahun_mutasi']
    raw_id_fields = ['id_kontrak_jalan_irigasi_jaringan']



class FotoJalanIrigasiJaringanInline(admin.TabularInline):
    model = FotoJalanIrigasiJaringan
    extra = 0
    fields = ['id_jalan_irigasi_jaringan', 'foto', 'tanggal',
                    'catatan', ]


class JalanIrigasiJaringanAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'konstruksi', 'panjang', 'lebar', 'luas',
                    'tahun',
                    'tanggal_dokumen', 'nomor_dokumen',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'id_tanah', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    #save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang']
    list_per_page = 10
    radio_fields = {"id_golongan_barang" : admin.HORIZONTAL}
    raw_id_fields = ['id_kode_barang', 'id_tanah']
    inlines = [HargaJalanIrigasiJaringanInline,
                SKPDAsalJalanIrigasiJaringanInline,
                FotoJalanIrigasiJaringanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__in=[2,3,4])
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=4)
        return super(JalanIrigasiJaringanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



class PenghapusanJalanIrigasiJaringanInline(admin.TabularInline):
    model = PenghapusanJalanIrigasiJaringan
    extra = 0


class PemanfaatanJalanIrigasiJaringanInline(admin.TabularInline):
    model = PemanfaatanJalanIrigasiJaringan
    extra = 0


class TahunBerkurangUsulHapusJalanIrigasiJaringanInline(admin.TabularInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringan
    extra = 0


class TahunBerkurangJalanIrigasiJaringanInline(admin.TabularInline):
    model = TahunBerkurangJalanIrigasiJaringan
    extra = 0


class KontrakJalanIrigasiJaringanAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga')
    search_fields = ['nomor_sp2d']
    date_hierarchy = 'tanggal_sp2d'
    list_per_page = 10
    list_filter = ['id_skpd']



class KontrakJalanIrigasiJaringanUmumAdmin(KontrakJalanIrigasiJaringanAdmin):
    readonly_fields = ['nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga']



class JalanIrigasiJaringanPenghapusanAdmin(JalanIrigasiJaringanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'konstruksi', 'panjang', 'lebar', 'luas',
                    'tahun',
                    'tanggal_dokumen', 'nomor_dokumen',
                    'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    inlines = [PenghapusanJalanIrigasiJaringanInline,
                    TahunBerkurangJalanIrigasiJaringanInline,
                    SKPDAsalJalanIrigasiJaringanInline,
                    SKPDTujuanJalanIrigasiJaringanInline,
                    FotoJalanIrigasiJaringanInline, ]


class JalanIrigasiJaringanUsulHapusAdmin(JalanIrigasiJaringanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'konstruksi', 'panjang', 'lebar', 'luas',
                    'tahun',
                    'tanggal_dokumen', 'nomor_dokumen',
                    'banyak_barang',
                    'id_satuan_barang', 'id_tanah']
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanInline,
                    SKPDAsalJalanIrigasiJaringanInline,
                    FotoJalanIrigasiJaringanInline, ]


class JalanIrigasiJaringanPemanfaatanAdmin(JalanIrigasiJaringanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'konstruksi', 'panjang', 'lebar', 'luas',
                    'tahun',
                    'tanggal_dokumen', 'nomor_dokumen',
                    'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    inlines = [PemanfaatanJalanIrigasiJaringanInline,
                    SKPDAsalJalanIrigasiJaringanInline,
                    SKPDTujuanJalanIrigasiJaringanInline, ]


class HargaJalanIrigasiJaringanAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_jalan_irigasi_jaringan', 'id_asal_usul',
                    'tahun', 'id_kontrak_jalan_irigasi_jaringan',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    list_display = ('id_jalan_irigasi_jaringan', 'id_asal_usul',
                    'tahun', 'id_kontrak_jalan_irigasi_jaringan',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan')
    readonly_fields = ['id_jalan_irigasi_jaringan', 'id_asal_usul',
                    'tahun', 'id_kontrak_jalan_irigasi_jaringan',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    #search_fields = ['id_tanah']
    list_filter = ['tahun', 'id_asal_usul']
    list_per_page = 10
    raw_id_fields = ['id_kontrak_jalan_irigasi_jaringan']




class KDPJalanIrigasiJaringanAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'konstruksi', 'panjang', 'lebar', 'luas',
                    'tahun',
                    'tanggal_dokumen', 'nomor_dokumen',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'id_tanah', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    #save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang']
    list_per_page = 10
    radio_fields = {"id_golongan_barang" : admin.HORIZONTAL}
    raw_id_fields = ['id_kode_barang', 'id_tanah']
    inlines = [HargaJalanIrigasiJaringanInline,
                    SKPDAsalJalanIrigasiJaringanInline,
                    FotoJalanIrigasiJaringanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__in=[2,3,4])
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=6)
        return super(KDPJalanIrigasiJaringanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_golongan_barang__exact=6)



class KDPJalanIrigasiJaringanReklasAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'konstruksi', 'panjang', 'lebar', 'luas',
                    'tahun',
                    'tanggal_dokumen', 'nomor_dokumen',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'id_tanah', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang']
    list_per_page = 10
    radio_fields = {"id_golongan_barang" : admin.HORIZONTAL}
    raw_id_fields = ['id_kode_barang', 'id_tanah']
    inlines = [HargaJalanIrigasiJaringanInline,
                    SKPDAsalJalanIrigasiJaringanInline,
                    SKPDTujuanJalanIrigasiJaringanInline,
                    FotoJalanIrigasiJaringanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__in=[2,3,4])
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__in=[4,6])
        return super(KDPJalanIrigasiJaringanReklasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_mutasi_berkurang__exact=9)







###Register JalanIrigasiJaringan

admin.site.register(JalanIrigasiJaringan, JalanIrigasiJaringanAdmin)
admin.site.register(KDPJalanIrigasiJaringan, KDPJalanIrigasiJaringanAdmin)
admin.site.register(KDPJalanIrigasiJaringanReklas, KDPJalanIrigasiJaringanReklasAdmin)
admin.site.register(KontrakJalanIrigasiJaringan, KontrakJalanIrigasiJaringanUmumAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanPenghapusanAdmin)
admin.site.register(JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPemanfaatanAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapus, JalanIrigasiJaringanUsulHapusAdmin)
admin.site.register(HargaJalanIrigasiJaringan, HargaJalanIrigasiJaringanAdmin)
