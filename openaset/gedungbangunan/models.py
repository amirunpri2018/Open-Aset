### $Id: models.py,v 1.83 2017/12/10 01:54:39 muntaza Exp $



from django.db import models

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah



### Kumpulan Table KIB C Gedung dan Bangunan

class StatusTingkat(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    status_tingkat = models.CharField("Status Tingkat", max_length=100,
                    db_column="status_tingkat", unique=True)

    class Meta:
        db_table = "status_tingkat"
        verbose_name = "Status Tingkat"
        verbose_name_plural = "Status Tingkat"

    def __unicode__(self):
        return self.status_tingkat




class StatusBeton(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    status_beton = models.CharField("Status Beton", max_length=100,
                    db_column="status_beton", unique=True)

    class Meta:
        db_table = "status_beton"
        verbose_name = "Status Beton"
        verbose_name_plural = "Status Beton"

    def __unicode__(self):
        return self.status_beton




class GedungBangunan(models.Model):
    id = models.AutoField(primary_key=True,
                    verbose_name="Register",
                    db_column="id")
    id_sub_skpd = models.ForeignKey(SUBSKPD,
                    verbose_name="SUB SKPD",
                    db_column="id_sub_skpd")
    id_golongan_barang = models.ForeignKey(GolonganBarang,
                    verbose_name="Golongan Barang",
                    default=3,
                    db_column="id_golongan_barang")
    nama_barang = models.CharField("Nama Barang",
                    max_length=300,
                    db_column="nama_barang")
    id_kode_barang = models.ForeignKey(KodeBarang,
                    verbose_name="Kode Barang",
                    limit_choices_to = {'id__gt': 7267, 'id__lt': 7621},
                    db_column="id_kode_barang")
    id_keadaan_barang = models.ForeignKey(KeadaanBarang,
                    default=1,
                    verbose_name="Keadaan Barang",
                    db_column="id_keadaan_barang")
    id_status_tingkat = models.ForeignKey(StatusTingkat,
                    verbose_name="Status Tingkat",
                    db_column="id_status_tingkat")
    id_status_beton = models.ForeignKey(StatusBeton,
                    verbose_name="Status Beton",
                    db_column="id_status_beton")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun Awal",
                    help_text="Tahun Awal Kapitalisasi",
                    db_column="tahun")
    tanggal_dokumen_gedung = models.DateField("Tanggal Dokumen Gedung",
                    null=True, blank=True,
                    db_column="tanggal_dokumen_gedung")
    nomor_dokumen_gedung = models.CharField("Nomor Dokumen Gedung",
                    max_length=300,
                    null=True, blank=True,
                    db_column="nomor_dokumen_gedung")
    id_mutasi_berkurang = models.ForeignKey(MutasiBerkurang,
                    default=5,
                    verbose_name="Mutasi Berkurang",
                    db_column="id_mutasi_berkurang")
    banyak_barang = models.IntegerField("Banyak Barang",
                    default=1,
                    db_column="banyak_barang")
    id_satuan_barang = models.ForeignKey(SatuanBarang,
                    verbose_name="Satuan Barang",
                    db_column="id_satuan_barang")
    id_tanah = models.ForeignKey(Tanah,
                    verbose_name="Tanah",
                    db_column="id_tanah")
    keterangan = models.TextField("Keterangan",
                    null=True, blank=True,
                    db_column="keterangan")

    class Meta:
        db_table = "gedung_bangunan"
        verbose_name = "Gedung Bangunan"
        verbose_name_plural = "Gedung Bangunan"

    def __unicode__(self):
        return self.nama_barang




class Ruangan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_gedung_bangunan = models.ForeignKey(GedungBangunan,
                    verbose_name="Gedung Bangunan",
                    db_column="id_gedung_bangunan")
    kode_ruangan = models.CharField("Kode Ruangan", max_length=10,
                    db_column="kode_ruangan")
    nama_ruangan = models.CharField("Nama Ruangan", max_length=250,
                    db_column="nama_ruangan")

    class Meta:
        db_table = "ruangan"
        verbose_name = "Ruangan"
        verbose_name_plural = "Ruangan"
        ordering = ['id_gedung_bangunan', 'kode_ruangan']

    def __unicode__(self):
        return "%s : %s : %s" % (self.id_gedung_bangunan, self.kode_ruangan, self.nama_ruangan)



class Persen(models.Model):
    persen = models.IntegerField(primary_key=True, db_column="persen")

    class Meta:
        db_table = "persen"
        verbose_name = "Persen"
        verbose_name_plural = "Persen"
        ordering = ['persen']

    def __unicode__(self):
        return "%i" % (self.persen)



class PenambahanUmur(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    kode_barang = models.CharField("Kode Barang", max_length=50,
                    db_column="kode_barang")
    persen = models.ForeignKey(Persen,
                    verbose_name="Persen",
                    db_column="persen")
    umur = models.IntegerField("Umur",
                    db_column="umur")

    class Meta:
        db_table = "penambahan_umur"
        verbose_name = "Penambahan Umur"
        verbose_name_plural = "Penambahan Umur"
        ordering = ['kode_barang', 'persen']

    def __unicode__(self):
        return "%s : %s : %s" % (self.kode_barang, self.persen, self.umur)



#untuk menampung inline Ruangan
class GedungBangunanRuangan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "Gedung Bangunan Ruangan"
        verbose_name_plural = "Gedung Bangunan Ruangan"

    def __unicode__(self):
        return self.nama_barang



#untuk menampung inline PenghapusanGedungBangunan
class GedungBangunanPenghapusan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "Gedung Bangunan Penghapusan"
        verbose_name_plural = "Gedung Bangunan Penghapusan"

    def __unicode__(self):
        return self.nama_barang



#untuk menampung inline TahunBerkurangUsulHapusGedung
class GedungBangunanUsulHapus(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "Gedung Bangunan Usul Hapus"
        verbose_name_plural = "Gedung Bangunan Usul Hapus"

    def __unicode__(self):
        return self.nama_barang



#untuk menampung inline PemanfaatanGedungBangunan
class GedungBangunanPemanfaatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "Gedung Bangunan Pemanfaatan"
        verbose_name_plural = "Gedung Bangunan Pemanfaatan"

    def __unicode__(self):
        return self.nama_barang


class KontrakGedungBangunan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    pihak_ketiga = models.CharField("Pihak Ketiga",
                    max_length=200,
                    db_column="pihak_ketiga")
    nomor_kontrak = models.CharField("Nomor Kontrak",
                    max_length=200,
                    null=True, blank=True,
                    db_column="nomor_kontrak")
    tanggal_kontrak = models.DateField("Tanggal Kontrak",
                    null=True, blank=True,
                    db_column="tanggal_kontrak")
    nomor_sp2d = models.CharField("Nomor SP2D",
                    max_length=200,
                    db_column="nomor_sp2d")
    tanggal_sp2d = models.DateField("Tanggal SP2D",
                    null=True, blank=True,
                    db_column="tanggal_sp2d")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "kontrak_gedung_bangunan"
	verbose_name = "Kontrak Gedung Bangunan"
        verbose_name_plural = "Kontrak Gedung Bangunan"

    def __unicode__(self):
        return self.nomor_sp2d



class TahunBerkurangGedungBangunan(models.Model):
    id = models.OneToOneField(GedungBangunan, primary_key=True,
                    db_column="id_gedung_bangunan")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_gedung_bangunan"
	verbose_name = "Tahun Berkurang Gedung Bangunan"
        verbose_name_plural = "Tahun Berkurang Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id)




class TahunBerkurangUsulHapusGedung(models.Model):
    id = models.OneToOneField(GedungBangunan, primary_key=True,
                    db_column="id_gedung_bangunan")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_usul_hapus_gedung"
	verbose_name = "Tahun Berkurang Usul Hapus Gedung"
        verbose_name_plural = "Tahun Berkurang Usul Hapus Gedung"

    def __unicode__(self):
        return "%s" % (self.id)




class PenghapusanGedungBangunan(models.Model):
    id = models.OneToOneField(GedungBangunan, primary_key=True,
                    db_column="id_gedung_bangunan")
    id_sk_penghapusan = models.ForeignKey(SKPenghapusan,
                    verbose_name="SK Penghapusan",
                    db_column="id_sk_penghapusan")

    class Meta:
        db_table = "penghapusan_gedung_bangunan"
	verbose_name = "Penghapusan Gedung Bangunan"
        verbose_name_plural = "Penghapusan Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id)


class PemanfaatanGedungBangunan(models.Model):
    id = models.OneToOneField(GedungBangunan, primary_key=True,
                    db_column="id_gedung_bangunan")
    id_jenis_pemanfaatan = models.ForeignKey(JenisPemanfaatan,
                    verbose_name="Jenis Pemanfaatan",
                    db_column="id_jenis_pemanfaatan")

    class Meta:
        db_table = "pemanfaatan_gedung_bangunan"
	verbose_name = "Pemanfaatan Gedung Bangunan"
        verbose_name_plural = "Pemanfaatan Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id)


class HargaGedungBangunan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_gedung_bangunan = models.ForeignKey(GedungBangunan,
                    verbose_name="Gedung Bangunan",
                    db_column="id_gedung_bangunan")
    luas_lantai = models.DecimalField("Luas Lantai (m2)",
                    max_digits=10, decimal_places=1, default=0,
                    db_column="luas_lantai")
    id_asal_usul = models.ForeignKey(AsalUsul,
                    verbose_name="Asal Usul",
                    db_column="id_asal_usul")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun",
                    help_text="Tahun Anggaran",
                    db_column="tahun")
    id_kontrak_gedung_bangunan = models.ForeignKey(KontrakGedungBangunan,
                    verbose_name="Kontrak Gedung Bangunan",
                    db_column="id_kontrak_gedung_bangunan")
    harga_bertambah = models.DecimalField("Harga Bertambah",
                    max_digits=15, decimal_places=0, default=0,
                    db_column="harga_bertambah")
    harga_berkurang = models.DecimalField("Harga Berkurang",
                    max_digits=15, decimal_places=0, default=0,
                    db_column="harga_berkurang")
    catatan = models.CharField("Catatan",
                    max_length=250,
                    help_text="Catatan pada Daftar Pengadaan",
                    db_column="catatan")
    tahun_mutasi = models.ForeignKey(Tahun,
                    verbose_name="Tahun Mutasi",
                    null=True, blank=True,
                    related_name='+',
                    help_text="Tahun Mutasi",
                    db_column="tahun_mutasi")

    class Meta:
        db_table = "harga_gedung_bangunan"
	verbose_name = "Harga Gedung Bangunan"
        verbose_name_plural = "Harga Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)

















#KDPGedungBangunanReklas, untuk melakukan reklasifikasi dari dan ke KDP
class KDPGedungBangunanReklas(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "KDP Gedung Bangunan Reklas"
        verbose_name_plural = "KDP Gedung Bangunan Reklas"

    def __unicode__(self):
        return self.nama_barang






#KDPGedungBangunan, untuk menampung data KIB F
class KDPGedungBangunan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "KDP Gedung Bangunan"
        verbose_name_plural = "KDP Gedung Bangunan"

    def __unicode__(self):
        return self.nama_barang



class SKPDAsalGedungBangunan(models.Model):
    id = models.OneToOneField(GedungBangunan, primary_key=True,
                    db_column="id_gedung_bangunan")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_asal_gedung_bangunan"
	verbose_name = "SKPD Asal Gedung Bangunan"
        verbose_name_plural = "SKPD Asal Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunan(models.Model):
    id = models.OneToOneField(GedungBangunan, primary_key=True,
                    db_column="id_gedung_bangunan")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_tujuan_gedung_bangunan"
	verbose_name = "SKPD Tujuan Gedung Bangunan"
        verbose_name_plural = "SKPD Tujuan Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_gedung_bangunan = models.ForeignKey(GedungBangunan,
                    verbose_name="Gedung Bangunan",
                    db_column="id_gedung_bangunan")
    foto = models.FileField("Foto",
                    upload_to='gedung_bangunan/',
                    help_text="PERINGATAN: Hanya Foto Aset dan Hasil Scan File Dokumen Kepemilikan, Bukan Foto Pengguna Aset!!!",
                    db_column="foto")
    tanggal = models.DateField("Tanggal",
                    null=True, blank=True,
                    help_text="Tanggal Foto yang di Upload",
                    db_column="tanggal")
    catatan = models.CharField("Catatan",
                    max_length=200,
                    help_text="Catatan Mengenai File yang di Upload",
                    db_column="catatan")

    class Meta:
        db_table = "foto_gedung_bangunan"
	verbose_name = "Foto Gedung Bangunan"
        verbose_name_plural = "Foto Gedung Bangunan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Setwan
##model pada app Setwan
class GedungBangunanSetwan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Gedung Setwan"
        verbose_name_plural = "01 Gedung Setwan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanSetwan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 KDP Gedung Setwan"
        verbose_name_plural = "01 KDP Gedung Setwan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganSetwan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Gedung Ruangan Setwan"
        verbose_name_plural = "01 Gedung Ruangan Setwan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusSetwan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Gedung Usul Hapus Setwan"
        verbose_name_plural = "01 Gedung Usul Hapus Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungSetwan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "01 Usul Hapus Gedung Setwan"
        verbose_name_plural = "01 Usul Hapus Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanSetwan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Kontrak Gedung Setwan"
        verbose_name_plural = "01 Kontrak Gedung Setwan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanSetwan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Harga Gedung Setwan"
        verbose_name_plural = "01 Harga Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanSetwan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Gedung Penghapusan Setwan"
        verbose_name_plural = "01 Gedung Penghapusan Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanSetwan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Tahun Berkurang Gedung Setwan"
        verbose_name_plural = "01 Tahun Berkurang Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanSetwan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Penghapusan Gedung Setwan"
        verbose_name_plural = "01 Penghapusan Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanSetwan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Asal Gedung Setwan"
        verbose_name_plural = "01 SKPD Asal Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanSetwan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Tujuan Gedung Setwan"
        verbose_name_plural = "01 SKPD Tujuan Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanSetwan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "01 Foto Gedung Setwan"
        verbose_name_plural = "01 Foto Gedung Setwan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Setda
##model pada app Setda
class GedungBangunanSetda(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Gedung Setda"
        verbose_name_plural = "02 Gedung Setda"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanSetda(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 KDP Gedung Setda"
        verbose_name_plural = "02 KDP Gedung Setda"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganSetda(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Gedung Ruangan Setda"
        verbose_name_plural = "02 Gedung Ruangan Setda"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusSetda(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Gedung Usul Hapus Setda"
        verbose_name_plural = "02 Gedung Usul Hapus Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungSetda(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "02 Usul Hapus Gedung Setda"
        verbose_name_plural = "02 Usul Hapus Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanSetda(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Kontrak Gedung Setda"
        verbose_name_plural = "02 Kontrak Gedung Setda"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanSetda(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Harga Gedung Setda"
        verbose_name_plural = "02 Harga Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanSetda(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Gedung Penghapusan Setda"
        verbose_name_plural = "02 Gedung Penghapusan Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanSetda(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Tahun Berkurang Gedung Setda"
        verbose_name_plural = "02 Tahun Berkurang Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanSetda(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Penghapusan Gedung Setda"
        verbose_name_plural = "02 Penghapusan Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanSetda(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Asal Gedung Setda"
        verbose_name_plural = "02 SKPD Asal Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanSetda(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Tujuan Gedung Setda"
        verbose_name_plural = "02 SKPD Tujuan Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanSetda(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "02 Foto Gedung Setda"
        verbose_name_plural = "02 Foto Gedung Setda"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DPUPR
##model pada app DPUPR
class GedungBangunanDPUPR(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Gedung DPUPR"
        verbose_name_plural = "03 Gedung DPUPR"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDPUPR(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 KDP Gedung DPUPR"
        verbose_name_plural = "03 KDP Gedung DPUPR"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDPUPR(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Gedung Ruangan DPUPR"
        verbose_name_plural = "03 Gedung Ruangan DPUPR"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDPUPR(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Gedung Usul Hapus DPUPR"
        verbose_name_plural = "03 Gedung Usul Hapus DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDPUPR(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "03 Usul Hapus Gedung DPUPR"
        verbose_name_plural = "03 Usul Hapus Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDPUPR(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Kontrak Gedung DPUPR"
        verbose_name_plural = "03 Kontrak Gedung DPUPR"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDPUPR(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Harga Gedung DPUPR"
        verbose_name_plural = "03 Harga Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDPUPR(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Gedung Penghapusan DPUPR"
        verbose_name_plural = "03 Gedung Penghapusan DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDPUPR(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Tahun Berkurang Gedung DPUPR"
        verbose_name_plural = "03 Tahun Berkurang Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDPUPR(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Penghapusan Gedung DPUPR"
        verbose_name_plural = "03 Penghapusan Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDPUPR(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Asal Gedung DPUPR"
        verbose_name_plural = "03 SKPD Asal Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDPUPR(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Tujuan Gedung DPUPR"
        verbose_name_plural = "03 SKPD Tujuan Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDPUPR(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "03 Foto Gedung DPUPR"
        verbose_name_plural = "03 Foto Gedung DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Dishub
##model pada app Dishub
class GedungBangunanDishub(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Gedung Dishub"
        verbose_name_plural = "04 Gedung Dishub"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDishub(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 KDP Gedung Dishub"
        verbose_name_plural = "04 KDP Gedung Dishub"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDishub(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Gedung Ruangan Dishub"
        verbose_name_plural = "04 Gedung Ruangan Dishub"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDishub(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Gedung Usul Hapus Dishub"
        verbose_name_plural = "04 Gedung Usul Hapus Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDishub(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "04 Usul Hapus Gedung Dishub"
        verbose_name_plural = "04 Usul Hapus Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDishub(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Kontrak Gedung Dishub"
        verbose_name_plural = "04 Kontrak Gedung Dishub"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDishub(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Harga Gedung Dishub"
        verbose_name_plural = "04 Harga Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDishub(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Gedung Penghapusan Dishub"
        verbose_name_plural = "04 Gedung Penghapusan Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDishub(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Tahun Berkurang Gedung Dishub"
        verbose_name_plural = "04 Tahun Berkurang Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDishub(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Penghapusan Gedung Dishub"
        verbose_name_plural = "04 Penghapusan Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDishub(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Asal Gedung Dishub"
        verbose_name_plural = "04 SKPD Asal Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDishub(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Tujuan Gedung Dishub"
        verbose_name_plural = "04 SKPD Tujuan Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDishub(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "04 Foto Gedung Dishub"
        verbose_name_plural = "04 Foto Gedung Dishub"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Dinkes
##model pada app Dinkes
class GedungBangunanDinkes(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes"
        verbose_name_plural = "05 Gedung Dinkes"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDinkes(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 KDP Gedung Dinkes"
        verbose_name_plural = "05 KDP Gedung Dinkes"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDinkes(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes"
        verbose_name_plural = "05 Gedung Ruangan Dinkes"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDinkes(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Usul Hapus Dinkes"
        verbose_name_plural = "05 Gedung Usul Hapus Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDinkes(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "05 Usul Hapus Gedung Dinkes"
        verbose_name_plural = "05 Usul Hapus Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDinkes(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Kontrak Gedung Dinkes"
        verbose_name_plural = "05 Kontrak Gedung Dinkes"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDinkes(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes"
        verbose_name_plural = "05 Harga Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDinkes(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Penghapusan Dinkes"
        verbose_name_plural = "05 Gedung Penghapusan Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDinkes(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Tahun Berkurang Gedung Dinkes"
        verbose_name_plural = "05 Tahun Berkurang Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDinkes(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Penghapusan Gedung Dinkes"
        verbose_name_plural = "05 Penghapusan Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDinkes(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDinkes(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Tujuan Gedung Dinkes"
        verbose_name_plural = "05 SKPD Tujuan Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkes(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes"
        verbose_name_plural = "05 Foto Gedung Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##RSUD
##model pada app RSUD
class GedungBangunanRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Gedung RSUD"
        verbose_name_plural = "06 Gedung RSUD"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 KDP Gedung RSUD"
        verbose_name_plural = "06 KDP Gedung RSUD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Gedung Ruangan RSUD"
        verbose_name_plural = "06 Gedung Ruangan RSUD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Gedung Usul Hapus RSUD"
        verbose_name_plural = "06 Gedung Usul Hapus RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungRSUD(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "06 Usul Hapus Gedung RSUD"
        verbose_name_plural = "06 Usul Hapus Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanRSUD(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Kontrak Gedung RSUD"
        verbose_name_plural = "06 Kontrak Gedung RSUD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanRSUD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Harga Gedung RSUD"
        verbose_name_plural = "06 Harga Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Gedung Penghapusan RSUD"
        verbose_name_plural = "06 Gedung Penghapusan RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanRSUD(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Tahun Berkurang Gedung RSUD"
        verbose_name_plural = "06 Tahun Berkurang Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanRSUD(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Penghapusan Gedung RSUD"
        verbose_name_plural = "06 Penghapusan Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanRSUD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Asal Gedung RSUD"
        verbose_name_plural = "06 SKPD Asal Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanRSUD(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Tujuan Gedung RSUD"
        verbose_name_plural = "06 SKPD Tujuan Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanRSUD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "06 Foto Gedung RSUD"
        verbose_name_plural = "06 Foto Gedung RSUD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Disdik
##model pada app Disdik
class GedungBangunanDisdik(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik"
        verbose_name_plural = "07 Gedung Disdik"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDisdik(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 KDP Gedung Disdik"
        verbose_name_plural = "07 KDP Gedung Disdik"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDisdik(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik"
        verbose_name_plural = "07 Gedung Ruangan Disdik"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDisdik(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Usul Hapus Disdik"
        verbose_name_plural = "07 Gedung Usul Hapus Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDisdik(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "07 Usul Hapus Gedung Disdik"
        verbose_name_plural = "07 Usul Hapus Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDisdik(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Kontrak Gedung Disdik"
        verbose_name_plural = "07 Kontrak Gedung Disdik"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDisdik(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik"
        verbose_name_plural = "07 Harga Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDisdik(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Penghapusan Disdik"
        verbose_name_plural = "07 Gedung Penghapusan Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDisdik(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Tahun Berkurang Gedung Disdik"
        verbose_name_plural = "07 Tahun Berkurang Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDisdik(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Penghapusan Gedung Disdik"
        verbose_name_plural = "07 Penghapusan Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDisdik(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDisdik(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Tujuan Gedung Disdik"
        verbose_name_plural = "07 SKPD Tujuan Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdik(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik"
        verbose_name_plural = "07 Foto Gedung Disdik"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Perpustakaan
##model pada app Perpustakaan
class GedungBangunanPerpustakaan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Gedung Perpustakaan"
        verbose_name_plural = "08 Gedung Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanPerpustakaan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 KDP Gedung Perpustakaan"
        verbose_name_plural = "08 KDP Gedung Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganPerpustakaan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Gedung Ruangan Perpustakaan"
        verbose_name_plural = "08 Gedung Ruangan Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusPerpustakaan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Gedung Usul Hapus Perpustakaan"
        verbose_name_plural = "08 Gedung Usul Hapus Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungPerpustakaan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "08 Usul Hapus Gedung Perpustakaan"
        verbose_name_plural = "08 Usul Hapus Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanPerpustakaan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Kontrak Gedung Perpustakaan"
        verbose_name_plural = "08 Kontrak Gedung Perpustakaan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanPerpustakaan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Harga Gedung Perpustakaan"
        verbose_name_plural = "08 Harga Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanPerpustakaan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Gedung Penghapusan Perpustakaan"
        verbose_name_plural = "08 Gedung Penghapusan Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanPerpustakaan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Tahun Berkurang Gedung Perpustakaan"
        verbose_name_plural = "08 Tahun Berkurang Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanPerpustakaan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Penghapusan Gedung Perpustakaan"
        verbose_name_plural = "08 Penghapusan Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanPerpustakaan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Asal Gedung Perpustakaan"
        verbose_name_plural = "08 SKPD Asal Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanPerpustakaan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Tujuan Gedung Perpustakaan"
        verbose_name_plural = "08 SKPD Tujuan Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanPerpustakaan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "08 Foto Gedung Perpustakaan"
        verbose_name_plural = "08 Foto Gedung Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Sosial
##model pada app Sosial
class GedungBangunanSosial(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Gedung Sosial"
        verbose_name_plural = "09 Gedung Sosial"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanSosial(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 KDP Gedung Sosial"
        verbose_name_plural = "09 KDP Gedung Sosial"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganSosial(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Gedung Ruangan Sosial"
        verbose_name_plural = "09 Gedung Ruangan Sosial"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusSosial(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Gedung Usul Hapus Sosial"
        verbose_name_plural = "09 Gedung Usul Hapus Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungSosial(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "09 Usul Hapus Gedung Sosial"
        verbose_name_plural = "09 Usul Hapus Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanSosial(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Kontrak Gedung Sosial"
        verbose_name_plural = "09 Kontrak Gedung Sosial"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanSosial(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Harga Gedung Sosial"
        verbose_name_plural = "09 Harga Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanSosial(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Gedung Penghapusan Sosial"
        verbose_name_plural = "09 Gedung Penghapusan Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanSosial(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Tahun Berkurang Gedung Sosial"
        verbose_name_plural = "09 Tahun Berkurang Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanSosial(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Penghapusan Gedung Sosial"
        verbose_name_plural = "09 Penghapusan Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanSosial(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Asal Gedung Sosial"
        verbose_name_plural = "09 SKPD Asal Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanSosial(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Tujuan Gedung Sosial"
        verbose_name_plural = "09 SKPD Tujuan Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanSosial(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "09 Foto Gedung Sosial"
        verbose_name_plural = "09 Foto Gedung Sosial"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DPMD
##model pada app DPMD
class GedungBangunanDPMD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Gedung DPMD"
        verbose_name_plural = "10 Gedung DPMD"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDPMD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 KDP Gedung DPMD"
        verbose_name_plural = "10 KDP Gedung DPMD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDPMD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Gedung Ruangan DPMD"
        verbose_name_plural = "10 Gedung Ruangan DPMD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDPMD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Gedung Usul Hapus DPMD"
        verbose_name_plural = "10 Gedung Usul Hapus DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDPMD(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "10 Usul Hapus Gedung DPMD"
        verbose_name_plural = "10 Usul Hapus Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDPMD(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Kontrak Gedung DPMD"
        verbose_name_plural = "10 Kontrak Gedung DPMD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDPMD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Harga Gedung DPMD"
        verbose_name_plural = "10 Harga Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDPMD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Gedung Penghapusan DPMD"
        verbose_name_plural = "10 Gedung Penghapusan DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDPMD(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Tahun Berkurang Gedung DPMD"
        verbose_name_plural = "10 Tahun Berkurang Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDPMD(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Penghapusan Gedung DPMD"
        verbose_name_plural = "10 Penghapusan Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDPMD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Asal Gedung DPMD"
        verbose_name_plural = "10 SKPD Asal Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDPMD(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Tujuan Gedung DPMD"
        verbose_name_plural = "10 SKPD Tujuan Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDPMD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "10 Foto Gedung DPMD"
        verbose_name_plural = "10 Foto Gedung DPMD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DPPPA
##model pada app DPPPA
class GedungBangunanDPPPA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Gedung DPPPA"
        verbose_name_plural = "11 Gedung DPPPA"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDPPPA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 KDP Gedung DPPPA"
        verbose_name_plural = "11 KDP Gedung DPPPA"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDPPPA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Gedung Ruangan DPPPA"
        verbose_name_plural = "11 Gedung Ruangan DPPPA"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDPPPA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Gedung Usul Hapus DPPPA"
        verbose_name_plural = "11 Gedung Usul Hapus DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDPPPA(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "11 Usul Hapus Gedung DPPPA"
        verbose_name_plural = "11 Usul Hapus Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDPPPA(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Kontrak Gedung DPPPA"
        verbose_name_plural = "11 Kontrak Gedung DPPPA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDPPPA(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Harga Gedung DPPPA"
        verbose_name_plural = "11 Harga Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDPPPA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Gedung Penghapusan DPPPA"
        verbose_name_plural = "11 Gedung Penghapusan DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDPPPA(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Tahun Berkurang Gedung DPPPA"
        verbose_name_plural = "11 Tahun Berkurang Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDPPPA(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Penghapusan Gedung DPPPA"
        verbose_name_plural = "11 Penghapusan Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDPPPA(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Asal Gedung DPPPA"
        verbose_name_plural = "11 SKPD Asal Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDPPPA(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Tujuan Gedung DPPPA"
        verbose_name_plural = "11 SKPD Tujuan Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDPPPA(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "11 Foto Gedung DPPPA"
        verbose_name_plural = "11 Foto Gedung DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DukCatPil
##model pada app DukCatPil
class GedungBangunanDukCatPil(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Gedung DukCatPil"
        verbose_name_plural = "12 Gedung DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDukCatPil(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 KDP Gedung DukCatPil"
        verbose_name_plural = "12 KDP Gedung DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDukCatPil(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Gedung Ruangan DukCatPil"
        verbose_name_plural = "12 Gedung Ruangan DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDukCatPil(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Gedung Usul Hapus DukCatPil"
        verbose_name_plural = "12 Gedung Usul Hapus DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDukCatPil(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "12 Usul Hapus Gedung DukCatPil"
        verbose_name_plural = "12 Usul Hapus Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDukCatPil(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Kontrak Gedung DukCatPil"
        verbose_name_plural = "12 Kontrak Gedung DukCatPil"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDukCatPil(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Harga Gedung DukCatPil"
        verbose_name_plural = "12 Harga Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDukCatPil(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Gedung Penghapusan DukCatPil"
        verbose_name_plural = "12 Gedung Penghapusan DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDukCatPil(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Tahun Berkurang Gedung DukCatPil"
        verbose_name_plural = "12 Tahun Berkurang Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDukCatPil(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Penghapusan Gedung DukCatPil"
        verbose_name_plural = "12 Penghapusan Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDukCatPil(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Asal Gedung DukCatPil"
        verbose_name_plural = "12 SKPD Asal Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDukCatPil(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Tujuan Gedung DukCatPil"
        verbose_name_plural = "12 SKPD Tujuan Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDukCatPil(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "12 Foto Gedung DukCatPil"
        verbose_name_plural = "12 Foto Gedung DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Pertanian
##model pada app Pertanian
class GedungBangunanPertanian(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Gedung Pertanian"
        verbose_name_plural = "13 Gedung Pertanian"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanPertanian(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 KDP Gedung Pertanian"
        verbose_name_plural = "13 KDP Gedung Pertanian"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganPertanian(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Gedung Ruangan Pertanian"
        verbose_name_plural = "13 Gedung Ruangan Pertanian"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusPertanian(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Gedung Usul Hapus Pertanian"
        verbose_name_plural = "13 Gedung Usul Hapus Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungPertanian(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "13 Usul Hapus Gedung Pertanian"
        verbose_name_plural = "13 Usul Hapus Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanPertanian(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Kontrak Gedung Pertanian"
        verbose_name_plural = "13 Kontrak Gedung Pertanian"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanPertanian(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Harga Gedung Pertanian"
        verbose_name_plural = "13 Harga Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanPertanian(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Gedung Penghapusan Pertanian"
        verbose_name_plural = "13 Gedung Penghapusan Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanPertanian(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Tahun Berkurang Gedung Pertanian"
        verbose_name_plural = "13 Tahun Berkurang Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanPertanian(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Penghapusan Gedung Pertanian"
        verbose_name_plural = "13 Penghapusan Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanPertanian(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Asal Gedung Pertanian"
        verbose_name_plural = "13 SKPD Asal Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanPertanian(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Tujuan Gedung Pertanian"
        verbose_name_plural = "13 SKPD Tujuan Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanPertanian(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "13 Foto Gedung Pertanian"
        verbose_name_plural = "13 Foto Gedung Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Kehutanan
##model pada app Kehutanan
class GedungBangunanKehutanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Gedung Kehutanan"
        verbose_name_plural = "14 Gedung Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanKehutanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 KDP Gedung Kehutanan"
        verbose_name_plural = "14 KDP Gedung Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganKehutanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Gedung Ruangan Kehutanan"
        verbose_name_plural = "14 Gedung Ruangan Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusKehutanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Gedung Usul Hapus Kehutanan"
        verbose_name_plural = "14 Gedung Usul Hapus Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungKehutanan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "14 Usul Hapus Gedung Kehutanan"
        verbose_name_plural = "14 Usul Hapus Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanKehutanan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Kontrak Gedung Kehutanan"
        verbose_name_plural = "14 Kontrak Gedung Kehutanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanKehutanan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Harga Gedung Kehutanan"
        verbose_name_plural = "14 Harga Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanKehutanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Gedung Penghapusan Kehutanan"
        verbose_name_plural = "14 Gedung Penghapusan Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanKehutanan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Tahun Berkurang Gedung Kehutanan"
        verbose_name_plural = "14 Tahun Berkurang Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanKehutanan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Penghapusan Gedung Kehutanan"
        verbose_name_plural = "14 Penghapusan Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanKehutanan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Asal Gedung Kehutanan"
        verbose_name_plural = "14 SKPD Asal Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanKehutanan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Tujuan Gedung Kehutanan"
        verbose_name_plural = "14 SKPD Tujuan Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanKehutanan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "14 Foto Gedung Kehutanan"
        verbose_name_plural = "14 Foto Gedung Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DKP
##model pada app DKP
class GedungBangunanDKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Gedung DKP"
        verbose_name_plural = "15 Gedung DKP"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 KDP Gedung DKP"
        verbose_name_plural = "15 KDP Gedung DKP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Gedung Ruangan DKP"
        verbose_name_plural = "15 Gedung Ruangan DKP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Gedung Usul Hapus DKP"
        verbose_name_plural = "15 Gedung Usul Hapus DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDKP(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "15 Usul Hapus Gedung DKP"
        verbose_name_plural = "15 Usul Hapus Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDKP(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Kontrak Gedung DKP"
        verbose_name_plural = "15 Kontrak Gedung DKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDKP(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Harga Gedung DKP"
        verbose_name_plural = "15 Harga Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Gedung Penghapusan DKP"
        verbose_name_plural = "15 Gedung Penghapusan DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDKP(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Tahun Berkurang Gedung DKP"
        verbose_name_plural = "15 Tahun Berkurang Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDKP(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Penghapusan Gedung DKP"
        verbose_name_plural = "15 Penghapusan Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDKP(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Asal Gedung DKP"
        verbose_name_plural = "15 SKPD Asal Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDKP(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Tujuan Gedung DKP"
        verbose_name_plural = "15 SKPD Tujuan Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDKP(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "15 Foto Gedung DKP"
        verbose_name_plural = "15 Foto Gedung DKP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DKUKMP
##model pada app DKUKMP
class GedungBangunanDKUKMP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Gedung DKUKMP"
        verbose_name_plural = "16 Gedung DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDKUKMP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 KDP Gedung DKUKMP"
        verbose_name_plural = "16 KDP Gedung DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDKUKMP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Gedung Ruangan DKUKMP"
        verbose_name_plural = "16 Gedung Ruangan DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDKUKMP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Gedung Usul Hapus DKUKMP"
        verbose_name_plural = "16 Gedung Usul Hapus DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDKUKMP(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "16 Usul Hapus Gedung DKUKMP"
        verbose_name_plural = "16 Usul Hapus Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDKUKMP(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Kontrak Gedung DKUKMP"
        verbose_name_plural = "16 Kontrak Gedung DKUKMP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDKUKMP(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Harga Gedung DKUKMP"
        verbose_name_plural = "16 Harga Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDKUKMP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Gedung Penghapusan DKUKMP"
        verbose_name_plural = "16 Gedung Penghapusan DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDKUKMP(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Tahun Berkurang Gedung DKUKMP"
        verbose_name_plural = "16 Tahun Berkurang Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDKUKMP(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Penghapusan Gedung DKUKMP"
        verbose_name_plural = "16 Penghapusan Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDKUKMP(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Asal Gedung DKUKMP"
        verbose_name_plural = "16 SKPD Asal Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDKUKMP(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Tujuan Gedung DKUKMP"
        verbose_name_plural = "16 SKPD Tujuan Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDKUKMP(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "16 Foto Gedung DKUKMP"
        verbose_name_plural = "16 Foto Gedung DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Distamben
##model pada app Distamben
class GedungBangunanDistamben(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Gedung Distamben"
        verbose_name_plural = "17 Gedung Distamben"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDistamben(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 KDP Gedung Distamben"
        verbose_name_plural = "17 KDP Gedung Distamben"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDistamben(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Gedung Ruangan Distamben"
        verbose_name_plural = "17 Gedung Ruangan Distamben"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDistamben(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Gedung Usul Hapus Distamben"
        verbose_name_plural = "17 Gedung Usul Hapus Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDistamben(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "17 Usul Hapus Gedung Distamben"
        verbose_name_plural = "17 Usul Hapus Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDistamben(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Kontrak Gedung Distamben"
        verbose_name_plural = "17 Kontrak Gedung Distamben"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDistamben(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Harga Gedung Distamben"
        verbose_name_plural = "17 Harga Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDistamben(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Gedung Penghapusan Distamben"
        verbose_name_plural = "17 Gedung Penghapusan Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDistamben(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Tahun Berkurang Gedung Distamben"
        verbose_name_plural = "17 Tahun Berkurang Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDistamben(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Penghapusan Gedung Distamben"
        verbose_name_plural = "17 Penghapusan Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDistamben(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Asal Gedung Distamben"
        verbose_name_plural = "17 SKPD Asal Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDistamben(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Tujuan Gedung Distamben"
        verbose_name_plural = "17 SKPD Tujuan Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDistamben(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "17 Foto Gedung Distamben"
        verbose_name_plural = "17 Foto Gedung Distamben"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DPMPTSP
##model pada app DPMPTSP
class GedungBangunanDPMPTSP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Gedung DPMPTSP"
        verbose_name_plural = "18 Gedung DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDPMPTSP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 KDP Gedung DPMPTSP"
        verbose_name_plural = "18 KDP Gedung DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDPMPTSP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Gedung Ruangan DPMPTSP"
        verbose_name_plural = "18 Gedung Ruangan DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDPMPTSP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Gedung Usul Hapus DPMPTSP"
        verbose_name_plural = "18 Gedung Usul Hapus DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDPMPTSP(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "18 Usul Hapus Gedung DPMPTSP"
        verbose_name_plural = "18 Usul Hapus Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDPMPTSP(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Kontrak Gedung DPMPTSP"
        verbose_name_plural = "18 Kontrak Gedung DPMPTSP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDPMPTSP(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Harga Gedung DPMPTSP"
        verbose_name_plural = "18 Harga Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDPMPTSP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Gedung Penghapusan DPMPTSP"
        verbose_name_plural = "18 Gedung Penghapusan DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDPMPTSP(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Tahun Berkurang Gedung DPMPTSP"
        verbose_name_plural = "18 Tahun Berkurang Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDPMPTSP(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Penghapusan Gedung DPMPTSP"
        verbose_name_plural = "18 Penghapusan Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDPMPTSP(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Asal Gedung DPMPTSP"
        verbose_name_plural = "18 SKPD Asal Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDPMPTSP(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Tujuan Gedung DPMPTSP"
        verbose_name_plural = "18 SKPD Tujuan Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDPMPTSP(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "18 Foto Gedung DPMPTSP"
        verbose_name_plural = "18 Foto Gedung DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##BKD
##model pada app BKD
class GedungBangunanBKD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Gedung BKD"
        verbose_name_plural = "19 Gedung BKD"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBKD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 KDP Gedung BKD"
        verbose_name_plural = "19 KDP Gedung BKD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBKD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Gedung Ruangan BKD"
        verbose_name_plural = "19 Gedung Ruangan BKD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBKD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Gedung Usul Hapus BKD"
        verbose_name_plural = "19 Gedung Usul Hapus BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBKD(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "19 Usul Hapus Gedung BKD"
        verbose_name_plural = "19 Usul Hapus Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBKD(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Kontrak Gedung BKD"
        verbose_name_plural = "19 Kontrak Gedung BKD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBKD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Harga Gedung BKD"
        verbose_name_plural = "19 Harga Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBKD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Gedung Penghapusan BKD"
        verbose_name_plural = "19 Gedung Penghapusan BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBKD(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Tahun Berkurang Gedung BKD"
        verbose_name_plural = "19 Tahun Berkurang Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBKD(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Penghapusan Gedung BKD"
        verbose_name_plural = "19 Penghapusan Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBKD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Asal Gedung BKD"
        verbose_name_plural = "19 SKPD Asal Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBKD(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Tujuan Gedung BKD"
        verbose_name_plural = "19 SKPD Tujuan Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBKD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "19 Foto Gedung BKD"
        verbose_name_plural = "19 Foto Gedung BKD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Inspektorat
##model pada app Inspektorat
class GedungBangunanInspektorat(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Gedung Inspektorat"
        verbose_name_plural = "20 Gedung Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanInspektorat(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 KDP Gedung Inspektorat"
        verbose_name_plural = "20 KDP Gedung Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganInspektorat(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Gedung Ruangan Inspektorat"
        verbose_name_plural = "20 Gedung Ruangan Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusInspektorat(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Gedung Usul Hapus Inspektorat"
        verbose_name_plural = "20 Gedung Usul Hapus Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungInspektorat(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "20 Usul Hapus Gedung Inspektorat"
        verbose_name_plural = "20 Usul Hapus Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanInspektorat(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Kontrak Gedung Inspektorat"
        verbose_name_plural = "20 Kontrak Gedung Inspektorat"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanInspektorat(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Harga Gedung Inspektorat"
        verbose_name_plural = "20 Harga Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanInspektorat(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Gedung Penghapusan Inspektorat"
        verbose_name_plural = "20 Gedung Penghapusan Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanInspektorat(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Tahun Berkurang Gedung Inspektorat"
        verbose_name_plural = "20 Tahun Berkurang Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanInspektorat(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Penghapusan Gedung Inspektorat"
        verbose_name_plural = "20 Penghapusan Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanInspektorat(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Asal Gedung Inspektorat"
        verbose_name_plural = "20 SKPD Asal Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanInspektorat(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Tujuan Gedung Inspektorat"
        verbose_name_plural = "20 SKPD Tujuan Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanInspektorat(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "20 Foto Gedung Inspektorat"
        verbose_name_plural = "20 Foto Gedung Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##BAPPEDA
##model pada app BAPPEDA
class GedungBangunanBAPPEDA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Gedung BAPPEDA"
        verbose_name_plural = "21 Gedung BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBAPPEDA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 KDP Gedung BAPPEDA"
        verbose_name_plural = "21 KDP Gedung BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBAPPEDA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Gedung Ruangan BAPPEDA"
        verbose_name_plural = "21 Gedung Ruangan BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBAPPEDA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Gedung Usul Hapus BAPPEDA"
        verbose_name_plural = "21 Gedung Usul Hapus BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBAPPEDA(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "21 Usul Hapus Gedung BAPPEDA"
        verbose_name_plural = "21 Usul Hapus Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBAPPEDA(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Kontrak Gedung BAPPEDA"
        verbose_name_plural = "21 Kontrak Gedung BAPPEDA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBAPPEDA(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Harga Gedung BAPPEDA"
        verbose_name_plural = "21 Harga Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBAPPEDA(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Gedung Penghapusan BAPPEDA"
        verbose_name_plural = "21 Gedung Penghapusan BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBAPPEDA(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Tahun Berkurang Gedung BAPPEDA"
        verbose_name_plural = "21 Tahun Berkurang Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBAPPEDA(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Penghapusan Gedung BAPPEDA"
        verbose_name_plural = "21 Penghapusan Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBAPPEDA(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Asal Gedung BAPPEDA"
        verbose_name_plural = "21 SKPD Asal Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBAPPEDA(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Tujuan Gedung BAPPEDA"
        verbose_name_plural = "21 SKPD Tujuan Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBAPPEDA(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "21 Foto Gedung BAPPEDA"
        verbose_name_plural = "21 Foto Gedung BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DLH
##model pada app DLH
class GedungBangunanDLH(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Gedung DLH"
        verbose_name_plural = "22 Gedung DLH"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDLH(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 KDP Gedung DLH"
        verbose_name_plural = "22 KDP Gedung DLH"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDLH(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Gedung Ruangan DLH"
        verbose_name_plural = "22 Gedung Ruangan DLH"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDLH(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Gedung Usul Hapus DLH"
        verbose_name_plural = "22 Gedung Usul Hapus DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDLH(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "22 Usul Hapus Gedung DLH"
        verbose_name_plural = "22 Usul Hapus Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDLH(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Kontrak Gedung DLH"
        verbose_name_plural = "22 Kontrak Gedung DLH"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDLH(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Harga Gedung DLH"
        verbose_name_plural = "22 Harga Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDLH(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Gedung Penghapusan DLH"
        verbose_name_plural = "22 Gedung Penghapusan DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDLH(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Tahun Berkurang Gedung DLH"
        verbose_name_plural = "22 Tahun Berkurang Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDLH(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Penghapusan Gedung DLH"
        verbose_name_plural = "22 Penghapusan Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDLH(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Asal Gedung DLH"
        verbose_name_plural = "22 SKPD Asal Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDLH(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Tujuan Gedung DLH"
        verbose_name_plural = "22 SKPD Tujuan Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDLH(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "22 Foto Gedung DLH"
        verbose_name_plural = "22 Foto Gedung DLH"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DKO
##model pada app DKO
class GedungBangunanDKO(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Gedung DKO"
        verbose_name_plural = "23 Gedung DKO"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDKO(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 KDP Gedung DKO"
        verbose_name_plural = "23 KDP Gedung DKO"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDKO(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Gedung Ruangan DKO"
        verbose_name_plural = "23 Gedung Ruangan DKO"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDKO(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Gedung Usul Hapus DKO"
        verbose_name_plural = "23 Gedung Usul Hapus DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDKO(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "23 Usul Hapus Gedung DKO"
        verbose_name_plural = "23 Usul Hapus Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDKO(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Kontrak Gedung DKO"
        verbose_name_plural = "23 Kontrak Gedung DKO"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDKO(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Harga Gedung DKO"
        verbose_name_plural = "23 Harga Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDKO(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Gedung Penghapusan DKO"
        verbose_name_plural = "23 Gedung Penghapusan DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDKO(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Tahun Berkurang Gedung DKO"
        verbose_name_plural = "23 Tahun Berkurang Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDKO(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Penghapusan Gedung DKO"
        verbose_name_plural = "23 Penghapusan Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDKO(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Asal Gedung DKO"
        verbose_name_plural = "23 SKPD Asal Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDKO(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Tujuan Gedung DKO"
        verbose_name_plural = "23 SKPD Tujuan Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDKO(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "23 Foto Gedung DKO"
        verbose_name_plural = "23 Foto Gedung DKO"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##KESBANGPOL
##model pada app KESBANGPOL
class GedungBangunanKESBANGPOL(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Gedung KESBANGPOL"
        verbose_name_plural = "24 Gedung KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanKESBANGPOL(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 KDP Gedung KESBANGPOL"
        verbose_name_plural = "24 KDP Gedung KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganKESBANGPOL(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Gedung Ruangan KESBANGPOL"
        verbose_name_plural = "24 Gedung Ruangan KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusKESBANGPOL(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Gedung Usul Hapus KESBANGPOL"
        verbose_name_plural = "24 Gedung Usul Hapus KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungKESBANGPOL(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "24 Usul Hapus Gedung KESBANGPOL"
        verbose_name_plural = "24 Usul Hapus Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanKESBANGPOL(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Kontrak Gedung KESBANGPOL"
        verbose_name_plural = "24 Kontrak Gedung KESBANGPOL"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanKESBANGPOL(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Harga Gedung KESBANGPOL"
        verbose_name_plural = "24 Harga Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanKESBANGPOL(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Gedung Penghapusan KESBANGPOL"
        verbose_name_plural = "24 Gedung Penghapusan KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanKESBANGPOL(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Tahun Berkurang Gedung KESBANGPOL"
        verbose_name_plural = "24 Tahun Berkurang Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanKESBANGPOL(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Penghapusan Gedung KESBANGPOL"
        verbose_name_plural = "24 Penghapusan Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanKESBANGPOL(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Asal Gedung KESBANGPOL"
        verbose_name_plural = "24 SKPD Asal Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanKESBANGPOL(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Tujuan Gedung KESBANGPOL"
        verbose_name_plural = "24 SKPD Tujuan Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanKESBANGPOL(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "24 Foto Gedung KESBANGPOL"
        verbose_name_plural = "24 Foto Gedung KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##SATPOLPP
##model pada app SATPOLPP
class GedungBangunanSATPOLPP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Gedung SATPOLPP"
        verbose_name_plural = "25 Gedung SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanSATPOLPP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 KDP Gedung SATPOLPP"
        verbose_name_plural = "25 KDP Gedung SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganSATPOLPP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Gedung Ruangan SATPOLPP"
        verbose_name_plural = "25 Gedung Ruangan SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusSATPOLPP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Gedung Usul Hapus SATPOLPP"
        verbose_name_plural = "25 Gedung Usul Hapus SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungSATPOLPP(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "25 Usul Hapus Gedung SATPOLPP"
        verbose_name_plural = "25 Usul Hapus Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanSATPOLPP(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Kontrak Gedung SATPOLPP"
        verbose_name_plural = "25 Kontrak Gedung SATPOLPP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanSATPOLPP(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Harga Gedung SATPOLPP"
        verbose_name_plural = "25 Harga Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanSATPOLPP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Gedung Penghapusan SATPOLPP"
        verbose_name_plural = "25 Gedung Penghapusan SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanSATPOLPP(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Tahun Berkurang Gedung SATPOLPP"
        verbose_name_plural = "25 Tahun Berkurang Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanSATPOLPP(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Penghapusan Gedung SATPOLPP"
        verbose_name_plural = "25 Penghapusan Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanSATPOLPP(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Asal Gedung SATPOLPP"
        verbose_name_plural = "25 SKPD Asal Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanSATPOLPP(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Tujuan Gedung SATPOLPP"
        verbose_name_plural = "25 SKPD Tujuan Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanSATPOLPP(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "25 Foto Gedung SATPOLPP"
        verbose_name_plural = "25 Foto Gedung SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##BKPPD
##model pada app BKPPD
class GedungBangunanBKPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Gedung BKPPD"
        verbose_name_plural = "26 Gedung BKPPD"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBKPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 KDP Gedung BKPPD"
        verbose_name_plural = "26 KDP Gedung BKPPD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBKPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Gedung Ruangan BKPPD"
        verbose_name_plural = "26 Gedung Ruangan BKPPD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBKPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Gedung Usul Hapus BKPPD"
        verbose_name_plural = "26 Gedung Usul Hapus BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBKPPD(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "26 Usul Hapus Gedung BKPPD"
        verbose_name_plural = "26 Usul Hapus Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBKPPD(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Kontrak Gedung BKPPD"
        verbose_name_plural = "26 Kontrak Gedung BKPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBKPPD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Harga Gedung BKPPD"
        verbose_name_plural = "26 Harga Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBKPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Gedung Penghapusan BKPPD"
        verbose_name_plural = "26 Gedung Penghapusan BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBKPPD(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Tahun Berkurang Gedung BKPPD"
        verbose_name_plural = "26 Tahun Berkurang Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBKPPD(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Penghapusan Gedung BKPPD"
        verbose_name_plural = "26 Penghapusan Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBKPPD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Asal Gedung BKPPD"
        verbose_name_plural = "26 SKPD Asal Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBKPPD(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Tujuan Gedung BKPPD"
        verbose_name_plural = "26 SKPD Tujuan Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBKPPD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "26 Foto Gedung BKPPD"
        verbose_name_plural = "26 Foto Gedung BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##SekretariatKorpri
##model pada app SekretariatKorpri
class GedungBangunanSekretariatKorpri(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Gedung Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanSekretariatKorpri(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 KDP Gedung Sekretariat Korpri"
        verbose_name_plural = "27 KDP Gedung Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganSekretariatKorpri(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Gedung Ruangan Sekretariat Korpri"
        verbose_name_plural = "27 Gedung Ruangan Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusSekretariatKorpri(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Gedung Usul Hapus Sekretariat Korpri"
        verbose_name_plural = "27 Gedung Usul Hapus Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungSekretariatKorpri(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "27 Usul Hapus Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Usul Hapus Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanSekretariatKorpri(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Kontrak Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Kontrak Gedung Sekretariat Korpri"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanSekretariatKorpri(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Harga Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Harga Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanSekretariatKorpri(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Gedung Penghapusan Sekretariat Korpri"
        verbose_name_plural = "27 Gedung Penghapusan Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanSekretariatKorpri(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Tahun Berkurang Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Tahun Berkurang Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanSekretariatKorpri(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Penghapusan Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Penghapusan Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanSekretariatKorpri(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Asal Gedung Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Asal Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanSekretariatKorpri(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Tujuan Gedung Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Tujuan Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanSekretariatKorpri(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "27 Foto Gedung Sekretariat Korpri"
        verbose_name_plural = "27 Foto Gedung Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Paringin
##model pada app Paringin
class GedungBangunanParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Gedung Paringin"
        verbose_name_plural = "28 Gedung Paringin"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 KDP Gedung Paringin"
        verbose_name_plural = "28 KDP Gedung Paringin"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Gedung Ruangan Paringin"
        verbose_name_plural = "28 Gedung Ruangan Paringin"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Gedung Usul Hapus Paringin"
        verbose_name_plural = "28 Gedung Usul Hapus Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungParingin(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "28 Usul Hapus Gedung Paringin"
        verbose_name_plural = "28 Usul Hapus Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanParingin(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Kontrak Gedung Paringin"
        verbose_name_plural = "28 Kontrak Gedung Paringin"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanParingin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Harga Gedung Paringin"
        verbose_name_plural = "28 Harga Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Gedung Penghapusan Paringin"
        verbose_name_plural = "28 Gedung Penghapusan Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanParingin(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Tahun Berkurang Gedung Paringin"
        verbose_name_plural = "28 Tahun Berkurang Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanParingin(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Penghapusan Gedung Paringin"
        verbose_name_plural = "28 Penghapusan Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanParingin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Asal Gedung Paringin"
        verbose_name_plural = "28 SKPD Asal Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanParingin(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Tujuan Gedung Paringin"
        verbose_name_plural = "28 SKPD Tujuan Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanParingin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "28 Foto Gedung Paringin"
        verbose_name_plural = "28 Foto Gedung Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##ParinginKota
##model pada app ParinginKota
class GedungBangunanParinginKota(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Gedung Paringin Kota"
        verbose_name_plural = "29 Gedung Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanParinginKota(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 KDP Gedung Paringin Kota"
        verbose_name_plural = "29 KDP Gedung Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganParinginKota(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Gedung Ruangan Paringin Kota"
        verbose_name_plural = "29 Gedung Ruangan Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusParinginKota(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Gedung Usul Hapus Paringin Kota"
        verbose_name_plural = "29 Gedung Usul Hapus Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungParinginKota(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "29 Usul Hapus Gedung Paringin Kota"
        verbose_name_plural = "29 Usul Hapus Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanParinginKota(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Kontrak Gedung Paringin Kota"
        verbose_name_plural = "29 Kontrak Gedung Paringin Kota"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanParinginKota(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Harga Gedung Paringin Kota"
        verbose_name_plural = "29 Harga Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanParinginKota(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Gedung Penghapusan Paringin Kota"
        verbose_name_plural = "29 Gedung Penghapusan Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanParinginKota(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Tahun Berkurang Gedung Paringin Kota"
        verbose_name_plural = "29 Tahun Berkurang Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanParinginKota(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Penghapusan Gedung Paringin Kota"
        verbose_name_plural = "29 Penghapusan Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanParinginKota(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Asal Gedung Paringin Kota"
        verbose_name_plural = "29 SKPD Asal Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanParinginKota(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Tujuan Gedung Paringin Kota"
        verbose_name_plural = "29 SKPD Tujuan Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanParinginKota(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "29 Foto Gedung Paringin Kota"
        verbose_name_plural = "29 Foto Gedung Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##ParinginTimur
##model pada app ParinginTimur
class GedungBangunanParinginTimur(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Gedung Paringin Timur"
        verbose_name_plural = "30 Gedung Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanParinginTimur(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 KDP Gedung Paringin Timur"
        verbose_name_plural = "30 KDP Gedung Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganParinginTimur(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Gedung Ruangan Paringin Timur"
        verbose_name_plural = "30 Gedung Ruangan Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusParinginTimur(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Gedung Usul Hapus Paringin Timur"
        verbose_name_plural = "30 Gedung Usul Hapus Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungParinginTimur(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "30 Usul Hapus Gedung Paringin Timur"
        verbose_name_plural = "30 Usul Hapus Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanParinginTimur(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Kontrak Gedung Paringin Timur"
        verbose_name_plural = "30 Kontrak Gedung Paringin Timur"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanParinginTimur(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Harga Gedung Paringin Timur"
        verbose_name_plural = "30 Harga Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanParinginTimur(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Gedung Penghapusan Paringin Timur"
        verbose_name_plural = "30 Gedung Penghapusan Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanParinginTimur(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Tahun Berkurang Gedung Paringin Timur"
        verbose_name_plural = "30 Tahun Berkurang Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanParinginTimur(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Penghapusan Gedung Paringin Timur"
        verbose_name_plural = "30 Penghapusan Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanParinginTimur(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Asal Gedung Paringin Timur"
        verbose_name_plural = "30 SKPD Asal Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanParinginTimur(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Tujuan Gedung Paringin Timur"
        verbose_name_plural = "30 SKPD Tujuan Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanParinginTimur(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "30 Foto Gedung Paringin Timur"
        verbose_name_plural = "30 Foto Gedung Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Lampihong
##model pada app Lampihong
class GedungBangunanLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Gedung Lampihong"
        verbose_name_plural = "31 Gedung Lampihong"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 KDP Gedung Lampihong"
        verbose_name_plural = "31 KDP Gedung Lampihong"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Gedung Ruangan Lampihong"
        verbose_name_plural = "31 Gedung Ruangan Lampihong"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Gedung Usul Hapus Lampihong"
        verbose_name_plural = "31 Gedung Usul Hapus Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungLampihong(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "31 Usul Hapus Gedung Lampihong"
        verbose_name_plural = "31 Usul Hapus Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanLampihong(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Kontrak Gedung Lampihong"
        verbose_name_plural = "31 Kontrak Gedung Lampihong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanLampihong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Harga Gedung Lampihong"
        verbose_name_plural = "31 Harga Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Gedung Penghapusan Lampihong"
        verbose_name_plural = "31 Gedung Penghapusan Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanLampihong(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Tahun Berkurang Gedung Lampihong"
        verbose_name_plural = "31 Tahun Berkurang Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanLampihong(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Penghapusan Gedung Lampihong"
        verbose_name_plural = "31 Penghapusan Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanLampihong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Asal Gedung Lampihong"
        verbose_name_plural = "31 SKPD Asal Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanLampihong(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Tujuan Gedung Lampihong"
        verbose_name_plural = "31 SKPD Tujuan Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanLampihong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "31 Foto Gedung Lampihong"
        verbose_name_plural = "31 Foto Gedung Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Batumandi
##model pada app Batumandi
class GedungBangunanBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Gedung Batumandi"
        verbose_name_plural = "32 Gedung Batumandi"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 KDP Gedung Batumandi"
        verbose_name_plural = "32 KDP Gedung Batumandi"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Gedung Ruangan Batumandi"
        verbose_name_plural = "32 Gedung Ruangan Batumandi"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Gedung Usul Hapus Batumandi"
        verbose_name_plural = "32 Gedung Usul Hapus Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBatumandi(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "32 Usul Hapus Gedung Batumandi"
        verbose_name_plural = "32 Usul Hapus Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBatumandi(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Kontrak Gedung Batumandi"
        verbose_name_plural = "32 Kontrak Gedung Batumandi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBatumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Harga Gedung Batumandi"
        verbose_name_plural = "32 Harga Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Gedung Penghapusan Batumandi"
        verbose_name_plural = "32 Gedung Penghapusan Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBatumandi(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Tahun Berkurang Gedung Batumandi"
        verbose_name_plural = "32 Tahun Berkurang Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBatumandi(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Penghapusan Gedung Batumandi"
        verbose_name_plural = "32 Penghapusan Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBatumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Asal Gedung Batumandi"
        verbose_name_plural = "32 SKPD Asal Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBatumandi(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Tujuan Gedung Batumandi"
        verbose_name_plural = "32 SKPD Tujuan Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBatumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "32 Foto Gedung Batumandi"
        verbose_name_plural = "32 Foto Gedung Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Juai
##model pada app Juai
class GedungBangunanJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Gedung Juai"
        verbose_name_plural = "33 Gedung Juai"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 KDP Gedung Juai"
        verbose_name_plural = "33 KDP Gedung Juai"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Gedung Ruangan Juai"
        verbose_name_plural = "33 Gedung Ruangan Juai"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Gedung Usul Hapus Juai"
        verbose_name_plural = "33 Gedung Usul Hapus Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungJuai(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "33 Usul Hapus Gedung Juai"
        verbose_name_plural = "33 Usul Hapus Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanJuai(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Kontrak Gedung Juai"
        verbose_name_plural = "33 Kontrak Gedung Juai"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanJuai(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Harga Gedung Juai"
        verbose_name_plural = "33 Harga Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Gedung Penghapusan Juai"
        verbose_name_plural = "33 Gedung Penghapusan Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanJuai(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Tahun Berkurang Gedung Juai"
        verbose_name_plural = "33 Tahun Berkurang Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanJuai(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Penghapusan Gedung Juai"
        verbose_name_plural = "33 Penghapusan Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanJuai(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Asal Gedung Juai"
        verbose_name_plural = "33 SKPD Asal Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanJuai(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Tujuan Gedung Juai"
        verbose_name_plural = "33 SKPD Tujuan Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanJuai(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "33 Foto Gedung Juai"
        verbose_name_plural = "33 Foto Gedung Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Awayan
##model pada app Awayan
class GedungBangunanAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Gedung Awayan"
        verbose_name_plural = "34 Gedung Awayan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 KDP Gedung Awayan"
        verbose_name_plural = "34 KDP Gedung Awayan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Gedung Ruangan Awayan"
        verbose_name_plural = "34 Gedung Ruangan Awayan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Gedung Usul Hapus Awayan"
        verbose_name_plural = "34 Gedung Usul Hapus Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungAwayan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "34 Usul Hapus Gedung Awayan"
        verbose_name_plural = "34 Usul Hapus Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanAwayan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Kontrak Gedung Awayan"
        verbose_name_plural = "34 Kontrak Gedung Awayan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanAwayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Harga Gedung Awayan"
        verbose_name_plural = "34 Harga Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Gedung Penghapusan Awayan"
        verbose_name_plural = "34 Gedung Penghapusan Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanAwayan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Tahun Berkurang Gedung Awayan"
        verbose_name_plural = "34 Tahun Berkurang Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanAwayan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Penghapusan Gedung Awayan"
        verbose_name_plural = "34 Penghapusan Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanAwayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Asal Gedung Awayan"
        verbose_name_plural = "34 SKPD Asal Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanAwayan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Tujuan Gedung Awayan"
        verbose_name_plural = "34 SKPD Tujuan Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanAwayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "34 Foto Gedung Awayan"
        verbose_name_plural = "34 Foto Gedung Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Halong
##model pada app Halong
class GedungBangunanHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Gedung Halong"
        verbose_name_plural = "35 Gedung Halong"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 KDP Gedung Halong"
        verbose_name_plural = "35 KDP Gedung Halong"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Gedung Ruangan Halong"
        verbose_name_plural = "35 Gedung Ruangan Halong"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Gedung Usul Hapus Halong"
        verbose_name_plural = "35 Gedung Usul Hapus Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungHalong(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "35 Usul Hapus Gedung Halong"
        verbose_name_plural = "35 Usul Hapus Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanHalong(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Kontrak Gedung Halong"
        verbose_name_plural = "35 Kontrak Gedung Halong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanHalong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Harga Gedung Halong"
        verbose_name_plural = "35 Harga Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Gedung Penghapusan Halong"
        verbose_name_plural = "35 Gedung Penghapusan Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanHalong(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Tahun Berkurang Gedung Halong"
        verbose_name_plural = "35 Tahun Berkurang Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanHalong(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Penghapusan Gedung Halong"
        verbose_name_plural = "35 Penghapusan Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanHalong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Asal Gedung Halong"
        verbose_name_plural = "35 SKPD Asal Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanHalong(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Tujuan Gedung Halong"
        verbose_name_plural = "35 SKPD Tujuan Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanHalong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "35 Foto Gedung Halong"
        verbose_name_plural = "35 Foto Gedung Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##ParinginSelatan
##model pada app ParinginSelatan
class GedungBangunanParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Gedung Paringin Selatan"
        verbose_name_plural = "36 Gedung Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 KDP Gedung Paringin Selatan"
        verbose_name_plural = "36 KDP Gedung Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Gedung Ruangan Paringin Selatan"
        verbose_name_plural = "36 Gedung Ruangan Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Gedung Usul Hapus Paringin Selatan"
        verbose_name_plural = "36 Gedung Usul Hapus Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungParinginSelatan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "36 Usul Hapus Gedung Paringin Selatan"
        verbose_name_plural = "36 Usul Hapus Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanParinginSelatan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Kontrak Gedung Paringin Selatan"
        verbose_name_plural = "36 Kontrak Gedung Paringin Selatan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanParinginSelatan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Harga Gedung Paringin Selatan"
        verbose_name_plural = "36 Harga Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Gedung Penghapusan Paringin Selatan"
        verbose_name_plural = "36 Gedung Penghapusan Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanParinginSelatan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Tahun Berkurang Gedung Paringin Selatan"
        verbose_name_plural = "36 Tahun Berkurang Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanParinginSelatan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Penghapusan Gedung Paringin Selatan"
        verbose_name_plural = "36 Penghapusan Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanParinginSelatan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Asal Gedung Paringin Selatan"
        verbose_name_plural = "36 SKPD Asal Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanParinginSelatan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Tujuan Gedung Paringin Selatan"
        verbose_name_plural = "36 SKPD Tujuan Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanParinginSelatan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "36 Foto Gedung Paringin Selatan"
        verbose_name_plural = "36 Foto Gedung Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##BatuPiring
##model pada app BatuPiring
class GedungBangunanBatuPiring(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Gedung Batu Piring"
        verbose_name_plural = "37 Gedung Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBatuPiring(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 KDP Gedung Batu Piring"
        verbose_name_plural = "37 KDP Gedung Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBatuPiring(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Gedung Ruangan Batu Piring"
        verbose_name_plural = "37 Gedung Ruangan Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBatuPiring(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Gedung Usul Hapus Batu Piring"
        verbose_name_plural = "37 Gedung Usul Hapus Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBatuPiring(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "37 Usul Hapus Gedung Batu Piring"
        verbose_name_plural = "37 Usul Hapus Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBatuPiring(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Kontrak Gedung Batu Piring"
        verbose_name_plural = "37 Kontrak Gedung Batu Piring"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBatuPiring(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Harga Gedung Batu Piring"
        verbose_name_plural = "37 Harga Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBatuPiring(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Gedung Penghapusan Batu Piring"
        verbose_name_plural = "37 Gedung Penghapusan Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBatuPiring(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Tahun Berkurang Gedung Batu Piring"
        verbose_name_plural = "37 Tahun Berkurang Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBatuPiring(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Penghapusan Gedung Batu Piring"
        verbose_name_plural = "37 Penghapusan Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBatuPiring(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Asal Gedung Batu Piring"
        verbose_name_plural = "37 SKPD Asal Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBatuPiring(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Tujuan Gedung Batu Piring"
        verbose_name_plural = "37 SKPD Tujuan Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBatuPiring(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "37 Foto Gedung Batu Piring"
        verbose_name_plural = "37 Foto Gedung Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##TebingTinggi
##model pada app TebingTinggi
class GedungBangunanTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Gedung Tebing Tinggi"
        verbose_name_plural = "38 Gedung Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 KDP Gedung Tebing Tinggi"
        verbose_name_plural = "38 KDP Gedung Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Gedung Ruangan Tebing Tinggi"
        verbose_name_plural = "38 Gedung Ruangan Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Gedung Usul Hapus Tebing Tinggi"
        verbose_name_plural = "38 Gedung Usul Hapus Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungTebingTinggi(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "38 Usul Hapus Gedung Tebing Tinggi"
        verbose_name_plural = "38 Usul Hapus Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanTebingTinggi(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Kontrak Gedung Tebing Tinggi"
        verbose_name_plural = "38 Kontrak Gedung Tebing Tinggi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanTebingTinggi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Harga Gedung Tebing Tinggi"
        verbose_name_plural = "38 Harga Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Gedung Penghapusan Tebing Tinggi"
        verbose_name_plural = "38 Gedung Penghapusan Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanTebingTinggi(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Tahun Berkurang Gedung Tebing Tinggi"
        verbose_name_plural = "38 Tahun Berkurang Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanTebingTinggi(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Penghapusan Gedung Tebing Tinggi"
        verbose_name_plural = "38 Penghapusan Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanTebingTinggi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Asal Gedung Tebing Tinggi"
        verbose_name_plural = "38 SKPD Asal Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanTebingTinggi(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Tujuan Gedung Tebing Tinggi"
        verbose_name_plural = "38 SKPD Tujuan Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanTebingTinggi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "38 Foto Gedung Tebing Tinggi"
        verbose_name_plural = "38 Foto Gedung Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##BPBD
##model pada app BPBD
class GedungBangunanBPBD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Gedung BPBD"
        verbose_name_plural = "39 Gedung BPBD"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBPBD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 KDP Gedung BPBD"
        verbose_name_plural = "39 KDP Gedung BPBD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBPBD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Gedung Ruangan BPBD"
        verbose_name_plural = "39 Gedung Ruangan BPBD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBPBD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Gedung Usul Hapus BPBD"
        verbose_name_plural = "39 Gedung Usul Hapus BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBPBD(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "39 Usul Hapus Gedung BPBD"
        verbose_name_plural = "39 Usul Hapus Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBPBD(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Kontrak Gedung BPBD"
        verbose_name_plural = "39 Kontrak Gedung BPBD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBPBD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Harga Gedung BPBD"
        verbose_name_plural = "39 Harga Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBPBD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Gedung Penghapusan BPBD"
        verbose_name_plural = "39 Gedung Penghapusan BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBPBD(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Tahun Berkurang Gedung BPBD"
        verbose_name_plural = "39 Tahun Berkurang Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBPBD(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Penghapusan Gedung BPBD"
        verbose_name_plural = "39 Penghapusan Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBPBD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Asal Gedung BPBD"
        verbose_name_plural = "39 SKPD Asal Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBPBD(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Tujuan Gedung BPBD"
        verbose_name_plural = "39 SKPD Tujuan Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBPBD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "39 Foto Gedung BPBD"
        verbose_name_plural = "39 Foto Gedung BPBD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DPKP
##model pada app DPKP
class GedungBangunanDPKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Gedung DPKP"
        verbose_name_plural = "40 Gedung DPKP"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDPKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 KDP Gedung DPKP"
        verbose_name_plural = "40 KDP Gedung DPKP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDPKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Gedung Ruangan DPKP"
        verbose_name_plural = "40 Gedung Ruangan DPKP"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDPKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Gedung Usul Hapus DPKP"
        verbose_name_plural = "40 Gedung Usul Hapus DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDPKP(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "40 Usul Hapus Gedung DPKP"
        verbose_name_plural = "40 Usul Hapus Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDPKP(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Kontrak Gedung DPKP"
        verbose_name_plural = "40 Kontrak Gedung DPKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDPKP(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Harga Gedung DPKP"
        verbose_name_plural = "40 Harga Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDPKP(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Gedung Penghapusan DPKP"
        verbose_name_plural = "40 Gedung Penghapusan DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDPKP(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Tahun Berkurang Gedung DPKP"
        verbose_name_plural = "40 Tahun Berkurang Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDPKP(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Penghapusan Gedung DPKP"
        verbose_name_plural = "40 Penghapusan Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDPKP(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Asal Gedung DPKP"
        verbose_name_plural = "40 SKPD Asal Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDPKP(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Tujuan Gedung DPKP"
        verbose_name_plural = "40 SKPD Tujuan Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDPKP(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "40 Foto Gedung DPKP"
        verbose_name_plural = "40 Foto Gedung DPKP"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Disnakertrans
##model pada app Disnakertrans
class GedungBangunanDisnakertrans(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Gedung Disnakertrans"
        verbose_name_plural = "41 Gedung Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDisnakertrans(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 KDP Gedung Disnakertrans"
        verbose_name_plural = "41 KDP Gedung Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDisnakertrans(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Gedung Ruangan Disnakertrans"
        verbose_name_plural = "41 Gedung Ruangan Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDisnakertrans(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Gedung Usul Hapus Disnakertrans"
        verbose_name_plural = "41 Gedung Usul Hapus Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDisnakertrans(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "41 Usul Hapus Gedung Disnakertrans"
        verbose_name_plural = "41 Usul Hapus Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDisnakertrans(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Kontrak Gedung Disnakertrans"
        verbose_name_plural = "41 Kontrak Gedung Disnakertrans"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDisnakertrans(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Harga Gedung Disnakertrans"
        verbose_name_plural = "41 Harga Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDisnakertrans(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Gedung Penghapusan Disnakertrans"
        verbose_name_plural = "41 Gedung Penghapusan Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDisnakertrans(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Tahun Berkurang Gedung Disnakertrans"
        verbose_name_plural = "41 Tahun Berkurang Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDisnakertrans(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Penghapusan Gedung Disnakertrans"
        verbose_name_plural = "41 Penghapusan Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDisnakertrans(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Asal Gedung Disnakertrans"
        verbose_name_plural = "41 SKPD Asal Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDisnakertrans(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Tujuan Gedung Disnakertrans"
        verbose_name_plural = "41 SKPD Tujuan Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisnakertrans(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "41 Foto Gedung Disnakertrans"
        verbose_name_plural = "41 Foto Gedung Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##DPPKB
##model pada app DPPKB
class GedungBangunanDPPKB(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Gedung DPPKB"
        verbose_name_plural = "42 Gedung DPPKB"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanDPPKB(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 KDP Gedung DPPKB"
        verbose_name_plural = "42 KDP Gedung DPPKB"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganDPPKB(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Gedung Ruangan DPPKB"
        verbose_name_plural = "42 Gedung Ruangan DPPKB"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusDPPKB(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Gedung Usul Hapus DPPKB"
        verbose_name_plural = "42 Gedung Usul Hapus DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungDPPKB(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "42 Usul Hapus Gedung DPPKB"
        verbose_name_plural = "42 Usul Hapus Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanDPPKB(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Kontrak Gedung DPPKB"
        verbose_name_plural = "42 Kontrak Gedung DPPKB"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanDPPKB(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Harga Gedung DPPKB"
        verbose_name_plural = "42 Harga Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanDPPKB(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Gedung Penghapusan DPPKB"
        verbose_name_plural = "42 Gedung Penghapusan DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanDPPKB(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Tahun Berkurang Gedung DPPKB"
        verbose_name_plural = "42 Tahun Berkurang Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanDPPKB(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Penghapusan Gedung DPPKB"
        verbose_name_plural = "42 Penghapusan Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanDPPKB(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Asal Gedung DPPKB"
        verbose_name_plural = "42 SKPD Asal Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanDPPKB(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Tujuan Gedung DPPKB"
        verbose_name_plural = "42 SKPD Tujuan Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDPPKB(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "42 Foto Gedung DPPKB"
        verbose_name_plural = "42 Foto Gedung DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Kominfo
##model pada app Kominfo
class GedungBangunanKominfo(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Gedung Kominfo"
        verbose_name_plural = "43 Gedung Kominfo"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanKominfo(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 KDP Gedung Kominfo"
        verbose_name_plural = "43 KDP Gedung Kominfo"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganKominfo(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Gedung Ruangan Kominfo"
        verbose_name_plural = "43 Gedung Ruangan Kominfo"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusKominfo(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Gedung Usul Hapus Kominfo"
        verbose_name_plural = "43 Gedung Usul Hapus Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungKominfo(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "43 Usul Hapus Gedung Kominfo"
        verbose_name_plural = "43 Usul Hapus Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanKominfo(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Kontrak Gedung Kominfo"
        verbose_name_plural = "43 Kontrak Gedung Kominfo"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanKominfo(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Harga Gedung Kominfo"
        verbose_name_plural = "43 Harga Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanKominfo(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Gedung Penghapusan Kominfo"
        verbose_name_plural = "43 Gedung Penghapusan Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanKominfo(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Tahun Berkurang Gedung Kominfo"
        verbose_name_plural = "43 Tahun Berkurang Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanKominfo(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Penghapusan Gedung Kominfo"
        verbose_name_plural = "43 Penghapusan Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanKominfo(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Asal Gedung Kominfo"
        verbose_name_plural = "43 SKPD Asal Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanKominfo(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Tujuan Gedung Kominfo"
        verbose_name_plural = "43 SKPD Tujuan Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanKominfo(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "43 Foto Gedung Kominfo"
        verbose_name_plural = "43 Foto Gedung Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Kearsipan
##model pada app Kearsipan
class GedungBangunanKearsipan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Gedung Kearsipan"
        verbose_name_plural = "44 Gedung Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanKearsipan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 KDP Gedung Kearsipan"
        verbose_name_plural = "44 KDP Gedung Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganKearsipan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Gedung Ruangan Kearsipan"
        verbose_name_plural = "44 Gedung Ruangan Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusKearsipan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Gedung Usul Hapus Kearsipan"
        verbose_name_plural = "44 Gedung Usul Hapus Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungKearsipan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "44 Usul Hapus Gedung Kearsipan"
        verbose_name_plural = "44 Usul Hapus Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanKearsipan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Kontrak Gedung Kearsipan"
        verbose_name_plural = "44 Kontrak Gedung Kearsipan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanKearsipan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Harga Gedung Kearsipan"
        verbose_name_plural = "44 Harga Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanKearsipan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Gedung Penghapusan Kearsipan"
        verbose_name_plural = "44 Gedung Penghapusan Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanKearsipan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Tahun Berkurang Gedung Kearsipan"
        verbose_name_plural = "44 Tahun Berkurang Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanKearsipan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Penghapusan Gedung Kearsipan"
        verbose_name_plural = "44 Penghapusan Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanKearsipan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Asal Gedung Kearsipan"
        verbose_name_plural = "44 SKPD Asal Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanKearsipan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Tujuan Gedung Kearsipan"
        verbose_name_plural = "44 SKPD Tujuan Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanKearsipan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "44 Foto Gedung Kearsipan"
        verbose_name_plural = "44 Foto Gedung Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Perikanan
##model pada app Perikanan
class GedungBangunanPerikanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Gedung Perikanan"
        verbose_name_plural = "45 Gedung Perikanan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanPerikanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 KDP Gedung Perikanan"
        verbose_name_plural = "45 KDP Gedung Perikanan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganPerikanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Gedung Ruangan Perikanan"
        verbose_name_plural = "45 Gedung Ruangan Perikanan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusPerikanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Gedung Usul Hapus Perikanan"
        verbose_name_plural = "45 Gedung Usul Hapus Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungPerikanan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "45 Usul Hapus Gedung Perikanan"
        verbose_name_plural = "45 Usul Hapus Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanPerikanan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Kontrak Gedung Perikanan"
        verbose_name_plural = "45 Kontrak Gedung Perikanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanPerikanan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Harga Gedung Perikanan"
        verbose_name_plural = "45 Harga Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanPerikanan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Gedung Penghapusan Perikanan"
        verbose_name_plural = "45 Gedung Penghapusan Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanPerikanan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Tahun Berkurang Gedung Perikanan"
        verbose_name_plural = "45 Tahun Berkurang Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanPerikanan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Penghapusan Gedung Perikanan"
        verbose_name_plural = "45 Penghapusan Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanPerikanan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Asal Gedung Perikanan"
        verbose_name_plural = "45 SKPD Asal Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanPerikanan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Tujuan Gedung Perikanan"
        verbose_name_plural = "45 SKPD Tujuan Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanPerikanan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "45 Foto Gedung Perikanan"
        verbose_name_plural = "45 Foto Gedung Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Pariwisata
##model pada app Pariwisata
class GedungBangunanPariwisata(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Gedung Pariwisata"
        verbose_name_plural = "46 Gedung Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanPariwisata(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 KDP Gedung Pariwisata"
        verbose_name_plural = "46 KDP Gedung Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganPariwisata(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Gedung Ruangan Pariwisata"
        verbose_name_plural = "46 Gedung Ruangan Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusPariwisata(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Gedung Usul Hapus Pariwisata"
        verbose_name_plural = "46 Gedung Usul Hapus Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungPariwisata(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "46 Usul Hapus Gedung Pariwisata"
        verbose_name_plural = "46 Usul Hapus Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanPariwisata(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Kontrak Gedung Pariwisata"
        verbose_name_plural = "46 Kontrak Gedung Pariwisata"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanPariwisata(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Harga Gedung Pariwisata"
        verbose_name_plural = "46 Harga Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanPariwisata(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Gedung Penghapusan Pariwisata"
        verbose_name_plural = "46 Gedung Penghapusan Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanPariwisata(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Tahun Berkurang Gedung Pariwisata"
        verbose_name_plural = "46 Tahun Berkurang Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanPariwisata(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Penghapusan Gedung Pariwisata"
        verbose_name_plural = "46 Penghapusan Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanPariwisata(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Asal Gedung Pariwisata"
        verbose_name_plural = "46 SKPD Asal Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanPariwisata(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Tujuan Gedung Pariwisata"
        verbose_name_plural = "46 SKPD Tujuan Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanPariwisata(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "46 Foto Gedung Pariwisata"
        verbose_name_plural = "46 Foto Gedung Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##Perdagangan
##model pada app Perdagangan
class GedungBangunanPerdagangan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Gedung Perdagangan"
        verbose_name_plural = "47 Gedung Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanPerdagangan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 KDP Gedung Perdagangan"
        verbose_name_plural = "47 KDP Gedung Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganPerdagangan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Gedung Ruangan Perdagangan"
        verbose_name_plural = "47 Gedung Ruangan Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusPerdagangan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Gedung Usul Hapus Perdagangan"
        verbose_name_plural = "47 Gedung Usul Hapus Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungPerdagangan(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "47 Usul Hapus Gedung Perdagangan"
        verbose_name_plural = "47 Usul Hapus Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanPerdagangan(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Kontrak Gedung Perdagangan"
        verbose_name_plural = "47 Kontrak Gedung Perdagangan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanPerdagangan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Harga Gedung Perdagangan"
        verbose_name_plural = "47 Harga Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanPerdagangan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Gedung Penghapusan Perdagangan"
        verbose_name_plural = "47 Gedung Penghapusan Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanPerdagangan(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Tahun Berkurang Gedung Perdagangan"
        verbose_name_plural = "47 Tahun Berkurang Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanPerdagangan(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Penghapusan Gedung Perdagangan"
        verbose_name_plural = "47 Penghapusan Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanPerdagangan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Asal Gedung Perdagangan"
        verbose_name_plural = "47 SKPD Asal Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanPerdagangan(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Tujuan Gedung Perdagangan"
        verbose_name_plural = "47 SKPD Tujuan Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanPerdagangan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "47 Foto Gedung Perdagangan"
        verbose_name_plural = "47 Foto Gedung Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



##BPPD
##model pada app BPPD
class GedungBangunanBPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Gedung BPPD"
        verbose_name_plural = "48 Gedung BPPD"

    def __unicode__(self):
        return self.nama_barang


class KDPGedungBangunanBPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 KDP Gedung BPPD"
        verbose_name_plural = "48 KDP Gedung BPPD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanRuanganBPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Gedung Ruangan BPPD"
        verbose_name_plural = "48 Gedung Ruangan BPPD"

    def __unicode__(self):
        return self.nama_barang


class GedungBangunanUsulHapusBPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Gedung Usul Hapus BPPD"
        verbose_name_plural = "48 Gedung Usul Hapus BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusGedungBPPD(TahunBerkurangUsulHapusGedung):
    class Meta:
        proxy = True
        verbose_name = "48 Usul Hapus Gedung BPPD"
        verbose_name_plural = "48 Usul Hapus Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakGedungBangunanBPPD(KontrakGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Kontrak Gedung BPPD"
        verbose_name_plural = "48 Kontrak Gedung BPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaGedungBangunanBPPD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Harga Gedung BPPD"
        verbose_name_plural = "48 Harga Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)




class GedungBangunanPenghapusanBPPD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Gedung Penghapusan BPPD"
        verbose_name_plural = "48 Gedung Penghapusan BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangGedungBangunanBPPD(TahunBerkurangGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Tahun Berkurang Gedung BPPD"
        verbose_name_plural = "48 Tahun Berkurang Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanGedungBangunanBPPD(PenghapusanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Penghapusan Gedung BPPD"
        verbose_name_plural = "48 Penghapusan Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalGedungBangunanBPPD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Asal Gedung BPPD"
        verbose_name_plural = "48 SKPD Asal Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanGedungBangunanBPPD(SKPDTujuanGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Tujuan Gedung BPPD"
        verbose_name_plural = "48 SKPD Tujuan Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanBPPD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "48 Foto Gedung BPPD"
        verbose_name_plural = "48 Foto Gedung BPPD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 1 Awayan

class GedungBangunanDisdikSMPN1Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Gedung Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN1Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN1Awayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN1Awayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN1Awayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 1 Batumandi

class GedungBangunanDisdikSMPN1Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Gedung Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN1Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN1Batumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN1Batumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN1Batumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 1 Halong

class GedungBangunanDisdikSMPN1Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Gedung Disdik SMPN 1 Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN1Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 1 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN1Halong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN1Halong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 1 Halong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN1Halong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 1 Juai

class GedungBangunanDisdikSMPN1Juai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Gedung Disdik SMPN 1 Juai"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN1Juai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 1 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN1Juai(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN1Juai(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 1 Juai"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN1Juai(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 1 Lampihong

class GedungBangunanDisdikSMPN1Lampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Gedung Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN1Lampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN1Lampihong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN1Lampihong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN1Lampihong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 1 Paringin

class GedungBangunanDisdikSMPN1Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Gedung Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN1Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN1Paringin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN1Paringin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN1Paringin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 2 Awayan

class GedungBangunanDisdikSMPN2Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Gedung Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN2Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN2Awayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN2Awayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN2Awayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 2 Batumandi

class GedungBangunanDisdikSMPN2Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Gedung Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN2Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN2Batumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN2Batumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN2Batumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 2 Halong

class GedungBangunanDisdikSMPN2Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Gedung Disdik SMPN 2 Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN2Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 2 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN2Halong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN2Halong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 2 Halong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN2Halong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 2 Juai

class GedungBangunanDisdikSMPN2Juai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Gedung Disdik SMPN 2 Juai"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN2Juai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 2 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN2Juai(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN2Juai(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 2 Juai"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN2Juai(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 2 Lampihong

class GedungBangunanDisdikSMPN2Lampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Gedung Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN2Lampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN2Lampihong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN2Lampihong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN2Lampihong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 2 Paringin

class GedungBangunanDisdikSMPN2Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Gedung Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN2Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN2Paringin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN2Paringin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN2Paringin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 3 Awayan

class GedungBangunanDisdikSMPN3Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Gedung Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN3Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN3Awayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN3Awayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN3Awayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 3 Batumandi

class GedungBangunanDisdikSMPN3Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Gedung Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN3Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN3Batumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN3Batumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN3Batumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 3 Halong

class GedungBangunanDisdikSMPN3Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Gedung Disdik SMPN 3 Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN3Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 3 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN3Halong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN3Halong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 3 Halong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN3Halong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 3 Paringin

class GedungBangunanDisdikSMPN3Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Gedung Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN3Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN3Paringin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN3Paringin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN3Paringin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 4 Awayan

class GedungBangunanDisdikSMPN4Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Gedung Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN4Awayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN4Awayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN4Awayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN4Awayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 4 Batumandi

class GedungBangunanDisdikSMPN4Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Gedung Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN4Batumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN4Batumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN4Batumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN4Batumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 4 Halong

class GedungBangunanDisdikSMPN4Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Gedung Disdik SMPN 4 Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN4Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 4 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN4Halong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN4Halong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 4 Halong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN4Halong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 4 Paringin

class GedungBangunanDisdikSMPN4Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Gedung Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN4Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN4Paringin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN4Paringin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN4Paringin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 5 Halong

class GedungBangunanDisdikSMPN5Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Gedung Disdik SMPN 5 Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN5Halong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 5 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN5Halong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN5Halong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 5 Halong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN5Halong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik SMPN 5 Paringin

class GedungBangunanDisdikSMPN5Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Gedung Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikSMPN5Paringin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Gedung Ruangan Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikSMPN5Paringin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Harga Gedung Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikSMPN5Paringin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikSMPN5Paringin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Foto Gedung Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Paringin

class GedungBangunanDinkesParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Paringin"
        verbose_name_plural = "05 Gedung Dinkes Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Paringin"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesParingin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Paringin"
        verbose_name_plural = "05 Harga Gedung Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesParingin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Paringin"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesParingin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Paringin"
        verbose_name_plural = "05 Foto Gedung Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Lampihong

class GedungBangunanDinkesLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Lampihong"
        verbose_name_plural = "05 Gedung Dinkes Lampihong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Lampihong"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesLampihong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Lampihong"
        verbose_name_plural = "05 Harga Gedung Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesLampihong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Lampihong"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesLampihong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Lampihong"
        verbose_name_plural = "05 Foto Gedung Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Batumandi

class GedungBangunanDinkesBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Batumandi"
        verbose_name_plural = "05 Gedung Dinkes Batumandi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Batumandi"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesBatumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Batumandi"
        verbose_name_plural = "05 Harga Gedung Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesBatumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Batumandi"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesBatumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Batumandi"
        verbose_name_plural = "05 Foto Gedung Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Awayan

class GedungBangunanDinkesAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Awayan"
        verbose_name_plural = "05 Gedung Dinkes Awayan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Awayan"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesAwayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Awayan"
        verbose_name_plural = "05 Harga Gedung Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesAwayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Awayan"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesAwayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Awayan"
        verbose_name_plural = "05 Foto Gedung Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Juai

class GedungBangunanDinkesJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Juai"
        verbose_name_plural = "05 Gedung Dinkes Juai"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Juai"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesJuai(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Juai"
        verbose_name_plural = "05 Harga Gedung Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesJuai(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Juai"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesJuai(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Juai"
        verbose_name_plural = "05 Foto Gedung Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Halong

class GedungBangunanDinkesHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Halong"
        verbose_name_plural = "05 Gedung Dinkes Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Halong"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesHalong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Halong"
        verbose_name_plural = "05 Harga Gedung Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesHalong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Halong"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesHalong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Halong"
        verbose_name_plural = "05 Foto Gedung Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Lokbatu

class GedungBangunanDinkesLokbatu(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Lokbatu"
        verbose_name_plural = "05 Gedung Dinkes Lokbatu"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesLokbatu(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Lokbatu"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Lokbatu"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesLokbatu(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Lokbatu"
        verbose_name_plural = "05 Harga Gedung Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesLokbatu(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Lokbatu"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesLokbatu(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Lokbatu"
        verbose_name_plural = "05 Foto Gedung Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Uren

class GedungBangunanDinkesUren(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Uren"
        verbose_name_plural = "05 Gedung Dinkes Uren"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesUren(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Uren"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Uren"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesUren(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Uren"
        verbose_name_plural = "05 Harga Gedung Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesUren(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Uren"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesUren(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Uren"
        verbose_name_plural = "05 Foto Gedung Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Pirsus

class GedungBangunanDinkesPirsus(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Pirsus"
        verbose_name_plural = "05 Gedung Dinkes Pirsus"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesPirsus(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Pirsus"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Pirsus"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesPirsus(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Pirsus"
        verbose_name_plural = "05 Harga Gedung Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesPirsus(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Pirsus"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesPirsus(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Pirsus"
        verbose_name_plural = "05 Foto Gedung Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Paringin Selatan

class GedungBangunanDinkesParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Paringin Selatan"
        verbose_name_plural = "05 Gedung Dinkes Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Paringin Selatan"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesParinginSelatan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Paringin Selatan"
        verbose_name_plural = "05 Harga Gedung Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesParinginSelatan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Paringin Selatan"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesParinginSelatan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Paringin Selatan"
        verbose_name_plural = "05 Foto Gedung Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Tebing Tinggi

class GedungBangunanDinkesTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Gedung Dinkes Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesTebingTinggi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Harga Gedung Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesTebingTinggi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Tebing Tinggi"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesTebingTinggi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Foto Gedung Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Tanah Habang

class GedungBangunanDinkesTanahHabang(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Tanah Habang"
        verbose_name_plural = "05 Gedung Dinkes Tanah Habang"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesTanahHabang(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Tanah Habang"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Tanah Habang"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesTanahHabang(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Tanah Habang"
        verbose_name_plural = "05 Harga Gedung Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesTanahHabang(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Tanah Habang"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesTanahHabang(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Tanah Habang"
        verbose_name_plural = "05 Foto Gedung Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes RSUD

class GedungBangunanDinkesRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes RSUD"
        verbose_name_plural = "05 Gedung Dinkes RSUD"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesRSUD(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes RSUD"
        verbose_name_plural = "05 Gedung Ruangan Dinkes RSUD"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesRSUD(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes RSUD"
        verbose_name_plural = "05 Harga Gedung Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesRSUD(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes RSUD"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesRSUD(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes RSUD"
        verbose_name_plural = "05 Foto Gedung Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Paringin

class GedungBangunanDisdikParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Paringin"
        verbose_name_plural = "07 Gedung Disdik Paringin"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikParingin(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Paringin"
        verbose_name_plural = "07 Gedung Ruangan Disdik Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikParingin(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Paringin"
        verbose_name_plural = "07 Harga Gedung Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikParingin(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Paringin"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikParingin(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Paringin"
        verbose_name_plural = "07 Foto Gedung Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Lampihong

class GedungBangunanDisdikLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Lampihong"
        verbose_name_plural = "07 Gedung Disdik Lampihong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikLampihong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Lampihong"
        verbose_name_plural = "07 Gedung Ruangan Disdik Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikLampihong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Lampihong"
        verbose_name_plural = "07 Harga Gedung Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikLampihong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Lampihong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikLampihong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Lampihong"
        verbose_name_plural = "07 Foto Gedung Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Awayan

class GedungBangunanDisdikAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Awayan"
        verbose_name_plural = "07 Gedung Disdik Awayan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikAwayan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Awayan"
        verbose_name_plural = "07 Gedung Ruangan Disdik Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikAwayan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Awayan"
        verbose_name_plural = "07 Harga Gedung Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikAwayan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Awayan"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikAwayan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Awayan"
        verbose_name_plural = "07 Foto Gedung Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Batumandi

class GedungBangunanDisdikBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Batumandi"
        verbose_name_plural = "07 Gedung Disdik Batumandi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikBatumandi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Batumandi"
        verbose_name_plural = "07 Gedung Ruangan Disdik Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikBatumandi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Batumandi"
        verbose_name_plural = "07 Harga Gedung Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikBatumandi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Batumandi"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikBatumandi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Batumandi"
        verbose_name_plural = "07 Foto Gedung Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Juai

class GedungBangunanDisdikJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Juai"
        verbose_name_plural = "07 Gedung Disdik Juai"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikJuai(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Juai"
        verbose_name_plural = "07 Gedung Ruangan Disdik Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikJuai(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Juai"
        verbose_name_plural = "07 Harga Gedung Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikJuai(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Juai"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikJuai(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Juai"
        verbose_name_plural = "07 Foto Gedung Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Halong

class GedungBangunanDisdikHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Halong"
        verbose_name_plural = "07 Gedung Disdik Halong"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikHalong(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Halong"
        verbose_name_plural = "07 Gedung Ruangan Disdik Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikHalong(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Halong"
        verbose_name_plural = "07 Harga Gedung Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikHalong(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Halong"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikHalong(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Halong"
        verbose_name_plural = "07 Foto Gedung Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Tebing Tinggi

class GedungBangunanDisdikTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Tebing Tinggi"
        verbose_name_plural = "07 Gedung Disdik Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikTebingTinggi(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Tebing Tinggi"
        verbose_name_plural = "07 Gedung Ruangan Disdik Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikTebingTinggi(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Tebing Tinggi"
        verbose_name_plural = "07 Harga Gedung Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikTebingTinggi(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Tebing Tinggi"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikTebingTinggi(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Tebing Tinggi"
        verbose_name_plural = "07 Foto Gedung Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Paringin Selatan

class GedungBangunanDisdikParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Paringin Selatan"
        verbose_name_plural = "07 Gedung Disdik Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikParinginSelatan(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Paringin Selatan"
        verbose_name_plural = "07 Gedung Ruangan Disdik Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikParinginSelatan(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Paringin Selatan"
        verbose_name_plural = "07 Harga Gedung Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikParinginSelatan(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Paringin Selatan"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikParinginSelatan(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Paringin Selatan"
        verbose_name_plural = "07 Foto Gedung Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Disdik Kantor

class GedungBangunanDisdikKantor(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Disdik Kantor"
        verbose_name_plural = "07 Gedung Disdik Kantor"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDisdikKantor(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Gedung Ruangan Disdik Kantor"
        verbose_name_plural = "07 Gedung Ruangan Disdik Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDisdikKantor(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Gedung Disdik Kantor"
        verbose_name_plural = "07 Harga Gedung Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDisdikKantor(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Gedung Disdik Kantor"
        verbose_name_plural = "07 SKPD Asal Gedung Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDisdikKantor(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Gedung Disdik Kantor"
        verbose_name_plural = "07 Foto Gedung Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



#Dinkes Kantor

class GedungBangunanDinkesKantor(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Dinkes Kantor"
        verbose_name_plural = "05 Gedung Dinkes Kantor"

    def __unicode__(self):
        return self.nama_barang



class GedungBangunanRuanganDinkesKantor(GedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Gedung Ruangan Dinkes Kantor"
        verbose_name_plural = "05 Gedung Ruangan Dinkes Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaGedungBangunanDinkesKantor(HargaGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Gedung Dinkes Kantor"
        verbose_name_plural = "05 Harga Gedung Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



class SKPDAsalGedungBangunanDinkesKantor(SKPDAsalGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Gedung Dinkes Kantor"
        verbose_name_plural = "05 SKPD Asal Gedung Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoGedungBangunanDinkesKantor(FotoGedungBangunan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Gedung Dinkes Kantor"
        verbose_name_plural = "05 Foto Gedung Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_gedung_bangunan)



