### $Id: admin.py,v 1.32 2017/12/18 03:09:34 muntaza Exp $


from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus, TahunBerkurangTanah

from umum.models import TanahReklas, SKPDAsalTanah, SKPDTujuanTanah, FotoTanah

from umum.forms import HargaTanahForm


###Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan



### class Umum


class ProvinsiAdmin(admin.ModelAdmin):
    list_display = ("kode_provinsi", "nama_provinsi")

class KabupatenAdmin(admin.ModelAdmin):
    list_display = ("kode_kabupaten", "nama_kabupaten", "id_provinsi")

class SKPDInline(admin.TabularInline):
    model = SKPD
    extra = 0

class LokasiBidangAdmin(admin.ModelAdmin):
    list_display = ("kode_lokasi_bidang", "nama_lokasi_bidang", "id_kabupaten")
    ordering = ["kode_lokasi_bidang"]
    list_per_page = 10
    inlines = [SKPDInline]

class SUBSKPDInline(admin.TabularInline):
    model = SUBSKPD
    extra = 0

class SKPDAdmin(admin.ModelAdmin):
    list_display = ("kode_skpd", "nama_skpd", "id_lokasi_bidang")
    ordering = ["id"]
    list_per_page = 10
    inlines = [SUBSKPDInline]

class SUBSKPDAdmin(admin.ModelAdmin):
    list_display = ("kode_sub_skpd", "nama_sub_skpd", "id_skpd")
    search_fields = ["nama_sub_skpd",]
    ordering = ["id"]
    list_per_page = 10

class KodeBarangAdmin(admin.ModelAdmin):
    list_display = ("kode_barang",)
    ordering = ["id"]
    list_per_page = 10
    search_fields = ["kode_barang",]
    readonly_fields = ["kode_barang", "umur"]

class HakTanahAdmin(admin.ModelAdmin):
    list_display = ("hak_tanah",)
    ordering = ["id"]
    list_per_page = 10

class SatuanBarangAdmin(admin.ModelAdmin):
    list_display = ("satuan_barang",)
    ordering = ["id"]
    list_per_page = 10

class KeadaanBarangAdmin(admin.ModelAdmin):
    list_display = ("keadaan_barang",)
    ordering = ["id"]
    list_per_page = 10

class SKPenghapusanAdmin(admin.ModelAdmin):
    list_display = ("tanggal_sk_penghapusan", "nomor_sk_penghapusan")
    ordering = ["id"]
    date_hierarchy = 'tanggal_sk_penghapusan'
    list_per_page = 10

class MutasiBerkurangAdmin(admin.ModelAdmin):
    list_display = ("mutasi_berkurang",)
    ordering = ["id"]
    list_per_page = 10

class JenisPemanfaatanAdmin(admin.ModelAdmin):
    list_display = ("jenis_pemanfaatan",)
    ordering = ["id"]
    list_per_page = 10

class AsalUsulAdmin(admin.ModelAdmin):
    list_display = ("asal_usul",)
    ordering = ["id"]
    list_per_page = 10

class TahunAdmin(admin.ModelAdmin):
    list_display = ("tahun",)
    list_per_page = 10

class GolonganBarangAdmin(admin.ModelAdmin):
    list_display = ("golongan_barang",)
    ordering = ["id"]
    list_per_page = 10


### Inline Gedung Bangunan
class GedungBangunanInline(admin.TabularInline):
    model = GedungBangunan
    extra = 0
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'tahun',
                    'id_mutasi_berkurang']
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'tahun',
                    'id_mutasi_berkurang']




### Class Tanah
class TahunBerkurangTanahInline(admin.TabularInline):
    model = TahunBerkurangTanah
    extra = 0


class TahunBerkurangUsulHapusTanahInline(admin.TabularInline):
    model = TahunBerkurangUsulHapusTanah
    extra = 0


class PenghapusanTanahInline(admin.TabularInline):
    model = PenghapusanTanah
    extra = 0

class SKPDAsalTanahInline(admin.TabularInline):
    model = SKPDAsalTanah
    extra = 0

class SKPDTujuanTanahInline(admin.TabularInline):
    model = SKPDTujuanTanah
    extra = 0

class PemanfaatanTanahInline(admin.TabularInline):
    model = PemanfaatanTanah
    extra = 0

class HargaTanahInline(admin.TabularInline):
    model = HargaTanah
    form = HargaTanahForm
    extra = 0
    fields = ['id_tanah', 'id_asal_usul', 'luas',
                    'tahun', 'id_kontrak', 'harga_bertambah', 'harga_berkurang',
                    'catatan', 'tahun_mutasi']
    raw_id_fields = ['id_kontrak']


class FotoTanahInline(admin.TabularInline):
    model = FotoTanah
    extra = 0
    fields = ['id_tanah', 'foto', 'tanggal',
                    'catatan', ]



class TanahAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'tahun', 'letak_alamat',
                    'id_hak_tanah', 'tanggal_sertifikat', 'nomor_sertifikat',
                    'penggunaan', 'banyak_barang', 'id_keadaan_barang',
                    'id_satuan_barang', 'id_mutasi_berkurang', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'letak_alamat', 'penggunaan', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    #save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang']
    list_per_page = 10
    radio_fields = {"id_golongan_barang" : admin.HORIZONTAL}
    raw_id_fields = ['id_kode_barang']
    inlines = [HargaTanahInline, SKPDAsalTanahInline,
                    FotoTanahInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #    if db_field.name == "id_sub_skpd":
    #        kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=2)
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=4)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=1)
        return super(TanahAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TanahUmumAdmin(TanahAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'tahun', 'letak_alamat',
                    'id_hak_tanah', 'tanggal_sertifikat', 'nomor_sertifikat',
                    'penggunaan', 'banyak_barang', 'id_keadaan_barang',
                    'id_satuan_barang', 'id_mutasi_berkurang', 'keterangan']


class KontrakTanahAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga')
    search_fields = ['nomor_sp2d']
    date_hierarchy = 'tanggal_sp2d'
    list_per_page = 10
    list_filter = ['id_skpd']



class KontrakTanahUmumAdmin(KontrakTanahAdmin):
    readonly_fields = ['nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga']


class TanahUsulHapusAdmin(TanahAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'tahun', 'letak_alamat',
                    'id_hak_tanah', 'tanggal_sertifikat', 'nomor_sertifikat',
                    'penggunaan', 'banyak_barang',
                    'id_satuan_barang']
    inlines = [TahunBerkurangUsulHapusTanahInline, SKPDAsalTanahInline,
                    FotoTanahInline, ]


class TanahPenghapusanAdmin(TanahAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'tahun', 'letak_alamat',
                    'id_hak_tanah', 'tanggal_sertifikat', 'nomor_sertifikat',
                    'penggunaan', 'banyak_barang',
                    'id_satuan_barang', 'keterangan']
    inlines = [PenghapusanTanahInline, TahunBerkurangTanahInline,
                SKPDAsalTanahInline, SKPDTujuanTanahInline,
                FotoTanahInline, ]


class TanahPemanfaatanAdmin(TanahAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'tahun', 'letak_alamat',
                    'id_hak_tanah', 'tanggal_sertifikat', 'nomor_sertifikat',
                    'penggunaan', 'banyak_barang', 'id_keadaan_barang',
                    'id_satuan_barang', 'id_mutasi_berkurang', 'keterangan']
    inlines = [PemanfaatanTanahInline,]


class HargaTanahAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_tanah', 'id_asal_usul', 'luas',
                    'tahun', 'id_kontrak', 'harga_bertambah', 'harga_berkurang',
                    'catatan']
    list_display = ('id_tanah', 'luas', 'id_asal_usul',
                    'tahun', 'id_kontrak', 'harga_bertambah', 'harga_berkurang',
                    'catatan')
    readonly_fields = ['id_tanah', 'luas', 'id_asal_usul',
                    'tahun', 'id_kontrak', 'harga_bertambah', 'harga_berkurang',
                    'catatan']
    search_fields = ['id_tanah']
    list_filter = ['tahun']
    list_per_page = 10
    raw_id_fields = ['id_kontrak']





class TanahReklasAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'tahun', 'letak_alamat',
                    'id_hak_tanah', 'tanggal_sertifikat', 'nomor_sertifikat',
                    'penggunaan', 'banyak_barang', 'id_keadaan_barang',
                    'id_satuan_barang', 'id_mutasi_berkurang', 'keterangan']
    list_display = ('nama_barang', 'id', 'id_golongan_barang', 'id_sub_skpd',
            'tahun', 'letak_alamat', 'penggunaan', 'id_mutasi_berkurang',
            'keterangan')
    search_fields = ['nama_barang', 'id']
    save_as = True
    readonly_fields = ['id']
    list_filter = ['tahun', 'id_mutasi_berkurang']
    list_per_page = 10
    radio_fields = {"id_golongan_barang" : admin.HORIZONTAL}
    raw_id_fields = ['id_kode_barang', 'id_sub_skpd', ]
    inlines = [HargaTanahInline, TahunBerkurangTanahInline, SKPDAsalTanahInline,
                    FotoTanahInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=4)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=1)
        return super(TanahReklasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_mutasi_berkurang__exact=9)



###Register UMUM
admin.site.register(Provinsi, ProvinsiAdmin)
admin.site.register(Kabupaten, KabupatenAdmin)
admin.site.register(LokasiBidang, LokasiBidangAdmin)
admin.site.register(SKPD, SKPDAdmin)
admin.site.register(SUBSKPD, SUBSKPDAdmin)
admin.site.register(KodeBarang, KodeBarangAdmin)
admin.site.register(HakTanah, HakTanahAdmin)
admin.site.register(SatuanBarang, SatuanBarangAdmin)
admin.site.register(KeadaanBarang, KeadaanBarangAdmin)
admin.site.register(SKPenghapusan, SKPenghapusanAdmin)
admin.site.register(MutasiBerkurang, MutasiBerkurangAdmin)
admin.site.register(JenisPemanfaatan, JenisPemanfaatanAdmin)
admin.site.register(AsalUsul, AsalUsulAdmin)
admin.site.register(Tahun, TahunAdmin)
admin.site.register(GolonganBarang, GolonganBarangAdmin)


###Register Tanah
admin.site.register(Tanah, TanahUmumAdmin)
admin.site.register(KontrakTanah, KontrakTanahUmumAdmin)
admin.site.register(TanahUsulHapus, TanahUsulHapusAdmin)
admin.site.register(TanahPenghapusan, TanahPenghapusanAdmin)
admin.site.register(TanahPemanfaatan, TanahPemanfaatanAdmin)
admin.site.register(HargaTanah, HargaTanahAdmin)
admin.site.register(TanahReklas, TanahReklasAdmin)
