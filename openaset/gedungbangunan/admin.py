### $Id: admin.py,v 1.32 2017/12/18 03:24:36 muntaza Exp $



from django.contrib import admin

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah

from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung, Persen, PenambahanUmur


#untuk menampung inline
from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, KDPGedungBangunan, KDPGedungBangunanReklas, GedungBangunanUsulHapus

from gedungbangunan.models import SKPDAsalGedungBangunan, SKPDTujuanGedungBangunan, FotoGedungBangunan

from umum.forms import HargaTanahForm


### class Gedung Bangunan
class SKPDAsalGedungBangunanInline(admin.TabularInline):
    model = SKPDAsalGedungBangunan
    extra = 0

class SKPDTujuanGedungBangunanInline(admin.TabularInline):
    model = SKPDTujuanGedungBangunan
    extra = 0

class RuanganAdmin(admin.ModelAdmin):
    readonly_fields = ['id_gedung_bangunan', 'kode_ruangan', 'nama_ruangan']
    list_display = ("nama_ruangan",)
    ordering = ["id"]
    list_per_page = 10


class StatusTingkatAdmin(admin.ModelAdmin):
    list_display = ("status_tingkat",)
    ordering = ["id"]
    list_per_page = 10


class StatusBetonAdmin(admin.ModelAdmin):
    list_display = ("status_beton",)
    ordering = ["id"]
    list_per_page = 10


class PersenAdmin(admin.ModelAdmin):
    list_display = ("persen",)
    list_per_page = 10


class PenambahanUmurAdmin(admin.ModelAdmin):
    list_display = ("kode_barang", "persen", "umur")
    ordering = ["kode_barang", "persen"]
    list_per_page = 10


class HargaGedungBangunanInline(admin.TabularInline):
    model = HargaGedungBangunan
    form = HargaTanahForm
    extra = 0
    fields = ['id_gedung_bangunan', 'id_asal_usul', 'luas_lantai',
                    'tahun', 'id_kontrak_gedung_bangunan', 'harga_bertambah',
                    'harga_berkurang',
                    'catatan', 'tahun_mutasi']
    raw_id_fields = ['id_kontrak_gedung_bangunan']



class FotoGedungBangunanInline(admin.TabularInline):
    model = FotoGedungBangunan
    extra = 0
    fields = ['id_gedung_bangunan', 'foto', 'tanggal',
                    'catatan', ]



class GedungBangunanAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
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
    inlines = [HargaGedungBangunanInline, SKPDAsalGedungBangunanInline,
                    FotoGedungBangunanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=2)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=3)
        return super(GedungBangunanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_golongan_barang__exact=3)


class RuanganInline(admin.TabularInline):
    model = Ruangan
    extra = 0


class PenghapusanGedungBangunanInline(admin.TabularInline):
    model = PenghapusanGedungBangunan
    extra = 0


class PemanfaatanGedungBangunanInline(admin.TabularInline):
    model = PemanfaatanGedungBangunan
    extra = 0


class TahunBerkurangGedungBangunanInline(admin.TabularInline):
    model = TahunBerkurangGedungBangunan
    extra = 0


class TahunBerkurangUsulHapusGedungInline(admin.TabularInline):
    model = TahunBerkurangUsulHapusGedung
    extra = 0


class KontrakGedungBangunanAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga')
    search_fields = ['nomor_sp2d']
    date_hierarchy = 'tanggal_sp2d'
    list_per_page = 10
    list_filter = ['id_skpd']



class KontrakGedungBangunanUmumAdmin(KontrakGedungBangunanAdmin):
    readonly_fields = ['nomor_sp2d', 'tanggal_sp2d',
            'id_skpd', 'nomor_kontrak', 'tanggal_kontrak', 'pihak_ketiga']




class KDPGedungBangunanAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
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
    inlines = [HargaGedungBangunanInline, RuanganInline,
                    TahunBerkurangGedungBangunanInline,
                    SKPDAsalGedungBangunanInline,
                    SKPDTujuanGedungBangunanInline,
                    FotoGedungBangunanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=2)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__exact=6)
        return super(KDPGedungBangunanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_golongan_barang__exact=6)



class KDPGedungBangunanReklasAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
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
    inlines = [HargaGedungBangunanInline, RuanganInline,
                    TahunBerkurangGedungBangunanInline,
                    SKPDAsalGedungBangunanInline,
                    SKPDTujuanGedungBangunanInline,
                    FotoGedungBangunanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=2)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__in=[3,6])
        return super(KDPGedungBangunanReklasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_mutasi_berkurang__exact=9)






class GedungBangunanRuanganAdmin(GedungBangunanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    inlines = [RuanganInline]


class GedungBangunanPenghapusanAdmin(GedungBangunanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
                    'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    inlines = [PenghapusanGedungBangunanInline,
                    TahunBerkurangGedungBangunanInline,
                    SKPDAsalGedungBangunanInline,
                    SKPDTujuanGedungBangunanInline,
                    FotoGedungBangunanInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_satuan_barang":
            kwargs["queryset"] = SatuanBarang.objects.filter(id__exact=2)
        if db_field.name == "id_golongan_barang":
            kwargs["queryset"] = GolonganBarang.objects.filter(id__in=[3,6])
        return super(GedungBangunanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_golongan_barang__in=[3.6])



class GedungBangunanUsulHapusAdmin(GedungBangunanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
                    'banyak_barang',
                    'id_satuan_barang', 'id_tanah']
    inlines = [TahunBerkurangUsulHapusGedungInline,
                    SKPDAsalGedungBangunanInline,
                    FotoGedungBangunanInline, ]



class GedungBangunanPemanfaatanAdmin(GedungBangunanAdmin):
    readonly_fields = ['id_sub_skpd', 'id_golongan_barang', 'nama_barang',
                    'id', 'id_kode_barang', 'id_keadaan_barang',
                    'id_status_tingkat', 'id_status_beton', 'tahun',
                    'tanggal_dokumen_gedung', 'nomor_dokumen_gedung',
                    'id_mutasi_berkurang', 'banyak_barang',
                    'id_satuan_barang', 'id_tanah', 'keterangan']
    inlines = [PemanfaatanGedungBangunanInline]


class HargaGedungBangunanAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = ['id_gedung_bangunan', 'id_asal_usul', 'luas_lantai',
                    'tahun', 'id_kontrak_gedung_bangunan',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    list_display = ('id_gedung_bangunan', 'id_asal_usul', 'luas_lantai',
                    'tahun', 'id_kontrak_gedung_bangunan',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan')
    readonly_fields = ['id_gedung_bangunan', 'id_asal_usul', 'luas_lantai',
                    'tahun', 'id_kontrak_gedung_bangunan',
                    'harga_bertambah', 'harga_berkurang',
                    'catatan']
    #search_fields = ['id_tanah']
    list_filter = ['tahun', 'id_asal_usul']
    list_per_page = 10
    raw_id_fields = ['id_kontrak_gedung_bangunan']




###Register UMUM Gedung Bangunan
admin.site.register(Ruangan, RuanganAdmin)
admin.site.register(StatusTingkat, StatusTingkatAdmin)
admin.site.register(StatusBeton, StatusBetonAdmin)


###Register GedungBangunan

admin.site.register(GedungBangunan, GedungBangunanAdmin)
admin.site.register(KDPGedungBangunan, KDPGedungBangunanAdmin)
admin.site.register(KDPGedungBangunanReklas, KDPGedungBangunanReklasAdmin)
admin.site.register(KontrakGedungBangunan, KontrakGedungBangunanUmumAdmin)
admin.site.register(GedungBangunanRuangan, GedungBangunanRuanganAdmin)
admin.site.register(GedungBangunanPenghapusan, GedungBangunanPenghapusanAdmin)
admin.site.register(GedungBangunanUsulHapus, GedungBangunanUsulHapusAdmin)
admin.site.register(GedungBangunanPemanfaatan, GedungBangunanPemanfaatanAdmin)
admin.site.register(HargaGedungBangunan, HargaGedungBangunanAdmin)
admin.site.register(Persen, PersenAdmin)
admin.site.register(PenambahanUmur, PenambahanUmurAdmin)
