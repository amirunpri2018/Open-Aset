from django.db import models


### Table Umum yang digunakan pada semua KIB

class Provinsi(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    kode_provinsi = models.CharField("Kode Provinsi", max_length=20,
                    db_column="kode_provinsi")
    nama_provinsi = models.CharField("Nama Provinsi", max_length=200,
                    db_column="nama_provinsi")

    class Meta:
        db_table = "provinsi"
        verbose_name = "Provinsi"
        verbose_name_plural = "Provinsi"

    def __unicode__(self):
        return self.nama_provinsi


class Kabupaten(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_provinsi = models.ForeignKey(Provinsi, verbose_name="Provinsi",
                    db_column="id_provinsi")
    kode_kabupaten = models.CharField("Kode Kabupaten", max_length=20,
                    db_column="kode_kabupaten")
    nama_kabupaten = models.CharField("Nama Kabupaten", max_length=200,
                    db_column="nama_kabupaten")

    class Meta:
        db_table = "kabupaten"
        verbose_name = "Kabupaten"
        verbose_name_plural = "Kabupaten"

    def __unicode__(self):
        return self.nama_kabupaten


class LokasiBidang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_kabupaten = models.ForeignKey(Kabupaten, verbose_name="Kabupaten",
                    db_column="id_kabupaten")
    kode_lokasi_bidang = models.CharField("Kode Lokasi Bidang", max_length=20,
                    db_column="kode_lokasi_bidang")
    nama_lokasi_bidang = models.CharField("Nama Lokasi Bidang", max_length=200,
                    db_column="nama_lokasi_bidang")

    class Meta:
        db_table = "lokasi_bidang"
        verbose_name = "Lokasi Bidang"
        verbose_name_plural = "Lokasi Bidang"

    def __unicode__(self):
        return "%s  %s" % (self.kode_lokasi_bidang, self.nama_lokasi_bidang)


class SKPD(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_lokasi_bidang = models.ForeignKey(LokasiBidang,
                    verbose_name="Lokasi Bidang",
                    db_column="id_lokasi_bidang")
    kode_skpd = models.CharField("Kode SKPD", max_length=20,
                    db_column="kode_skpd")
    nama_skpd = models.CharField("Nama SKPD", max_length=200,
                    db_column="nama_skpd")

    class Meta:
        db_table = "skpd"
        verbose_name = "SKPD"
        verbose_name_plural = "SKPD"

    def __unicode__(self):
        return self.nama_skpd


class SUBSKPD(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")
    kode_sub_skpd = models.CharField("Kode SUB SKPD", max_length=20,
                    db_column="kode_sub_skpd")
    nama_sub_skpd = models.CharField("Nama SUB SKPD", max_length=200,
                    db_column="nama_sub_skpd")

    class Meta:
        db_table = "sub_skpd"
        verbose_name = "SUB SKPD"
        verbose_name_plural = "SUB SKPD"
        ordering = ['id',]

    def __unicode__(self):
        return self.nama_sub_skpd


class KodeBarang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    kode_barang = models.CharField("Kode Barang", max_length=200,
                    db_column="kode_barang", unique=True)
    umur = models.IntegerField("Umur",
                    default=0,
                    db_column="umur")

    class Meta:
        db_table = "kode_barang"
        verbose_name = "Kode Barang"
        verbose_name_plural = "Kode Barang"

    def __unicode__(self):
        return self.kode_barang




class SatuanBarang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    satuan_barang = models.CharField("Satuan Barang", max_length=100,
                    db_column="satuan_barang", unique=True)

    class Meta:
        db_table = "satuan_barang"
        verbose_name = "Satuan Barang"
        verbose_name_plural = "Satuan Barang"

    def __unicode__(self):
        return self.satuan_barang


class KeadaanBarang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    keadaan_barang = models.CharField("Keadaan Barang", max_length=100,
                    db_column="keadaan_barang", unique=True)

    class Meta:
        db_table = "keadaan_barang"
        verbose_name = "Keadaan Barang"
        verbose_name_plural = "Keadaan Barang"

    def __unicode__(self):
        return self.keadaan_barang


class SKPenghapusan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    tanggal_sk_penghapusan = models.DateField("Tanggal SK Penghapusan",
                    db_column="tanggal_sk_penghapusan")
    nomor_sk_penghapusan = models.CharField("Nomor SK Penghapusan",
                    max_length=100,
                    db_column="nomor_sk_penghapusan")

    class Meta:
        db_table = "sk_penghapusan"
        verbose_name = "SK Penghapusan"
        verbose_name_plural = "SK Penghapusan"

    def __unicode__(self):
        return "tanggal: %s  nomor:%s" % (self.tanggal_sk_penghapusan, self.nomor_sk_penghapusan)


class MutasiBerkurang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    mutasi_berkurang = models.CharField("Mutasi Berkurang", max_length=100,
                    db_column="mutasi_berkurang", unique=True)

    class Meta:
        db_table = "mutasi_berkurang"
        verbose_name = "Mutasi Berkurang"
        verbose_name_plural = "Mutasi Berkurang"

    def __unicode__(self):
        return self.mutasi_berkurang

class JenisPemanfaatan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    jenis_pemanfaatan = models.CharField("Jenis Pemanfaatan", max_length=100,
                    db_column="jenis_pemanfaatan", unique=True)

    class Meta:
        db_table = "jenis_pemanfaatan"
        verbose_name = "Jenis Pemanfaatan"
        verbose_name_plural = "Jenis Pemanfaatan"

    def __unicode__(self):
        return self.jenis_pemanfaatan


class AsalUsul(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    asal_usul = models.CharField("Asal Usul", max_length=100,
                    db_column="asal_usul", unique=True)

    class Meta:
        db_table = "asal_usul"
        verbose_name = "Asal Usul"
        verbose_name_plural = "Asal Usul"

    def __unicode__(self):
        return self.asal_usul


class Tahun(models.Model):
    tahun = models.IntegerField(primary_key=True, db_column="tahun")

    class Meta:
        db_table = "tahun"
        verbose_name = "Tahun"
        verbose_name_plural = "Tahun"
        ordering = ['tahun']

    def __unicode__(self):
        return "%i" % (self.tahun)


class GolonganBarang(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    golongan_barang = models.CharField("Golongan Barang", max_length=100,
                    db_column="golongan_barang", unique=True)

    class Meta:
        db_table = "golongan_barang"
        verbose_name = "Golongan Barang"
        verbose_name_plural = "Golongan Barang"

    def __unicode__(self):
        return self.golongan_barang




### Kumpulan Table KIB A Tanah

class HakTanah(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    hak_tanah = models.CharField("Hak Tanah", max_length=100,
                    db_column="hak_tanah", unique=True)

    class Meta:
        db_table = "hak_tanah"
        verbose_name = "Hak Tanah"
        verbose_name_plural = "Hak Tanah"

    def __unicode__(self):
        return self.hak_tanah


class Tanah(models.Model):
    id = models.AutoField(primary_key=True,
                    verbose_name="Register",
                    db_column="id")
    id_sub_skpd = models.ForeignKey(SUBSKPD,
                    verbose_name="SUB SKPD",
                    db_column="id_sub_skpd")
    id_golongan_barang = models.ForeignKey(GolonganBarang,
                    verbose_name="Golongan Barang",
                    default=1,
                    db_column="id_golongan_barang")
    nama_barang = models.CharField("Nama Barang",
                    max_length=300,
                    db_column="nama_barang")
    id_kode_barang = models.ForeignKey(KodeBarang,
                    verbose_name="Kode Barang",
                    limit_choices_to = {'id__lt': 386},
                    db_column="id_kode_barang")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun Awal",
                    help_text="Tahun Awal Kapitalisasi",
                    db_column="tahun")
    letak_alamat = models.CharField("Letak Alamat",
                    max_length=300,
                    null=True, blank=True,
                    db_column="letak_alamat")
    id_hak_tanah = models.ForeignKey(HakTanah,
                    verbose_name="Hak Tanah",
                    db_column="id_hak_tanah")
    tanggal_sertifikat = models.DateField("Tanggal Sertifikat",
                    null=True, blank=True,
                    db_column="tanggal_sertifikat")
    nomor_sertifikat = models.CharField("Nomor Sertifikat",
                    max_length=100,
                    null=True, blank=True,
                    db_column="nomor_sertifikat")
    penggunaan = models.CharField("Penggunaan",
                    max_length=300,
                    null=True, blank=True,
                    db_column="penggunaan")
    banyak_barang = models.IntegerField("Banyak Barang",
                    default=1,
                    db_column="banyak_barang")
    id_keadaan_barang = models.ForeignKey(KeadaanBarang,
                    default=1,
                    verbose_name="Keadaan Barang",
                    db_column="id_keadaan_barang")
    id_satuan_barang = models.ForeignKey(SatuanBarang,
                    verbose_name="Satuan Barang",
                    db_column="id_satuan_barang")
    id_mutasi_berkurang = models.ForeignKey(MutasiBerkurang,
                    default=5,
                    verbose_name="Mutasi Berkurang",
                    db_column="id_mutasi_berkurang")
    keterangan = models.TextField("Keterangan",
                    null=True, blank=True,
                    db_column="keterangan")

    class Meta:
        db_table = "tanah"
        verbose_name = "Tanah"
        verbose_name_plural = "Tanah"

    def __unicode__(self):
        return self.nama_barang


#untuk menanmpung inline PenghapusanTanah
class TanahPenghapusan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "Tanah Penghapusan"
        verbose_name_plural = "Tanah Penghapusan"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline TahunBerkurangUsulHapusTanah
class TanahUsulHapus(Tanah):
    class Meta:
        proxy = True
        verbose_name = "Tanah Usul Hapus"
        verbose_name_plural = "Tanah Usul Hapus"

    def __unicode__(self):
        return self.nama_barang



#untuk menanmpung inline PemanfaatanTanah
class TanahPemanfaatan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "Tanah Pemanfaatan"
        verbose_name_plural = "Tanah Pemanfaatan"

    def __unicode__(self):
        return self.nama_barang


class KontrakTanah(models.Model):
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
        db_table = "kontrak_tanah"
	verbose_name = "Kontrak Tanah"
        verbose_name_plural = "Kontrak Tanah"

    def __unicode__(self):
        return self.nomor_sp2d


class TahunBerkurangTanah(models.Model):
    id = models.OneToOneField(Tanah, primary_key=True,
                    db_column="id_tanah")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_tanah"
	verbose_name = "Tahun Berkurang Tanah"
        verbose_name_plural = "Tahun Berkurang Tanah"

    def __unicode__(self):
        return "%s" % (self.id)




class TahunBerkurangUsulHapusTanah(models.Model):
    id = models.OneToOneField(Tanah, primary_key=True,
                    db_column="id_tanah")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_usul_hapus_tanah"
	verbose_name = "Tahun Berkurang Usul Hapus Tanah"
        verbose_name_plural = "Tahun Berkurang Usul Hapus Tanah"

    def __unicode__(self):
        return "%s" % (self.id)




class PenghapusanTanah(models.Model):
    id = models.OneToOneField(Tanah, primary_key=True,
                    db_column="id_tanah")
    id_sk_penghapusan = models.ForeignKey(SKPenghapusan,
                    verbose_name="SK Penghapusan",
                    db_column="id_sk_penghapusan")

    class Meta:
        db_table = "penghapusan_tanah"
	verbose_name = "Penghapusan Tanah"
        verbose_name_plural = "Penghapusan Tanah"

    def __unicode__(self):
        return "%s" % (self.id)


class PemanfaatanTanah(models.Model):
    id = models.OneToOneField(Tanah, primary_key=True,
                    db_column="id_tanah")
    id_jenis_pemanfaatan = models.ForeignKey(JenisPemanfaatan,
                    verbose_name="Jenis Pemanfaatan",
                    db_column="id_jenis_pemanfaatan")

    class Meta:
        db_table = "pemanfaatan_tanah"
	verbose_name = "Pemanfaatan Tanah"
        verbose_name_plural = "Pemanfaatan Tanah"

    def __unicode__(self):
        return "%s" % (self.id)


class HargaTanah(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_tanah = models.ForeignKey(Tanah,
                    verbose_name="Tanah",
                    db_column="id_tanah")
    luas = models.IntegerField("Luas",
                    default=0,
                    db_column="luas")
    id_asal_usul = models.ForeignKey(AsalUsul,
                    verbose_name="Asal Usul",
                    db_column="id_asal_usul")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun",
                    help_text="Tahun Anggaran",
                    db_column="tahun")
    id_kontrak = models.ForeignKey(KontrakTanah,
                    verbose_name="Kontrak Tanah",
                    db_column="id_kontrak")
    harga_bertambah = models.DecimalField("Harga Bertambah",
                    max_digits=15, decimal_places=0, default=0,
                    db_column="harga_bertambah")
    harga_berkurang = models.DecimalField("Harga Berkurang",
                    max_digits=15, decimal_places=0, default=0,
                    db_column="harga_berkurang")
    catatan = models.CharField("Catatan",
                    max_length=100,
                    help_text="Catatan pada Daftar Pengadaan",
                    db_column="catatan")
    tahun_mutasi = models.ForeignKey(Tahun,
                    verbose_name="Tahun Mutasi",
                    null=True, blank=True,
                    related_name='+',
                    help_text="Tahun Mutasi",
                    db_column="tahun_mutasi")

    class Meta:
        db_table = "harga_tanah"
	verbose_name = "Harga Tanah"
        verbose_name_plural = "Harga Tanah"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



#TanahReklas, untuk melakukan mutasi Antar SKPD
class TanahReklas(Tanah):
    class Meta:
        proxy = True
        verbose_name = "Tanah Reklas"
        verbose_name_plural = "Tanah Reklas"

    def __unicode__(self):
        return self.nama_barang



class SKPDAsalTanah(models.Model):
    id = models.OneToOneField(Tanah, primary_key=True,
                    db_column="id_tanah")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_asal_tanah"
	verbose_name = "SKPD Asal Tanah"
        verbose_name_plural = "SKPD Asal Tanah"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanah(models.Model):
    id = models.OneToOneField(Tanah, primary_key=True,
                    db_column="id_tanah")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_tujuan_tanah"
	verbose_name = "SKPD Tujuan Tanah"
        verbose_name_plural = "SKPD Tujuan Tanah"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanah(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_tanah = models.ForeignKey(Tanah,
                    verbose_name="Tanah",
                    db_column="id_tanah")
    foto = models.FileField("Foto",
                    upload_to='tanah/',
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
        db_table = "foto_tanah"
	verbose_name = "Foto Tanah"
        verbose_name_plural = "Foto Tanah"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



##Setwan
##model pada app Setwan
class TanahSetwan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "01 Tanah Setwan"
        verbose_name_plural = "01 Tanah Setwan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusSetwan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "01 Tanah Usul Hapus Setwan"
        verbose_name_plural = "01 Tanah Usul Hapus Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahSetwan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "01 Usul Hapus Tanah Setwan"
        verbose_name_plural = "01 Usul Hapus Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahSetwan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "01 Kontrak Tanah Setwan"
        verbose_name_plural = "01 Kontrak Tanah Setwan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahSetwan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "01 Harga Tanah Setwan"
        verbose_name_plural = "01 Harga Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanSetwan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "01 Tanah Penghapusan Setwan"
        verbose_name_plural = "01 Tanah Penghapusan Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahSetwan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "01 Tahun Berkurang Tanah Setwan"
        verbose_name_plural = "01 Tahun Berkurang Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahSetwan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "01 Penghapusan Tanah Setwan"
        verbose_name_plural = "01 Penghapusan Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahSetwan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Asal Tanah Setwan"
        verbose_name_plural = "01 SKPD Asal Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahSetwan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Tujuan Tanah Setwan"
        verbose_name_plural = "01 SKPD Tujuan Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahSetwan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "01 Foto Tanah Setwan"
        verbose_name_plural = "01 Foto Tanah Setwan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Setda
##model pada app Setda
class TanahSetda(Tanah):
    class Meta:
        proxy = True
        verbose_name = "02 Tanah Setda"
        verbose_name_plural = "02 Tanah Setda"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusSetda(Tanah):
    class Meta:
        proxy = True
        verbose_name = "02 Tanah Usul Hapus Setda"
        verbose_name_plural = "02 Tanah Usul Hapus Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahSetda(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "02 Usul Hapus Tanah Setda"
        verbose_name_plural = "02 Usul Hapus Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahSetda(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "02 Kontrak Tanah Setda"
        verbose_name_plural = "02 Kontrak Tanah Setda"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahSetda(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "02 Harga Tanah Setda"
        verbose_name_plural = "02 Harga Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanSetda(Tanah):
    class Meta:
        proxy = True
        verbose_name = "02 Tanah Penghapusan Setda"
        verbose_name_plural = "02 Tanah Penghapusan Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahSetda(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "02 Tahun Berkurang Tanah Setda"
        verbose_name_plural = "02 Tahun Berkurang Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahSetda(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "02 Penghapusan Tanah Setda"
        verbose_name_plural = "02 Penghapusan Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahSetda(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Asal Tanah Setda"
        verbose_name_plural = "02 SKPD Asal Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahSetda(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Tujuan Tanah Setda"
        verbose_name_plural = "02 SKPD Tujuan Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahSetda(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "02 Foto Tanah Setda"
        verbose_name_plural = "02 Foto Tanah Setda"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DPUPR
##model pada app DPUPR
class TanahDPUPR(Tanah):
    class Meta:
        proxy = True
        verbose_name = "03 Tanah DPUPR"
        verbose_name_plural = "03 Tanah DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDPUPR(Tanah):
    class Meta:
        proxy = True
        verbose_name = "03 Tanah Usul Hapus DPUPR"
        verbose_name_plural = "03 Tanah Usul Hapus DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDPUPR(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "03 Usul Hapus Tanah DPUPR"
        verbose_name_plural = "03 Usul Hapus Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDPUPR(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "03 Kontrak Tanah DPUPR"
        verbose_name_plural = "03 Kontrak Tanah DPUPR"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDPUPR(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "03 Harga Tanah DPUPR"
        verbose_name_plural = "03 Harga Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDPUPR(Tanah):
    class Meta:
        proxy = True
        verbose_name = "03 Tanah Penghapusan DPUPR"
        verbose_name_plural = "03 Tanah Penghapusan DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDPUPR(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "03 Tahun Berkurang Tanah DPUPR"
        verbose_name_plural = "03 Tahun Berkurang Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDPUPR(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "03 Penghapusan Tanah DPUPR"
        verbose_name_plural = "03 Penghapusan Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDPUPR(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Asal Tanah DPUPR"
        verbose_name_plural = "03 SKPD Asal Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDPUPR(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Tujuan Tanah DPUPR"
        verbose_name_plural = "03 SKPD Tujuan Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDPUPR(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "03 Foto Tanah DPUPR"
        verbose_name_plural = "03 Foto Tanah DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Dishub
##model pada app Dishub
class TanahDishub(Tanah):
    class Meta:
        proxy = True
        verbose_name = "04 Tanah Dishub"
        verbose_name_plural = "04 Tanah Dishub"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDishub(Tanah):
    class Meta:
        proxy = True
        verbose_name = "04 Tanah Usul Hapus Dishub"
        verbose_name_plural = "04 Tanah Usul Hapus Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDishub(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "04 Usul Hapus Tanah Dishub"
        verbose_name_plural = "04 Usul Hapus Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDishub(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "04 Kontrak Tanah Dishub"
        verbose_name_plural = "04 Kontrak Tanah Dishub"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDishub(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "04 Harga Tanah Dishub"
        verbose_name_plural = "04 Harga Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDishub(Tanah):
    class Meta:
        proxy = True
        verbose_name = "04 Tanah Penghapusan Dishub"
        verbose_name_plural = "04 Tanah Penghapusan Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDishub(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "04 Tahun Berkurang Tanah Dishub"
        verbose_name_plural = "04 Tahun Berkurang Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDishub(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "04 Penghapusan Tanah Dishub"
        verbose_name_plural = "04 Penghapusan Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDishub(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Asal Tanah Dishub"
        verbose_name_plural = "04 SKPD Asal Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDishub(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Tujuan Tanah Dishub"
        verbose_name_plural = "04 SKPD Tujuan Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDishub(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "04 Foto Tanah Dishub"
        verbose_name_plural = "04 Foto Tanah Dishub"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Dinkes
##model pada app Dinkes
class TanahDinkes(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes"
        verbose_name_plural = "05 Tanah Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDinkes(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Usul Hapus Dinkes"
        verbose_name_plural = "05 Tanah Usul Hapus Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDinkes(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Usul Hapus Tanah Dinkes"
        verbose_name_plural = "05 Usul Hapus Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDinkes(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Kontrak Tanah Dinkes"
        verbose_name_plural = "05 Kontrak Tanah Dinkes"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDinkes(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes"
        verbose_name_plural = "05 Harga Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDinkes(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Penghapusan Dinkes"
        verbose_name_plural = "05 Tanah Penghapusan Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDinkes(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tahun Berkurang Tanah Dinkes"
        verbose_name_plural = "05 Tahun Berkurang Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDinkes(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Penghapusan Tanah Dinkes"
        verbose_name_plural = "05 Penghapusan Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDinkes(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDinkes(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Tujuan Tanah Dinkes"
        verbose_name_plural = "05 SKPD Tujuan Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkes(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes"
        verbose_name_plural = "05 Foto Tanah Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##RSUD
##model pada app RSUD
class TanahRSUD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "06 Tanah RSUD"
        verbose_name_plural = "06 Tanah RSUD"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusRSUD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "06 Tanah Usul Hapus RSUD"
        verbose_name_plural = "06 Tanah Usul Hapus RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahRSUD(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "06 Usul Hapus Tanah RSUD"
        verbose_name_plural = "06 Usul Hapus Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahRSUD(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "06 Kontrak Tanah RSUD"
        verbose_name_plural = "06 Kontrak Tanah RSUD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahRSUD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "06 Harga Tanah RSUD"
        verbose_name_plural = "06 Harga Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanRSUD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "06 Tanah Penghapusan RSUD"
        verbose_name_plural = "06 Tanah Penghapusan RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahRSUD(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "06 Tahun Berkurang Tanah RSUD"
        verbose_name_plural = "06 Tahun Berkurang Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahRSUD(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "06 Penghapusan Tanah RSUD"
        verbose_name_plural = "06 Penghapusan Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahRSUD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Asal Tanah RSUD"
        verbose_name_plural = "06 SKPD Asal Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahRSUD(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Tujuan Tanah RSUD"
        verbose_name_plural = "06 SKPD Tujuan Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahRSUD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "06 Foto Tanah RSUD"
        verbose_name_plural = "06 Foto Tanah RSUD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Disdik
##model pada app Disdik
class TanahDisdik(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik"
        verbose_name_plural = "07 Tanah Disdik"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDisdik(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Usul Hapus Disdik"
        verbose_name_plural = "07 Tanah Usul Hapus Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDisdik(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Usul Hapus Tanah Disdik"
        verbose_name_plural = "07 Usul Hapus Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDisdik(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Kontrak Tanah Disdik"
        verbose_name_plural = "07 Kontrak Tanah Disdik"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDisdik(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik"
        verbose_name_plural = "07 Harga Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDisdik(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Penghapusan Disdik"
        verbose_name_plural = "07 Tanah Penghapusan Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDisdik(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tahun Berkurang Tanah Disdik"
        verbose_name_plural = "07 Tahun Berkurang Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDisdik(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Penghapusan Tanah Disdik"
        verbose_name_plural = "07 Penghapusan Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDisdik(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDisdik(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Tujuan Tanah Disdik"
        verbose_name_plural = "07 SKPD Tujuan Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdik(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik"
        verbose_name_plural = "07 Foto Tanah Disdik"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Perpustakaan
##model pada app Perpustakaan
class TanahPerpustakaan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "08 Tanah Perpustakaan"
        verbose_name_plural = "08 Tanah Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusPerpustakaan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "08 Tanah Usul Hapus Perpustakaan"
        verbose_name_plural = "08 Tanah Usul Hapus Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahPerpustakaan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "08 Usul Hapus Tanah Perpustakaan"
        verbose_name_plural = "08 Usul Hapus Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahPerpustakaan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "08 Kontrak Tanah Perpustakaan"
        verbose_name_plural = "08 Kontrak Tanah Perpustakaan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahPerpustakaan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "08 Harga Tanah Perpustakaan"
        verbose_name_plural = "08 Harga Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanPerpustakaan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "08 Tanah Penghapusan Perpustakaan"
        verbose_name_plural = "08 Tanah Penghapusan Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahPerpustakaan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "08 Tahun Berkurang Tanah Perpustakaan"
        verbose_name_plural = "08 Tahun Berkurang Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahPerpustakaan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "08 Penghapusan Tanah Perpustakaan"
        verbose_name_plural = "08 Penghapusan Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahPerpustakaan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Asal Tanah Perpustakaan"
        verbose_name_plural = "08 SKPD Asal Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahPerpustakaan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Tujuan Tanah Perpustakaan"
        verbose_name_plural = "08 SKPD Tujuan Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahPerpustakaan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "08 Foto Tanah Perpustakaan"
        verbose_name_plural = "08 Foto Tanah Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Sosial
##model pada app Sosial
class TanahSosial(Tanah):
    class Meta:
        proxy = True
        verbose_name = "09 Tanah Sosial"
        verbose_name_plural = "09 Tanah Sosial"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusSosial(Tanah):
    class Meta:
        proxy = True
        verbose_name = "09 Tanah Usul Hapus Sosial"
        verbose_name_plural = "09 Tanah Usul Hapus Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahSosial(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "09 Usul Hapus Tanah Sosial"
        verbose_name_plural = "09 Usul Hapus Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahSosial(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "09 Kontrak Tanah Sosial"
        verbose_name_plural = "09 Kontrak Tanah Sosial"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahSosial(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "09 Harga Tanah Sosial"
        verbose_name_plural = "09 Harga Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanSosial(Tanah):
    class Meta:
        proxy = True
        verbose_name = "09 Tanah Penghapusan Sosial"
        verbose_name_plural = "09 Tanah Penghapusan Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahSosial(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "09 Tahun Berkurang Tanah Sosial"
        verbose_name_plural = "09 Tahun Berkurang Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahSosial(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "09 Penghapusan Tanah Sosial"
        verbose_name_plural = "09 Penghapusan Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahSosial(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Asal Tanah Sosial"
        verbose_name_plural = "09 SKPD Asal Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahSosial(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Tujuan Tanah Sosial"
        verbose_name_plural = "09 SKPD Tujuan Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahSosial(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "09 Foto Tanah Sosial"
        verbose_name_plural = "09 Foto Tanah Sosial"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DPMD
##model pada app DPMD
class TanahDPMD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "10 Tanah DPMD"
        verbose_name_plural = "10 Tanah DPMD"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDPMD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "10 Tanah Usul Hapus DPMD"
        verbose_name_plural = "10 Tanah Usul Hapus DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDPMD(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "10 Usul Hapus Tanah DPMD"
        verbose_name_plural = "10 Usul Hapus Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDPMD(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "10 Kontrak Tanah DPMD"
        verbose_name_plural = "10 Kontrak Tanah DPMD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDPMD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "10 Harga Tanah DPMD"
        verbose_name_plural = "10 Harga Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDPMD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "10 Tanah Penghapusan DPMD"
        verbose_name_plural = "10 Tanah Penghapusan DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDPMD(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "10 Tahun Berkurang Tanah DPMD"
        verbose_name_plural = "10 Tahun Berkurang Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDPMD(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "10 Penghapusan Tanah DPMD"
        verbose_name_plural = "10 Penghapusan Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDPMD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Asal Tanah DPMD"
        verbose_name_plural = "10 SKPD Asal Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDPMD(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Tujuan Tanah DPMD"
        verbose_name_plural = "10 SKPD Tujuan Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDPMD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "10 Foto Tanah DPMD"
        verbose_name_plural = "10 Foto Tanah DPMD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DPPPA
##model pada app DPPPA
class TanahDPPPA(Tanah):
    class Meta:
        proxy = True
        verbose_name = "11 Tanah DPPPA"
        verbose_name_plural = "11 Tanah DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDPPPA(Tanah):
    class Meta:
        proxy = True
        verbose_name = "11 Tanah Usul Hapus DPPPA"
        verbose_name_plural = "11 Tanah Usul Hapus DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDPPPA(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "11 Usul Hapus Tanah DPPPA"
        verbose_name_plural = "11 Usul Hapus Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDPPPA(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "11 Kontrak Tanah DPPPA"
        verbose_name_plural = "11 Kontrak Tanah DPPPA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDPPPA(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "11 Harga Tanah DPPPA"
        verbose_name_plural = "11 Harga Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDPPPA(Tanah):
    class Meta:
        proxy = True
        verbose_name = "11 Tanah Penghapusan DPPPA"
        verbose_name_plural = "11 Tanah Penghapusan DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDPPPA(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "11 Tahun Berkurang Tanah DPPPA"
        verbose_name_plural = "11 Tahun Berkurang Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDPPPA(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "11 Penghapusan Tanah DPPPA"
        verbose_name_plural = "11 Penghapusan Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDPPPA(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Asal Tanah DPPPA"
        verbose_name_plural = "11 SKPD Asal Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDPPPA(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Tujuan Tanah DPPPA"
        verbose_name_plural = "11 SKPD Tujuan Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDPPPA(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "11 Foto Tanah DPPPA"
        verbose_name_plural = "11 Foto Tanah DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DukCatPil
##model pada app DukCatPil
class TanahDukCatPil(Tanah):
    class Meta:
        proxy = True
        verbose_name = "12 Tanah DukCatPil"
        verbose_name_plural = "12 Tanah DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDukCatPil(Tanah):
    class Meta:
        proxy = True
        verbose_name = "12 Tanah Usul Hapus DukCatPil"
        verbose_name_plural = "12 Tanah Usul Hapus DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDukCatPil(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "12 Usul Hapus Tanah DukCatPil"
        verbose_name_plural = "12 Usul Hapus Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDukCatPil(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "12 Kontrak Tanah DukCatPil"
        verbose_name_plural = "12 Kontrak Tanah DukCatPil"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDukCatPil(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "12 Harga Tanah DukCatPil"
        verbose_name_plural = "12 Harga Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDukCatPil(Tanah):
    class Meta:
        proxy = True
        verbose_name = "12 Tanah Penghapusan DukCatPil"
        verbose_name_plural = "12 Tanah Penghapusan DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDukCatPil(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "12 Tahun Berkurang Tanah DukCatPil"
        verbose_name_plural = "12 Tahun Berkurang Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDukCatPil(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "12 Penghapusan Tanah DukCatPil"
        verbose_name_plural = "12 Penghapusan Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDukCatPil(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Asal Tanah DukCatPil"
        verbose_name_plural = "12 SKPD Asal Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDukCatPil(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Tujuan Tanah DukCatPil"
        verbose_name_plural = "12 SKPD Tujuan Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDukCatPil(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "12 Foto Tanah DukCatPil"
        verbose_name_plural = "12 Foto Tanah DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Pertanian
##model pada app Pertanian
class TanahPertanian(Tanah):
    class Meta:
        proxy = True
        verbose_name = "13 Tanah Pertanian"
        verbose_name_plural = "13 Tanah Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusPertanian(Tanah):
    class Meta:
        proxy = True
        verbose_name = "13 Tanah Usul Hapus Pertanian"
        verbose_name_plural = "13 Tanah Usul Hapus Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahPertanian(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "13 Usul Hapus Tanah Pertanian"
        verbose_name_plural = "13 Usul Hapus Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahPertanian(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "13 Kontrak Tanah Pertanian"
        verbose_name_plural = "13 Kontrak Tanah Pertanian"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahPertanian(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "13 Harga Tanah Pertanian"
        verbose_name_plural = "13 Harga Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanPertanian(Tanah):
    class Meta:
        proxy = True
        verbose_name = "13 Tanah Penghapusan Pertanian"
        verbose_name_plural = "13 Tanah Penghapusan Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahPertanian(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "13 Tahun Berkurang Tanah Pertanian"
        verbose_name_plural = "13 Tahun Berkurang Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahPertanian(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "13 Penghapusan Tanah Pertanian"
        verbose_name_plural = "13 Penghapusan Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahPertanian(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Asal Tanah Pertanian"
        verbose_name_plural = "13 SKPD Asal Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahPertanian(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Tujuan Tanah Pertanian"
        verbose_name_plural = "13 SKPD Tujuan Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahPertanian(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "13 Foto Tanah Pertanian"
        verbose_name_plural = "13 Foto Tanah Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Kehutanan
##model pada app Kehutanan
class TanahKehutanan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "14 Tanah Kehutanan"
        verbose_name_plural = "14 Tanah Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusKehutanan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "14 Tanah Usul Hapus Kehutanan"
        verbose_name_plural = "14 Tanah Usul Hapus Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahKehutanan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "14 Usul Hapus Tanah Kehutanan"
        verbose_name_plural = "14 Usul Hapus Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahKehutanan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "14 Kontrak Tanah Kehutanan"
        verbose_name_plural = "14 Kontrak Tanah Kehutanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahKehutanan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "14 Harga Tanah Kehutanan"
        verbose_name_plural = "14 Harga Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanKehutanan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "14 Tanah Penghapusan Kehutanan"
        verbose_name_plural = "14 Tanah Penghapusan Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahKehutanan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "14 Tahun Berkurang Tanah Kehutanan"
        verbose_name_plural = "14 Tahun Berkurang Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahKehutanan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "14 Penghapusan Tanah Kehutanan"
        verbose_name_plural = "14 Penghapusan Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahKehutanan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Asal Tanah Kehutanan"
        verbose_name_plural = "14 SKPD Asal Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahKehutanan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Tujuan Tanah Kehutanan"
        verbose_name_plural = "14 SKPD Tujuan Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahKehutanan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "14 Foto Tanah Kehutanan"
        verbose_name_plural = "14 Foto Tanah Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DKP
##model pada app DKP
class TanahDKP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "15 Tanah DKP"
        verbose_name_plural = "15 Tanah DKP"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDKP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "15 Tanah Usul Hapus DKP"
        verbose_name_plural = "15 Tanah Usul Hapus DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDKP(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "15 Usul Hapus Tanah DKP"
        verbose_name_plural = "15 Usul Hapus Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDKP(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "15 Kontrak Tanah DKP"
        verbose_name_plural = "15 Kontrak Tanah DKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDKP(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "15 Harga Tanah DKP"
        verbose_name_plural = "15 Harga Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDKP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "15 Tanah Penghapusan DKP"
        verbose_name_plural = "15 Tanah Penghapusan DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDKP(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "15 Tahun Berkurang Tanah DKP"
        verbose_name_plural = "15 Tahun Berkurang Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDKP(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "15 Penghapusan Tanah DKP"
        verbose_name_plural = "15 Penghapusan Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDKP(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Asal Tanah DKP"
        verbose_name_plural = "15 SKPD Asal Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDKP(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Tujuan Tanah DKP"
        verbose_name_plural = "15 SKPD Tujuan Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDKP(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "15 Foto Tanah DKP"
        verbose_name_plural = "15 Foto Tanah DKP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DKUKMP
##model pada app DKUKMP
class TanahDKUKMP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "16 Tanah DKUKMP"
        verbose_name_plural = "16 Tanah DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDKUKMP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "16 Tanah Usul Hapus DKUKMP"
        verbose_name_plural = "16 Tanah Usul Hapus DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDKUKMP(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "16 Usul Hapus Tanah DKUKMP"
        verbose_name_plural = "16 Usul Hapus Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDKUKMP(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "16 Kontrak Tanah DKUKMP"
        verbose_name_plural = "16 Kontrak Tanah DKUKMP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDKUKMP(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "16 Harga Tanah DKUKMP"
        verbose_name_plural = "16 Harga Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDKUKMP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "16 Tanah Penghapusan DKUKMP"
        verbose_name_plural = "16 Tanah Penghapusan DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDKUKMP(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "16 Tahun Berkurang Tanah DKUKMP"
        verbose_name_plural = "16 Tahun Berkurang Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDKUKMP(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "16 Penghapusan Tanah DKUKMP"
        verbose_name_plural = "16 Penghapusan Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDKUKMP(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Asal Tanah DKUKMP"
        verbose_name_plural = "16 SKPD Asal Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDKUKMP(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Tujuan Tanah DKUKMP"
        verbose_name_plural = "16 SKPD Tujuan Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDKUKMP(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "16 Foto Tanah DKUKMP"
        verbose_name_plural = "16 Foto Tanah DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Distamben
##model pada app Distamben
class TanahDistamben(Tanah):
    class Meta:
        proxy = True
        verbose_name = "17 Tanah Distamben"
        verbose_name_plural = "17 Tanah Distamben"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDistamben(Tanah):
    class Meta:
        proxy = True
        verbose_name = "17 Tanah Usul Hapus Distamben"
        verbose_name_plural = "17 Tanah Usul Hapus Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDistamben(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "17 Usul Hapus Tanah Distamben"
        verbose_name_plural = "17 Usul Hapus Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDistamben(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "17 Kontrak Tanah Distamben"
        verbose_name_plural = "17 Kontrak Tanah Distamben"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDistamben(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "17 Harga Tanah Distamben"
        verbose_name_plural = "17 Harga Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDistamben(Tanah):
    class Meta:
        proxy = True
        verbose_name = "17 Tanah Penghapusan Distamben"
        verbose_name_plural = "17 Tanah Penghapusan Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDistamben(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "17 Tahun Berkurang Tanah Distamben"
        verbose_name_plural = "17 Tahun Berkurang Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDistamben(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "17 Penghapusan Tanah Distamben"
        verbose_name_plural = "17 Penghapusan Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDistamben(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Asal Tanah Distamben"
        verbose_name_plural = "17 SKPD Asal Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDistamben(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Tujuan Tanah Distamben"
        verbose_name_plural = "17 SKPD Tujuan Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDistamben(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "17 Foto Tanah Distamben"
        verbose_name_plural = "17 Foto Tanah Distamben"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DPMPTSP
##model pada app DPMPTSP
class TanahDPMPTSP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "18 Tanah DPMPTSP"
        verbose_name_plural = "18 Tanah DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDPMPTSP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "18 Tanah Usul Hapus DPMPTSP"
        verbose_name_plural = "18 Tanah Usul Hapus DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDPMPTSP(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "18 Usul Hapus Tanah DPMPTSP"
        verbose_name_plural = "18 Usul Hapus Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDPMPTSP(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "18 Kontrak Tanah DPMPTSP"
        verbose_name_plural = "18 Kontrak Tanah DPMPTSP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDPMPTSP(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "18 Harga Tanah DPMPTSP"
        verbose_name_plural = "18 Harga Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDPMPTSP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "18 Tanah Penghapusan DPMPTSP"
        verbose_name_plural = "18 Tanah Penghapusan DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDPMPTSP(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "18 Tahun Berkurang Tanah DPMPTSP"
        verbose_name_plural = "18 Tahun Berkurang Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDPMPTSP(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "18 Penghapusan Tanah DPMPTSP"
        verbose_name_plural = "18 Penghapusan Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDPMPTSP(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Asal Tanah DPMPTSP"
        verbose_name_plural = "18 SKPD Asal Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDPMPTSP(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Tujuan Tanah DPMPTSP"
        verbose_name_plural = "18 SKPD Tujuan Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDPMPTSP(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "18 Foto Tanah DPMPTSP"
        verbose_name_plural = "18 Foto Tanah DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##BKD
##model pada app BKD
class TanahBKD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "19 Tanah BKD"
        verbose_name_plural = "19 Tanah BKD"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBKD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "19 Tanah Usul Hapus BKD"
        verbose_name_plural = "19 Tanah Usul Hapus BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBKD(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "19 Usul Hapus Tanah BKD"
        verbose_name_plural = "19 Usul Hapus Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBKD(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "19 Kontrak Tanah BKD"
        verbose_name_plural = "19 Kontrak Tanah BKD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBKD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "19 Harga Tanah BKD"
        verbose_name_plural = "19 Harga Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBKD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "19 Tanah Penghapusan BKD"
        verbose_name_plural = "19 Tanah Penghapusan BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBKD(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "19 Tahun Berkurang Tanah BKD"
        verbose_name_plural = "19 Tahun Berkurang Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBKD(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "19 Penghapusan Tanah BKD"
        verbose_name_plural = "19 Penghapusan Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBKD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Asal Tanah BKD"
        verbose_name_plural = "19 SKPD Asal Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBKD(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Tujuan Tanah BKD"
        verbose_name_plural = "19 SKPD Tujuan Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBKD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "19 Foto Tanah BKD"
        verbose_name_plural = "19 Foto Tanah BKD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Inspektorat
##model pada app Inspektorat
class TanahInspektorat(Tanah):
    class Meta:
        proxy = True
        verbose_name = "20 Tanah Inspektorat"
        verbose_name_plural = "20 Tanah Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusInspektorat(Tanah):
    class Meta:
        proxy = True
        verbose_name = "20 Tanah Usul Hapus Inspektorat"
        verbose_name_plural = "20 Tanah Usul Hapus Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahInspektorat(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "20 Usul Hapus Tanah Inspektorat"
        verbose_name_plural = "20 Usul Hapus Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahInspektorat(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "20 Kontrak Tanah Inspektorat"
        verbose_name_plural = "20 Kontrak Tanah Inspektorat"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahInspektorat(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "20 Harga Tanah Inspektorat"
        verbose_name_plural = "20 Harga Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanInspektorat(Tanah):
    class Meta:
        proxy = True
        verbose_name = "20 Tanah Penghapusan Inspektorat"
        verbose_name_plural = "20 Tanah Penghapusan Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahInspektorat(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "20 Tahun Berkurang Tanah Inspektorat"
        verbose_name_plural = "20 Tahun Berkurang Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahInspektorat(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "20 Penghapusan Tanah Inspektorat"
        verbose_name_plural = "20 Penghapusan Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahInspektorat(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Asal Tanah Inspektorat"
        verbose_name_plural = "20 SKPD Asal Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahInspektorat(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Tujuan Tanah Inspektorat"
        verbose_name_plural = "20 SKPD Tujuan Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahInspektorat(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "20 Foto Tanah Inspektorat"
        verbose_name_plural = "20 Foto Tanah Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##BAPPEDA
##model pada app BAPPEDA
class TanahBAPPEDA(Tanah):
    class Meta:
        proxy = True
        verbose_name = "21 Tanah BAPPEDA"
        verbose_name_plural = "21 Tanah BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBAPPEDA(Tanah):
    class Meta:
        proxy = True
        verbose_name = "21 Tanah Usul Hapus BAPPEDA"
        verbose_name_plural = "21 Tanah Usul Hapus BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBAPPEDA(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "21 Usul Hapus Tanah BAPPEDA"
        verbose_name_plural = "21 Usul Hapus Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBAPPEDA(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "21 Kontrak Tanah BAPPEDA"
        verbose_name_plural = "21 Kontrak Tanah BAPPEDA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBAPPEDA(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "21 Harga Tanah BAPPEDA"
        verbose_name_plural = "21 Harga Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBAPPEDA(Tanah):
    class Meta:
        proxy = True
        verbose_name = "21 Tanah Penghapusan BAPPEDA"
        verbose_name_plural = "21 Tanah Penghapusan BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBAPPEDA(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "21 Tahun Berkurang Tanah BAPPEDA"
        verbose_name_plural = "21 Tahun Berkurang Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBAPPEDA(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "21 Penghapusan Tanah BAPPEDA"
        verbose_name_plural = "21 Penghapusan Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBAPPEDA(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Asal Tanah BAPPEDA"
        verbose_name_plural = "21 SKPD Asal Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBAPPEDA(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Tujuan Tanah BAPPEDA"
        verbose_name_plural = "21 SKPD Tujuan Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBAPPEDA(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "21 Foto Tanah BAPPEDA"
        verbose_name_plural = "21 Foto Tanah BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DLH
##model pada app DLH
class TanahDLH(Tanah):
    class Meta:
        proxy = True
        verbose_name = "22 Tanah DLH"
        verbose_name_plural = "22 Tanah DLH"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDLH(Tanah):
    class Meta:
        proxy = True
        verbose_name = "22 Tanah Usul Hapus DLH"
        verbose_name_plural = "22 Tanah Usul Hapus DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDLH(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "22 Usul Hapus Tanah DLH"
        verbose_name_plural = "22 Usul Hapus Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDLH(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "22 Kontrak Tanah DLH"
        verbose_name_plural = "22 Kontrak Tanah DLH"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDLH(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "22 Harga Tanah DLH"
        verbose_name_plural = "22 Harga Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDLH(Tanah):
    class Meta:
        proxy = True
        verbose_name = "22 Tanah Penghapusan DLH"
        verbose_name_plural = "22 Tanah Penghapusan DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDLH(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "22 Tahun Berkurang Tanah DLH"
        verbose_name_plural = "22 Tahun Berkurang Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDLH(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "22 Penghapusan Tanah DLH"
        verbose_name_plural = "22 Penghapusan Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDLH(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Asal Tanah DLH"
        verbose_name_plural = "22 SKPD Asal Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDLH(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Tujuan Tanah DLH"
        verbose_name_plural = "22 SKPD Tujuan Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDLH(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "22 Foto Tanah DLH"
        verbose_name_plural = "22 Foto Tanah DLH"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DKO
##model pada app DKO
class TanahDKO(Tanah):
    class Meta:
        proxy = True
        verbose_name = "23 Tanah DKO"
        verbose_name_plural = "23 Tanah DKO"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDKO(Tanah):
    class Meta:
        proxy = True
        verbose_name = "23 Tanah Usul Hapus DKO"
        verbose_name_plural = "23 Tanah Usul Hapus DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDKO(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "23 Usul Hapus Tanah DKO"
        verbose_name_plural = "23 Usul Hapus Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDKO(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "23 Kontrak Tanah DKO"
        verbose_name_plural = "23 Kontrak Tanah DKO"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDKO(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "23 Harga Tanah DKO"
        verbose_name_plural = "23 Harga Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDKO(Tanah):
    class Meta:
        proxy = True
        verbose_name = "23 Tanah Penghapusan DKO"
        verbose_name_plural = "23 Tanah Penghapusan DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDKO(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "23 Tahun Berkurang Tanah DKO"
        verbose_name_plural = "23 Tahun Berkurang Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDKO(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "23 Penghapusan Tanah DKO"
        verbose_name_plural = "23 Penghapusan Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDKO(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Asal Tanah DKO"
        verbose_name_plural = "23 SKPD Asal Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDKO(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Tujuan Tanah DKO"
        verbose_name_plural = "23 SKPD Tujuan Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDKO(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "23 Foto Tanah DKO"
        verbose_name_plural = "23 Foto Tanah DKO"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##KESBANGPOL
##model pada app KESBANGPOL
class TanahKESBANGPOL(Tanah):
    class Meta:
        proxy = True
        verbose_name = "24 Tanah KESBANGPOL"
        verbose_name_plural = "24 Tanah KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusKESBANGPOL(Tanah):
    class Meta:
        proxy = True
        verbose_name = "24 Tanah Usul Hapus KESBANGPOL"
        verbose_name_plural = "24 Tanah Usul Hapus KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahKESBANGPOL(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "24 Usul Hapus Tanah KESBANGPOL"
        verbose_name_plural = "24 Usul Hapus Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahKESBANGPOL(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "24 Kontrak Tanah KESBANGPOL"
        verbose_name_plural = "24 Kontrak Tanah KESBANGPOL"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahKESBANGPOL(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "24 Harga Tanah KESBANGPOL"
        verbose_name_plural = "24 Harga Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanKESBANGPOL(Tanah):
    class Meta:
        proxy = True
        verbose_name = "24 Tanah Penghapusan KESBANGPOL"
        verbose_name_plural = "24 Tanah Penghapusan KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahKESBANGPOL(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "24 Tahun Berkurang Tanah KESBANGPOL"
        verbose_name_plural = "24 Tahun Berkurang Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahKESBANGPOL(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "24 Penghapusan Tanah KESBANGPOL"
        verbose_name_plural = "24 Penghapusan Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahKESBANGPOL(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Asal Tanah KESBANGPOL"
        verbose_name_plural = "24 SKPD Asal Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahKESBANGPOL(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Tujuan Tanah KESBANGPOL"
        verbose_name_plural = "24 SKPD Tujuan Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahKESBANGPOL(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "24 Foto Tanah KESBANGPOL"
        verbose_name_plural = "24 Foto Tanah KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##SATPOLPP
##model pada app SATPOLPP
class TanahSATPOLPP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "25 Tanah SATPOLPP"
        verbose_name_plural = "25 Tanah SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusSATPOLPP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "25 Tanah Usul Hapus SATPOLPP"
        verbose_name_plural = "25 Tanah Usul Hapus SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahSATPOLPP(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "25 Usul Hapus Tanah SATPOLPP"
        verbose_name_plural = "25 Usul Hapus Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahSATPOLPP(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "25 Kontrak Tanah SATPOLPP"
        verbose_name_plural = "25 Kontrak Tanah SATPOLPP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahSATPOLPP(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "25 Harga Tanah SATPOLPP"
        verbose_name_plural = "25 Harga Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanSATPOLPP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "25 Tanah Penghapusan SATPOLPP"
        verbose_name_plural = "25 Tanah Penghapusan SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahSATPOLPP(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "25 Tahun Berkurang Tanah SATPOLPP"
        verbose_name_plural = "25 Tahun Berkurang Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahSATPOLPP(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "25 Penghapusan Tanah SATPOLPP"
        verbose_name_plural = "25 Penghapusan Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahSATPOLPP(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Asal Tanah SATPOLPP"
        verbose_name_plural = "25 SKPD Asal Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahSATPOLPP(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Tujuan Tanah SATPOLPP"
        verbose_name_plural = "25 SKPD Tujuan Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahSATPOLPP(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "25 Foto Tanah SATPOLPP"
        verbose_name_plural = "25 Foto Tanah SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##BKPPD
##model pada app BKPPD
class TanahBKPPD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "26 Tanah BKPPD"
        verbose_name_plural = "26 Tanah BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBKPPD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "26 Tanah Usul Hapus BKPPD"
        verbose_name_plural = "26 Tanah Usul Hapus BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBKPPD(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "26 Usul Hapus Tanah BKPPD"
        verbose_name_plural = "26 Usul Hapus Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBKPPD(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "26 Kontrak Tanah BKPPD"
        verbose_name_plural = "26 Kontrak Tanah BKPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBKPPD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "26 Harga Tanah BKPPD"
        verbose_name_plural = "26 Harga Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBKPPD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "26 Tanah Penghapusan BKPPD"
        verbose_name_plural = "26 Tanah Penghapusan BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBKPPD(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "26 Tahun Berkurang Tanah BKPPD"
        verbose_name_plural = "26 Tahun Berkurang Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBKPPD(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "26 Penghapusan Tanah BKPPD"
        verbose_name_plural = "26 Penghapusan Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBKPPD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Asal Tanah BKPPD"
        verbose_name_plural = "26 SKPD Asal Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBKPPD(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Tujuan Tanah BKPPD"
        verbose_name_plural = "26 SKPD Tujuan Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBKPPD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "26 Foto Tanah BKPPD"
        verbose_name_plural = "26 Foto Tanah BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##SekretariatKorpri
##model pada app SekretariatKorpri
class TanahSekretariatKorpri(Tanah):
    class Meta:
        proxy = True
        verbose_name = "27 Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Tanah Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusSekretariatKorpri(Tanah):
    class Meta:
        proxy = True
        verbose_name = "27 Tanah Usul Hapus Sekretariat Korpri"
        verbose_name_plural = "27 Tanah Usul Hapus Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahSekretariatKorpri(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "27 Usul Hapus Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Usul Hapus Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahSekretariatKorpri(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "27 Kontrak Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Kontrak Tanah Sekretariat Korpri"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahSekretariatKorpri(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "27 Harga Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Harga Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanSekretariatKorpri(Tanah):
    class Meta:
        proxy = True
        verbose_name = "27 Tanah Penghapusan Sekretariat Korpri"
        verbose_name_plural = "27 Tanah Penghapusan Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahSekretariatKorpri(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "27 Tahun Berkurang Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Tahun Berkurang Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahSekretariatKorpri(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "27 Penghapusan Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Penghapusan Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahSekretariatKorpri(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Asal Tanah Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Asal Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahSekretariatKorpri(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Tujuan Tanah Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Tujuan Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahSekretariatKorpri(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "27 Foto Tanah Sekretariat Korpri"
        verbose_name_plural = "27 Foto Tanah Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Paringin
##model pada app Paringin
class TanahParingin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "28 Tanah Paringin"
        verbose_name_plural = "28 Tanah Paringin"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusParingin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "28 Tanah Usul Hapus Paringin"
        verbose_name_plural = "28 Tanah Usul Hapus Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahParingin(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "28 Usul Hapus Tanah Paringin"
        verbose_name_plural = "28 Usul Hapus Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahParingin(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "28 Kontrak Tanah Paringin"
        verbose_name_plural = "28 Kontrak Tanah Paringin"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahParingin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "28 Harga Tanah Paringin"
        verbose_name_plural = "28 Harga Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanParingin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "28 Tanah Penghapusan Paringin"
        verbose_name_plural = "28 Tanah Penghapusan Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahParingin(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "28 Tahun Berkurang Tanah Paringin"
        verbose_name_plural = "28 Tahun Berkurang Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahParingin(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "28 Penghapusan Tanah Paringin"
        verbose_name_plural = "28 Penghapusan Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahParingin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Asal Tanah Paringin"
        verbose_name_plural = "28 SKPD Asal Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahParingin(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Tujuan Tanah Paringin"
        verbose_name_plural = "28 SKPD Tujuan Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahParingin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "28 Foto Tanah Paringin"
        verbose_name_plural = "28 Foto Tanah Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##ParinginKota
##model pada app ParinginKota
class TanahParinginKota(Tanah):
    class Meta:
        proxy = True
        verbose_name = "29 Tanah Paringin Kota"
        verbose_name_plural = "29 Tanah Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusParinginKota(Tanah):
    class Meta:
        proxy = True
        verbose_name = "29 Tanah Usul Hapus Paringin Kota"
        verbose_name_plural = "29 Tanah Usul Hapus Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahParinginKota(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "29 Usul Hapus Tanah Paringin Kota"
        verbose_name_plural = "29 Usul Hapus Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahParinginKota(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "29 Kontrak Tanah Paringin Kota"
        verbose_name_plural = "29 Kontrak Tanah Paringin Kota"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahParinginKota(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "29 Harga Tanah Paringin Kota"
        verbose_name_plural = "29 Harga Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanParinginKota(Tanah):
    class Meta:
        proxy = True
        verbose_name = "29 Tanah Penghapusan Paringin Kota"
        verbose_name_plural = "29 Tanah Penghapusan Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahParinginKota(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "29 Tahun Berkurang Tanah Paringin Kota"
        verbose_name_plural = "29 Tahun Berkurang Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahParinginKota(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "29 Penghapusan Tanah Paringin Kota"
        verbose_name_plural = "29 Penghapusan Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahParinginKota(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Asal Tanah Paringin Kota"
        verbose_name_plural = "29 SKPD Asal Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahParinginKota(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Tujuan Tanah Paringin Kota"
        verbose_name_plural = "29 SKPD Tujuan Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahParinginKota(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "29 Foto Tanah Paringin Kota"
        verbose_name_plural = "29 Foto Tanah Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##ParinginTimur
##model pada app ParinginTimur
class TanahParinginTimur(Tanah):
    class Meta:
        proxy = True
        verbose_name = "30 Tanah Paringin Timur"
        verbose_name_plural = "30 Tanah Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusParinginTimur(Tanah):
    class Meta:
        proxy = True
        verbose_name = "30 Tanah Usul Hapus Paringin Timur"
        verbose_name_plural = "30 Tanah Usul Hapus Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahParinginTimur(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "30 Usul Hapus Tanah Paringin Timur"
        verbose_name_plural = "30 Usul Hapus Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahParinginTimur(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "30 Kontrak Tanah Paringin Timur"
        verbose_name_plural = "30 Kontrak Tanah Paringin Timur"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahParinginTimur(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "30 Harga Tanah Paringin Timur"
        verbose_name_plural = "30 Harga Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanParinginTimur(Tanah):
    class Meta:
        proxy = True
        verbose_name = "30 Tanah Penghapusan Paringin Timur"
        verbose_name_plural = "30 Tanah Penghapusan Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahParinginTimur(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "30 Tahun Berkurang Tanah Paringin Timur"
        verbose_name_plural = "30 Tahun Berkurang Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahParinginTimur(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "30 Penghapusan Tanah Paringin Timur"
        verbose_name_plural = "30 Penghapusan Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahParinginTimur(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Asal Tanah Paringin Timur"
        verbose_name_plural = "30 SKPD Asal Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahParinginTimur(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Tujuan Tanah Paringin Timur"
        verbose_name_plural = "30 SKPD Tujuan Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahParinginTimur(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "30 Foto Tanah Paringin Timur"
        verbose_name_plural = "30 Foto Tanah Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Lampihong
##model pada app Lampihong
class TanahLampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "31 Tanah Lampihong"
        verbose_name_plural = "31 Tanah Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusLampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "31 Tanah Usul Hapus Lampihong"
        verbose_name_plural = "31 Tanah Usul Hapus Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahLampihong(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "31 Usul Hapus Tanah Lampihong"
        verbose_name_plural = "31 Usul Hapus Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahLampihong(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "31 Kontrak Tanah Lampihong"
        verbose_name_plural = "31 Kontrak Tanah Lampihong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahLampihong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "31 Harga Tanah Lampihong"
        verbose_name_plural = "31 Harga Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanLampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "31 Tanah Penghapusan Lampihong"
        verbose_name_plural = "31 Tanah Penghapusan Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahLampihong(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "31 Tahun Berkurang Tanah Lampihong"
        verbose_name_plural = "31 Tahun Berkurang Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahLampihong(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "31 Penghapusan Tanah Lampihong"
        verbose_name_plural = "31 Penghapusan Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahLampihong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Asal Tanah Lampihong"
        verbose_name_plural = "31 SKPD Asal Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahLampihong(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Tujuan Tanah Lampihong"
        verbose_name_plural = "31 SKPD Tujuan Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahLampihong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "31 Foto Tanah Lampihong"
        verbose_name_plural = "31 Foto Tanah Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Batumandi
##model pada app Batumandi
class TanahBatumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "32 Tanah Batumandi"
        verbose_name_plural = "32 Tanah Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBatumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "32 Tanah Usul Hapus Batumandi"
        verbose_name_plural = "32 Tanah Usul Hapus Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBatumandi(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "32 Usul Hapus Tanah Batumandi"
        verbose_name_plural = "32 Usul Hapus Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBatumandi(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "32 Kontrak Tanah Batumandi"
        verbose_name_plural = "32 Kontrak Tanah Batumandi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBatumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "32 Harga Tanah Batumandi"
        verbose_name_plural = "32 Harga Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBatumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "32 Tanah Penghapusan Batumandi"
        verbose_name_plural = "32 Tanah Penghapusan Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBatumandi(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "32 Tahun Berkurang Tanah Batumandi"
        verbose_name_plural = "32 Tahun Berkurang Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBatumandi(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "32 Penghapusan Tanah Batumandi"
        verbose_name_plural = "32 Penghapusan Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBatumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Asal Tanah Batumandi"
        verbose_name_plural = "32 SKPD Asal Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBatumandi(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Tujuan Tanah Batumandi"
        verbose_name_plural = "32 SKPD Tujuan Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBatumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "32 Foto Tanah Batumandi"
        verbose_name_plural = "32 Foto Tanah Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Juai
##model pada app Juai
class TanahJuai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "33 Tanah Juai"
        verbose_name_plural = "33 Tanah Juai"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusJuai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "33 Tanah Usul Hapus Juai"
        verbose_name_plural = "33 Tanah Usul Hapus Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahJuai(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "33 Usul Hapus Tanah Juai"
        verbose_name_plural = "33 Usul Hapus Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahJuai(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "33 Kontrak Tanah Juai"
        verbose_name_plural = "33 Kontrak Tanah Juai"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahJuai(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "33 Harga Tanah Juai"
        verbose_name_plural = "33 Harga Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanJuai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "33 Tanah Penghapusan Juai"
        verbose_name_plural = "33 Tanah Penghapusan Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahJuai(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "33 Tahun Berkurang Tanah Juai"
        verbose_name_plural = "33 Tahun Berkurang Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahJuai(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "33 Penghapusan Tanah Juai"
        verbose_name_plural = "33 Penghapusan Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahJuai(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Asal Tanah Juai"
        verbose_name_plural = "33 SKPD Asal Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahJuai(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Tujuan Tanah Juai"
        verbose_name_plural = "33 SKPD Tujuan Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahJuai(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "33 Foto Tanah Juai"
        verbose_name_plural = "33 Foto Tanah Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Awayan
##model pada app Awayan
class TanahAwayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "34 Tanah Awayan"
        verbose_name_plural = "34 Tanah Awayan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusAwayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "34 Tanah Usul Hapus Awayan"
        verbose_name_plural = "34 Tanah Usul Hapus Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahAwayan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "34 Usul Hapus Tanah Awayan"
        verbose_name_plural = "34 Usul Hapus Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahAwayan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "34 Kontrak Tanah Awayan"
        verbose_name_plural = "34 Kontrak Tanah Awayan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahAwayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "34 Harga Tanah Awayan"
        verbose_name_plural = "34 Harga Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanAwayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "34 Tanah Penghapusan Awayan"
        verbose_name_plural = "34 Tanah Penghapusan Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahAwayan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "34 Tahun Berkurang Tanah Awayan"
        verbose_name_plural = "34 Tahun Berkurang Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahAwayan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "34 Penghapusan Tanah Awayan"
        verbose_name_plural = "34 Penghapusan Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahAwayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Asal Tanah Awayan"
        verbose_name_plural = "34 SKPD Asal Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahAwayan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Tujuan Tanah Awayan"
        verbose_name_plural = "34 SKPD Tujuan Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahAwayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "34 Foto Tanah Awayan"
        verbose_name_plural = "34 Foto Tanah Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Halong
##model pada app Halong
class TanahHalong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "35 Tanah Halong"
        verbose_name_plural = "35 Tanah Halong"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusHalong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "35 Tanah Usul Hapus Halong"
        verbose_name_plural = "35 Tanah Usul Hapus Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahHalong(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "35 Usul Hapus Tanah Halong"
        verbose_name_plural = "35 Usul Hapus Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahHalong(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "35 Kontrak Tanah Halong"
        verbose_name_plural = "35 Kontrak Tanah Halong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahHalong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "35 Harga Tanah Halong"
        verbose_name_plural = "35 Harga Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanHalong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "35 Tanah Penghapusan Halong"
        verbose_name_plural = "35 Tanah Penghapusan Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahHalong(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "35 Tahun Berkurang Tanah Halong"
        verbose_name_plural = "35 Tahun Berkurang Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahHalong(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "35 Penghapusan Tanah Halong"
        verbose_name_plural = "35 Penghapusan Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahHalong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Asal Tanah Halong"
        verbose_name_plural = "35 SKPD Asal Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahHalong(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Tujuan Tanah Halong"
        verbose_name_plural = "35 SKPD Tujuan Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahHalong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "35 Foto Tanah Halong"
        verbose_name_plural = "35 Foto Tanah Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##ParinginSelatan
##model pada app ParinginSelatan
class TanahParinginSelatan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "36 Tanah Paringin Selatan"
        verbose_name_plural = "36 Tanah Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusParinginSelatan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "36 Tanah Usul Hapus Paringin Selatan"
        verbose_name_plural = "36 Tanah Usul Hapus Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahParinginSelatan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "36 Usul Hapus Tanah Paringin Selatan"
        verbose_name_plural = "36 Usul Hapus Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahParinginSelatan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "36 Kontrak Tanah Paringin Selatan"
        verbose_name_plural = "36 Kontrak Tanah Paringin Selatan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahParinginSelatan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "36 Harga Tanah Paringin Selatan"
        verbose_name_plural = "36 Harga Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanParinginSelatan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "36 Tanah Penghapusan Paringin Selatan"
        verbose_name_plural = "36 Tanah Penghapusan Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahParinginSelatan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "36 Tahun Berkurang Tanah Paringin Selatan"
        verbose_name_plural = "36 Tahun Berkurang Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahParinginSelatan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "36 Penghapusan Tanah Paringin Selatan"
        verbose_name_plural = "36 Penghapusan Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahParinginSelatan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Asal Tanah Paringin Selatan"
        verbose_name_plural = "36 SKPD Asal Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahParinginSelatan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Tujuan Tanah Paringin Selatan"
        verbose_name_plural = "36 SKPD Tujuan Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahParinginSelatan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "36 Foto Tanah Paringin Selatan"
        verbose_name_plural = "36 Foto Tanah Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##BatuPiring
##model pada app BatuPiring
class TanahBatuPiring(Tanah):
    class Meta:
        proxy = True
        verbose_name = "37 Tanah Batu Piring"
        verbose_name_plural = "37 Tanah Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBatuPiring(Tanah):
    class Meta:
        proxy = True
        verbose_name = "37 Tanah Usul Hapus Batu Piring"
        verbose_name_plural = "37 Tanah Usul Hapus Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBatuPiring(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "37 Usul Hapus Tanah Batu Piring"
        verbose_name_plural = "37 Usul Hapus Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBatuPiring(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "37 Kontrak Tanah Batu Piring"
        verbose_name_plural = "37 Kontrak Tanah Batu Piring"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBatuPiring(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "37 Harga Tanah Batu Piring"
        verbose_name_plural = "37 Harga Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBatuPiring(Tanah):
    class Meta:
        proxy = True
        verbose_name = "37 Tanah Penghapusan Batu Piring"
        verbose_name_plural = "37 Tanah Penghapusan Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBatuPiring(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "37 Tahun Berkurang Tanah Batu Piring"
        verbose_name_plural = "37 Tahun Berkurang Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBatuPiring(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "37 Penghapusan Tanah Batu Piring"
        verbose_name_plural = "37 Penghapusan Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBatuPiring(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Asal Tanah Batu Piring"
        verbose_name_plural = "37 SKPD Asal Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBatuPiring(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Tujuan Tanah Batu Piring"
        verbose_name_plural = "37 SKPD Tujuan Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBatuPiring(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "37 Foto Tanah Batu Piring"
        verbose_name_plural = "37 Foto Tanah Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##TebingTinggi
##model pada app TebingTinggi
class TanahTebingTinggi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "38 Tanah Tebing Tinggi"
        verbose_name_plural = "38 Tanah Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusTebingTinggi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "38 Tanah Usul Hapus Tebing Tinggi"
        verbose_name_plural = "38 Tanah Usul Hapus Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahTebingTinggi(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "38 Usul Hapus Tanah Tebing Tinggi"
        verbose_name_plural = "38 Usul Hapus Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahTebingTinggi(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "38 Kontrak Tanah Tebing Tinggi"
        verbose_name_plural = "38 Kontrak Tanah Tebing Tinggi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahTebingTinggi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "38 Harga Tanah Tebing Tinggi"
        verbose_name_plural = "38 Harga Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanTebingTinggi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "38 Tanah Penghapusan Tebing Tinggi"
        verbose_name_plural = "38 Tanah Penghapusan Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahTebingTinggi(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "38 Tahun Berkurang Tanah Tebing Tinggi"
        verbose_name_plural = "38 Tahun Berkurang Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahTebingTinggi(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "38 Penghapusan Tanah Tebing Tinggi"
        verbose_name_plural = "38 Penghapusan Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahTebingTinggi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Asal Tanah Tebing Tinggi"
        verbose_name_plural = "38 SKPD Asal Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahTebingTinggi(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Tujuan Tanah Tebing Tinggi"
        verbose_name_plural = "38 SKPD Tujuan Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahTebingTinggi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "38 Foto Tanah Tebing Tinggi"
        verbose_name_plural = "38 Foto Tanah Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##BPBD
##model pada app BPBD
class TanahBPBD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "39 Tanah BPBD"
        verbose_name_plural = "39 Tanah BPBD"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBPBD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "39 Tanah Usul Hapus BPBD"
        verbose_name_plural = "39 Tanah Usul Hapus BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBPBD(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "39 Usul Hapus Tanah BPBD"
        verbose_name_plural = "39 Usul Hapus Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBPBD(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "39 Kontrak Tanah BPBD"
        verbose_name_plural = "39 Kontrak Tanah BPBD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBPBD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "39 Harga Tanah BPBD"
        verbose_name_plural = "39 Harga Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBPBD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "39 Tanah Penghapusan BPBD"
        verbose_name_plural = "39 Tanah Penghapusan BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBPBD(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "39 Tahun Berkurang Tanah BPBD"
        verbose_name_plural = "39 Tahun Berkurang Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBPBD(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "39 Penghapusan Tanah BPBD"
        verbose_name_plural = "39 Penghapusan Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBPBD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Asal Tanah BPBD"
        verbose_name_plural = "39 SKPD Asal Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBPBD(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Tujuan Tanah BPBD"
        verbose_name_plural = "39 SKPD Tujuan Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBPBD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "39 Foto Tanah BPBD"
        verbose_name_plural = "39 Foto Tanah BPBD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DPKP
##model pada app DPKP
class TanahDPKP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "40 Tanah DPKP"
        verbose_name_plural = "40 Tanah DPKP"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDPKP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "40 Tanah Usul Hapus DPKP"
        verbose_name_plural = "40 Tanah Usul Hapus DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDPKP(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "40 Usul Hapus Tanah DPKP"
        verbose_name_plural = "40 Usul Hapus Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDPKP(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "40 Kontrak Tanah DPKP"
        verbose_name_plural = "40 Kontrak Tanah DPKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDPKP(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "40 Harga Tanah DPKP"
        verbose_name_plural = "40 Harga Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDPKP(Tanah):
    class Meta:
        proxy = True
        verbose_name = "40 Tanah Penghapusan DPKP"
        verbose_name_plural = "40 Tanah Penghapusan DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDPKP(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "40 Tahun Berkurang Tanah DPKP"
        verbose_name_plural = "40 Tahun Berkurang Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDPKP(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "40 Penghapusan Tanah DPKP"
        verbose_name_plural = "40 Penghapusan Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDPKP(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Asal Tanah DPKP"
        verbose_name_plural = "40 SKPD Asal Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDPKP(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Tujuan Tanah DPKP"
        verbose_name_plural = "40 SKPD Tujuan Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDPKP(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "40 Foto Tanah DPKP"
        verbose_name_plural = "40 Foto Tanah DPKP"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Disnakertrans
##model pada app Disnakertrans
class TanahDisnakertrans(Tanah):
    class Meta:
        proxy = True
        verbose_name = "41 Tanah Disnakertrans"
        verbose_name_plural = "41 Tanah Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDisnakertrans(Tanah):
    class Meta:
        proxy = True
        verbose_name = "41 Tanah Usul Hapus Disnakertrans"
        verbose_name_plural = "41 Tanah Usul Hapus Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDisnakertrans(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "41 Usul Hapus Tanah Disnakertrans"
        verbose_name_plural = "41 Usul Hapus Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDisnakertrans(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "41 Kontrak Tanah Disnakertrans"
        verbose_name_plural = "41 Kontrak Tanah Disnakertrans"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDisnakertrans(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "41 Harga Tanah Disnakertrans"
        verbose_name_plural = "41 Harga Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDisnakertrans(Tanah):
    class Meta:
        proxy = True
        verbose_name = "41 Tanah Penghapusan Disnakertrans"
        verbose_name_plural = "41 Tanah Penghapusan Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDisnakertrans(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "41 Tahun Berkurang Tanah Disnakertrans"
        verbose_name_plural = "41 Tahun Berkurang Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDisnakertrans(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "41 Penghapusan Tanah Disnakertrans"
        verbose_name_plural = "41 Penghapusan Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDisnakertrans(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Asal Tanah Disnakertrans"
        verbose_name_plural = "41 SKPD Asal Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDisnakertrans(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Tujuan Tanah Disnakertrans"
        verbose_name_plural = "41 SKPD Tujuan Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisnakertrans(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "41 Foto Tanah Disnakertrans"
        verbose_name_plural = "41 Foto Tanah Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##DPPKB
##model pada app DPPKB
class TanahDPPKB(Tanah):
    class Meta:
        proxy = True
        verbose_name = "42 Tanah DPPKB"
        verbose_name_plural = "42 Tanah DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusDPPKB(Tanah):
    class Meta:
        proxy = True
        verbose_name = "42 Tanah Usul Hapus DPPKB"
        verbose_name_plural = "42 Tanah Usul Hapus DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahDPPKB(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "42 Usul Hapus Tanah DPPKB"
        verbose_name_plural = "42 Usul Hapus Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahDPPKB(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "42 Kontrak Tanah DPPKB"
        verbose_name_plural = "42 Kontrak Tanah DPPKB"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahDPPKB(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "42 Harga Tanah DPPKB"
        verbose_name_plural = "42 Harga Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanDPPKB(Tanah):
    class Meta:
        proxy = True
        verbose_name = "42 Tanah Penghapusan DPPKB"
        verbose_name_plural = "42 Tanah Penghapusan DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahDPPKB(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "42 Tahun Berkurang Tanah DPPKB"
        verbose_name_plural = "42 Tahun Berkurang Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahDPPKB(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "42 Penghapusan Tanah DPPKB"
        verbose_name_plural = "42 Penghapusan Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahDPPKB(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Asal Tanah DPPKB"
        verbose_name_plural = "42 SKPD Asal Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahDPPKB(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Tujuan Tanah DPPKB"
        verbose_name_plural = "42 SKPD Tujuan Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDPPKB(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "42 Foto Tanah DPPKB"
        verbose_name_plural = "42 Foto Tanah DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Kominfo
##model pada app Kominfo
class TanahKominfo(Tanah):
    class Meta:
        proxy = True
        verbose_name = "43 Tanah Kominfo"
        verbose_name_plural = "43 Tanah Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusKominfo(Tanah):
    class Meta:
        proxy = True
        verbose_name = "43 Tanah Usul Hapus Kominfo"
        verbose_name_plural = "43 Tanah Usul Hapus Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahKominfo(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "43 Usul Hapus Tanah Kominfo"
        verbose_name_plural = "43 Usul Hapus Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahKominfo(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "43 Kontrak Tanah Kominfo"
        verbose_name_plural = "43 Kontrak Tanah Kominfo"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahKominfo(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "43 Harga Tanah Kominfo"
        verbose_name_plural = "43 Harga Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanKominfo(Tanah):
    class Meta:
        proxy = True
        verbose_name = "43 Tanah Penghapusan Kominfo"
        verbose_name_plural = "43 Tanah Penghapusan Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahKominfo(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "43 Tahun Berkurang Tanah Kominfo"
        verbose_name_plural = "43 Tahun Berkurang Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahKominfo(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "43 Penghapusan Tanah Kominfo"
        verbose_name_plural = "43 Penghapusan Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahKominfo(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Asal Tanah Kominfo"
        verbose_name_plural = "43 SKPD Asal Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahKominfo(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Tujuan Tanah Kominfo"
        verbose_name_plural = "43 SKPD Tujuan Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahKominfo(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "43 Foto Tanah Kominfo"
        verbose_name_plural = "43 Foto Tanah Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Kearsipan
##model pada app Kearsipan
class TanahKearsipan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "44 Tanah Kearsipan"
        verbose_name_plural = "44 Tanah Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusKearsipan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "44 Tanah Usul Hapus Kearsipan"
        verbose_name_plural = "44 Tanah Usul Hapus Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahKearsipan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "44 Usul Hapus Tanah Kearsipan"
        verbose_name_plural = "44 Usul Hapus Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahKearsipan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "44 Kontrak Tanah Kearsipan"
        verbose_name_plural = "44 Kontrak Tanah Kearsipan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahKearsipan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "44 Harga Tanah Kearsipan"
        verbose_name_plural = "44 Harga Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanKearsipan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "44 Tanah Penghapusan Kearsipan"
        verbose_name_plural = "44 Tanah Penghapusan Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahKearsipan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "44 Tahun Berkurang Tanah Kearsipan"
        verbose_name_plural = "44 Tahun Berkurang Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahKearsipan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "44 Penghapusan Tanah Kearsipan"
        verbose_name_plural = "44 Penghapusan Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahKearsipan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Asal Tanah Kearsipan"
        verbose_name_plural = "44 SKPD Asal Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahKearsipan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Tujuan Tanah Kearsipan"
        verbose_name_plural = "44 SKPD Tujuan Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahKearsipan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "44 Foto Tanah Kearsipan"
        verbose_name_plural = "44 Foto Tanah Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Perikanan
##model pada app Perikanan
class TanahPerikanan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "45 Tanah Perikanan"
        verbose_name_plural = "45 Tanah Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusPerikanan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "45 Tanah Usul Hapus Perikanan"
        verbose_name_plural = "45 Tanah Usul Hapus Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahPerikanan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "45 Usul Hapus Tanah Perikanan"
        verbose_name_plural = "45 Usul Hapus Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahPerikanan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "45 Kontrak Tanah Perikanan"
        verbose_name_plural = "45 Kontrak Tanah Perikanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahPerikanan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "45 Harga Tanah Perikanan"
        verbose_name_plural = "45 Harga Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanPerikanan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "45 Tanah Penghapusan Perikanan"
        verbose_name_plural = "45 Tanah Penghapusan Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahPerikanan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "45 Tahun Berkurang Tanah Perikanan"
        verbose_name_plural = "45 Tahun Berkurang Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahPerikanan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "45 Penghapusan Tanah Perikanan"
        verbose_name_plural = "45 Penghapusan Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahPerikanan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Asal Tanah Perikanan"
        verbose_name_plural = "45 SKPD Asal Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahPerikanan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Tujuan Tanah Perikanan"
        verbose_name_plural = "45 SKPD Tujuan Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahPerikanan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "45 Foto Tanah Perikanan"
        verbose_name_plural = "45 Foto Tanah Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Pariwisata
##model pada app Pariwisata
class TanahPariwisata(Tanah):
    class Meta:
        proxy = True
        verbose_name = "46 Tanah Pariwisata"
        verbose_name_plural = "46 Tanah Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusPariwisata(Tanah):
    class Meta:
        proxy = True
        verbose_name = "46 Tanah Usul Hapus Pariwisata"
        verbose_name_plural = "46 Tanah Usul Hapus Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahPariwisata(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "46 Usul Hapus Tanah Pariwisata"
        verbose_name_plural = "46 Usul Hapus Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahPariwisata(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "46 Kontrak Tanah Pariwisata"
        verbose_name_plural = "46 Kontrak Tanah Pariwisata"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahPariwisata(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "46 Harga Tanah Pariwisata"
        verbose_name_plural = "46 Harga Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanPariwisata(Tanah):
    class Meta:
        proxy = True
        verbose_name = "46 Tanah Penghapusan Pariwisata"
        verbose_name_plural = "46 Tanah Penghapusan Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahPariwisata(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "46 Tahun Berkurang Tanah Pariwisata"
        verbose_name_plural = "46 Tahun Berkurang Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahPariwisata(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "46 Penghapusan Tanah Pariwisata"
        verbose_name_plural = "46 Penghapusan Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahPariwisata(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Asal Tanah Pariwisata"
        verbose_name_plural = "46 SKPD Asal Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahPariwisata(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Tujuan Tanah Pariwisata"
        verbose_name_plural = "46 SKPD Tujuan Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahPariwisata(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "46 Foto Tanah Pariwisata"
        verbose_name_plural = "46 Foto Tanah Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##Perdagangan
##model pada app Perdagangan
class TanahPerdagangan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "47 Tanah Perdagangan"
        verbose_name_plural = "47 Tanah Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusPerdagangan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "47 Tanah Usul Hapus Perdagangan"
        verbose_name_plural = "47 Tanah Usul Hapus Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahPerdagangan(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "47 Usul Hapus Tanah Perdagangan"
        verbose_name_plural = "47 Usul Hapus Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahPerdagangan(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "47 Kontrak Tanah Perdagangan"
        verbose_name_plural = "47 Kontrak Tanah Perdagangan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahPerdagangan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "47 Harga Tanah Perdagangan"
        verbose_name_plural = "47 Harga Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanPerdagangan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "47 Tanah Penghapusan Perdagangan"
        verbose_name_plural = "47 Tanah Penghapusan Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahPerdagangan(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "47 Tahun Berkurang Tanah Perdagangan"
        verbose_name_plural = "47 Tahun Berkurang Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahPerdagangan(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "47 Penghapusan Tanah Perdagangan"
        verbose_name_plural = "47 Penghapusan Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahPerdagangan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Asal Tanah Perdagangan"
        verbose_name_plural = "47 SKPD Asal Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahPerdagangan(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Tujuan Tanah Perdagangan"
        verbose_name_plural = "47 SKPD Tujuan Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahPerdagangan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "47 Foto Tanah Perdagangan"
        verbose_name_plural = "47 Foto Tanah Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




##BPPD
##model pada app BPPD
class TanahBPPD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "48 Tanah BPPD"
        verbose_name_plural = "48 Tanah BPPD"

    def __unicode__(self):
        return self.nama_barang


class TanahUsulHapusBPPD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "48 Tanah Usul Hapus BPPD"
        verbose_name_plural = "48 Tanah Usul Hapus BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusTanahBPPD(TahunBerkurangUsulHapusTanah):
    class Meta:
        proxy = True
        verbose_name = "48 Usul Hapus Tanah BPPD"
        verbose_name_plural = "48 Usul Hapus Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakTanahBPPD(KontrakTanah):
    class Meta:
        proxy = True
        verbose_name = "48 Kontrak Tanah BPPD"
        verbose_name_plural = "48 Kontrak Tanah BPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaTanahBPPD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "48 Harga Tanah BPPD"
        verbose_name_plural = "48 Harga Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




class TanahPenghapusanBPPD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "48 Tanah Penghapusan BPPD"
        verbose_name_plural = "48 Tanah Penghapusan BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangTanahBPPD(TahunBerkurangTanah):
    class Meta:
        proxy = True
        verbose_name = "48 Tahun Berkurang Tanah BPPD"
        verbose_name_plural = "48 Tahun Berkurang Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanTanahBPPD(PenghapusanTanah):
    class Meta:
        proxy = True
        verbose_name = "48 Penghapusan Tanah BPPD"
        verbose_name_plural = "48 Penghapusan Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalTanahBPPD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Asal Tanah BPPD"
        verbose_name_plural = "48 SKPD Asal Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanTanahBPPD(SKPDTujuanTanah):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Tujuan Tanah BPPD"
        verbose_name_plural = "48 SKPD Tujuan Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahBPPD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "48 Foto Tanah BPPD"
        verbose_name_plural = "48 Foto Tanah BPPD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 1 Awayan


class TanahDisdikSMPN1Awayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Tanah Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN1Awayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN1Awayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN1Awayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 1 Batumandi


class TanahDisdikSMPN1Batumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Tanah Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN1Batumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN1Batumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN1Batumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 1 Halong


class TanahDisdikSMPN1Halong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Tanah Disdik SMPN 1 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN1Halong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN1Halong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 1 Halong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN1Halong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 1 Juai


class TanahDisdikSMPN1Juai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Tanah Disdik SMPN 1 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN1Juai(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN1Juai(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 1 Juai"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN1Juai(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 1 Lampihong


class TanahDisdikSMPN1Lampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Tanah Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN1Lampihong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN1Lampihong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN1Lampihong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 1 Paringin


class TanahDisdikSMPN1Paringin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Tanah Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN1Paringin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN1Paringin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN1Paringin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 2 Awayan


class TanahDisdikSMPN2Awayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Tanah Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN2Awayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN2Awayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN2Awayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 2 Batumandi


class TanahDisdikSMPN2Batumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Tanah Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN2Batumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN2Batumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN2Batumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 2 Halong


class TanahDisdikSMPN2Halong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Tanah Disdik SMPN 2 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN2Halong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN2Halong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 2 Halong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN2Halong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 2 Juai


class TanahDisdikSMPN2Juai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Tanah Disdik SMPN 2 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN2Juai(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN2Juai(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 2 Juai"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN2Juai(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 2 Lampihong


class TanahDisdikSMPN2Lampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Tanah Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN2Lampihong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN2Lampihong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN2Lampihong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 2 Paringin


class TanahDisdikSMPN2Paringin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Tanah Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN2Paringin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN2Paringin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN2Paringin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 3 Awayan


class TanahDisdikSMPN3Awayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Tanah Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN3Awayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN3Awayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN3Awayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 3 Batumandi


class TanahDisdikSMPN3Batumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Tanah Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN3Batumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN3Batumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN3Batumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 3 Halong


class TanahDisdikSMPN3Halong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Tanah Disdik SMPN 3 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN3Halong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN3Halong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 3 Halong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN3Halong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 3 Paringin


class TanahDisdikSMPN3Paringin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Tanah Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN3Paringin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN3Paringin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN3Paringin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 4 Awayan


class TanahDisdikSMPN4Awayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Tanah Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN4Awayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN4Awayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN4Awayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 4 Batumandi


class TanahDisdikSMPN4Batumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Tanah Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN4Batumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN4Batumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN4Batumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 4 Halong


class TanahDisdikSMPN4Halong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Tanah Disdik SMPN 4 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN4Halong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN4Halong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 4 Halong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN4Halong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 4 Paringin


class TanahDisdikSMPN4Paringin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Tanah Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN4Paringin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN4Paringin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN4Paringin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 5 Halong


class TanahDisdikSMPN5Halong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Tanah Disdik SMPN 5 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN5Halong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN5Halong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 5 Halong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN5Halong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik SMPN 5 Paringin


class TanahDisdikSMPN5Paringin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Tanah Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikSMPN5Paringin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Harga Tanah Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikSMPN5Paringin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikSMPN5Paringin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Foto Tanah Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Paringin


class TanahDinkesParingin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Paringin"
        verbose_name_plural = "05 Tanah Dinkes Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesParingin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Paringin"
        verbose_name_plural = "05 Harga Tanah Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesParingin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Paringin"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesParingin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Paringin"
        verbose_name_plural = "05 Foto Tanah Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Lampihong


class TanahDinkesLampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Lampihong"
        verbose_name_plural = "05 Tanah Dinkes Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesLampihong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Lampihong"
        verbose_name_plural = "05 Harga Tanah Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesLampihong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Lampihong"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesLampihong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Lampihong"
        verbose_name_plural = "05 Foto Tanah Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Batumandi


class TanahDinkesBatumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Batumandi"
        verbose_name_plural = "05 Tanah Dinkes Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesBatumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Batumandi"
        verbose_name_plural = "05 Harga Tanah Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesBatumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Batumandi"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesBatumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Batumandi"
        verbose_name_plural = "05 Foto Tanah Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Awayan


class TanahDinkesAwayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Awayan"
        verbose_name_plural = "05 Tanah Dinkes Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesAwayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Awayan"
        verbose_name_plural = "05 Harga Tanah Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesAwayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Awayan"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesAwayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Awayan"
        verbose_name_plural = "05 Foto Tanah Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Juai


class TanahDinkesJuai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Juai"
        verbose_name_plural = "05 Tanah Dinkes Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesJuai(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Juai"
        verbose_name_plural = "05 Harga Tanah Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesJuai(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Juai"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesJuai(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Juai"
        verbose_name_plural = "05 Foto Tanah Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Halong


class TanahDinkesHalong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Halong"
        verbose_name_plural = "05 Tanah Dinkes Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesHalong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Halong"
        verbose_name_plural = "05 Harga Tanah Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesHalong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Halong"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesHalong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Halong"
        verbose_name_plural = "05 Foto Tanah Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Lokbatu


class TanahDinkesLokbatu(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Lokbatu"
        verbose_name_plural = "05 Tanah Dinkes Lokbatu"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesLokbatu(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Lokbatu"
        verbose_name_plural = "05 Harga Tanah Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesLokbatu(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Lokbatu"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesLokbatu(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Lokbatu"
        verbose_name_plural = "05 Foto Tanah Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Uren


class TanahDinkesUren(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Uren"
        verbose_name_plural = "05 Tanah Dinkes Uren"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesUren(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Uren"
        verbose_name_plural = "05 Harga Tanah Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesUren(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Uren"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesUren(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Uren"
        verbose_name_plural = "05 Foto Tanah Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Pirsus


class TanahDinkesPirsus(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Pirsus"
        verbose_name_plural = "05 Tanah Dinkes Pirsus"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesPirsus(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Pirsus"
        verbose_name_plural = "05 Harga Tanah Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesPirsus(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Pirsus"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesPirsus(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Pirsus"
        verbose_name_plural = "05 Foto Tanah Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Paringin Selatan


class TanahDinkesParinginSelatan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Paringin Selatan"
        verbose_name_plural = "05 Tanah Dinkes Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesParinginSelatan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Paringin Selatan"
        verbose_name_plural = "05 Harga Tanah Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesParinginSelatan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Paringin Selatan"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesParinginSelatan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Paringin Selatan"
        verbose_name_plural = "05 Foto Tanah Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Tebing Tinggi


class TanahDinkesTebingTinggi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Tanah Dinkes Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesTebingTinggi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Harga Tanah Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesTebingTinggi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Tebing Tinggi"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesTebingTinggi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Foto Tanah Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Tanah Habang


class TanahDinkesTanahHabang(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Tanah Habang"
        verbose_name_plural = "05 Tanah Dinkes Tanah Habang"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesTanahHabang(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Tanah Habang"
        verbose_name_plural = "05 Harga Tanah Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesTanahHabang(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Tanah Habang"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesTanahHabang(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Tanah Habang"
        verbose_name_plural = "05 Foto Tanah Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes RSUD


class TanahDinkesRSUD(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes RSUD"
        verbose_name_plural = "05 Tanah Dinkes RSUD"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesRSUD(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes RSUD"
        verbose_name_plural = "05 Harga Tanah Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesRSUD(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes RSUD"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesRSUD(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes RSUD"
        verbose_name_plural = "05 Foto Tanah Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Paringin


class TanahDisdikParingin(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Paringin"
        verbose_name_plural = "07 Tanah Disdik Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikParingin(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Paringin"
        verbose_name_plural = "07 Harga Tanah Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikParingin(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Paringin"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikParingin(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Paringin"
        verbose_name_plural = "07 Foto Tanah Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Lampihong


class TanahDisdikLampihong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Lampihong"
        verbose_name_plural = "07 Tanah Disdik Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikLampihong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Lampihong"
        verbose_name_plural = "07 Harga Tanah Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikLampihong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Lampihong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikLampihong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Lampihong"
        verbose_name_plural = "07 Foto Tanah Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Awayan


class TanahDisdikAwayan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Awayan"
        verbose_name_plural = "07 Tanah Disdik Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikAwayan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Awayan"
        verbose_name_plural = "07 Harga Tanah Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikAwayan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Awayan"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikAwayan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Awayan"
        verbose_name_plural = "07 Foto Tanah Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Batumandi


class TanahDisdikBatumandi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Batumandi"
        verbose_name_plural = "07 Tanah Disdik Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikBatumandi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Batumandi"
        verbose_name_plural = "07 Harga Tanah Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikBatumandi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Batumandi"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikBatumandi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Batumandi"
        verbose_name_plural = "07 Foto Tanah Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Juai


class TanahDisdikJuai(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Juai"
        verbose_name_plural = "07 Tanah Disdik Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikJuai(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Juai"
        verbose_name_plural = "07 Harga Tanah Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikJuai(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Juai"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikJuai(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Juai"
        verbose_name_plural = "07 Foto Tanah Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Halong


class TanahDisdikHalong(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Halong"
        verbose_name_plural = "07 Tanah Disdik Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikHalong(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Halong"
        verbose_name_plural = "07 Harga Tanah Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikHalong(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Halong"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikHalong(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Halong"
        verbose_name_plural = "07 Foto Tanah Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Tebing Tinggi


class TanahDisdikTebingTinggi(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Tebing Tinggi"
        verbose_name_plural = "07 Tanah Disdik Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikTebingTinggi(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Tebing Tinggi"
        verbose_name_plural = "07 Harga Tanah Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikTebingTinggi(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Tebing Tinggi"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikTebingTinggi(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Tebing Tinggi"
        verbose_name_plural = "07 Foto Tanah Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Paringin Selatan


class TanahDisdikParinginSelatan(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Paringin Selatan"
        verbose_name_plural = "07 Tanah Disdik Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikParinginSelatan(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Paringin Selatan"
        verbose_name_plural = "07 Harga Tanah Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikParinginSelatan(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Paringin Selatan"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikParinginSelatan(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Paringin Selatan"
        verbose_name_plural = "07 Foto Tanah Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Disdik Kantor


class TanahDisdikKantor(Tanah):
    class Meta:
        proxy = True
        verbose_name = "07 Tanah Disdik Kantor"
        verbose_name_plural = "07 Tanah Disdik Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDisdikKantor(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Harga Tanah Disdik Kantor"
        verbose_name_plural = "07 Harga Tanah Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDisdikKantor(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal Tanah Disdik Kantor"
        verbose_name_plural = "07 SKPD Asal Tanah Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDisdikKantor(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "07 Foto Tanah Disdik Kantor"
        verbose_name_plural = "07 Foto Tanah Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




#Dinkes Kantor


class TanahDinkesKantor(Tanah):
    class Meta:
        proxy = True
        verbose_name = "05 Tanah Dinkes Kantor"
        verbose_name_plural = "05 Tanah Dinkes Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaTanahDinkesKantor(HargaTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Harga Tanah Dinkes Kantor"
        verbose_name_plural = "05 Harga Tanah Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_tanah)



class SKPDAsalTanahDinkesKantor(SKPDAsalTanah):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal Tanah Dinkes Kantor"
        verbose_name_plural = "05 SKPD Asal Tanah Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoTanahDinkesKantor(FotoTanah):
    class Meta:
        proxy = True
        verbose_name = "05 Foto Tanah Dinkes Kantor"
        verbose_name_plural = "05 Foto Tanah Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_tanah)




