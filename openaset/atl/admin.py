### $Id: admin.py,v 1.15 2017/12/18 03:50:25 muntaza Exp $



from django.contrib import admin

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah

from gedungbangunan.models import Ruangan

from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL
from atl.models import ATLReklas


#untuk menampung inline
from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import SKPDAsalATL, SKPDTujuanATL, FotoATL

from umum.forms import HargaTanahForm


### class Aset Tetap Lainnya
class SKPDAsalATLInline(admin.TabularInline):
    model = SKPDAsalATL
    extra = 0

class SKPDTujuanATLInline(admin.TabularInline):
    model = SKPDTujuanATL
    extra = 0


class HargaATLInline(admin.TabularInline):
    model = HargaATL
    form = HargaTanahForm
    extra = 0
    fields = ['id_atl', 'id_asal_usul',
                    'tahun', 'id_kontrak_atl', 'harga_bertambah',
                    'harga_berkurang',
                    'catatan', 'tahun_mutasi']
    raw_id_fields = ['id_kontrak_atl']



class FotoATLInline(admin.TabularInline):
    model = FotoATL
    extra = 0
    fields = ['id_atl', 'foto', 'tanggal',
                    'catatan', ]



class ATLAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'judul_pencipta_buku', 'spesifikasi_buku',
                    'asal_daerah_barang_seni', 'pencipta_barang_seni',
                    'bahan_barang_seni',
                    'jenis_hewan_tumbuhan', 'ukuran_hewan_tumbuhan',
                    'tahun',
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
    inlines = [HargaATLInline,
                SKPDAsalATLInline, FotoATLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__in=[1,5,6])
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=5)
        return super(ATLAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)







class PenghapusanATLInline(admin.TabularInline):
    model = PenghapusanATL
    extra = 0

class PemanfaatanATLInline(admin.TabularInline):
    model = PemanfaatanATL
    extra = 0

class TahunBerkurangATLInline(admin.TabularInline):
    model = TahunBerkurangATL
    extra = 0


class TahunBerkurangUsulHapusATLInline(admin.TabularInline):
    model = TahunBerkurangUsulHapusATL
    extra = 0


class KontrakATLAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga')
    search_fields = ['nomor_sp2d']
    date_hierarchy = 'tanggal_sp2d'
    list_per_page = 10
    list_filter = ['id_skpd']



class KontrakATLUmumAdmin(KontrakATLAdmin):
    readonly_fields = ['nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga']


class ATLPenghapusanAdmin(ATLAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'judul_pencipta_buku', 'spesifikasi_buku',
                    'asal_daerah_barang_seni', 'pencipta_barang_seni',
                    'bahan_barang_seni',
                    'jenis_hewan_tumbuhan', 'ukuran_hewan_tumbuhan',
                    'tahun',
                    'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', 'keterangan']
    save_as = False
    inlines = [PenghapusanATLInline,
                    TahunBerkurangATLInline,
                    SKPDAsalATLInline,
                    SKPDTujuanATLInline, FotoATLInline, ]

class ATLPemanfaatanAdmin(ATLAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'judul_pencipta_buku', 'spesifikasi_buku',
                    'asal_daerah_barang_seni', 'pencipta_barang_seni',
                    'bahan_barang_seni',
                    'jenis_hewan_tumbuhan', 'ukuran_hewan_tumbuhan',
                    'tahun',
                    'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', 'keterangan']
    save_as = False
    inlines = [PemanfaatanATLInline]


class ATLUsulHapusAdmin(ATLAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'judul_pencipta_buku', 'spesifikasi_buku',
                    'asal_daerah_barang_seni', 'pencipta_barang_seni',
                    'bahan_barang_seni',
                    'jenis_hewan_tumbuhan', 'ukuran_hewan_tumbuhan',
                    'tahun',
                    'banyak_barang',
                    'id_satuan_barang', 'id_ruangan', ]
    save_as = False
    inlines = [TahunBerkurangUsulHapusATLInline,
                    SKPDAsalATLInline, FotoATLInline, ]


class HargaATLAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_atl', 'id_asal_usul',
                    'tahun', 'id_kontrak_atl',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    list_display = ('id_atl', 'id_asal_usul',
                    'tahun', 'id_kontrak_atl',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan')
    readonly_fields = ['id_atl', 'id_asal_usul',
                    'tahun', 'id_kontrak_atl',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    #search_fields = ['id_ruangan']
    list_filter = ['tahun', 'id_asal_usul']
    list_per_page = 10
    raw_id_fields = ['id_kontrak_atl']



class ATLReklasAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'judul_pencipta_buku', 'spesifikasi_buku',
                    'asal_daerah_barang_seni', 'pencipta_barang_seni',
                    'bahan_barang_seni',
                    'jenis_hewan_tumbuhan', 'ukuran_hewan_tumbuhan',
                    'tahun',
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
    raw_id_fields = ['id_kode_barang', 'id_sub_skpd', ]
    inlines = [HargaATLInline, PenghapusanATLInline, TahunBerkurangATLInline,
                    SKPDAsalATLInline,
                    SKPDTujuanATLInline, FotoATLInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__in=[1,5,6])
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=5)
        return super(ATLReklasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_mutasi_berkurang__exact=9)

###Register UMUM ATL


###Register ATL
admin.site.register(ATL, ATLAdmin)
admin.site.register(KontrakATL, KontrakATLUmumAdmin)
admin.site.register(ATLPenghapusan, ATLPenghapusanAdmin)
admin.site.register(ATLUsulHapus, ATLUsulHapusAdmin)
admin.site.register(ATLPemanfaatan, ATLPemanfaatanAdmin)
admin.site.register(HargaATL, HargaATLAdmin)
admin.site.register(ATLReklas, ATLReklasAdmin)
