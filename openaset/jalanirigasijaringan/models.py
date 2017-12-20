### $Id: models.py,v 1.37 2017/12/10 01:55:49 muntaza Exp $



from django.db import models

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah



### Kumpulan Table KIB D Jalan, Irigasi dan Jaringan

class JalanIrigasiJaringan(models.Model):
    id = models.AutoField(primary_key=True,
                    verbose_name="Register",
                    db_column="id")
    id_sub_skpd = models.ForeignKey(SUBSKPD,
                    verbose_name="SUB SKPD",
                    db_column="id_sub_skpd")
    id_golongan_barang = models.ForeignKey(GolonganBarang,
                    verbose_name="Golongan Barang",
                    default=4,
                    db_column="id_golongan_barang")
    nama_barang = models.CharField("Nama Barang",
                    max_length=300,
                    db_column="nama_barang")
    id_kode_barang = models.ForeignKey(KodeBarang,
                    verbose_name="Kode Barang",
                    limit_choices_to = {'id__gt': 7620, 'id__lt': 8253},
                    db_column="id_kode_barang")
    id_keadaan_barang = models.ForeignKey(KeadaanBarang,
                    default=1,
                    verbose_name="Keadaan Barang",
                    db_column="id_keadaan_barang")
    konstruksi = models.CharField("Konstruksi",
                    max_length=200,
                    help_text="Misalnya: Aspal, Beton dan lain sebagainya",
                    db_column="konstruksi")
    panjang = models.DecimalField("Panjang",
                    max_digits=15, decimal_places=2, default=0,
                    help_text="diisi dalam satuan M",
                    db_column="panjang")
    lebar = models.DecimalField("Lebar",
                    max_digits=15, decimal_places=2, default=0,
                    help_text="diisi dalam satuan M",
                    db_column="lebar")
    luas = models.DecimalField("Luas",
                    max_digits=15, decimal_places=2, default=0,
                    help_text="diisi dalam satuan M2",
                    db_column="luas")
    tanggal_dokumen = models.DateField("Tanggal Dokumen",
                    null=True, blank=True,
                    db_column="tanggal_dokumen")
    nomor_dokumen = models.CharField("Nomor Dokumen",
                    max_length=300,
                    null=True, blank=True,
                    db_column="nomor_dokumen")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun Awal",
                    help_text="Tahun Awal Kapitalisasi",
                    db_column="tahun")
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
        db_table = "jalan_irigasi_jaringan"
        verbose_name = "Jalan Irigasi Jaringan"
        verbose_name_plural = "Jalan Irigasi Jaringan"

    def __unicode__(self):
        return self.nama_barang



#untuk menampung inline TahunBerkurangUsulHapusJalanIrigasiJaringan
class JalanIrigasiJaringanUsulHapus(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "Jalan Irigasi Jaringan Usul Hapus"
        verbose_name_plural = "Jalan Irigasi Jaringan Usul Hapus"

    def __unicode__(self):
        return self.nama_barang



#untuk menampung inline PenghapusanJalanIrigasiJaringan
class JalanIrigasiJaringanPenghapusan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "Jalan Irigasi Jaringan Penghapusan"
        verbose_name_plural = "Jalan Irigasi Jaringan Penghapusan"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline PemanfaatanJalanIrigasiJaringan
class JalanIrigasiJaringanPemanfaatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "Jalan Irigasi Jaringan Pemanfaatan"
        verbose_name_plural = "Jalan Irigasi Jaringan Pemanfaatan"

    def __unicode__(self):
        return self.nama_barang


class KontrakJalanIrigasiJaringan(models.Model):
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
        db_table = "kontrak_jalan_irigasi_jaringan"
	verbose_name = "Kontrak Jalan Irigasi Jaringan"
        verbose_name_plural = "Kontrak Jalan Irigasi Jaringan"

    def __unicode__(self):
        return self.nomor_sp2d



class TahunBerkurangUsulHapusJalanIrigasiJaringan(models.Model):
    id = models.OneToOneField(JalanIrigasiJaringan, primary_key=True,
                    db_column="id_jalan_irigasi_jaringan")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_usul_hapus_jij"
	verbose_name = "Tahun Berkurang Usul Hapus JIJ"
        verbose_name_plural = "Tahun Berkurang Usul Hapus JIJ"

    def __unicode__(self):
        return "%s" % (self.id)




class TahunBerkurangJalanIrigasiJaringan(models.Model):
    id = models.OneToOneField(JalanIrigasiJaringan, primary_key=True,
                    db_column="id_jalan_irigasi_jaringan")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_jij"
	verbose_name = "Tahun Berkurang JIJ"
        verbose_name_plural = "Tahun Berkurang JIJ"

    def __unicode__(self):
        return "%s" % (self.id)




class PenghapusanJalanIrigasiJaringan(models.Model):
    id = models.OneToOneField(JalanIrigasiJaringan, primary_key=True,
                    db_column="id_jalan_irigasi_jaringan")
    id_sk_penghapusan = models.ForeignKey(SKPenghapusan,
                    verbose_name="SK Penghapusan",
                    db_column="id_sk_penghapusan")

    class Meta:
        db_table = "penghapusan_jalan_irigasi_jaringan"
	verbose_name = "Penghapusan Jalan Irigasi Jaringan"
        verbose_name_plural = "Penghapusan Jalan Irigasi Jaringan"

    def __unicode__(self):
        return "%s" % (self.id)


class PemanfaatanJalanIrigasiJaringan(models.Model):
    id = models.OneToOneField(JalanIrigasiJaringan, primary_key=True,
                    db_column="id_jalan_irigasi_jaringan")
    id_jenis_pemanfaatan = models.ForeignKey(JenisPemanfaatan,
                    verbose_name="Jenis Pemanfaatan",
                    db_column="id_jenis_pemanfaatan")

    class Meta:
        db_table = "pemanfaatan_jalan_irigasi_jaringan"
	verbose_name = "Pemanfaatan Jalan Irigasi Jaringan"
        verbose_name_plural = "Pemanfaatan Jalan Irigasi Jaringan"

    def __unicode__(self):
        return "%s" % (self.id)


class HargaJalanIrigasiJaringan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_jalan_irigasi_jaringan = models.ForeignKey(JalanIrigasiJaringan,
                    verbose_name="Jalan Irigasi Jaringan",
                    db_column="id_jalan_irigasi_jaringan")
    id_asal_usul = models.ForeignKey(AsalUsul,
                    verbose_name="Asal Usul",
                    db_column="id_asal_usul")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun",
                    help_text="Tahun Anggaran",
                    db_column="tahun")
    id_kontrak_jalan_irigasi_jaringan = models.ForeignKey(KontrakJalanIrigasiJaringan,
                    verbose_name="Kontrak Jalan Irigasi Jaringan",
                    db_column="id_kontrak_jalan_irigasi_jaringan")
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
        db_table = "harga_jalan_irigasi_jaringan"
	verbose_name = "Harga Jalan Irigasi Jaringan"
        verbose_name_plural = "Harga Jalan Irigasi Jaringan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)





#KDP JIJ Reklas, untuk menampung data JIJ Reklas kabupaten
class KDPJalanIrigasiJaringanReklas(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "KDP JIJ Reklas"
        verbose_name_plural = "KDP JIJ Reklas"

    def __unicode__(self):
        return self.nama_barang






#KDP JIJ, untuk menampung data JIJ kabupaten
class KDPJalanIrigasiJaringan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "KDP JIJ"
        verbose_name_plural = "KDP JIJ"

    def __unicode__(self):
        return self.nama_barang



class SKPDAsalJalanIrigasiJaringan(models.Model):
    id = models.OneToOneField(JalanIrigasiJaringan, primary_key=True,
                    db_column="id_jalan_irigasi_jaringan")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_asal_jalan_irigasi_jaringan"
	verbose_name = "SKPD Asal Jalan Irigasi Jaringan"
        verbose_name_plural = "SKPD Asal Jalan Irigasi Jaringan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringan(models.Model):
    id = models.OneToOneField(JalanIrigasiJaringan, primary_key=True,
                    db_column="id_jalan_irigasi_jaringan")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_tujuan_jalan_irigasi_jaringan"
	verbose_name = "SKPD Tujuan Jalan Irigasi Jaringan"
        verbose_name_plural = "SKPD Tujuan Jalan Irigasi Jaringan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringan(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_jalan_irigasi_jaringan = models.ForeignKey(JalanIrigasiJaringan,
                    verbose_name="Jalan Irigasi Jaringan",
                    db_column="id_jalan_irigasi_jaringan")
    foto = models.FileField("Foto",
                    upload_to='jalan_irigasi_jaringan/',
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
        db_table = "foto_jalan_irigasi_jaringan"
	verbose_name = "Foto Jalan Irigasi Jaringan"
        verbose_name_plural = "Foto Jalan Irigasi Jaringan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Setwan
##model pada app Setwan
class JalanIrigasiJaringanSetwan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 JIJ Setwan"
        verbose_name_plural = "01 JIJ Setwan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanSetwan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 KDP JIJ Setwan"
        verbose_name_plural = "01 KDP JIJ Setwan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusSetwan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 JIJ Usul Hapus Setwan"
        verbose_name_plural = "01 JIJ Usul Hapus Setwan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanSetwan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 Usul Hapus JIJ Setwan"
        verbose_name_plural = "01 Usul Hapus JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanSetwan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 Kontrak JIJ Setwan"
        verbose_name_plural = "01 Kontrak JIJ Setwan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanSetwan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 Harga JIJ Setwan"
        verbose_name_plural = "01 Harga JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanSetwan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 JIJ Penghapusan Setwan"
        verbose_name_plural = "01 JIJ Penghapusan Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanSetwan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 Tahun Berkurang JIJ Setwan"
        verbose_name_plural = "01 Tahun Berkurang JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanSetwan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 Penghapusan JIJ Setwan"
        verbose_name_plural = "01 Penghapusan JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanSetwan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Asal JIJ Setwan"
        verbose_name_plural = "01 SKPD Asal JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanSetwan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Tujuan JIJ Setwan"
        verbose_name_plural = "01 SKPD Tujuan JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanSetwan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "01 Foto JIJ Setwan"
        verbose_name_plural = "01 Foto JIJ Setwan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Setda
##model pada app Setda
class JalanIrigasiJaringanSetda(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 JIJ Setda"
        verbose_name_plural = "02 JIJ Setda"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanSetda(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 KDP JIJ Setda"
        verbose_name_plural = "02 KDP JIJ Setda"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusSetda(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 JIJ Usul Hapus Setda"
        verbose_name_plural = "02 JIJ Usul Hapus Setda"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanSetda(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 Usul Hapus JIJ Setda"
        verbose_name_plural = "02 Usul Hapus JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanSetda(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 Kontrak JIJ Setda"
        verbose_name_plural = "02 Kontrak JIJ Setda"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanSetda(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 Harga JIJ Setda"
        verbose_name_plural = "02 Harga JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanSetda(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 JIJ Penghapusan Setda"
        verbose_name_plural = "02 JIJ Penghapusan Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanSetda(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 Tahun Berkurang JIJ Setda"
        verbose_name_plural = "02 Tahun Berkurang JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanSetda(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 Penghapusan JIJ Setda"
        verbose_name_plural = "02 Penghapusan JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanSetda(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Asal JIJ Setda"
        verbose_name_plural = "02 SKPD Asal JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanSetda(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Tujuan JIJ Setda"
        verbose_name_plural = "02 SKPD Tujuan JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanSetda(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "02 Foto JIJ Setda"
        verbose_name_plural = "02 Foto JIJ Setda"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DPUPR
##model pada app DPUPR
class JalanIrigasiJaringanDPUPR(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 JIJ DPUPR"
        verbose_name_plural = "03 JIJ DPUPR"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDPUPR(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 KDP JIJ DPUPR"
        verbose_name_plural = "03 KDP JIJ DPUPR"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDPUPR(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 JIJ Usul Hapus DPUPR"
        verbose_name_plural = "03 JIJ Usul Hapus DPUPR"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPUPR(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 Usul Hapus JIJ DPUPR"
        verbose_name_plural = "03 Usul Hapus JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDPUPR(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 Kontrak JIJ DPUPR"
        verbose_name_plural = "03 Kontrak JIJ DPUPR"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDPUPR(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 Harga JIJ DPUPR"
        verbose_name_plural = "03 Harga JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDPUPR(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 JIJ Penghapusan DPUPR"
        verbose_name_plural = "03 JIJ Penghapusan DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDPUPR(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 Tahun Berkurang JIJ DPUPR"
        verbose_name_plural = "03 Tahun Berkurang JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDPUPR(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 Penghapusan JIJ DPUPR"
        verbose_name_plural = "03 Penghapusan JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDPUPR(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Asal JIJ DPUPR"
        verbose_name_plural = "03 SKPD Asal JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDPUPR(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Tujuan JIJ DPUPR"
        verbose_name_plural = "03 SKPD Tujuan JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDPUPR(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "03 Foto JIJ DPUPR"
        verbose_name_plural = "03 Foto JIJ DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Dishub
##model pada app Dishub
class JalanIrigasiJaringanDishub(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 JIJ Dishub"
        verbose_name_plural = "04 JIJ Dishub"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDishub(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 KDP JIJ Dishub"
        verbose_name_plural = "04 KDP JIJ Dishub"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDishub(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 JIJ Usul Hapus Dishub"
        verbose_name_plural = "04 JIJ Usul Hapus Dishub"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDishub(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 Usul Hapus JIJ Dishub"
        verbose_name_plural = "04 Usul Hapus JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDishub(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 Kontrak JIJ Dishub"
        verbose_name_plural = "04 Kontrak JIJ Dishub"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDishub(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 Harga JIJ Dishub"
        verbose_name_plural = "04 Harga JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDishub(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 JIJ Penghapusan Dishub"
        verbose_name_plural = "04 JIJ Penghapusan Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDishub(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 Tahun Berkurang JIJ Dishub"
        verbose_name_plural = "04 Tahun Berkurang JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDishub(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 Penghapusan JIJ Dishub"
        verbose_name_plural = "04 Penghapusan JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDishub(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Asal JIJ Dishub"
        verbose_name_plural = "04 SKPD Asal JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDishub(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Tujuan JIJ Dishub"
        verbose_name_plural = "04 SKPD Tujuan JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDishub(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "04 Foto JIJ Dishub"
        verbose_name_plural = "04 Foto JIJ Dishub"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Dinkes
##model pada app Dinkes
class JalanIrigasiJaringanDinkes(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes"
        verbose_name_plural = "05 JIJ Dinkes"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDinkes(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 KDP JIJ Dinkes"
        verbose_name_plural = "05 KDP JIJ Dinkes"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDinkes(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Usul Hapus Dinkes"
        verbose_name_plural = "05 JIJ Usul Hapus Dinkes"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDinkes(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Usul Hapus JIJ Dinkes"
        verbose_name_plural = "05 Usul Hapus JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDinkes(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Kontrak JIJ Dinkes"
        verbose_name_plural = "05 Kontrak JIJ Dinkes"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDinkes(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes"
        verbose_name_plural = "05 Harga JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDinkes(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Penghapusan Dinkes"
        verbose_name_plural = "05 JIJ Penghapusan Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDinkes(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Tahun Berkurang JIJ Dinkes"
        verbose_name_plural = "05 Tahun Berkurang JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDinkes(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Penghapusan JIJ Dinkes"
        verbose_name_plural = "05 Penghapusan JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDinkes(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDinkes(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Tujuan JIJ Dinkes"
        verbose_name_plural = "05 SKPD Tujuan JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkes(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes"
        verbose_name_plural = "05 Foto JIJ Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##RSUD
##model pada app RSUD
class JalanIrigasiJaringanRSUD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 JIJ RSUD"
        verbose_name_plural = "06 JIJ RSUD"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanRSUD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 KDP JIJ RSUD"
        verbose_name_plural = "06 KDP JIJ RSUD"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusRSUD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 JIJ Usul Hapus RSUD"
        verbose_name_plural = "06 JIJ Usul Hapus RSUD"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanRSUD(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 Usul Hapus JIJ RSUD"
        verbose_name_plural = "06 Usul Hapus JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanRSUD(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 Kontrak JIJ RSUD"
        verbose_name_plural = "06 Kontrak JIJ RSUD"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanRSUD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 Harga JIJ RSUD"
        verbose_name_plural = "06 Harga JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanRSUD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 JIJ Penghapusan RSUD"
        verbose_name_plural = "06 JIJ Penghapusan RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanRSUD(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 Tahun Berkurang JIJ RSUD"
        verbose_name_plural = "06 Tahun Berkurang JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanRSUD(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 Penghapusan JIJ RSUD"
        verbose_name_plural = "06 Penghapusan JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanRSUD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Asal JIJ RSUD"
        verbose_name_plural = "06 SKPD Asal JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanRSUD(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Tujuan JIJ RSUD"
        verbose_name_plural = "06 SKPD Tujuan JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanRSUD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "06 Foto JIJ RSUD"
        verbose_name_plural = "06 Foto JIJ RSUD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Disdik
##model pada app Disdik
class JalanIrigasiJaringanDisdik(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik"
        verbose_name_plural = "07 JIJ Disdik"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDisdik(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 KDP JIJ Disdik"
        verbose_name_plural = "07 KDP JIJ Disdik"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDisdik(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Usul Hapus Disdik"
        verbose_name_plural = "07 JIJ Usul Hapus Disdik"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDisdik(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Usul Hapus JIJ Disdik"
        verbose_name_plural = "07 Usul Hapus JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDisdik(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Kontrak JIJ Disdik"
        verbose_name_plural = "07 Kontrak JIJ Disdik"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDisdik(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik"
        verbose_name_plural = "07 Harga JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDisdik(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Penghapusan Disdik"
        verbose_name_plural = "07 JIJ Penghapusan Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDisdik(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Tahun Berkurang JIJ Disdik"
        verbose_name_plural = "07 Tahun Berkurang JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDisdik(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Penghapusan JIJ Disdik"
        verbose_name_plural = "07 Penghapusan JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDisdik(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDisdik(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Tujuan JIJ Disdik"
        verbose_name_plural = "07 SKPD Tujuan JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdik(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik"
        verbose_name_plural = "07 Foto JIJ Disdik"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Perpustakaan
##model pada app Perpustakaan
class JalanIrigasiJaringanPerpustakaan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 JIJ Perpustakaan"
        verbose_name_plural = "08 JIJ Perpustakaan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanPerpustakaan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 KDP JIJ Perpustakaan"
        verbose_name_plural = "08 KDP JIJ Perpustakaan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusPerpustakaan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 JIJ Usul Hapus Perpustakaan"
        verbose_name_plural = "08 JIJ Usul Hapus Perpustakaan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanPerpustakaan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 Usul Hapus JIJ Perpustakaan"
        verbose_name_plural = "08 Usul Hapus JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanPerpustakaan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 Kontrak JIJ Perpustakaan"
        verbose_name_plural = "08 Kontrak JIJ Perpustakaan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanPerpustakaan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 Harga JIJ Perpustakaan"
        verbose_name_plural = "08 Harga JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanPerpustakaan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 JIJ Penghapusan Perpustakaan"
        verbose_name_plural = "08 JIJ Penghapusan Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanPerpustakaan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 Tahun Berkurang JIJ Perpustakaan"
        verbose_name_plural = "08 Tahun Berkurang JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanPerpustakaan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 Penghapusan JIJ Perpustakaan"
        verbose_name_plural = "08 Penghapusan JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanPerpustakaan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Asal JIJ Perpustakaan"
        verbose_name_plural = "08 SKPD Asal JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanPerpustakaan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Tujuan JIJ Perpustakaan"
        verbose_name_plural = "08 SKPD Tujuan JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanPerpustakaan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "08 Foto JIJ Perpustakaan"
        verbose_name_plural = "08 Foto JIJ Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Sosial
##model pada app Sosial
class JalanIrigasiJaringanSosial(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 JIJ Sosial"
        verbose_name_plural = "09 JIJ Sosial"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanSosial(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 KDP JIJ Sosial"
        verbose_name_plural = "09 KDP JIJ Sosial"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusSosial(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 JIJ Usul Hapus Sosial"
        verbose_name_plural = "09 JIJ Usul Hapus Sosial"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanSosial(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 Usul Hapus JIJ Sosial"
        verbose_name_plural = "09 Usul Hapus JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanSosial(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 Kontrak JIJ Sosial"
        verbose_name_plural = "09 Kontrak JIJ Sosial"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanSosial(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 Harga JIJ Sosial"
        verbose_name_plural = "09 Harga JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanSosial(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 JIJ Penghapusan Sosial"
        verbose_name_plural = "09 JIJ Penghapusan Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanSosial(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 Tahun Berkurang JIJ Sosial"
        verbose_name_plural = "09 Tahun Berkurang JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanSosial(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 Penghapusan JIJ Sosial"
        verbose_name_plural = "09 Penghapusan JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanSosial(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Asal JIJ Sosial"
        verbose_name_plural = "09 SKPD Asal JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanSosial(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Tujuan JIJ Sosial"
        verbose_name_plural = "09 SKPD Tujuan JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanSosial(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "09 Foto JIJ Sosial"
        verbose_name_plural = "09 Foto JIJ Sosial"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DPMD
##model pada app DPMD
class JalanIrigasiJaringanDPMD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 JIJ DPMD"
        verbose_name_plural = "10 JIJ DPMD"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDPMD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 KDP JIJ DPMD"
        verbose_name_plural = "10 KDP JIJ DPMD"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDPMD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 JIJ Usul Hapus DPMD"
        verbose_name_plural = "10 JIJ Usul Hapus DPMD"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPMD(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 Usul Hapus JIJ DPMD"
        verbose_name_plural = "10 Usul Hapus JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDPMD(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 Kontrak JIJ DPMD"
        verbose_name_plural = "10 Kontrak JIJ DPMD"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDPMD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 Harga JIJ DPMD"
        verbose_name_plural = "10 Harga JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDPMD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 JIJ Penghapusan DPMD"
        verbose_name_plural = "10 JIJ Penghapusan DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDPMD(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 Tahun Berkurang JIJ DPMD"
        verbose_name_plural = "10 Tahun Berkurang JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDPMD(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 Penghapusan JIJ DPMD"
        verbose_name_plural = "10 Penghapusan JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDPMD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Asal JIJ DPMD"
        verbose_name_plural = "10 SKPD Asal JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDPMD(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Tujuan JIJ DPMD"
        verbose_name_plural = "10 SKPD Tujuan JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDPMD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "10 Foto JIJ DPMD"
        verbose_name_plural = "10 Foto JIJ DPMD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DPPPA
##model pada app DPPPA
class JalanIrigasiJaringanDPPPA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 JIJ DPPPA"
        verbose_name_plural = "11 JIJ DPPPA"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDPPPA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 KDP JIJ DPPPA"
        verbose_name_plural = "11 KDP JIJ DPPPA"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDPPPA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 JIJ Usul Hapus DPPPA"
        verbose_name_plural = "11 JIJ Usul Hapus DPPPA"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPPPA(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 Usul Hapus JIJ DPPPA"
        verbose_name_plural = "11 Usul Hapus JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDPPPA(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 Kontrak JIJ DPPPA"
        verbose_name_plural = "11 Kontrak JIJ DPPPA"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDPPPA(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 Harga JIJ DPPPA"
        verbose_name_plural = "11 Harga JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDPPPA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 JIJ Penghapusan DPPPA"
        verbose_name_plural = "11 JIJ Penghapusan DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDPPPA(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 Tahun Berkurang JIJ DPPPA"
        verbose_name_plural = "11 Tahun Berkurang JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDPPPA(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 Penghapusan JIJ DPPPA"
        verbose_name_plural = "11 Penghapusan JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDPPPA(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Asal JIJ DPPPA"
        verbose_name_plural = "11 SKPD Asal JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDPPPA(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Tujuan JIJ DPPPA"
        verbose_name_plural = "11 SKPD Tujuan JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDPPPA(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "11 Foto JIJ DPPPA"
        verbose_name_plural = "11 Foto JIJ DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DukCatPil
##model pada app DukCatPil
class JalanIrigasiJaringanDukCatPil(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 JIJ DukCatPil"
        verbose_name_plural = "12 JIJ DukCatPil"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDukCatPil(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 KDP JIJ DukCatPil"
        verbose_name_plural = "12 KDP JIJ DukCatPil"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDukCatPil(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 JIJ Usul Hapus DukCatPil"
        verbose_name_plural = "12 JIJ Usul Hapus DukCatPil"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDukCatPil(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 Usul Hapus JIJ DukCatPil"
        verbose_name_plural = "12 Usul Hapus JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDukCatPil(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 Kontrak JIJ DukCatPil"
        verbose_name_plural = "12 Kontrak JIJ DukCatPil"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDukCatPil(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 Harga JIJ DukCatPil"
        verbose_name_plural = "12 Harga JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDukCatPil(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 JIJ Penghapusan DukCatPil"
        verbose_name_plural = "12 JIJ Penghapusan DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDukCatPil(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 Tahun Berkurang JIJ DukCatPil"
        verbose_name_plural = "12 Tahun Berkurang JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDukCatPil(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 Penghapusan JIJ DukCatPil"
        verbose_name_plural = "12 Penghapusan JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDukCatPil(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Asal JIJ DukCatPil"
        verbose_name_plural = "12 SKPD Asal JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDukCatPil(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Tujuan JIJ DukCatPil"
        verbose_name_plural = "12 SKPD Tujuan JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDukCatPil(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "12 Foto JIJ DukCatPil"
        verbose_name_plural = "12 Foto JIJ DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Pertanian
##model pada app Pertanian
class JalanIrigasiJaringanPertanian(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 JIJ Pertanian"
        verbose_name_plural = "13 JIJ Pertanian"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanPertanian(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 KDP JIJ Pertanian"
        verbose_name_plural = "13 KDP JIJ Pertanian"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusPertanian(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 JIJ Usul Hapus Pertanian"
        verbose_name_plural = "13 JIJ Usul Hapus Pertanian"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanPertanian(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 Usul Hapus JIJ Pertanian"
        verbose_name_plural = "13 Usul Hapus JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanPertanian(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 Kontrak JIJ Pertanian"
        verbose_name_plural = "13 Kontrak JIJ Pertanian"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanPertanian(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 Harga JIJ Pertanian"
        verbose_name_plural = "13 Harga JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanPertanian(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 JIJ Penghapusan Pertanian"
        verbose_name_plural = "13 JIJ Penghapusan Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanPertanian(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 Tahun Berkurang JIJ Pertanian"
        verbose_name_plural = "13 Tahun Berkurang JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanPertanian(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 Penghapusan JIJ Pertanian"
        verbose_name_plural = "13 Penghapusan JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanPertanian(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Asal JIJ Pertanian"
        verbose_name_plural = "13 SKPD Asal JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanPertanian(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Tujuan JIJ Pertanian"
        verbose_name_plural = "13 SKPD Tujuan JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanPertanian(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "13 Foto JIJ Pertanian"
        verbose_name_plural = "13 Foto JIJ Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Kehutanan
##model pada app Kehutanan
class JalanIrigasiJaringanKehutanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 JIJ Kehutanan"
        verbose_name_plural = "14 JIJ Kehutanan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanKehutanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 KDP JIJ Kehutanan"
        verbose_name_plural = "14 KDP JIJ Kehutanan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusKehutanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 JIJ Usul Hapus Kehutanan"
        verbose_name_plural = "14 JIJ Usul Hapus Kehutanan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanKehutanan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 Usul Hapus JIJ Kehutanan"
        verbose_name_plural = "14 Usul Hapus JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanKehutanan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 Kontrak JIJ Kehutanan"
        verbose_name_plural = "14 Kontrak JIJ Kehutanan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanKehutanan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 Harga JIJ Kehutanan"
        verbose_name_plural = "14 Harga JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanKehutanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 JIJ Penghapusan Kehutanan"
        verbose_name_plural = "14 JIJ Penghapusan Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanKehutanan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 Tahun Berkurang JIJ Kehutanan"
        verbose_name_plural = "14 Tahun Berkurang JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanKehutanan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 Penghapusan JIJ Kehutanan"
        verbose_name_plural = "14 Penghapusan JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanKehutanan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Asal JIJ Kehutanan"
        verbose_name_plural = "14 SKPD Asal JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanKehutanan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Tujuan JIJ Kehutanan"
        verbose_name_plural = "14 SKPD Tujuan JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanKehutanan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "14 Foto JIJ Kehutanan"
        verbose_name_plural = "14 Foto JIJ Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DKP
##model pada app DKP
class JalanIrigasiJaringanDKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 JIJ DKP"
        verbose_name_plural = "15 JIJ DKP"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 KDP JIJ DKP"
        verbose_name_plural = "15 KDP JIJ DKP"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 JIJ Usul Hapus DKP"
        verbose_name_plural = "15 JIJ Usul Hapus DKP"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDKP(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 Usul Hapus JIJ DKP"
        verbose_name_plural = "15 Usul Hapus JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDKP(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 Kontrak JIJ DKP"
        verbose_name_plural = "15 Kontrak JIJ DKP"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDKP(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 Harga JIJ DKP"
        verbose_name_plural = "15 Harga JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 JIJ Penghapusan DKP"
        verbose_name_plural = "15 JIJ Penghapusan DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDKP(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 Tahun Berkurang JIJ DKP"
        verbose_name_plural = "15 Tahun Berkurang JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDKP(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 Penghapusan JIJ DKP"
        verbose_name_plural = "15 Penghapusan JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDKP(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Asal JIJ DKP"
        verbose_name_plural = "15 SKPD Asal JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDKP(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Tujuan JIJ DKP"
        verbose_name_plural = "15 SKPD Tujuan JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDKP(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "15 Foto JIJ DKP"
        verbose_name_plural = "15 Foto JIJ DKP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DKUKMP
##model pada app DKUKMP
class JalanIrigasiJaringanDKUKMP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 JIJ DKUKMP"
        verbose_name_plural = "16 JIJ DKUKMP"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDKUKMP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 KDP JIJ DKUKMP"
        verbose_name_plural = "16 KDP JIJ DKUKMP"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDKUKMP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 JIJ Usul Hapus DKUKMP"
        verbose_name_plural = "16 JIJ Usul Hapus DKUKMP"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDKUKMP(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 Usul Hapus JIJ DKUKMP"
        verbose_name_plural = "16 Usul Hapus JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDKUKMP(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 Kontrak JIJ DKUKMP"
        verbose_name_plural = "16 Kontrak JIJ DKUKMP"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDKUKMP(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 Harga JIJ DKUKMP"
        verbose_name_plural = "16 Harga JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDKUKMP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 JIJ Penghapusan DKUKMP"
        verbose_name_plural = "16 JIJ Penghapusan DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDKUKMP(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 Tahun Berkurang JIJ DKUKMP"
        verbose_name_plural = "16 Tahun Berkurang JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDKUKMP(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 Penghapusan JIJ DKUKMP"
        verbose_name_plural = "16 Penghapusan JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDKUKMP(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Asal JIJ DKUKMP"
        verbose_name_plural = "16 SKPD Asal JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDKUKMP(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Tujuan JIJ DKUKMP"
        verbose_name_plural = "16 SKPD Tujuan JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDKUKMP(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "16 Foto JIJ DKUKMP"
        verbose_name_plural = "16 Foto JIJ DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Distamben
##model pada app Distamben
class JalanIrigasiJaringanDistamben(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 JIJ Distamben"
        verbose_name_plural = "17 JIJ Distamben"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDistamben(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 KDP JIJ Distamben"
        verbose_name_plural = "17 KDP JIJ Distamben"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDistamben(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 JIJ Usul Hapus Distamben"
        verbose_name_plural = "17 JIJ Usul Hapus Distamben"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDistamben(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 Usul Hapus JIJ Distamben"
        verbose_name_plural = "17 Usul Hapus JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDistamben(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 Kontrak JIJ Distamben"
        verbose_name_plural = "17 Kontrak JIJ Distamben"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDistamben(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 Harga JIJ Distamben"
        verbose_name_plural = "17 Harga JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDistamben(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 JIJ Penghapusan Distamben"
        verbose_name_plural = "17 JIJ Penghapusan Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDistamben(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 Tahun Berkurang JIJ Distamben"
        verbose_name_plural = "17 Tahun Berkurang JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDistamben(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 Penghapusan JIJ Distamben"
        verbose_name_plural = "17 Penghapusan JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDistamben(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Asal JIJ Distamben"
        verbose_name_plural = "17 SKPD Asal JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDistamben(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Tujuan JIJ Distamben"
        verbose_name_plural = "17 SKPD Tujuan JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDistamben(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "17 Foto JIJ Distamben"
        verbose_name_plural = "17 Foto JIJ Distamben"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DPMPTSP
##model pada app DPMPTSP
class JalanIrigasiJaringanDPMPTSP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 JIJ DPMPTSP"
        verbose_name_plural = "18 JIJ DPMPTSP"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDPMPTSP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 KDP JIJ DPMPTSP"
        verbose_name_plural = "18 KDP JIJ DPMPTSP"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDPMPTSP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 JIJ Usul Hapus DPMPTSP"
        verbose_name_plural = "18 JIJ Usul Hapus DPMPTSP"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPMPTSP(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 Usul Hapus JIJ DPMPTSP"
        verbose_name_plural = "18 Usul Hapus JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDPMPTSP(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 Kontrak JIJ DPMPTSP"
        verbose_name_plural = "18 Kontrak JIJ DPMPTSP"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDPMPTSP(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 Harga JIJ DPMPTSP"
        verbose_name_plural = "18 Harga JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDPMPTSP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 JIJ Penghapusan DPMPTSP"
        verbose_name_plural = "18 JIJ Penghapusan DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDPMPTSP(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 Tahun Berkurang JIJ DPMPTSP"
        verbose_name_plural = "18 Tahun Berkurang JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDPMPTSP(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 Penghapusan JIJ DPMPTSP"
        verbose_name_plural = "18 Penghapusan JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDPMPTSP(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Asal JIJ DPMPTSP"
        verbose_name_plural = "18 SKPD Asal JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDPMPTSP(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Tujuan JIJ DPMPTSP"
        verbose_name_plural = "18 SKPD Tujuan JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDPMPTSP(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "18 Foto JIJ DPMPTSP"
        verbose_name_plural = "18 Foto JIJ DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##BKD
##model pada app BKD
class JalanIrigasiJaringanBKD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 JIJ BKD"
        verbose_name_plural = "19 JIJ BKD"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBKD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 KDP JIJ BKD"
        verbose_name_plural = "19 KDP JIJ BKD"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBKD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 JIJ Usul Hapus BKD"
        verbose_name_plural = "19 JIJ Usul Hapus BKD"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBKD(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 Usul Hapus JIJ BKD"
        verbose_name_plural = "19 Usul Hapus JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBKD(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 Kontrak JIJ BKD"
        verbose_name_plural = "19 Kontrak JIJ BKD"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBKD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 Harga JIJ BKD"
        verbose_name_plural = "19 Harga JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBKD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 JIJ Penghapusan BKD"
        verbose_name_plural = "19 JIJ Penghapusan BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBKD(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 Tahun Berkurang JIJ BKD"
        verbose_name_plural = "19 Tahun Berkurang JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBKD(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 Penghapusan JIJ BKD"
        verbose_name_plural = "19 Penghapusan JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBKD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Asal JIJ BKD"
        verbose_name_plural = "19 SKPD Asal JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBKD(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Tujuan JIJ BKD"
        verbose_name_plural = "19 SKPD Tujuan JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBKD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "19 Foto JIJ BKD"
        verbose_name_plural = "19 Foto JIJ BKD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Inspektorat
##model pada app Inspektorat
class JalanIrigasiJaringanInspektorat(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 JIJ Inspektorat"
        verbose_name_plural = "20 JIJ Inspektorat"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanInspektorat(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 KDP JIJ Inspektorat"
        verbose_name_plural = "20 KDP JIJ Inspektorat"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusInspektorat(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 JIJ Usul Hapus Inspektorat"
        verbose_name_plural = "20 JIJ Usul Hapus Inspektorat"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanInspektorat(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 Usul Hapus JIJ Inspektorat"
        verbose_name_plural = "20 Usul Hapus JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanInspektorat(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 Kontrak JIJ Inspektorat"
        verbose_name_plural = "20 Kontrak JIJ Inspektorat"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanInspektorat(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 Harga JIJ Inspektorat"
        verbose_name_plural = "20 Harga JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanInspektorat(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 JIJ Penghapusan Inspektorat"
        verbose_name_plural = "20 JIJ Penghapusan Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanInspektorat(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 Tahun Berkurang JIJ Inspektorat"
        verbose_name_plural = "20 Tahun Berkurang JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanInspektorat(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 Penghapusan JIJ Inspektorat"
        verbose_name_plural = "20 Penghapusan JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanInspektorat(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Asal JIJ Inspektorat"
        verbose_name_plural = "20 SKPD Asal JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanInspektorat(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Tujuan JIJ Inspektorat"
        verbose_name_plural = "20 SKPD Tujuan JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanInspektorat(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "20 Foto JIJ Inspektorat"
        verbose_name_plural = "20 Foto JIJ Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##BAPPEDA
##model pada app BAPPEDA
class JalanIrigasiJaringanBAPPEDA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 JIJ BAPPEDA"
        verbose_name_plural = "21 JIJ BAPPEDA"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBAPPEDA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 KDP JIJ BAPPEDA"
        verbose_name_plural = "21 KDP JIJ BAPPEDA"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBAPPEDA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 JIJ Usul Hapus BAPPEDA"
        verbose_name_plural = "21 JIJ Usul Hapus BAPPEDA"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBAPPEDA(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 Usul Hapus JIJ BAPPEDA"
        verbose_name_plural = "21 Usul Hapus JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBAPPEDA(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 Kontrak JIJ BAPPEDA"
        verbose_name_plural = "21 Kontrak JIJ BAPPEDA"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBAPPEDA(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 Harga JIJ BAPPEDA"
        verbose_name_plural = "21 Harga JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBAPPEDA(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 JIJ Penghapusan BAPPEDA"
        verbose_name_plural = "21 JIJ Penghapusan BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBAPPEDA(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 Tahun Berkurang JIJ BAPPEDA"
        verbose_name_plural = "21 Tahun Berkurang JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBAPPEDA(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 Penghapusan JIJ BAPPEDA"
        verbose_name_plural = "21 Penghapusan JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBAPPEDA(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Asal JIJ BAPPEDA"
        verbose_name_plural = "21 SKPD Asal JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBAPPEDA(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Tujuan JIJ BAPPEDA"
        verbose_name_plural = "21 SKPD Tujuan JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBAPPEDA(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "21 Foto JIJ BAPPEDA"
        verbose_name_plural = "21 Foto JIJ BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DLH
##model pada app DLH
class JalanIrigasiJaringanDLH(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 JIJ DLH"
        verbose_name_plural = "22 JIJ DLH"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDLH(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 KDP JIJ DLH"
        verbose_name_plural = "22 KDP JIJ DLH"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDLH(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 JIJ Usul Hapus DLH"
        verbose_name_plural = "22 JIJ Usul Hapus DLH"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDLH(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 Usul Hapus JIJ DLH"
        verbose_name_plural = "22 Usul Hapus JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDLH(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 Kontrak JIJ DLH"
        verbose_name_plural = "22 Kontrak JIJ DLH"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDLH(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 Harga JIJ DLH"
        verbose_name_plural = "22 Harga JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDLH(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 JIJ Penghapusan DLH"
        verbose_name_plural = "22 JIJ Penghapusan DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDLH(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 Tahun Berkurang JIJ DLH"
        verbose_name_plural = "22 Tahun Berkurang JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDLH(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 Penghapusan JIJ DLH"
        verbose_name_plural = "22 Penghapusan JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDLH(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Asal JIJ DLH"
        verbose_name_plural = "22 SKPD Asal JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDLH(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Tujuan JIJ DLH"
        verbose_name_plural = "22 SKPD Tujuan JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDLH(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "22 Foto JIJ DLH"
        verbose_name_plural = "22 Foto JIJ DLH"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DKO
##model pada app DKO
class JalanIrigasiJaringanDKO(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 JIJ DKO"
        verbose_name_plural = "23 JIJ DKO"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDKO(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 KDP JIJ DKO"
        verbose_name_plural = "23 KDP JIJ DKO"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDKO(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 JIJ Usul Hapus DKO"
        verbose_name_plural = "23 JIJ Usul Hapus DKO"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDKO(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 Usul Hapus JIJ DKO"
        verbose_name_plural = "23 Usul Hapus JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDKO(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 Kontrak JIJ DKO"
        verbose_name_plural = "23 Kontrak JIJ DKO"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDKO(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 Harga JIJ DKO"
        verbose_name_plural = "23 Harga JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDKO(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 JIJ Penghapusan DKO"
        verbose_name_plural = "23 JIJ Penghapusan DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDKO(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 Tahun Berkurang JIJ DKO"
        verbose_name_plural = "23 Tahun Berkurang JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDKO(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 Penghapusan JIJ DKO"
        verbose_name_plural = "23 Penghapusan JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDKO(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Asal JIJ DKO"
        verbose_name_plural = "23 SKPD Asal JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDKO(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Tujuan JIJ DKO"
        verbose_name_plural = "23 SKPD Tujuan JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDKO(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "23 Foto JIJ DKO"
        verbose_name_plural = "23 Foto JIJ DKO"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##KESBANGPOL
##model pada app KESBANGPOL
class JalanIrigasiJaringanKESBANGPOL(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 JIJ KESBANGPOL"
        verbose_name_plural = "24 JIJ KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanKESBANGPOL(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 KDP JIJ KESBANGPOL"
        verbose_name_plural = "24 KDP JIJ KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusKESBANGPOL(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 JIJ Usul Hapus KESBANGPOL"
        verbose_name_plural = "24 JIJ Usul Hapus KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanKESBANGPOL(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 Usul Hapus JIJ KESBANGPOL"
        verbose_name_plural = "24 Usul Hapus JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanKESBANGPOL(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 Kontrak JIJ KESBANGPOL"
        verbose_name_plural = "24 Kontrak JIJ KESBANGPOL"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanKESBANGPOL(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 Harga JIJ KESBANGPOL"
        verbose_name_plural = "24 Harga JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanKESBANGPOL(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 JIJ Penghapusan KESBANGPOL"
        verbose_name_plural = "24 JIJ Penghapusan KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanKESBANGPOL(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 Tahun Berkurang JIJ KESBANGPOL"
        verbose_name_plural = "24 Tahun Berkurang JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanKESBANGPOL(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 Penghapusan JIJ KESBANGPOL"
        verbose_name_plural = "24 Penghapusan JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanKESBANGPOL(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Asal JIJ KESBANGPOL"
        verbose_name_plural = "24 SKPD Asal JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanKESBANGPOL(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Tujuan JIJ KESBANGPOL"
        verbose_name_plural = "24 SKPD Tujuan JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanKESBANGPOL(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "24 Foto JIJ KESBANGPOL"
        verbose_name_plural = "24 Foto JIJ KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##SATPOLPP
##model pada app SATPOLPP
class JalanIrigasiJaringanSATPOLPP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 JIJ SATPOLPP"
        verbose_name_plural = "25 JIJ SATPOLPP"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanSATPOLPP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 KDP JIJ SATPOLPP"
        verbose_name_plural = "25 KDP JIJ SATPOLPP"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusSATPOLPP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 JIJ Usul Hapus SATPOLPP"
        verbose_name_plural = "25 JIJ Usul Hapus SATPOLPP"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanSATPOLPP(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 Usul Hapus JIJ SATPOLPP"
        verbose_name_plural = "25 Usul Hapus JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanSATPOLPP(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 Kontrak JIJ SATPOLPP"
        verbose_name_plural = "25 Kontrak JIJ SATPOLPP"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanSATPOLPP(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 Harga JIJ SATPOLPP"
        verbose_name_plural = "25 Harga JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanSATPOLPP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 JIJ Penghapusan SATPOLPP"
        verbose_name_plural = "25 JIJ Penghapusan SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanSATPOLPP(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 Tahun Berkurang JIJ SATPOLPP"
        verbose_name_plural = "25 Tahun Berkurang JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanSATPOLPP(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 Penghapusan JIJ SATPOLPP"
        verbose_name_plural = "25 Penghapusan JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanSATPOLPP(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Asal JIJ SATPOLPP"
        verbose_name_plural = "25 SKPD Asal JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanSATPOLPP(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Tujuan JIJ SATPOLPP"
        verbose_name_plural = "25 SKPD Tujuan JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanSATPOLPP(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "25 Foto JIJ SATPOLPP"
        verbose_name_plural = "25 Foto JIJ SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##BKPPD
##model pada app BKPPD
class JalanIrigasiJaringanBKPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 JIJ BKPPD"
        verbose_name_plural = "26 JIJ BKPPD"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBKPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 KDP JIJ BKPPD"
        verbose_name_plural = "26 KDP JIJ BKPPD"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBKPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 JIJ Usul Hapus BKPPD"
        verbose_name_plural = "26 JIJ Usul Hapus BKPPD"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBKPPD(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 Usul Hapus JIJ BKPPD"
        verbose_name_plural = "26 Usul Hapus JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBKPPD(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 Kontrak JIJ BKPPD"
        verbose_name_plural = "26 Kontrak JIJ BKPPD"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBKPPD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 Harga JIJ BKPPD"
        verbose_name_plural = "26 Harga JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBKPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 JIJ Penghapusan BKPPD"
        verbose_name_plural = "26 JIJ Penghapusan BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBKPPD(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 Tahun Berkurang JIJ BKPPD"
        verbose_name_plural = "26 Tahun Berkurang JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBKPPD(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 Penghapusan JIJ BKPPD"
        verbose_name_plural = "26 Penghapusan JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBKPPD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Asal JIJ BKPPD"
        verbose_name_plural = "26 SKPD Asal JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBKPPD(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Tujuan JIJ BKPPD"
        verbose_name_plural = "26 SKPD Tujuan JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBKPPD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "26 Foto JIJ BKPPD"
        verbose_name_plural = "26 Foto JIJ BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##SekretariatKorpri
##model pada app SekretariatKorpri
class JalanIrigasiJaringanSekretariatKorpri(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 JIJ Sekretariat Korpri"
        verbose_name_plural = "27 JIJ Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanSekretariatKorpri(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 KDP JIJ Sekretariat Korpri"
        verbose_name_plural = "27 KDP JIJ Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusSekretariatKorpri(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 JIJ Usul Hapus Sekretariat Korpri"
        verbose_name_plural = "27 JIJ Usul Hapus Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanSekretariatKorpri(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 Usul Hapus JIJ Sekretariat Korpri"
        verbose_name_plural = "27 Usul Hapus JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanSekretariatKorpri(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 Kontrak JIJ Sekretariat Korpri"
        verbose_name_plural = "27 Kontrak JIJ Sekretariat Korpri"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanSekretariatKorpri(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 Harga JIJ Sekretariat Korpri"
        verbose_name_plural = "27 Harga JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanSekretariatKorpri(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 JIJ Penghapusan Sekretariat Korpri"
        verbose_name_plural = "27 JIJ Penghapusan Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanSekretariatKorpri(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 Tahun Berkurang JIJ Sekretariat Korpri"
        verbose_name_plural = "27 Tahun Berkurang JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanSekretariatKorpri(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 Penghapusan JIJ Sekretariat Korpri"
        verbose_name_plural = "27 Penghapusan JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanSekretariatKorpri(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Asal JIJ Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Asal JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanSekretariatKorpri(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Tujuan JIJ Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Tujuan JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanSekretariatKorpri(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "27 Foto JIJ Sekretariat Korpri"
        verbose_name_plural = "27 Foto JIJ Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Paringin
##model pada app Paringin
class JalanIrigasiJaringanParingin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 JIJ Paringin"
        verbose_name_plural = "28 JIJ Paringin"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanParingin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 KDP JIJ Paringin"
        verbose_name_plural = "28 KDP JIJ Paringin"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusParingin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 JIJ Usul Hapus Paringin"
        verbose_name_plural = "28 JIJ Usul Hapus Paringin"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanParingin(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 Usul Hapus JIJ Paringin"
        verbose_name_plural = "28 Usul Hapus JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanParingin(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 Kontrak JIJ Paringin"
        verbose_name_plural = "28 Kontrak JIJ Paringin"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanParingin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 Harga JIJ Paringin"
        verbose_name_plural = "28 Harga JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanParingin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 JIJ Penghapusan Paringin"
        verbose_name_plural = "28 JIJ Penghapusan Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanParingin(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 Tahun Berkurang JIJ Paringin"
        verbose_name_plural = "28 Tahun Berkurang JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanParingin(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 Penghapusan JIJ Paringin"
        verbose_name_plural = "28 Penghapusan JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanParingin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Asal JIJ Paringin"
        verbose_name_plural = "28 SKPD Asal JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanParingin(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Tujuan JIJ Paringin"
        verbose_name_plural = "28 SKPD Tujuan JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanParingin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "28 Foto JIJ Paringin"
        verbose_name_plural = "28 Foto JIJ Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##ParinginKota
##model pada app ParinginKota
class JalanIrigasiJaringanParinginKota(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 JIJ Paringin Kota"
        verbose_name_plural = "29 JIJ Paringin Kota"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanParinginKota(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 KDP JIJ Paringin Kota"
        verbose_name_plural = "29 KDP JIJ Paringin Kota"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusParinginKota(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 JIJ Usul Hapus Paringin Kota"
        verbose_name_plural = "29 JIJ Usul Hapus Paringin Kota"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginKota(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 Usul Hapus JIJ Paringin Kota"
        verbose_name_plural = "29 Usul Hapus JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanParinginKota(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 Kontrak JIJ Paringin Kota"
        verbose_name_plural = "29 Kontrak JIJ Paringin Kota"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanParinginKota(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 Harga JIJ Paringin Kota"
        verbose_name_plural = "29 Harga JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanParinginKota(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 JIJ Penghapusan Paringin Kota"
        verbose_name_plural = "29 JIJ Penghapusan Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanParinginKota(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 Tahun Berkurang JIJ Paringin Kota"
        verbose_name_plural = "29 Tahun Berkurang JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanParinginKota(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 Penghapusan JIJ Paringin Kota"
        verbose_name_plural = "29 Penghapusan JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanParinginKota(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Asal JIJ Paringin Kota"
        verbose_name_plural = "29 SKPD Asal JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanParinginKota(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Tujuan JIJ Paringin Kota"
        verbose_name_plural = "29 SKPD Tujuan JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanParinginKota(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "29 Foto JIJ Paringin Kota"
        verbose_name_plural = "29 Foto JIJ Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##ParinginTimur
##model pada app ParinginTimur
class JalanIrigasiJaringanParinginTimur(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 JIJ Paringin Timur"
        verbose_name_plural = "30 JIJ Paringin Timur"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanParinginTimur(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 KDP JIJ Paringin Timur"
        verbose_name_plural = "30 KDP JIJ Paringin Timur"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusParinginTimur(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 JIJ Usul Hapus Paringin Timur"
        verbose_name_plural = "30 JIJ Usul Hapus Paringin Timur"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginTimur(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 Usul Hapus JIJ Paringin Timur"
        verbose_name_plural = "30 Usul Hapus JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanParinginTimur(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 Kontrak JIJ Paringin Timur"
        verbose_name_plural = "30 Kontrak JIJ Paringin Timur"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanParinginTimur(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 Harga JIJ Paringin Timur"
        verbose_name_plural = "30 Harga JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanParinginTimur(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 JIJ Penghapusan Paringin Timur"
        verbose_name_plural = "30 JIJ Penghapusan Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanParinginTimur(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 Tahun Berkurang JIJ Paringin Timur"
        verbose_name_plural = "30 Tahun Berkurang JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanParinginTimur(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 Penghapusan JIJ Paringin Timur"
        verbose_name_plural = "30 Penghapusan JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanParinginTimur(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Asal JIJ Paringin Timur"
        verbose_name_plural = "30 SKPD Asal JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanParinginTimur(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Tujuan JIJ Paringin Timur"
        verbose_name_plural = "30 SKPD Tujuan JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanParinginTimur(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "30 Foto JIJ Paringin Timur"
        verbose_name_plural = "30 Foto JIJ Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Lampihong
##model pada app Lampihong
class JalanIrigasiJaringanLampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 JIJ Lampihong"
        verbose_name_plural = "31 JIJ Lampihong"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanLampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 KDP JIJ Lampihong"
        verbose_name_plural = "31 KDP JIJ Lampihong"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusLampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 JIJ Usul Hapus Lampihong"
        verbose_name_plural = "31 JIJ Usul Hapus Lampihong"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanLampihong(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 Usul Hapus JIJ Lampihong"
        verbose_name_plural = "31 Usul Hapus JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanLampihong(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 Kontrak JIJ Lampihong"
        verbose_name_plural = "31 Kontrak JIJ Lampihong"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanLampihong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 Harga JIJ Lampihong"
        verbose_name_plural = "31 Harga JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanLampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 JIJ Penghapusan Lampihong"
        verbose_name_plural = "31 JIJ Penghapusan Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanLampihong(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 Tahun Berkurang JIJ Lampihong"
        verbose_name_plural = "31 Tahun Berkurang JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanLampihong(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 Penghapusan JIJ Lampihong"
        verbose_name_plural = "31 Penghapusan JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanLampihong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Asal JIJ Lampihong"
        verbose_name_plural = "31 SKPD Asal JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanLampihong(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Tujuan JIJ Lampihong"
        verbose_name_plural = "31 SKPD Tujuan JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanLampihong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "31 Foto JIJ Lampihong"
        verbose_name_plural = "31 Foto JIJ Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Batumandi
##model pada app Batumandi
class JalanIrigasiJaringanBatumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 JIJ Batumandi"
        verbose_name_plural = "32 JIJ Batumandi"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBatumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 KDP JIJ Batumandi"
        verbose_name_plural = "32 KDP JIJ Batumandi"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBatumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 JIJ Usul Hapus Batumandi"
        verbose_name_plural = "32 JIJ Usul Hapus Batumandi"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBatumandi(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 Usul Hapus JIJ Batumandi"
        verbose_name_plural = "32 Usul Hapus JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBatumandi(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 Kontrak JIJ Batumandi"
        verbose_name_plural = "32 Kontrak JIJ Batumandi"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBatumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 Harga JIJ Batumandi"
        verbose_name_plural = "32 Harga JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBatumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 JIJ Penghapusan Batumandi"
        verbose_name_plural = "32 JIJ Penghapusan Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBatumandi(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 Tahun Berkurang JIJ Batumandi"
        verbose_name_plural = "32 Tahun Berkurang JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBatumandi(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 Penghapusan JIJ Batumandi"
        verbose_name_plural = "32 Penghapusan JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBatumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Asal JIJ Batumandi"
        verbose_name_plural = "32 SKPD Asal JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBatumandi(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Tujuan JIJ Batumandi"
        verbose_name_plural = "32 SKPD Tujuan JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBatumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "32 Foto JIJ Batumandi"
        verbose_name_plural = "32 Foto JIJ Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Juai
##model pada app Juai
class JalanIrigasiJaringanJuai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 JIJ Juai"
        verbose_name_plural = "33 JIJ Juai"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanJuai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 KDP JIJ Juai"
        verbose_name_plural = "33 KDP JIJ Juai"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusJuai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 JIJ Usul Hapus Juai"
        verbose_name_plural = "33 JIJ Usul Hapus Juai"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanJuai(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 Usul Hapus JIJ Juai"
        verbose_name_plural = "33 Usul Hapus JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanJuai(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 Kontrak JIJ Juai"
        verbose_name_plural = "33 Kontrak JIJ Juai"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanJuai(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 Harga JIJ Juai"
        verbose_name_plural = "33 Harga JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanJuai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 JIJ Penghapusan Juai"
        verbose_name_plural = "33 JIJ Penghapusan Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanJuai(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 Tahun Berkurang JIJ Juai"
        verbose_name_plural = "33 Tahun Berkurang JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanJuai(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 Penghapusan JIJ Juai"
        verbose_name_plural = "33 Penghapusan JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanJuai(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Asal JIJ Juai"
        verbose_name_plural = "33 SKPD Asal JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanJuai(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Tujuan JIJ Juai"
        verbose_name_plural = "33 SKPD Tujuan JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanJuai(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "33 Foto JIJ Juai"
        verbose_name_plural = "33 Foto JIJ Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Awayan
##model pada app Awayan
class JalanIrigasiJaringanAwayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 JIJ Awayan"
        verbose_name_plural = "34 JIJ Awayan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanAwayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 KDP JIJ Awayan"
        verbose_name_plural = "34 KDP JIJ Awayan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusAwayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 JIJ Usul Hapus Awayan"
        verbose_name_plural = "34 JIJ Usul Hapus Awayan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanAwayan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 Usul Hapus JIJ Awayan"
        verbose_name_plural = "34 Usul Hapus JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanAwayan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 Kontrak JIJ Awayan"
        verbose_name_plural = "34 Kontrak JIJ Awayan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanAwayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 Harga JIJ Awayan"
        verbose_name_plural = "34 Harga JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanAwayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 JIJ Penghapusan Awayan"
        verbose_name_plural = "34 JIJ Penghapusan Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanAwayan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 Tahun Berkurang JIJ Awayan"
        verbose_name_plural = "34 Tahun Berkurang JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanAwayan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 Penghapusan JIJ Awayan"
        verbose_name_plural = "34 Penghapusan JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanAwayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Asal JIJ Awayan"
        verbose_name_plural = "34 SKPD Asal JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanAwayan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Tujuan JIJ Awayan"
        verbose_name_plural = "34 SKPD Tujuan JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanAwayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "34 Foto JIJ Awayan"
        verbose_name_plural = "34 Foto JIJ Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Halong
##model pada app Halong
class JalanIrigasiJaringanHalong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 JIJ Halong"
        verbose_name_plural = "35 JIJ Halong"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanHalong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 KDP JIJ Halong"
        verbose_name_plural = "35 KDP JIJ Halong"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusHalong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 JIJ Usul Hapus Halong"
        verbose_name_plural = "35 JIJ Usul Hapus Halong"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanHalong(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 Usul Hapus JIJ Halong"
        verbose_name_plural = "35 Usul Hapus JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanHalong(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 Kontrak JIJ Halong"
        verbose_name_plural = "35 Kontrak JIJ Halong"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanHalong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 Harga JIJ Halong"
        verbose_name_plural = "35 Harga JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanHalong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 JIJ Penghapusan Halong"
        verbose_name_plural = "35 JIJ Penghapusan Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanHalong(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 Tahun Berkurang JIJ Halong"
        verbose_name_plural = "35 Tahun Berkurang JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanHalong(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 Penghapusan JIJ Halong"
        verbose_name_plural = "35 Penghapusan JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanHalong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Asal JIJ Halong"
        verbose_name_plural = "35 SKPD Asal JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanHalong(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Tujuan JIJ Halong"
        verbose_name_plural = "35 SKPD Tujuan JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanHalong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "35 Foto JIJ Halong"
        verbose_name_plural = "35 Foto JIJ Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##ParinginSelatan
##model pada app ParinginSelatan
class JalanIrigasiJaringanParinginSelatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 JIJ Paringin Selatan"
        verbose_name_plural = "36 JIJ Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanParinginSelatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 KDP JIJ Paringin Selatan"
        verbose_name_plural = "36 KDP JIJ Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusParinginSelatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 JIJ Usul Hapus Paringin Selatan"
        verbose_name_plural = "36 JIJ Usul Hapus Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanParinginSelatan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 Usul Hapus JIJ Paringin Selatan"
        verbose_name_plural = "36 Usul Hapus JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanParinginSelatan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 Kontrak JIJ Paringin Selatan"
        verbose_name_plural = "36 Kontrak JIJ Paringin Selatan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanParinginSelatan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 Harga JIJ Paringin Selatan"
        verbose_name_plural = "36 Harga JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanParinginSelatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 JIJ Penghapusan Paringin Selatan"
        verbose_name_plural = "36 JIJ Penghapusan Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanParinginSelatan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 Tahun Berkurang JIJ Paringin Selatan"
        verbose_name_plural = "36 Tahun Berkurang JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanParinginSelatan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 Penghapusan JIJ Paringin Selatan"
        verbose_name_plural = "36 Penghapusan JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanParinginSelatan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Asal JIJ Paringin Selatan"
        verbose_name_plural = "36 SKPD Asal JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanParinginSelatan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Tujuan JIJ Paringin Selatan"
        verbose_name_plural = "36 SKPD Tujuan JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanParinginSelatan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "36 Foto JIJ Paringin Selatan"
        verbose_name_plural = "36 Foto JIJ Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##BatuPiring
##model pada app BatuPiring
class JalanIrigasiJaringanBatuPiring(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 JIJ Batu Piring"
        verbose_name_plural = "37 JIJ Batu Piring"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBatuPiring(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 KDP JIJ Batu Piring"
        verbose_name_plural = "37 KDP JIJ Batu Piring"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBatuPiring(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 JIJ Usul Hapus Batu Piring"
        verbose_name_plural = "37 JIJ Usul Hapus Batu Piring"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBatuPiring(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 Usul Hapus JIJ Batu Piring"
        verbose_name_plural = "37 Usul Hapus JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBatuPiring(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 Kontrak JIJ Batu Piring"
        verbose_name_plural = "37 Kontrak JIJ Batu Piring"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBatuPiring(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 Harga JIJ Batu Piring"
        verbose_name_plural = "37 Harga JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBatuPiring(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 JIJ Penghapusan Batu Piring"
        verbose_name_plural = "37 JIJ Penghapusan Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBatuPiring(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 Tahun Berkurang JIJ Batu Piring"
        verbose_name_plural = "37 Tahun Berkurang JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBatuPiring(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 Penghapusan JIJ Batu Piring"
        verbose_name_plural = "37 Penghapusan JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBatuPiring(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Asal JIJ Batu Piring"
        verbose_name_plural = "37 SKPD Asal JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBatuPiring(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Tujuan JIJ Batu Piring"
        verbose_name_plural = "37 SKPD Tujuan JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBatuPiring(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "37 Foto JIJ Batu Piring"
        verbose_name_plural = "37 Foto JIJ Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##TebingTinggi
##model pada app TebingTinggi
class JalanIrigasiJaringanTebingTinggi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 JIJ Tebing Tinggi"
        verbose_name_plural = "38 JIJ Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanTebingTinggi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 KDP JIJ Tebing Tinggi"
        verbose_name_plural = "38 KDP JIJ Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusTebingTinggi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 JIJ Usul Hapus Tebing Tinggi"
        verbose_name_plural = "38 JIJ Usul Hapus Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanTebingTinggi(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 Usul Hapus JIJ Tebing Tinggi"
        verbose_name_plural = "38 Usul Hapus JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanTebingTinggi(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 Kontrak JIJ Tebing Tinggi"
        verbose_name_plural = "38 Kontrak JIJ Tebing Tinggi"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanTebingTinggi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 Harga JIJ Tebing Tinggi"
        verbose_name_plural = "38 Harga JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanTebingTinggi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 JIJ Penghapusan Tebing Tinggi"
        verbose_name_plural = "38 JIJ Penghapusan Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanTebingTinggi(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 Tahun Berkurang JIJ Tebing Tinggi"
        verbose_name_plural = "38 Tahun Berkurang JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanTebingTinggi(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 Penghapusan JIJ Tebing Tinggi"
        verbose_name_plural = "38 Penghapusan JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanTebingTinggi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Asal JIJ Tebing Tinggi"
        verbose_name_plural = "38 SKPD Asal JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanTebingTinggi(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Tujuan JIJ Tebing Tinggi"
        verbose_name_plural = "38 SKPD Tujuan JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanTebingTinggi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "38 Foto JIJ Tebing Tinggi"
        verbose_name_plural = "38 Foto JIJ Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##BPBD
##model pada app BPBD
class JalanIrigasiJaringanBPBD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 JIJ BPBD"
        verbose_name_plural = "39 JIJ BPBD"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBPBD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 KDP JIJ BPBD"
        verbose_name_plural = "39 KDP JIJ BPBD"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBPBD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 JIJ Usul Hapus BPBD"
        verbose_name_plural = "39 JIJ Usul Hapus BPBD"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBPBD(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 Usul Hapus JIJ BPBD"
        verbose_name_plural = "39 Usul Hapus JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBPBD(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 Kontrak JIJ BPBD"
        verbose_name_plural = "39 Kontrak JIJ BPBD"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBPBD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 Harga JIJ BPBD"
        verbose_name_plural = "39 Harga JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBPBD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 JIJ Penghapusan BPBD"
        verbose_name_plural = "39 JIJ Penghapusan BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBPBD(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 Tahun Berkurang JIJ BPBD"
        verbose_name_plural = "39 Tahun Berkurang JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBPBD(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 Penghapusan JIJ BPBD"
        verbose_name_plural = "39 Penghapusan JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBPBD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Asal JIJ BPBD"
        verbose_name_plural = "39 SKPD Asal JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBPBD(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Tujuan JIJ BPBD"
        verbose_name_plural = "39 SKPD Tujuan JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBPBD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "39 Foto JIJ BPBD"
        verbose_name_plural = "39 Foto JIJ BPBD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DPKP
##model pada app DPKP
class JalanIrigasiJaringanDPKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 JIJ DPKP"
        verbose_name_plural = "40 JIJ DPKP"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDPKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 KDP JIJ DPKP"
        verbose_name_plural = "40 KDP JIJ DPKP"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDPKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 JIJ Usul Hapus DPKP"
        verbose_name_plural = "40 JIJ Usul Hapus DPKP"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPKP(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 Usul Hapus JIJ DPKP"
        verbose_name_plural = "40 Usul Hapus JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDPKP(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 Kontrak JIJ DPKP"
        verbose_name_plural = "40 Kontrak JIJ DPKP"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDPKP(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 Harga JIJ DPKP"
        verbose_name_plural = "40 Harga JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDPKP(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 JIJ Penghapusan DPKP"
        verbose_name_plural = "40 JIJ Penghapusan DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDPKP(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 Tahun Berkurang JIJ DPKP"
        verbose_name_plural = "40 Tahun Berkurang JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDPKP(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 Penghapusan JIJ DPKP"
        verbose_name_plural = "40 Penghapusan JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDPKP(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Asal JIJ DPKP"
        verbose_name_plural = "40 SKPD Asal JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDPKP(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Tujuan JIJ DPKP"
        verbose_name_plural = "40 SKPD Tujuan JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDPKP(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "40 Foto JIJ DPKP"
        verbose_name_plural = "40 Foto JIJ DPKP"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Disnakertrans
##model pada app Disnakertrans
class JalanIrigasiJaringanDisnakertrans(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 JIJ Disnakertrans"
        verbose_name_plural = "41 JIJ Disnakertrans"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDisnakertrans(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 KDP JIJ Disnakertrans"
        verbose_name_plural = "41 KDP JIJ Disnakertrans"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDisnakertrans(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 JIJ Usul Hapus Disnakertrans"
        verbose_name_plural = "41 JIJ Usul Hapus Disnakertrans"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDisnakertrans(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 Usul Hapus JIJ Disnakertrans"
        verbose_name_plural = "41 Usul Hapus JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDisnakertrans(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 Kontrak JIJ Disnakertrans"
        verbose_name_plural = "41 Kontrak JIJ Disnakertrans"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDisnakertrans(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 Harga JIJ Disnakertrans"
        verbose_name_plural = "41 Harga JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDisnakertrans(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 JIJ Penghapusan Disnakertrans"
        verbose_name_plural = "41 JIJ Penghapusan Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDisnakertrans(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 Tahun Berkurang JIJ Disnakertrans"
        verbose_name_plural = "41 Tahun Berkurang JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDisnakertrans(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 Penghapusan JIJ Disnakertrans"
        verbose_name_plural = "41 Penghapusan JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDisnakertrans(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Asal JIJ Disnakertrans"
        verbose_name_plural = "41 SKPD Asal JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDisnakertrans(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Tujuan JIJ Disnakertrans"
        verbose_name_plural = "41 SKPD Tujuan JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisnakertrans(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "41 Foto JIJ Disnakertrans"
        verbose_name_plural = "41 Foto JIJ Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##DPPKB
##model pada app DPPKB
class JalanIrigasiJaringanDPPKB(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 JIJ DPPKB"
        verbose_name_plural = "42 JIJ DPPKB"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanDPPKB(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 KDP JIJ DPPKB"
        verbose_name_plural = "42 KDP JIJ DPPKB"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusDPPKB(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 JIJ Usul Hapus DPPKB"
        verbose_name_plural = "42 JIJ Usul Hapus DPPKB"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPPKB(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 Usul Hapus JIJ DPPKB"
        verbose_name_plural = "42 Usul Hapus JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanDPPKB(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 Kontrak JIJ DPPKB"
        verbose_name_plural = "42 Kontrak JIJ DPPKB"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanDPPKB(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 Harga JIJ DPPKB"
        verbose_name_plural = "42 Harga JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanDPPKB(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 JIJ Penghapusan DPPKB"
        verbose_name_plural = "42 JIJ Penghapusan DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanDPPKB(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 Tahun Berkurang JIJ DPPKB"
        verbose_name_plural = "42 Tahun Berkurang JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanDPPKB(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 Penghapusan JIJ DPPKB"
        verbose_name_plural = "42 Penghapusan JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanDPPKB(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Asal JIJ DPPKB"
        verbose_name_plural = "42 SKPD Asal JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanDPPKB(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Tujuan JIJ DPPKB"
        verbose_name_plural = "42 SKPD Tujuan JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDPPKB(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "42 Foto JIJ DPPKB"
        verbose_name_plural = "42 Foto JIJ DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Kominfo
##model pada app Kominfo
class JalanIrigasiJaringanKominfo(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 JIJ Kominfo"
        verbose_name_plural = "43 JIJ Kominfo"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanKominfo(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 KDP JIJ Kominfo"
        verbose_name_plural = "43 KDP JIJ Kominfo"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusKominfo(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 JIJ Usul Hapus Kominfo"
        verbose_name_plural = "43 JIJ Usul Hapus Kominfo"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanKominfo(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 Usul Hapus JIJ Kominfo"
        verbose_name_plural = "43 Usul Hapus JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanKominfo(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 Kontrak JIJ Kominfo"
        verbose_name_plural = "43 Kontrak JIJ Kominfo"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanKominfo(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 Harga JIJ Kominfo"
        verbose_name_plural = "43 Harga JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanKominfo(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 JIJ Penghapusan Kominfo"
        verbose_name_plural = "43 JIJ Penghapusan Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanKominfo(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 Tahun Berkurang JIJ Kominfo"
        verbose_name_plural = "43 Tahun Berkurang JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanKominfo(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 Penghapusan JIJ Kominfo"
        verbose_name_plural = "43 Penghapusan JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanKominfo(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Asal JIJ Kominfo"
        verbose_name_plural = "43 SKPD Asal JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanKominfo(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Tujuan JIJ Kominfo"
        verbose_name_plural = "43 SKPD Tujuan JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanKominfo(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "43 Foto JIJ Kominfo"
        verbose_name_plural = "43 Foto JIJ Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Kearsipan
##model pada app Kearsipan
class JalanIrigasiJaringanKearsipan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 JIJ Kearsipan"
        verbose_name_plural = "44 JIJ Kearsipan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanKearsipan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 KDP JIJ Kearsipan"
        verbose_name_plural = "44 KDP JIJ Kearsipan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusKearsipan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 JIJ Usul Hapus Kearsipan"
        verbose_name_plural = "44 JIJ Usul Hapus Kearsipan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanKearsipan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 Usul Hapus JIJ Kearsipan"
        verbose_name_plural = "44 Usul Hapus JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanKearsipan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 Kontrak JIJ Kearsipan"
        verbose_name_plural = "44 Kontrak JIJ Kearsipan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanKearsipan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 Harga JIJ Kearsipan"
        verbose_name_plural = "44 Harga JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanKearsipan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 JIJ Penghapusan Kearsipan"
        verbose_name_plural = "44 JIJ Penghapusan Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanKearsipan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 Tahun Berkurang JIJ Kearsipan"
        verbose_name_plural = "44 Tahun Berkurang JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanKearsipan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 Penghapusan JIJ Kearsipan"
        verbose_name_plural = "44 Penghapusan JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanKearsipan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Asal JIJ Kearsipan"
        verbose_name_plural = "44 SKPD Asal JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanKearsipan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Tujuan JIJ Kearsipan"
        verbose_name_plural = "44 SKPD Tujuan JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanKearsipan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "44 Foto JIJ Kearsipan"
        verbose_name_plural = "44 Foto JIJ Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Perikanan
##model pada app Perikanan
class JalanIrigasiJaringanPerikanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 JIJ Perikanan"
        verbose_name_plural = "45 JIJ Perikanan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanPerikanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 KDP JIJ Perikanan"
        verbose_name_plural = "45 KDP JIJ Perikanan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusPerikanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 JIJ Usul Hapus Perikanan"
        verbose_name_plural = "45 JIJ Usul Hapus Perikanan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanPerikanan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 Usul Hapus JIJ Perikanan"
        verbose_name_plural = "45 Usul Hapus JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanPerikanan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 Kontrak JIJ Perikanan"
        verbose_name_plural = "45 Kontrak JIJ Perikanan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanPerikanan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 Harga JIJ Perikanan"
        verbose_name_plural = "45 Harga JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanPerikanan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 JIJ Penghapusan Perikanan"
        verbose_name_plural = "45 JIJ Penghapusan Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanPerikanan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 Tahun Berkurang JIJ Perikanan"
        verbose_name_plural = "45 Tahun Berkurang JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanPerikanan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 Penghapusan JIJ Perikanan"
        verbose_name_plural = "45 Penghapusan JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanPerikanan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Asal JIJ Perikanan"
        verbose_name_plural = "45 SKPD Asal JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanPerikanan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Tujuan JIJ Perikanan"
        verbose_name_plural = "45 SKPD Tujuan JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanPerikanan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "45 Foto JIJ Perikanan"
        verbose_name_plural = "45 Foto JIJ Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Pariwisata
##model pada app Pariwisata
class JalanIrigasiJaringanPariwisata(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 JIJ Pariwisata"
        verbose_name_plural = "46 JIJ Pariwisata"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanPariwisata(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 KDP JIJ Pariwisata"
        verbose_name_plural = "46 KDP JIJ Pariwisata"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusPariwisata(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 JIJ Usul Hapus Pariwisata"
        verbose_name_plural = "46 JIJ Usul Hapus Pariwisata"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanPariwisata(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 Usul Hapus JIJ Pariwisata"
        verbose_name_plural = "46 Usul Hapus JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanPariwisata(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 Kontrak JIJ Pariwisata"
        verbose_name_plural = "46 Kontrak JIJ Pariwisata"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanPariwisata(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 Harga JIJ Pariwisata"
        verbose_name_plural = "46 Harga JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanPariwisata(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 JIJ Penghapusan Pariwisata"
        verbose_name_plural = "46 JIJ Penghapusan Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanPariwisata(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 Tahun Berkurang JIJ Pariwisata"
        verbose_name_plural = "46 Tahun Berkurang JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanPariwisata(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 Penghapusan JIJ Pariwisata"
        verbose_name_plural = "46 Penghapusan JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanPariwisata(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Asal JIJ Pariwisata"
        verbose_name_plural = "46 SKPD Asal JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanPariwisata(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Tujuan JIJ Pariwisata"
        verbose_name_plural = "46 SKPD Tujuan JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanPariwisata(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "46 Foto JIJ Pariwisata"
        verbose_name_plural = "46 Foto JIJ Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##Perdagangan
##model pada app Perdagangan
class JalanIrigasiJaringanPerdagangan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 JIJ Perdagangan"
        verbose_name_plural = "47 JIJ Perdagangan"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanPerdagangan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 KDP JIJ Perdagangan"
        verbose_name_plural = "47 KDP JIJ Perdagangan"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusPerdagangan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 JIJ Usul Hapus Perdagangan"
        verbose_name_plural = "47 JIJ Usul Hapus Perdagangan"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanPerdagangan(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 Usul Hapus JIJ Perdagangan"
        verbose_name_plural = "47 Usul Hapus JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanPerdagangan(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 Kontrak JIJ Perdagangan"
        verbose_name_plural = "47 Kontrak JIJ Perdagangan"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanPerdagangan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 Harga JIJ Perdagangan"
        verbose_name_plural = "47 Harga JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanPerdagangan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 JIJ Penghapusan Perdagangan"
        verbose_name_plural = "47 JIJ Penghapusan Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanPerdagangan(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 Tahun Berkurang JIJ Perdagangan"
        verbose_name_plural = "47 Tahun Berkurang JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanPerdagangan(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 Penghapusan JIJ Perdagangan"
        verbose_name_plural = "47 Penghapusan JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanPerdagangan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Asal JIJ Perdagangan"
        verbose_name_plural = "47 SKPD Asal JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanPerdagangan(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Tujuan JIJ Perdagangan"
        verbose_name_plural = "47 SKPD Tujuan JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanPerdagangan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "47 Foto JIJ Perdagangan"
        verbose_name_plural = "47 Foto JIJ Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



##BPPD
##model pada app BPPD
class JalanIrigasiJaringanBPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 JIJ BPPD"
        verbose_name_plural = "48 JIJ BPPD"

    def __unicode__(self):
        return self.nama_barang



class KDPJalanIrigasiJaringanBPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 KDP JIJ BPPD"
        verbose_name_plural = "48 KDP JIJ BPPD"

    def __unicode__(self):
        return self.nama_barang



class JalanIrigasiJaringanUsulHapusBPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 JIJ Usul Hapus BPPD"
        verbose_name_plural = "48 JIJ Usul Hapus BPPD"

    def __unicode__(self):
        return self.nama_barang



class TahunBerkurangUsulHapusJalanIrigasiJaringanBPPD(TahunBerkurangUsulHapusJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 Usul Hapus JIJ BPPD"
        verbose_name_plural = "48 Usul Hapus JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class KontrakJalanIrigasiJaringanBPPD(KontrakJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 Kontrak JIJ BPPD"
        verbose_name_plural = "48 Kontrak JIJ BPPD"

    def __unicode__(self):
        return self.nomor_sp2d



class HargaJalanIrigasiJaringanBPPD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 Harga JIJ BPPD"
        verbose_name_plural = "48 Harga JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class JalanIrigasiJaringanPenghapusanBPPD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 JIJ Penghapusan BPPD"
        verbose_name_plural = "48 JIJ Penghapusan BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangJalanIrigasiJaringanBPPD(TahunBerkurangJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 Tahun Berkurang JIJ BPPD"
        verbose_name_plural = "48 Tahun Berkurang JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanJalanIrigasiJaringanBPPD(PenghapusanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 Penghapusan JIJ BPPD"
        verbose_name_plural = "48 Penghapusan JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalJalanIrigasiJaringanBPPD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Asal JIJ BPPD"
        verbose_name_plural = "48 SKPD Asal JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanJalanIrigasiJaringanBPPD(SKPDTujuanJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Tujuan JIJ BPPD"
        verbose_name_plural = "48 SKPD Tujuan JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanBPPD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "48 Foto JIJ BPPD"
        verbose_name_plural = "48 Foto JIJ BPPD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 1 Awayan

class JalanIrigasiJaringanDisdikSMPN1Awayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 JIJ Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN1Awayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN1Awayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN1Awayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 1 Batumandi

class JalanIrigasiJaringanDisdikSMPN1Batumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 JIJ Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN1Batumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN1Batumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN1Batumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 1 Halong

class JalanIrigasiJaringanDisdikSMPN1Halong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 1 Halong"
        verbose_name_plural = "07 JIJ Disdik SMPN 1 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN1Halong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN1Halong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 1 Halong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN1Halong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 1 Juai

class JalanIrigasiJaringanDisdikSMPN1Juai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 1 Juai"
        verbose_name_plural = "07 JIJ Disdik SMPN 1 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN1Juai(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN1Juai(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 1 Juai"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN1Juai(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 1 Lampihong

class JalanIrigasiJaringanDisdikSMPN1Lampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 JIJ Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN1Lampihong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN1Lampihong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN1Lampihong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 1 Paringin

class JalanIrigasiJaringanDisdikSMPN1Paringin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 JIJ Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN1Paringin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN1Paringin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN1Paringin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 2 Awayan

class JalanIrigasiJaringanDisdikSMPN2Awayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 JIJ Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN2Awayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN2Awayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN2Awayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 2 Batumandi

class JalanIrigasiJaringanDisdikSMPN2Batumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 JIJ Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN2Batumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN2Batumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN2Batumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 2 Halong

class JalanIrigasiJaringanDisdikSMPN2Halong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 2 Halong"
        verbose_name_plural = "07 JIJ Disdik SMPN 2 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN2Halong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN2Halong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 2 Halong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN2Halong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 2 Juai

class JalanIrigasiJaringanDisdikSMPN2Juai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 2 Juai"
        verbose_name_plural = "07 JIJ Disdik SMPN 2 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN2Juai(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN2Juai(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 2 Juai"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN2Juai(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 2 Lampihong

class JalanIrigasiJaringanDisdikSMPN2Lampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 JIJ Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN2Lampihong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN2Lampihong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN2Lampihong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 2 Paringin

class JalanIrigasiJaringanDisdikSMPN2Paringin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 JIJ Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN2Paringin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN2Paringin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN2Paringin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 3 Awayan

class JalanIrigasiJaringanDisdikSMPN3Awayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 JIJ Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN3Awayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN3Awayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN3Awayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 3 Batumandi

class JalanIrigasiJaringanDisdikSMPN3Batumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 JIJ Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN3Batumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN3Batumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN3Batumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 3 Halong

class JalanIrigasiJaringanDisdikSMPN3Halong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 3 Halong"
        verbose_name_plural = "07 JIJ Disdik SMPN 3 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN3Halong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN3Halong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 3 Halong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN3Halong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 3 Paringin

class JalanIrigasiJaringanDisdikSMPN3Paringin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 JIJ Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN3Paringin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN3Paringin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN3Paringin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 4 Awayan

class JalanIrigasiJaringanDisdikSMPN4Awayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 JIJ Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN4Awayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN4Awayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN4Awayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 4 Batumandi

class JalanIrigasiJaringanDisdikSMPN4Batumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 JIJ Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN4Batumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN4Batumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN4Batumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 4 Halong

class JalanIrigasiJaringanDisdikSMPN4Halong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 4 Halong"
        verbose_name_plural = "07 JIJ Disdik SMPN 4 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN4Halong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN4Halong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 4 Halong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN4Halong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 4 Paringin

class JalanIrigasiJaringanDisdikSMPN4Paringin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 JIJ Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN4Paringin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN4Paringin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN4Paringin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 5 Halong

class JalanIrigasiJaringanDisdikSMPN5Halong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 5 Halong"
        verbose_name_plural = "07 JIJ Disdik SMPN 5 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN5Halong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN5Halong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 5 Halong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN5Halong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik SMPN 5 Paringin

class JalanIrigasiJaringanDisdikSMPN5Paringin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 JIJ Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikSMPN5Paringin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Harga JIJ Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikSMPN5Paringin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikSMPN5Paringin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Foto JIJ Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Paringin

class JalanIrigasiJaringanDinkesParingin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Paringin"
        verbose_name_plural = "05 JIJ Dinkes Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesParingin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Paringin"
        verbose_name_plural = "05 Harga JIJ Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesParingin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Paringin"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesParingin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Paringin"
        verbose_name_plural = "05 Foto JIJ Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Lampihong

class JalanIrigasiJaringanDinkesLampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Lampihong"
        verbose_name_plural = "05 JIJ Dinkes Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesLampihong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Lampihong"
        verbose_name_plural = "05 Harga JIJ Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesLampihong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Lampihong"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesLampihong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Lampihong"
        verbose_name_plural = "05 Foto JIJ Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Batumandi

class JalanIrigasiJaringanDinkesBatumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Batumandi"
        verbose_name_plural = "05 JIJ Dinkes Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesBatumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Batumandi"
        verbose_name_plural = "05 Harga JIJ Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesBatumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Batumandi"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesBatumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Batumandi"
        verbose_name_plural = "05 Foto JIJ Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Awayan

class JalanIrigasiJaringanDinkesAwayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Awayan"
        verbose_name_plural = "05 JIJ Dinkes Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesAwayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Awayan"
        verbose_name_plural = "05 Harga JIJ Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesAwayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Awayan"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesAwayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Awayan"
        verbose_name_plural = "05 Foto JIJ Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Juai

class JalanIrigasiJaringanDinkesJuai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Juai"
        verbose_name_plural = "05 JIJ Dinkes Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesJuai(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Juai"
        verbose_name_plural = "05 Harga JIJ Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesJuai(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Juai"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesJuai(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Juai"
        verbose_name_plural = "05 Foto JIJ Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Halong

class JalanIrigasiJaringanDinkesHalong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Halong"
        verbose_name_plural = "05 JIJ Dinkes Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesHalong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Halong"
        verbose_name_plural = "05 Harga JIJ Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesHalong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Halong"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesHalong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Halong"
        verbose_name_plural = "05 Foto JIJ Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Lokbatu

class JalanIrigasiJaringanDinkesLokbatu(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Lokbatu"
        verbose_name_plural = "05 JIJ Dinkes Lokbatu"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesLokbatu(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Lokbatu"
        verbose_name_plural = "05 Harga JIJ Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesLokbatu(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Lokbatu"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesLokbatu(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Lokbatu"
        verbose_name_plural = "05 Foto JIJ Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Uren

class JalanIrigasiJaringanDinkesUren(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Uren"
        verbose_name_plural = "05 JIJ Dinkes Uren"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesUren(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Uren"
        verbose_name_plural = "05 Harga JIJ Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesUren(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Uren"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesUren(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Uren"
        verbose_name_plural = "05 Foto JIJ Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Pirsus

class JalanIrigasiJaringanDinkesPirsus(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Pirsus"
        verbose_name_plural = "05 JIJ Dinkes Pirsus"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesPirsus(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Pirsus"
        verbose_name_plural = "05 Harga JIJ Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesPirsus(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Pirsus"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesPirsus(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Pirsus"
        verbose_name_plural = "05 Foto JIJ Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Paringin Selatan

class JalanIrigasiJaringanDinkesParinginSelatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Paringin Selatan"
        verbose_name_plural = "05 JIJ Dinkes Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesParinginSelatan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Paringin Selatan"
        verbose_name_plural = "05 Harga JIJ Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesParinginSelatan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Paringin Selatan"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesParinginSelatan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Paringin Selatan"
        verbose_name_plural = "05 Foto JIJ Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Tebing Tinggi

class JalanIrigasiJaringanDinkesTebingTinggi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Tebing Tinggi"
        verbose_name_plural = "05 JIJ Dinkes Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesTebingTinggi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Harga JIJ Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesTebingTinggi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Tebing Tinggi"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesTebingTinggi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Foto JIJ Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Tanah Habang

class JalanIrigasiJaringanDinkesTanahHabang(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Tanah Habang"
        verbose_name_plural = "05 JIJ Dinkes Tanah Habang"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesTanahHabang(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Tanah Habang"
        verbose_name_plural = "05 Harga JIJ Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesTanahHabang(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Tanah Habang"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesTanahHabang(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Tanah Habang"
        verbose_name_plural = "05 Foto JIJ Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes RSUD

class JalanIrigasiJaringanDinkesRSUD(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes RSUD"
        verbose_name_plural = "05 JIJ Dinkes RSUD"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesRSUD(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes RSUD"
        verbose_name_plural = "05 Harga JIJ Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesRSUD(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes RSUD"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesRSUD(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes RSUD"
        verbose_name_plural = "05 Foto JIJ Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Paringin

class JalanIrigasiJaringanDisdikParingin(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Paringin"
        verbose_name_plural = "07 JIJ Disdik Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikParingin(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Paringin"
        verbose_name_plural = "07 Harga JIJ Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikParingin(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Paringin"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikParingin(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Paringin"
        verbose_name_plural = "07 Foto JIJ Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Lampihong

class JalanIrigasiJaringanDisdikLampihong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Lampihong"
        verbose_name_plural = "07 JIJ Disdik Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikLampihong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Lampihong"
        verbose_name_plural = "07 Harga JIJ Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikLampihong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Lampihong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikLampihong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Lampihong"
        verbose_name_plural = "07 Foto JIJ Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Awayan

class JalanIrigasiJaringanDisdikAwayan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Awayan"
        verbose_name_plural = "07 JIJ Disdik Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikAwayan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Awayan"
        verbose_name_plural = "07 Harga JIJ Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikAwayan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Awayan"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikAwayan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Awayan"
        verbose_name_plural = "07 Foto JIJ Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Batumandi

class JalanIrigasiJaringanDisdikBatumandi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Batumandi"
        verbose_name_plural = "07 JIJ Disdik Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikBatumandi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Batumandi"
        verbose_name_plural = "07 Harga JIJ Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikBatumandi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Batumandi"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikBatumandi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Batumandi"
        verbose_name_plural = "07 Foto JIJ Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Juai

class JalanIrigasiJaringanDisdikJuai(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Juai"
        verbose_name_plural = "07 JIJ Disdik Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikJuai(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Juai"
        verbose_name_plural = "07 Harga JIJ Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikJuai(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Juai"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikJuai(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Juai"
        verbose_name_plural = "07 Foto JIJ Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Halong

class JalanIrigasiJaringanDisdikHalong(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Halong"
        verbose_name_plural = "07 JIJ Disdik Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikHalong(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Halong"
        verbose_name_plural = "07 Harga JIJ Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikHalong(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Halong"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikHalong(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Halong"
        verbose_name_plural = "07 Foto JIJ Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Tebing Tinggi

class JalanIrigasiJaringanDisdikTebingTinggi(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Tebing Tinggi"
        verbose_name_plural = "07 JIJ Disdik Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikTebingTinggi(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Tebing Tinggi"
        verbose_name_plural = "07 Harga JIJ Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikTebingTinggi(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Tebing Tinggi"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikTebingTinggi(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Tebing Tinggi"
        verbose_name_plural = "07 Foto JIJ Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Paringin Selatan

class JalanIrigasiJaringanDisdikParinginSelatan(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Paringin Selatan"
        verbose_name_plural = "07 JIJ Disdik Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikParinginSelatan(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Paringin Selatan"
        verbose_name_plural = "07 Harga JIJ Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikParinginSelatan(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Paringin Selatan"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikParinginSelatan(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Paringin Selatan"
        verbose_name_plural = "07 Foto JIJ Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Disdik Kantor

class JalanIrigasiJaringanDisdikKantor(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 JIJ Disdik Kantor"
        verbose_name_plural = "07 JIJ Disdik Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDisdikKantor(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Harga JIJ Disdik Kantor"
        verbose_name_plural = "07 Harga JIJ Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDisdikKantor(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal JIJ Disdik Kantor"
        verbose_name_plural = "07 SKPD Asal JIJ Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDisdikKantor(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "07 Foto JIJ Disdik Kantor"
        verbose_name_plural = "07 Foto JIJ Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



#Dinkes Kantor

class JalanIrigasiJaringanDinkesKantor(JalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 JIJ Dinkes Kantor"
        verbose_name_plural = "05 JIJ Dinkes Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaJalanIrigasiJaringanDinkesKantor(HargaJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Harga JIJ Dinkes Kantor"
        verbose_name_plural = "05 Harga JIJ Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



class SKPDAsalJalanIrigasiJaringanDinkesKantor(SKPDAsalJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal JIJ Dinkes Kantor"
        verbose_name_plural = "05 SKPD Asal JIJ Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoJalanIrigasiJaringanDinkesKantor(FotoJalanIrigasiJaringan):
    class Meta:
        proxy = True
        verbose_name = "05 Foto JIJ Dinkes Kantor"
        verbose_name_plural = "05 Foto JIJ Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_jalan_irigasi_jaringan)



