### $Id: models.py,v 1.40 2017/12/10 01:51:27 muntaza Exp $



from django.db import models

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang

from gedungbangunan.models import Ruangan


### Kumpulan Table KIB B Peralatan dan Mesin


class PeralatanMesin(models.Model):
    id = models.AutoField(primary_key=True,
                    verbose_name="Register",
                    db_column="id")
    id_sub_skpd = models.ForeignKey(SUBSKPD,
                    verbose_name="SUB SKPD",
                    db_column="id_sub_skpd")
    id_golongan_barang = models.ForeignKey(GolonganBarang,
                    verbose_name="Golongan Barang",
                    default=2,
                    db_column="id_golongan_barang")
    nama_barang = models.CharField("Nama Barang",
                    max_length=300,
                    db_column="nama_barang")
    id_kode_barang = models.ForeignKey(KodeBarang,
                    verbose_name="Kode Barang",
                    limit_choices_to = {'id__gt': 385, 'id__lt': 7267},
                    db_column="id_kode_barang")
    id_keadaan_barang = models.ForeignKey(KeadaanBarang,
                    default=1,
                    verbose_name="Keadaan Barang",
                    db_column="id_keadaan_barang")
    merk_type = models.CharField("Merk / Type",
                    max_length=150,
                    null=True, blank=True,
                    db_column="merk_type")
    ukuran_cc = models.CharField("Ukuran / CC",
                    max_length=100,
                    null=True, blank=True,
                    db_column="ukuran_cc")
    bahan = models.CharField("Bahan",
                    max_length=100,
                    null=True, blank=True,
                    db_column="bahan")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun Awal",
                    help_text="Tahun Awal Kapitalisasi",
                    db_column="tahun")
    nomor_pabrik = models.CharField("Nomor Pabrik",
                    max_length=100,
                    null=True, blank=True,
                    db_column="nomor_pabrik")
    nomor_rangka = models.CharField("Nomor Rangka",
                    max_length=100,
                    db_column="nomor_rangka")
    nomor_mesin = models.CharField("Nomor Mesin",
                    max_length=100,
                    db_column="nomor_mesin")
    nomor_polisi = models.CharField("Nomor Polisi",
                    max_length=100,
                    db_column="nomor_polisi")
    nomor_bpkb = models.CharField("Nomor BPKB",
                    max_length=100,
                    db_column="nomor_bpkb")
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
    id_ruangan = models.ForeignKey(Ruangan,
                    verbose_name="Ruangan",
                    db_column="id_ruangan")
    keterangan = models.TextField("Keterangan",
                    null=True, blank=True,
                    db_column="keterangan")

    class Meta:
        db_table = "peralatan_mesin"
        verbose_name = "Peralatan Mesin"
        verbose_name_plural = "Peralatan Mesin"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline PenghapusanPeralatanMesin
class PeralatanMesinPenghapusan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "Peralatan Mesin Penghapusan"
        verbose_name_plural = "Peralatan Mesin Penghapusan"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline TahunBerkurangUsulHapusPeralatanMesin
class PeralatanMesinUsulHapus(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "Peralatan Mesin Usul Hapus"
        verbose_name_plural = "Peralatan Mesin Usul Hapus"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline PemanfaatanPeralatanMesin
class PeralatanMesinPemanfaatan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "Peralatan Mesin Pemanfaatan"
        verbose_name_plural = "Peralatan Mesin Pemanfaatan"

    def __unicode__(self):
        return self.nama_barang


class KontrakPeralatanMesin(models.Model):
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
        db_table = "kontrak_peralatan_mesin"
	verbose_name = "Kontrak Peralatan Mesin"
        verbose_name_plural = "Kontrak Peralatan Mesin"

    def __unicode__(self):
        return self.nomor_sp2d



class TahunBerkurangPeralatanMesin(models.Model):
    id = models.OneToOneField(PeralatanMesin, primary_key=True,
                    db_column="id_peralatan_mesin")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_peralatan_mesin"
	verbose_name = "Tahun Berkurang Peralatan Mesin"
        verbose_name_plural = "Tahun Berkurang Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id)




class TahunBerkurangUsulHapusPeralatanMesin(models.Model):
    id = models.OneToOneField(PeralatanMesin, primary_key=True,
                    db_column="id_peralatan_mesin")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_usul_hapus_pm"
	verbose_name = "Tahun Berkurang Usul Hapus PM"
        verbose_name_plural = "Tahun Berkurang Usul Hapus PM"

    def __unicode__(self):
        return "%s" % (self.id)




class PenghapusanPeralatanMesin(models.Model):
    id = models.OneToOneField(PeralatanMesin, primary_key=True,
                    db_column="id_peralatan_mesin")
    id_sk_penghapusan = models.ForeignKey(SKPenghapusan,
                    verbose_name="SK Penghapusan",
                    db_column="id_sk_penghapusan")

    class Meta:
        db_table = "penghapusan_peralatan_mesin"
	verbose_name = "Penghapusan Peralatan Mesin"
        verbose_name_plural = "Penghapusan Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id)


class PemanfaatanPeralatanMesin(models.Model):
    id = models.OneToOneField(PeralatanMesin, primary_key=True,
                    db_column="id_peralatan_mesin")
    id_jenis_pemanfaatan = models.ForeignKey(JenisPemanfaatan,
                    verbose_name="Jenis Pemanfaatan",
                    db_column="id_jenis_pemanfaatan")

    class Meta:
        db_table = "pemanfaatan_peralatan_mesin"
	verbose_name = "Pemanfaatan Peralatan Mesin"
        verbose_name_plural = "Pemanfaatan Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id)


class HargaPeralatanMesin(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_peralatan_mesin = models.ForeignKey(PeralatanMesin,
                    verbose_name="Peralatan Mesin",
                    db_column="id_peralatan_mesin")
    id_asal_usul = models.ForeignKey(AsalUsul,
                    verbose_name="Asal Usul",
                    db_column="id_asal_usul")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun",
                    help_text="Tahun Anggaran",
                    db_column="tahun")
    id_kontrak_peralatan_mesin = models.ForeignKey(KontrakPeralatanMesin,
                    verbose_name="Kontrak Peralatan Mesin",
                    db_column="id_kontrak_peralatan_mesin")
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
        db_table = "harga_peralatan_mesin"
	verbose_name = "Harga Peralatan Mesin"
        verbose_name_plural = "Harga Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#PeralatanMesinReklas, untuk melakukan mutasi Antar SKPD
class PeralatanMesinReklas(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "Peralatan Mesin Reklas"
        verbose_name_plural = "Peralatan Mesin Reklas"

    def __unicode__(self):
        return self.nama_barang



class SKPDAsalPeralatanMesin(models.Model):
    id = models.OneToOneField(PeralatanMesin, primary_key=True,
                    db_column="id_peralatan_mesin")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_asal_peralatan_mesin"
	verbose_name = "SKPD Asal Peralatan Mesin"
        verbose_name_plural = "SKPD Asal Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesin(models.Model):
    id = models.OneToOneField(PeralatanMesin, primary_key=True,
                    db_column="id_peralatan_mesin")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_tujuan_peralatan_mesin"
	verbose_name = "SKPD Tujuan Peralatan Mesin"
        verbose_name_plural = "SKPD Tujuan Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesin(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_peralatan_mesin = models.ForeignKey(PeralatanMesin,
                    verbose_name="Peralatan Mesin",
                    db_column="id_peralatan_mesin")
    foto = models.FileField("Foto",
                    upload_to='peralatan_mesin/',
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
        db_table = "foto_peralatan_mesin"
	verbose_name = "Foto Peralatan Mesin"
        verbose_name_plural = "Foto Peralatan Mesin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Setwan
##model pada app Setwan
class PeralatanMesinSetwan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 PM Setwan"
        verbose_name_plural = "01 PM Setwan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusSetwan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 PM Usul Hapus Setwan"
        verbose_name_plural = "01 PM Usul Hapus Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinSetwan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 Usul Hapus PM Setwan"
        verbose_name_plural = "01 Usul Hapus PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinSetwan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 Kontrak PM Setwan"
        verbose_name_plural = "01 Kontrak PM Setwan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinSetwan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 Harga PM Setwan"
        verbose_name_plural = "01 Harga PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanSetwan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 PM Penghapusan Setwan"
        verbose_name_plural = "01 PM Penghapusan Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinSetwan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 Tahun Berkurang PM Setwan"
        verbose_name_plural = "01 Tahun Berkurang PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinSetwan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 Penghapusan PM Setwan"
        verbose_name_plural = "01 Penghapusan PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinSetwan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Asal PM Setwan"
        verbose_name_plural = "01 SKPD Asal PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinSetwan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Tujuan PM Setwan"
        verbose_name_plural = "01 SKPD Tujuan PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinSetwan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "01 Foto PM Setwan"
        verbose_name_plural = "01 Foto PM Setwan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Setda
##model pada app Setda
class PeralatanMesinSetda(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 PM Setda"
        verbose_name_plural = "02 PM Setda"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusSetda(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 PM Usul Hapus Setda"
        verbose_name_plural = "02 PM Usul Hapus Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinSetda(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 Usul Hapus PM Setda"
        verbose_name_plural = "02 Usul Hapus PM Setda"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinSetda(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 Kontrak PM Setda"
        verbose_name_plural = "02 Kontrak PM Setda"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinSetda(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 Harga PM Setda"
        verbose_name_plural = "02 Harga PM Setda"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanSetda(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 PM Penghapusan Setda"
        verbose_name_plural = "02 PM Penghapusan Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinSetda(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 Tahun Berkurang PM Setda"
        verbose_name_plural = "02 Tahun Berkurang PM Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinSetda(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 Penghapusan PM Setda"
        verbose_name_plural = "02 Penghapusan PM Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinSetda(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Asal PM Setda"
        verbose_name_plural = "02 SKPD Asal PM Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinSetda(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Tujuan PM Setda"
        verbose_name_plural = "02 SKPD Tujuan PM Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinSetda(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "02 Foto PM Setda"
        verbose_name_plural = "02 Foto PM Setda"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DPUPR
##model pada app DPUPR
class PeralatanMesinDPUPR(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 PM DPUPR"
        verbose_name_plural = "03 PM DPUPR"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDPUPR(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 PM Usul Hapus DPUPR"
        verbose_name_plural = "03 PM Usul Hapus DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDPUPR(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 Usul Hapus PM DPUPR"
        verbose_name_plural = "03 Usul Hapus PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDPUPR(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 Kontrak PM DPUPR"
        verbose_name_plural = "03 Kontrak PM DPUPR"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDPUPR(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 Harga PM DPUPR"
        verbose_name_plural = "03 Harga PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDPUPR(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 PM Penghapusan DPUPR"
        verbose_name_plural = "03 PM Penghapusan DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDPUPR(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 Tahun Berkurang PM DPUPR"
        verbose_name_plural = "03 Tahun Berkurang PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDPUPR(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 Penghapusan PM DPUPR"
        verbose_name_plural = "03 Penghapusan PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDPUPR(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Asal PM DPUPR"
        verbose_name_plural = "03 SKPD Asal PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDPUPR(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Tujuan PM DPUPR"
        verbose_name_plural = "03 SKPD Tujuan PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDPUPR(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "03 Foto PM DPUPR"
        verbose_name_plural = "03 Foto PM DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Dishub
##model pada app Dishub
class PeralatanMesinDishub(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 PM Dishub"
        verbose_name_plural = "04 PM Dishub"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDishub(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 PM Usul Hapus Dishub"
        verbose_name_plural = "04 PM Usul Hapus Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDishub(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 Usul Hapus PM Dishub"
        verbose_name_plural = "04 Usul Hapus PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDishub(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 Kontrak PM Dishub"
        verbose_name_plural = "04 Kontrak PM Dishub"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDishub(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 Harga PM Dishub"
        verbose_name_plural = "04 Harga PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDishub(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 PM Penghapusan Dishub"
        verbose_name_plural = "04 PM Penghapusan Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDishub(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 Tahun Berkurang PM Dishub"
        verbose_name_plural = "04 Tahun Berkurang PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDishub(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 Penghapusan PM Dishub"
        verbose_name_plural = "04 Penghapusan PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDishub(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Asal PM Dishub"
        verbose_name_plural = "04 SKPD Asal PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDishub(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Tujuan PM Dishub"
        verbose_name_plural = "04 SKPD Tujuan PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDishub(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "04 Foto PM Dishub"
        verbose_name_plural = "04 Foto PM Dishub"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Dinkes
##model pada app Dinkes
class PeralatanMesinDinkes(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes"
        verbose_name_plural = "05 PM Dinkes"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDinkes(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Usul Hapus Dinkes"
        verbose_name_plural = "05 PM Usul Hapus Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDinkes(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Usul Hapus PM Dinkes"
        verbose_name_plural = "05 Usul Hapus PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDinkes(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Kontrak PM Dinkes"
        verbose_name_plural = "05 Kontrak PM Dinkes"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDinkes(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes"
        verbose_name_plural = "05 Harga PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDinkes(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Penghapusan Dinkes"
        verbose_name_plural = "05 PM Penghapusan Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDinkes(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Tahun Berkurang PM Dinkes"
        verbose_name_plural = "05 Tahun Berkurang PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDinkes(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Penghapusan PM Dinkes"
        verbose_name_plural = "05 Penghapusan PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDinkes(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes"
        verbose_name_plural = "05 SKPD Asal PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDinkes(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Tujuan PM Dinkes"
        verbose_name_plural = "05 SKPD Tujuan PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkes(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes"
        verbose_name_plural = "05 Foto PM Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##RSUD
##model pada app RSUD
class PeralatanMesinRSUD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 PM RSUD"
        verbose_name_plural = "06 PM RSUD"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusRSUD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 PM Usul Hapus RSUD"
        verbose_name_plural = "06 PM Usul Hapus RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinRSUD(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 Usul Hapus PM RSUD"
        verbose_name_plural = "06 Usul Hapus PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinRSUD(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 Kontrak PM RSUD"
        verbose_name_plural = "06 Kontrak PM RSUD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinRSUD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 Harga PM RSUD"
        verbose_name_plural = "06 Harga PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanRSUD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 PM Penghapusan RSUD"
        verbose_name_plural = "06 PM Penghapusan RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinRSUD(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 Tahun Berkurang PM RSUD"
        verbose_name_plural = "06 Tahun Berkurang PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinRSUD(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 Penghapusan PM RSUD"
        verbose_name_plural = "06 Penghapusan PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinRSUD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Asal PM RSUD"
        verbose_name_plural = "06 SKPD Asal PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinRSUD(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Tujuan PM RSUD"
        verbose_name_plural = "06 SKPD Tujuan PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinRSUD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "06 Foto PM RSUD"
        verbose_name_plural = "06 Foto PM RSUD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Disdik
##model pada app Disdik
class PeralatanMesinDisdik(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik"
        verbose_name_plural = "07 PM Disdik"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDisdik(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Usul Hapus Disdik"
        verbose_name_plural = "07 PM Usul Hapus Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDisdik(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Usul Hapus PM Disdik"
        verbose_name_plural = "07 Usul Hapus PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDisdik(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Kontrak PM Disdik"
        verbose_name_plural = "07 Kontrak PM Disdik"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDisdik(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik"
        verbose_name_plural = "07 Harga PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDisdik(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Penghapusan Disdik"
        verbose_name_plural = "07 PM Penghapusan Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDisdik(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Tahun Berkurang PM Disdik"
        verbose_name_plural = "07 Tahun Berkurang PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDisdik(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Penghapusan PM Disdik"
        verbose_name_plural = "07 Penghapusan PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDisdik(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik"
        verbose_name_plural = "07 SKPD Asal PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDisdik(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Tujuan PM Disdik"
        verbose_name_plural = "07 SKPD Tujuan PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdik(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik"
        verbose_name_plural = "07 Foto PM Disdik"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Perpustakaan
##model pada app Perpustakaan
class PeralatanMesinPerpustakaan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 PM Perpustakaan"
        verbose_name_plural = "08 PM Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusPerpustakaan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 PM Usul Hapus Perpustakaan"
        verbose_name_plural = "08 PM Usul Hapus Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinPerpustakaan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 Usul Hapus PM Perpustakaan"
        verbose_name_plural = "08 Usul Hapus PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinPerpustakaan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 Kontrak PM Perpustakaan"
        verbose_name_plural = "08 Kontrak PM Perpustakaan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinPerpustakaan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 Harga PM Perpustakaan"
        verbose_name_plural = "08 Harga PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanPerpustakaan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 PM Penghapusan Perpustakaan"
        verbose_name_plural = "08 PM Penghapusan Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinPerpustakaan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 Tahun Berkurang PM Perpustakaan"
        verbose_name_plural = "08 Tahun Berkurang PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinPerpustakaan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 Penghapusan PM Perpustakaan"
        verbose_name_plural = "08 Penghapusan PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinPerpustakaan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Asal PM Perpustakaan"
        verbose_name_plural = "08 SKPD Asal PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinPerpustakaan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Tujuan PM Perpustakaan"
        verbose_name_plural = "08 SKPD Tujuan PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinPerpustakaan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "08 Foto PM Perpustakaan"
        verbose_name_plural = "08 Foto PM Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Sosial
##model pada app Sosial
class PeralatanMesinSosial(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 PM Sosial"
        verbose_name_plural = "09 PM Sosial"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusSosial(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 PM Usul Hapus Sosial"
        verbose_name_plural = "09 PM Usul Hapus Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinSosial(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 Usul Hapus PM Sosial"
        verbose_name_plural = "09 Usul Hapus PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinSosial(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 Kontrak PM Sosial"
        verbose_name_plural = "09 Kontrak PM Sosial"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinSosial(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 Harga PM Sosial"
        verbose_name_plural = "09 Harga PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanSosial(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 PM Penghapusan Sosial"
        verbose_name_plural = "09 PM Penghapusan Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinSosial(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 Tahun Berkurang PM Sosial"
        verbose_name_plural = "09 Tahun Berkurang PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinSosial(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 Penghapusan PM Sosial"
        verbose_name_plural = "09 Penghapusan PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinSosial(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Asal PM Sosial"
        verbose_name_plural = "09 SKPD Asal PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinSosial(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Tujuan PM Sosial"
        verbose_name_plural = "09 SKPD Tujuan PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinSosial(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "09 Foto PM Sosial"
        verbose_name_plural = "09 Foto PM Sosial"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DPMD
##model pada app DPMD
class PeralatanMesinDPMD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 PM DPMD"
        verbose_name_plural = "10 PM DPMD"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDPMD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 PM Usul Hapus DPMD"
        verbose_name_plural = "10 PM Usul Hapus DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDPMD(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 Usul Hapus PM DPMD"
        verbose_name_plural = "10 Usul Hapus PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDPMD(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 Kontrak PM DPMD"
        verbose_name_plural = "10 Kontrak PM DPMD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDPMD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 Harga PM DPMD"
        verbose_name_plural = "10 Harga PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDPMD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 PM Penghapusan DPMD"
        verbose_name_plural = "10 PM Penghapusan DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDPMD(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 Tahun Berkurang PM DPMD"
        verbose_name_plural = "10 Tahun Berkurang PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDPMD(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 Penghapusan PM DPMD"
        verbose_name_plural = "10 Penghapusan PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDPMD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Asal PM DPMD"
        verbose_name_plural = "10 SKPD Asal PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDPMD(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Tujuan PM DPMD"
        verbose_name_plural = "10 SKPD Tujuan PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDPMD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "10 Foto PM DPMD"
        verbose_name_plural = "10 Foto PM DPMD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DPPPA
##model pada app DPPPA
class PeralatanMesinDPPPA(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 PM DPPPA"
        verbose_name_plural = "11 PM DPPPA"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDPPPA(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 PM Usul Hapus DPPPA"
        verbose_name_plural = "11 PM Usul Hapus DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDPPPA(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 Usul Hapus PM DPPPA"
        verbose_name_plural = "11 Usul Hapus PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDPPPA(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 Kontrak PM DPPPA"
        verbose_name_plural = "11 Kontrak PM DPPPA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDPPPA(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 Harga PM DPPPA"
        verbose_name_plural = "11 Harga PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDPPPA(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 PM Penghapusan DPPPA"
        verbose_name_plural = "11 PM Penghapusan DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDPPPA(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 Tahun Berkurang PM DPPPA"
        verbose_name_plural = "11 Tahun Berkurang PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDPPPA(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 Penghapusan PM DPPPA"
        verbose_name_plural = "11 Penghapusan PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDPPPA(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Asal PM DPPPA"
        verbose_name_plural = "11 SKPD Asal PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDPPPA(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Tujuan PM DPPPA"
        verbose_name_plural = "11 SKPD Tujuan PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDPPPA(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "11 Foto PM DPPPA"
        verbose_name_plural = "11 Foto PM DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DukCatPil
##model pada app DukCatPil
class PeralatanMesinDukCatPil(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 PM DukCatPil"
        verbose_name_plural = "12 PM DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDukCatPil(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 PM Usul Hapus DukCatPil"
        verbose_name_plural = "12 PM Usul Hapus DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDukCatPil(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 Usul Hapus PM DukCatPil"
        verbose_name_plural = "12 Usul Hapus PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDukCatPil(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 Kontrak PM DukCatPil"
        verbose_name_plural = "12 Kontrak PM DukCatPil"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDukCatPil(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 Harga PM DukCatPil"
        verbose_name_plural = "12 Harga PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDukCatPil(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 PM Penghapusan DukCatPil"
        verbose_name_plural = "12 PM Penghapusan DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDukCatPil(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 Tahun Berkurang PM DukCatPil"
        verbose_name_plural = "12 Tahun Berkurang PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDukCatPil(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 Penghapusan PM DukCatPil"
        verbose_name_plural = "12 Penghapusan PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDukCatPil(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Asal PM DukCatPil"
        verbose_name_plural = "12 SKPD Asal PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDukCatPil(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Tujuan PM DukCatPil"
        verbose_name_plural = "12 SKPD Tujuan PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDukCatPil(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "12 Foto PM DukCatPil"
        verbose_name_plural = "12 Foto PM DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Pertanian
##model pada app Pertanian
class PeralatanMesinPertanian(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 PM Pertanian"
        verbose_name_plural = "13 PM Pertanian"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusPertanian(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 PM Usul Hapus Pertanian"
        verbose_name_plural = "13 PM Usul Hapus Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinPertanian(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 Usul Hapus PM Pertanian"
        verbose_name_plural = "13 Usul Hapus PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinPertanian(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 Kontrak PM Pertanian"
        verbose_name_plural = "13 Kontrak PM Pertanian"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinPertanian(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 Harga PM Pertanian"
        verbose_name_plural = "13 Harga PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanPertanian(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 PM Penghapusan Pertanian"
        verbose_name_plural = "13 PM Penghapusan Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinPertanian(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 Tahun Berkurang PM Pertanian"
        verbose_name_plural = "13 Tahun Berkurang PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinPertanian(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 Penghapusan PM Pertanian"
        verbose_name_plural = "13 Penghapusan PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinPertanian(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Asal PM Pertanian"
        verbose_name_plural = "13 SKPD Asal PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinPertanian(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Tujuan PM Pertanian"
        verbose_name_plural = "13 SKPD Tujuan PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinPertanian(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "13 Foto PM Pertanian"
        verbose_name_plural = "13 Foto PM Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Kehutanan
##model pada app Kehutanan
class PeralatanMesinKehutanan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 PM Kehutanan"
        verbose_name_plural = "14 PM Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusKehutanan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 PM Usul Hapus Kehutanan"
        verbose_name_plural = "14 PM Usul Hapus Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinKehutanan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 Usul Hapus PM Kehutanan"
        verbose_name_plural = "14 Usul Hapus PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinKehutanan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 Kontrak PM Kehutanan"
        verbose_name_plural = "14 Kontrak PM Kehutanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinKehutanan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 Harga PM Kehutanan"
        verbose_name_plural = "14 Harga PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanKehutanan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 PM Penghapusan Kehutanan"
        verbose_name_plural = "14 PM Penghapusan Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinKehutanan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 Tahun Berkurang PM Kehutanan"
        verbose_name_plural = "14 Tahun Berkurang PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinKehutanan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 Penghapusan PM Kehutanan"
        verbose_name_plural = "14 Penghapusan PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinKehutanan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Asal PM Kehutanan"
        verbose_name_plural = "14 SKPD Asal PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinKehutanan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Tujuan PM Kehutanan"
        verbose_name_plural = "14 SKPD Tujuan PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinKehutanan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "14 Foto PM Kehutanan"
        verbose_name_plural = "14 Foto PM Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DKP
##model pada app DKP
class PeralatanMesinDKP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 PM DKP"
        verbose_name_plural = "15 PM DKP"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDKP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 PM Usul Hapus DKP"
        verbose_name_plural = "15 PM Usul Hapus DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDKP(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 Usul Hapus PM DKP"
        verbose_name_plural = "15 Usul Hapus PM DKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDKP(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 Kontrak PM DKP"
        verbose_name_plural = "15 Kontrak PM DKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDKP(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 Harga PM DKP"
        verbose_name_plural = "15 Harga PM DKP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDKP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 PM Penghapusan DKP"
        verbose_name_plural = "15 PM Penghapusan DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDKP(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 Tahun Berkurang PM DKP"
        verbose_name_plural = "15 Tahun Berkurang PM DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDKP(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 Penghapusan PM DKP"
        verbose_name_plural = "15 Penghapusan PM DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDKP(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Asal PM DKP"
        verbose_name_plural = "15 SKPD Asal PM DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDKP(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Tujuan PM DKP"
        verbose_name_plural = "15 SKPD Tujuan PM DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDKP(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "15 Foto PM DKP"
        verbose_name_plural = "15 Foto PM DKP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DKUKMP
##model pada app DKUKMP
class PeralatanMesinDKUKMP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 PM DKUKMP"
        verbose_name_plural = "16 PM DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDKUKMP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 PM Usul Hapus DKUKMP"
        verbose_name_plural = "16 PM Usul Hapus DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDKUKMP(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 Usul Hapus PM DKUKMP"
        verbose_name_plural = "16 Usul Hapus PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDKUKMP(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 Kontrak PM DKUKMP"
        verbose_name_plural = "16 Kontrak PM DKUKMP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDKUKMP(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 Harga PM DKUKMP"
        verbose_name_plural = "16 Harga PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDKUKMP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 PM Penghapusan DKUKMP"
        verbose_name_plural = "16 PM Penghapusan DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDKUKMP(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 Tahun Berkurang PM DKUKMP"
        verbose_name_plural = "16 Tahun Berkurang PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDKUKMP(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 Penghapusan PM DKUKMP"
        verbose_name_plural = "16 Penghapusan PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDKUKMP(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Asal PM DKUKMP"
        verbose_name_plural = "16 SKPD Asal PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDKUKMP(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Tujuan PM DKUKMP"
        verbose_name_plural = "16 SKPD Tujuan PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDKUKMP(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "16 Foto PM DKUKMP"
        verbose_name_plural = "16 Foto PM DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Distamben
##model pada app Distamben
class PeralatanMesinDistamben(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 PM Distamben"
        verbose_name_plural = "17 PM Distamben"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDistamben(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 PM Usul Hapus Distamben"
        verbose_name_plural = "17 PM Usul Hapus Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDistamben(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 Usul Hapus PM Distamben"
        verbose_name_plural = "17 Usul Hapus PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDistamben(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 Kontrak PM Distamben"
        verbose_name_plural = "17 Kontrak PM Distamben"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDistamben(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 Harga PM Distamben"
        verbose_name_plural = "17 Harga PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDistamben(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 PM Penghapusan Distamben"
        verbose_name_plural = "17 PM Penghapusan Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDistamben(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 Tahun Berkurang PM Distamben"
        verbose_name_plural = "17 Tahun Berkurang PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDistamben(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 Penghapusan PM Distamben"
        verbose_name_plural = "17 Penghapusan PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDistamben(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Asal PM Distamben"
        verbose_name_plural = "17 SKPD Asal PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDistamben(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Tujuan PM Distamben"
        verbose_name_plural = "17 SKPD Tujuan PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDistamben(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "17 Foto PM Distamben"
        verbose_name_plural = "17 Foto PM Distamben"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DPMPTSP
##model pada app DPMPTSP
class PeralatanMesinDPMPTSP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 PM DPMPTSP"
        verbose_name_plural = "18 PM DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDPMPTSP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 PM Usul Hapus DPMPTSP"
        verbose_name_plural = "18 PM Usul Hapus DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDPMPTSP(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 Usul Hapus PM DPMPTSP"
        verbose_name_plural = "18 Usul Hapus PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDPMPTSP(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 Kontrak PM DPMPTSP"
        verbose_name_plural = "18 Kontrak PM DPMPTSP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDPMPTSP(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 Harga PM DPMPTSP"
        verbose_name_plural = "18 Harga PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDPMPTSP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 PM Penghapusan DPMPTSP"
        verbose_name_plural = "18 PM Penghapusan DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDPMPTSP(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 Tahun Berkurang PM DPMPTSP"
        verbose_name_plural = "18 Tahun Berkurang PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDPMPTSP(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 Penghapusan PM DPMPTSP"
        verbose_name_plural = "18 Penghapusan PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDPMPTSP(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Asal PM DPMPTSP"
        verbose_name_plural = "18 SKPD Asal PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDPMPTSP(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Tujuan PM DPMPTSP"
        verbose_name_plural = "18 SKPD Tujuan PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDPMPTSP(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "18 Foto PM DPMPTSP"
        verbose_name_plural = "18 Foto PM DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##BKD
##model pada app BKD
class PeralatanMesinBKD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 PM BKD"
        verbose_name_plural = "19 PM BKD"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBKD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 PM Usul Hapus BKD"
        verbose_name_plural = "19 PM Usul Hapus BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBKD(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 Usul Hapus PM BKD"
        verbose_name_plural = "19 Usul Hapus PM BKD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBKD(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 Kontrak PM BKD"
        verbose_name_plural = "19 Kontrak PM BKD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBKD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 Harga PM BKD"
        verbose_name_plural = "19 Harga PM BKD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBKD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 PM Penghapusan BKD"
        verbose_name_plural = "19 PM Penghapusan BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBKD(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 Tahun Berkurang PM BKD"
        verbose_name_plural = "19 Tahun Berkurang PM BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBKD(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 Penghapusan PM BKD"
        verbose_name_plural = "19 Penghapusan PM BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBKD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Asal PM BKD"
        verbose_name_plural = "19 SKPD Asal PM BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBKD(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Tujuan PM BKD"
        verbose_name_plural = "19 SKPD Tujuan PM BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBKD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "19 Foto PM BKD"
        verbose_name_plural = "19 Foto PM BKD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Inspektorat
##model pada app Inspektorat
class PeralatanMesinInspektorat(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 PM Inspektorat"
        verbose_name_plural = "20 PM Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusInspektorat(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 PM Usul Hapus Inspektorat"
        verbose_name_plural = "20 PM Usul Hapus Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinInspektorat(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 Usul Hapus PM Inspektorat"
        verbose_name_plural = "20 Usul Hapus PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinInspektorat(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 Kontrak PM Inspektorat"
        verbose_name_plural = "20 Kontrak PM Inspektorat"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinInspektorat(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 Harga PM Inspektorat"
        verbose_name_plural = "20 Harga PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanInspektorat(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 PM Penghapusan Inspektorat"
        verbose_name_plural = "20 PM Penghapusan Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinInspektorat(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 Tahun Berkurang PM Inspektorat"
        verbose_name_plural = "20 Tahun Berkurang PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinInspektorat(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 Penghapusan PM Inspektorat"
        verbose_name_plural = "20 Penghapusan PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinInspektorat(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Asal PM Inspektorat"
        verbose_name_plural = "20 SKPD Asal PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinInspektorat(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Tujuan PM Inspektorat"
        verbose_name_plural = "20 SKPD Tujuan PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinInspektorat(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "20 Foto PM Inspektorat"
        verbose_name_plural = "20 Foto PM Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##BAPPEDA
##model pada app BAPPEDA
class PeralatanMesinBAPPEDA(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 PM BAPPEDA"
        verbose_name_plural = "21 PM BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBAPPEDA(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 PM Usul Hapus BAPPEDA"
        verbose_name_plural = "21 PM Usul Hapus BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBAPPEDA(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 Usul Hapus PM BAPPEDA"
        verbose_name_plural = "21 Usul Hapus PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBAPPEDA(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 Kontrak PM BAPPEDA"
        verbose_name_plural = "21 Kontrak PM BAPPEDA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBAPPEDA(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 Harga PM BAPPEDA"
        verbose_name_plural = "21 Harga PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBAPPEDA(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 PM Penghapusan BAPPEDA"
        verbose_name_plural = "21 PM Penghapusan BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBAPPEDA(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 Tahun Berkurang PM BAPPEDA"
        verbose_name_plural = "21 Tahun Berkurang PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBAPPEDA(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 Penghapusan PM BAPPEDA"
        verbose_name_plural = "21 Penghapusan PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBAPPEDA(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Asal PM BAPPEDA"
        verbose_name_plural = "21 SKPD Asal PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBAPPEDA(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Tujuan PM BAPPEDA"
        verbose_name_plural = "21 SKPD Tujuan PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBAPPEDA(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "21 Foto PM BAPPEDA"
        verbose_name_plural = "21 Foto PM BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DLH
##model pada app DLH
class PeralatanMesinDLH(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 PM DLH"
        verbose_name_plural = "22 PM DLH"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDLH(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 PM Usul Hapus DLH"
        verbose_name_plural = "22 PM Usul Hapus DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDLH(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 Usul Hapus PM DLH"
        verbose_name_plural = "22 Usul Hapus PM DLH"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDLH(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 Kontrak PM DLH"
        verbose_name_plural = "22 Kontrak PM DLH"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDLH(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 Harga PM DLH"
        verbose_name_plural = "22 Harga PM DLH"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDLH(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 PM Penghapusan DLH"
        verbose_name_plural = "22 PM Penghapusan DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDLH(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 Tahun Berkurang PM DLH"
        verbose_name_plural = "22 Tahun Berkurang PM DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDLH(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 Penghapusan PM DLH"
        verbose_name_plural = "22 Penghapusan PM DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDLH(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Asal PM DLH"
        verbose_name_plural = "22 SKPD Asal PM DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDLH(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Tujuan PM DLH"
        verbose_name_plural = "22 SKPD Tujuan PM DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDLH(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "22 Foto PM DLH"
        verbose_name_plural = "22 Foto PM DLH"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DKO
##model pada app DKO
class PeralatanMesinDKO(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 PM DKO"
        verbose_name_plural = "23 PM DKO"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDKO(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 PM Usul Hapus DKO"
        verbose_name_plural = "23 PM Usul Hapus DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDKO(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 Usul Hapus PM DKO"
        verbose_name_plural = "23 Usul Hapus PM DKO"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDKO(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 Kontrak PM DKO"
        verbose_name_plural = "23 Kontrak PM DKO"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDKO(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 Harga PM DKO"
        verbose_name_plural = "23 Harga PM DKO"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDKO(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 PM Penghapusan DKO"
        verbose_name_plural = "23 PM Penghapusan DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDKO(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 Tahun Berkurang PM DKO"
        verbose_name_plural = "23 Tahun Berkurang PM DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDKO(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 Penghapusan PM DKO"
        verbose_name_plural = "23 Penghapusan PM DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDKO(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Asal PM DKO"
        verbose_name_plural = "23 SKPD Asal PM DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDKO(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Tujuan PM DKO"
        verbose_name_plural = "23 SKPD Tujuan PM DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDKO(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "23 Foto PM DKO"
        verbose_name_plural = "23 Foto PM DKO"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##KESBANGPOL
##model pada app KESBANGPOL
class PeralatanMesinKESBANGPOL(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 PM KESBANGPOL"
        verbose_name_plural = "24 PM KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusKESBANGPOL(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 PM Usul Hapus KESBANGPOL"
        verbose_name_plural = "24 PM Usul Hapus KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinKESBANGPOL(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 Usul Hapus PM KESBANGPOL"
        verbose_name_plural = "24 Usul Hapus PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinKESBANGPOL(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 Kontrak PM KESBANGPOL"
        verbose_name_plural = "24 Kontrak PM KESBANGPOL"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinKESBANGPOL(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 Harga PM KESBANGPOL"
        verbose_name_plural = "24 Harga PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanKESBANGPOL(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 PM Penghapusan KESBANGPOL"
        verbose_name_plural = "24 PM Penghapusan KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinKESBANGPOL(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 Tahun Berkurang PM KESBANGPOL"
        verbose_name_plural = "24 Tahun Berkurang PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinKESBANGPOL(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 Penghapusan PM KESBANGPOL"
        verbose_name_plural = "24 Penghapusan PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinKESBANGPOL(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Asal PM KESBANGPOL"
        verbose_name_plural = "24 SKPD Asal PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinKESBANGPOL(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Tujuan PM KESBANGPOL"
        verbose_name_plural = "24 SKPD Tujuan PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinKESBANGPOL(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "24 Foto PM KESBANGPOL"
        verbose_name_plural = "24 Foto PM KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##SATPOLPP
##model pada app SATPOLPP
class PeralatanMesinSATPOLPP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 PM SATPOLPP"
        verbose_name_plural = "25 PM SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusSATPOLPP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 PM Usul Hapus SATPOLPP"
        verbose_name_plural = "25 PM Usul Hapus SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinSATPOLPP(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 Usul Hapus PM SATPOLPP"
        verbose_name_plural = "25 Usul Hapus PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinSATPOLPP(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 Kontrak PM SATPOLPP"
        verbose_name_plural = "25 Kontrak PM SATPOLPP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinSATPOLPP(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 Harga PM SATPOLPP"
        verbose_name_plural = "25 Harga PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanSATPOLPP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 PM Penghapusan SATPOLPP"
        verbose_name_plural = "25 PM Penghapusan SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinSATPOLPP(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 Tahun Berkurang PM SATPOLPP"
        verbose_name_plural = "25 Tahun Berkurang PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinSATPOLPP(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 Penghapusan PM SATPOLPP"
        verbose_name_plural = "25 Penghapusan PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinSATPOLPP(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Asal PM SATPOLPP"
        verbose_name_plural = "25 SKPD Asal PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinSATPOLPP(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Tujuan PM SATPOLPP"
        verbose_name_plural = "25 SKPD Tujuan PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinSATPOLPP(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "25 Foto PM SATPOLPP"
        verbose_name_plural = "25 Foto PM SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##BKPPD
##model pada app BKPPD
class PeralatanMesinBKPPD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 PM BKPPD"
        verbose_name_plural = "26 PM BKPPD"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBKPPD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 PM Usul Hapus BKPPD"
        verbose_name_plural = "26 PM Usul Hapus BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBKPPD(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 Usul Hapus PM BKPPD"
        verbose_name_plural = "26 Usul Hapus PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBKPPD(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 Kontrak PM BKPPD"
        verbose_name_plural = "26 Kontrak PM BKPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBKPPD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 Harga PM BKPPD"
        verbose_name_plural = "26 Harga PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBKPPD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 PM Penghapusan BKPPD"
        verbose_name_plural = "26 PM Penghapusan BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBKPPD(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 Tahun Berkurang PM BKPPD"
        verbose_name_plural = "26 Tahun Berkurang PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBKPPD(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 Penghapusan PM BKPPD"
        verbose_name_plural = "26 Penghapusan PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBKPPD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Asal PM BKPPD"
        verbose_name_plural = "26 SKPD Asal PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBKPPD(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Tujuan PM BKPPD"
        verbose_name_plural = "26 SKPD Tujuan PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBKPPD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "26 Foto PM BKPPD"
        verbose_name_plural = "26 Foto PM BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##SekretariatKorpri
##model pada app SekretariatKorpri
class PeralatanMesinSekretariatKorpri(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 PM Sekretariat Korpri"
        verbose_name_plural = "27 PM Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusSekretariatKorpri(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 PM Usul Hapus Sekretariat Korpri"
        verbose_name_plural = "27 PM Usul Hapus Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinSekretariatKorpri(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 Usul Hapus PM Sekretariat Korpri"
        verbose_name_plural = "27 Usul Hapus PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinSekretariatKorpri(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 Kontrak PM Sekretariat Korpri"
        verbose_name_plural = "27 Kontrak PM Sekretariat Korpri"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinSekretariatKorpri(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 Harga PM Sekretariat Korpri"
        verbose_name_plural = "27 Harga PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanSekretariatKorpri(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 PM Penghapusan Sekretariat Korpri"
        verbose_name_plural = "27 PM Penghapusan Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinSekretariatKorpri(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 Tahun Berkurang PM Sekretariat Korpri"
        verbose_name_plural = "27 Tahun Berkurang PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinSekretariatKorpri(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 Penghapusan PM Sekretariat Korpri"
        verbose_name_plural = "27 Penghapusan PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinSekretariatKorpri(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Asal PM Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Asal PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinSekretariatKorpri(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Tujuan PM Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Tujuan PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinSekretariatKorpri(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "27 Foto PM Sekretariat Korpri"
        verbose_name_plural = "27 Foto PM Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Paringin
##model pada app Paringin
class PeralatanMesinParingin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 PM Paringin"
        verbose_name_plural = "28 PM Paringin"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusParingin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 PM Usul Hapus Paringin"
        verbose_name_plural = "28 PM Usul Hapus Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinParingin(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 Usul Hapus PM Paringin"
        verbose_name_plural = "28 Usul Hapus PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinParingin(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 Kontrak PM Paringin"
        verbose_name_plural = "28 Kontrak PM Paringin"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinParingin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 Harga PM Paringin"
        verbose_name_plural = "28 Harga PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanParingin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 PM Penghapusan Paringin"
        verbose_name_plural = "28 PM Penghapusan Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinParingin(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 Tahun Berkurang PM Paringin"
        verbose_name_plural = "28 Tahun Berkurang PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinParingin(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 Penghapusan PM Paringin"
        verbose_name_plural = "28 Penghapusan PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinParingin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Asal PM Paringin"
        verbose_name_plural = "28 SKPD Asal PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinParingin(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Tujuan PM Paringin"
        verbose_name_plural = "28 SKPD Tujuan PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinParingin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "28 Foto PM Paringin"
        verbose_name_plural = "28 Foto PM Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##ParinginKota
##model pada app ParinginKota
class PeralatanMesinParinginKota(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 PM Paringin Kota"
        verbose_name_plural = "29 PM Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusParinginKota(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 PM Usul Hapus Paringin Kota"
        verbose_name_plural = "29 PM Usul Hapus Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinParinginKota(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 Usul Hapus PM Paringin Kota"
        verbose_name_plural = "29 Usul Hapus PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinParinginKota(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 Kontrak PM Paringin Kota"
        verbose_name_plural = "29 Kontrak PM Paringin Kota"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinParinginKota(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 Harga PM Paringin Kota"
        verbose_name_plural = "29 Harga PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanParinginKota(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 PM Penghapusan Paringin Kota"
        verbose_name_plural = "29 PM Penghapusan Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinParinginKota(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 Tahun Berkurang PM Paringin Kota"
        verbose_name_plural = "29 Tahun Berkurang PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinParinginKota(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 Penghapusan PM Paringin Kota"
        verbose_name_plural = "29 Penghapusan PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinParinginKota(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Asal PM Paringin Kota"
        verbose_name_plural = "29 SKPD Asal PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinParinginKota(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Tujuan PM Paringin Kota"
        verbose_name_plural = "29 SKPD Tujuan PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinParinginKota(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "29 Foto PM Paringin Kota"
        verbose_name_plural = "29 Foto PM Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##ParinginTimur
##model pada app ParinginTimur
class PeralatanMesinParinginTimur(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 PM Paringin Timur"
        verbose_name_plural = "30 PM Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusParinginTimur(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 PM Usul Hapus Paringin Timur"
        verbose_name_plural = "30 PM Usul Hapus Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinParinginTimur(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 Usul Hapus PM Paringin Timur"
        verbose_name_plural = "30 Usul Hapus PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinParinginTimur(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 Kontrak PM Paringin Timur"
        verbose_name_plural = "30 Kontrak PM Paringin Timur"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinParinginTimur(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 Harga PM Paringin Timur"
        verbose_name_plural = "30 Harga PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanParinginTimur(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 PM Penghapusan Paringin Timur"
        verbose_name_plural = "30 PM Penghapusan Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinParinginTimur(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 Tahun Berkurang PM Paringin Timur"
        verbose_name_plural = "30 Tahun Berkurang PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinParinginTimur(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 Penghapusan PM Paringin Timur"
        verbose_name_plural = "30 Penghapusan PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinParinginTimur(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Asal PM Paringin Timur"
        verbose_name_plural = "30 SKPD Asal PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinParinginTimur(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Tujuan PM Paringin Timur"
        verbose_name_plural = "30 SKPD Tujuan PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinParinginTimur(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "30 Foto PM Paringin Timur"
        verbose_name_plural = "30 Foto PM Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Lampihong
##model pada app Lampihong
class PeralatanMesinLampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 PM Lampihong"
        verbose_name_plural = "31 PM Lampihong"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusLampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 PM Usul Hapus Lampihong"
        verbose_name_plural = "31 PM Usul Hapus Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinLampihong(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 Usul Hapus PM Lampihong"
        verbose_name_plural = "31 Usul Hapus PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinLampihong(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 Kontrak PM Lampihong"
        verbose_name_plural = "31 Kontrak PM Lampihong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinLampihong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 Harga PM Lampihong"
        verbose_name_plural = "31 Harga PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanLampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 PM Penghapusan Lampihong"
        verbose_name_plural = "31 PM Penghapusan Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinLampihong(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 Tahun Berkurang PM Lampihong"
        verbose_name_plural = "31 Tahun Berkurang PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinLampihong(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 Penghapusan PM Lampihong"
        verbose_name_plural = "31 Penghapusan PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinLampihong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Asal PM Lampihong"
        verbose_name_plural = "31 SKPD Asal PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinLampihong(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Tujuan PM Lampihong"
        verbose_name_plural = "31 SKPD Tujuan PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinLampihong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "31 Foto PM Lampihong"
        verbose_name_plural = "31 Foto PM Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Batumandi
##model pada app Batumandi
class PeralatanMesinBatumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 PM Batumandi"
        verbose_name_plural = "32 PM Batumandi"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBatumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 PM Usul Hapus Batumandi"
        verbose_name_plural = "32 PM Usul Hapus Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBatumandi(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 Usul Hapus PM Batumandi"
        verbose_name_plural = "32 Usul Hapus PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBatumandi(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 Kontrak PM Batumandi"
        verbose_name_plural = "32 Kontrak PM Batumandi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBatumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 Harga PM Batumandi"
        verbose_name_plural = "32 Harga PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBatumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 PM Penghapusan Batumandi"
        verbose_name_plural = "32 PM Penghapusan Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBatumandi(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 Tahun Berkurang PM Batumandi"
        verbose_name_plural = "32 Tahun Berkurang PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBatumandi(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 Penghapusan PM Batumandi"
        verbose_name_plural = "32 Penghapusan PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBatumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Asal PM Batumandi"
        verbose_name_plural = "32 SKPD Asal PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBatumandi(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Tujuan PM Batumandi"
        verbose_name_plural = "32 SKPD Tujuan PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBatumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "32 Foto PM Batumandi"
        verbose_name_plural = "32 Foto PM Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Juai
##model pada app Juai
class PeralatanMesinJuai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 PM Juai"
        verbose_name_plural = "33 PM Juai"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusJuai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 PM Usul Hapus Juai"
        verbose_name_plural = "33 PM Usul Hapus Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinJuai(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 Usul Hapus PM Juai"
        verbose_name_plural = "33 Usul Hapus PM Juai"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinJuai(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 Kontrak PM Juai"
        verbose_name_plural = "33 Kontrak PM Juai"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinJuai(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 Harga PM Juai"
        verbose_name_plural = "33 Harga PM Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanJuai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 PM Penghapusan Juai"
        verbose_name_plural = "33 PM Penghapusan Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinJuai(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 Tahun Berkurang PM Juai"
        verbose_name_plural = "33 Tahun Berkurang PM Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinJuai(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 Penghapusan PM Juai"
        verbose_name_plural = "33 Penghapusan PM Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinJuai(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Asal PM Juai"
        verbose_name_plural = "33 SKPD Asal PM Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinJuai(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Tujuan PM Juai"
        verbose_name_plural = "33 SKPD Tujuan PM Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinJuai(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "33 Foto PM Juai"
        verbose_name_plural = "33 Foto PM Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Awayan
##model pada app Awayan
class PeralatanMesinAwayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 PM Awayan"
        verbose_name_plural = "34 PM Awayan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusAwayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 PM Usul Hapus Awayan"
        verbose_name_plural = "34 PM Usul Hapus Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinAwayan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 Usul Hapus PM Awayan"
        verbose_name_plural = "34 Usul Hapus PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinAwayan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 Kontrak PM Awayan"
        verbose_name_plural = "34 Kontrak PM Awayan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinAwayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 Harga PM Awayan"
        verbose_name_plural = "34 Harga PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanAwayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 PM Penghapusan Awayan"
        verbose_name_plural = "34 PM Penghapusan Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinAwayan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 Tahun Berkurang PM Awayan"
        verbose_name_plural = "34 Tahun Berkurang PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinAwayan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 Penghapusan PM Awayan"
        verbose_name_plural = "34 Penghapusan PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinAwayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Asal PM Awayan"
        verbose_name_plural = "34 SKPD Asal PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinAwayan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Tujuan PM Awayan"
        verbose_name_plural = "34 SKPD Tujuan PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinAwayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "34 Foto PM Awayan"
        verbose_name_plural = "34 Foto PM Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Halong
##model pada app Halong
class PeralatanMesinHalong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 PM Halong"
        verbose_name_plural = "35 PM Halong"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusHalong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 PM Usul Hapus Halong"
        verbose_name_plural = "35 PM Usul Hapus Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinHalong(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 Usul Hapus PM Halong"
        verbose_name_plural = "35 Usul Hapus PM Halong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinHalong(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 Kontrak PM Halong"
        verbose_name_plural = "35 Kontrak PM Halong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinHalong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 Harga PM Halong"
        verbose_name_plural = "35 Harga PM Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanHalong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 PM Penghapusan Halong"
        verbose_name_plural = "35 PM Penghapusan Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinHalong(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 Tahun Berkurang PM Halong"
        verbose_name_plural = "35 Tahun Berkurang PM Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinHalong(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 Penghapusan PM Halong"
        verbose_name_plural = "35 Penghapusan PM Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinHalong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Asal PM Halong"
        verbose_name_plural = "35 SKPD Asal PM Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinHalong(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Tujuan PM Halong"
        verbose_name_plural = "35 SKPD Tujuan PM Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinHalong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "35 Foto PM Halong"
        verbose_name_plural = "35 Foto PM Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##ParinginSelatan
##model pada app ParinginSelatan
class PeralatanMesinParinginSelatan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 PM Paringin Selatan"
        verbose_name_plural = "36 PM Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusParinginSelatan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 PM Usul Hapus Paringin Selatan"
        verbose_name_plural = "36 PM Usul Hapus Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinParinginSelatan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 Usul Hapus PM Paringin Selatan"
        verbose_name_plural = "36 Usul Hapus PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinParinginSelatan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 Kontrak PM Paringin Selatan"
        verbose_name_plural = "36 Kontrak PM Paringin Selatan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinParinginSelatan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 Harga PM Paringin Selatan"
        verbose_name_plural = "36 Harga PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanParinginSelatan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 PM Penghapusan Paringin Selatan"
        verbose_name_plural = "36 PM Penghapusan Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinParinginSelatan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 Tahun Berkurang PM Paringin Selatan"
        verbose_name_plural = "36 Tahun Berkurang PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinParinginSelatan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 Penghapusan PM Paringin Selatan"
        verbose_name_plural = "36 Penghapusan PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinParinginSelatan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Asal PM Paringin Selatan"
        verbose_name_plural = "36 SKPD Asal PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinParinginSelatan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Tujuan PM Paringin Selatan"
        verbose_name_plural = "36 SKPD Tujuan PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinParinginSelatan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "36 Foto PM Paringin Selatan"
        verbose_name_plural = "36 Foto PM Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##BatuPiring
##model pada app BatuPiring
class PeralatanMesinBatuPiring(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 PM Batu Piring"
        verbose_name_plural = "37 PM Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBatuPiring(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 PM Usul Hapus Batu Piring"
        verbose_name_plural = "37 PM Usul Hapus Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBatuPiring(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 Usul Hapus PM Batu Piring"
        verbose_name_plural = "37 Usul Hapus PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBatuPiring(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 Kontrak PM Batu Piring"
        verbose_name_plural = "37 Kontrak PM Batu Piring"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBatuPiring(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 Harga PM Batu Piring"
        verbose_name_plural = "37 Harga PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBatuPiring(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 PM Penghapusan Batu Piring"
        verbose_name_plural = "37 PM Penghapusan Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBatuPiring(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 Tahun Berkurang PM Batu Piring"
        verbose_name_plural = "37 Tahun Berkurang PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBatuPiring(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 Penghapusan PM Batu Piring"
        verbose_name_plural = "37 Penghapusan PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBatuPiring(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Asal PM Batu Piring"
        verbose_name_plural = "37 SKPD Asal PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBatuPiring(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Tujuan PM Batu Piring"
        verbose_name_plural = "37 SKPD Tujuan PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBatuPiring(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "37 Foto PM Batu Piring"
        verbose_name_plural = "37 Foto PM Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##TebingTinggi
##model pada app TebingTinggi
class PeralatanMesinTebingTinggi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 PM Tebing Tinggi"
        verbose_name_plural = "38 PM Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusTebingTinggi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 PM Usul Hapus Tebing Tinggi"
        verbose_name_plural = "38 PM Usul Hapus Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinTebingTinggi(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 Usul Hapus PM Tebing Tinggi"
        verbose_name_plural = "38 Usul Hapus PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinTebingTinggi(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 Kontrak PM Tebing Tinggi"
        verbose_name_plural = "38 Kontrak PM Tebing Tinggi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinTebingTinggi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 Harga PM Tebing Tinggi"
        verbose_name_plural = "38 Harga PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanTebingTinggi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 PM Penghapusan Tebing Tinggi"
        verbose_name_plural = "38 PM Penghapusan Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinTebingTinggi(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 Tahun Berkurang PM Tebing Tinggi"
        verbose_name_plural = "38 Tahun Berkurang PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinTebingTinggi(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 Penghapusan PM Tebing Tinggi"
        verbose_name_plural = "38 Penghapusan PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinTebingTinggi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Asal PM Tebing Tinggi"
        verbose_name_plural = "38 SKPD Asal PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinTebingTinggi(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Tujuan PM Tebing Tinggi"
        verbose_name_plural = "38 SKPD Tujuan PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinTebingTinggi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "38 Foto PM Tebing Tinggi"
        verbose_name_plural = "38 Foto PM Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##BPBD
##model pada app BPBD
class PeralatanMesinBPBD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 PM BPBD"
        verbose_name_plural = "39 PM BPBD"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBPBD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 PM Usul Hapus BPBD"
        verbose_name_plural = "39 PM Usul Hapus BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBPBD(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 Usul Hapus PM BPBD"
        verbose_name_plural = "39 Usul Hapus PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBPBD(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 Kontrak PM BPBD"
        verbose_name_plural = "39 Kontrak PM BPBD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBPBD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 Harga PM BPBD"
        verbose_name_plural = "39 Harga PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBPBD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 PM Penghapusan BPBD"
        verbose_name_plural = "39 PM Penghapusan BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBPBD(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 Tahun Berkurang PM BPBD"
        verbose_name_plural = "39 Tahun Berkurang PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBPBD(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 Penghapusan PM BPBD"
        verbose_name_plural = "39 Penghapusan PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBPBD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Asal PM BPBD"
        verbose_name_plural = "39 SKPD Asal PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBPBD(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Tujuan PM BPBD"
        verbose_name_plural = "39 SKPD Tujuan PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBPBD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "39 Foto PM BPBD"
        verbose_name_plural = "39 Foto PM BPBD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DPKP
##model pada app DPKP
class PeralatanMesinDPKP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 PM DPKP"
        verbose_name_plural = "40 PM DPKP"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDPKP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 PM Usul Hapus DPKP"
        verbose_name_plural = "40 PM Usul Hapus DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDPKP(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 Usul Hapus PM DPKP"
        verbose_name_plural = "40 Usul Hapus PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDPKP(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 Kontrak PM DPKP"
        verbose_name_plural = "40 Kontrak PM DPKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDPKP(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 Harga PM DPKP"
        verbose_name_plural = "40 Harga PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDPKP(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 PM Penghapusan DPKP"
        verbose_name_plural = "40 PM Penghapusan DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDPKP(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 Tahun Berkurang PM DPKP"
        verbose_name_plural = "40 Tahun Berkurang PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDPKP(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 Penghapusan PM DPKP"
        verbose_name_plural = "40 Penghapusan PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDPKP(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Asal PM DPKP"
        verbose_name_plural = "40 SKPD Asal PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDPKP(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Tujuan PM DPKP"
        verbose_name_plural = "40 SKPD Tujuan PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDPKP(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "40 Foto PM DPKP"
        verbose_name_plural = "40 Foto PM DPKP"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Disnakertrans
##model pada app Disnakertrans
class PeralatanMesinDisnakertrans(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 PM Disnakertrans"
        verbose_name_plural = "41 PM Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDisnakertrans(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 PM Usul Hapus Disnakertrans"
        verbose_name_plural = "41 PM Usul Hapus Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDisnakertrans(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 Usul Hapus PM Disnakertrans"
        verbose_name_plural = "41 Usul Hapus PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDisnakertrans(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 Kontrak PM Disnakertrans"
        verbose_name_plural = "41 Kontrak PM Disnakertrans"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDisnakertrans(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 Harga PM Disnakertrans"
        verbose_name_plural = "41 Harga PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDisnakertrans(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 PM Penghapusan Disnakertrans"
        verbose_name_plural = "41 PM Penghapusan Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDisnakertrans(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 Tahun Berkurang PM Disnakertrans"
        verbose_name_plural = "41 Tahun Berkurang PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDisnakertrans(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 Penghapusan PM Disnakertrans"
        verbose_name_plural = "41 Penghapusan PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDisnakertrans(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Asal PM Disnakertrans"
        verbose_name_plural = "41 SKPD Asal PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDisnakertrans(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Tujuan PM Disnakertrans"
        verbose_name_plural = "41 SKPD Tujuan PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisnakertrans(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "41 Foto PM Disnakertrans"
        verbose_name_plural = "41 Foto PM Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##DPPKB
##model pada app DPPKB
class PeralatanMesinDPPKB(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 PM DPPKB"
        verbose_name_plural = "42 PM DPPKB"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusDPPKB(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 PM Usul Hapus DPPKB"
        verbose_name_plural = "42 PM Usul Hapus DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinDPPKB(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 Usul Hapus PM DPPKB"
        verbose_name_plural = "42 Usul Hapus PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinDPPKB(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 Kontrak PM DPPKB"
        verbose_name_plural = "42 Kontrak PM DPPKB"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinDPPKB(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 Harga PM DPPKB"
        verbose_name_plural = "42 Harga PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanDPPKB(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 PM Penghapusan DPPKB"
        verbose_name_plural = "42 PM Penghapusan DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinDPPKB(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 Tahun Berkurang PM DPPKB"
        verbose_name_plural = "42 Tahun Berkurang PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinDPPKB(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 Penghapusan PM DPPKB"
        verbose_name_plural = "42 Penghapusan PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinDPPKB(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Asal PM DPPKB"
        verbose_name_plural = "42 SKPD Asal PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinDPPKB(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Tujuan PM DPPKB"
        verbose_name_plural = "42 SKPD Tujuan PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDPPKB(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "42 Foto PM DPPKB"
        verbose_name_plural = "42 Foto PM DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Kominfo
##model pada app Kominfo
class PeralatanMesinKominfo(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 PM Kominfo"
        verbose_name_plural = "43 PM Kominfo"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusKominfo(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 PM Usul Hapus Kominfo"
        verbose_name_plural = "43 PM Usul Hapus Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinKominfo(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 Usul Hapus PM Kominfo"
        verbose_name_plural = "43 Usul Hapus PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinKominfo(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 Kontrak PM Kominfo"
        verbose_name_plural = "43 Kontrak PM Kominfo"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinKominfo(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 Harga PM Kominfo"
        verbose_name_plural = "43 Harga PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanKominfo(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 PM Penghapusan Kominfo"
        verbose_name_plural = "43 PM Penghapusan Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinKominfo(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 Tahun Berkurang PM Kominfo"
        verbose_name_plural = "43 Tahun Berkurang PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinKominfo(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 Penghapusan PM Kominfo"
        verbose_name_plural = "43 Penghapusan PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinKominfo(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Asal PM Kominfo"
        verbose_name_plural = "43 SKPD Asal PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinKominfo(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Tujuan PM Kominfo"
        verbose_name_plural = "43 SKPD Tujuan PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinKominfo(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "43 Foto PM Kominfo"
        verbose_name_plural = "43 Foto PM Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Kearsipan
##model pada app Kearsipan
class PeralatanMesinKearsipan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 PM Kearsipan"
        verbose_name_plural = "44 PM Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusKearsipan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 PM Usul Hapus Kearsipan"
        verbose_name_plural = "44 PM Usul Hapus Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinKearsipan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 Usul Hapus PM Kearsipan"
        verbose_name_plural = "44 Usul Hapus PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinKearsipan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 Kontrak PM Kearsipan"
        verbose_name_plural = "44 Kontrak PM Kearsipan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinKearsipan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 Harga PM Kearsipan"
        verbose_name_plural = "44 Harga PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanKearsipan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 PM Penghapusan Kearsipan"
        verbose_name_plural = "44 PM Penghapusan Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinKearsipan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 Tahun Berkurang PM Kearsipan"
        verbose_name_plural = "44 Tahun Berkurang PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinKearsipan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 Penghapusan PM Kearsipan"
        verbose_name_plural = "44 Penghapusan PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinKearsipan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Asal PM Kearsipan"
        verbose_name_plural = "44 SKPD Asal PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinKearsipan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Tujuan PM Kearsipan"
        verbose_name_plural = "44 SKPD Tujuan PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinKearsipan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "44 Foto PM Kearsipan"
        verbose_name_plural = "44 Foto PM Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Perikanan
##model pada app Perikanan
class PeralatanMesinPerikanan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 PM Perikanan"
        verbose_name_plural = "45 PM Perikanan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusPerikanan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 PM Usul Hapus Perikanan"
        verbose_name_plural = "45 PM Usul Hapus Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinPerikanan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 Usul Hapus PM Perikanan"
        verbose_name_plural = "45 Usul Hapus PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinPerikanan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 Kontrak PM Perikanan"
        verbose_name_plural = "45 Kontrak PM Perikanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinPerikanan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 Harga PM Perikanan"
        verbose_name_plural = "45 Harga PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanPerikanan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 PM Penghapusan Perikanan"
        verbose_name_plural = "45 PM Penghapusan Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinPerikanan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 Tahun Berkurang PM Perikanan"
        verbose_name_plural = "45 Tahun Berkurang PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinPerikanan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 Penghapusan PM Perikanan"
        verbose_name_plural = "45 Penghapusan PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinPerikanan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Asal PM Perikanan"
        verbose_name_plural = "45 SKPD Asal PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinPerikanan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Tujuan PM Perikanan"
        verbose_name_plural = "45 SKPD Tujuan PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinPerikanan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "45 Foto PM Perikanan"
        verbose_name_plural = "45 Foto PM Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Pariwisata
##model pada app Pariwisata
class PeralatanMesinPariwisata(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 PM Pariwisata"
        verbose_name_plural = "46 PM Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusPariwisata(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 PM Usul Hapus Pariwisata"
        verbose_name_plural = "46 PM Usul Hapus Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinPariwisata(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 Usul Hapus PM Pariwisata"
        verbose_name_plural = "46 Usul Hapus PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinPariwisata(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 Kontrak PM Pariwisata"
        verbose_name_plural = "46 Kontrak PM Pariwisata"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinPariwisata(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 Harga PM Pariwisata"
        verbose_name_plural = "46 Harga PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanPariwisata(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 PM Penghapusan Pariwisata"
        verbose_name_plural = "46 PM Penghapusan Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinPariwisata(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 Tahun Berkurang PM Pariwisata"
        verbose_name_plural = "46 Tahun Berkurang PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinPariwisata(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 Penghapusan PM Pariwisata"
        verbose_name_plural = "46 Penghapusan PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinPariwisata(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Asal PM Pariwisata"
        verbose_name_plural = "46 SKPD Asal PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinPariwisata(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Tujuan PM Pariwisata"
        verbose_name_plural = "46 SKPD Tujuan PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinPariwisata(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "46 Foto PM Pariwisata"
        verbose_name_plural = "46 Foto PM Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##Perdagangan
##model pada app Perdagangan
class PeralatanMesinPerdagangan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 PM Perdagangan"
        verbose_name_plural = "47 PM Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusPerdagangan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 PM Usul Hapus Perdagangan"
        verbose_name_plural = "47 PM Usul Hapus Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinPerdagangan(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 Usul Hapus PM Perdagangan"
        verbose_name_plural = "47 Usul Hapus PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinPerdagangan(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 Kontrak PM Perdagangan"
        verbose_name_plural = "47 Kontrak PM Perdagangan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinPerdagangan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 Harga PM Perdagangan"
        verbose_name_plural = "47 Harga PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanPerdagangan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 PM Penghapusan Perdagangan"
        verbose_name_plural = "47 PM Penghapusan Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinPerdagangan(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 Tahun Berkurang PM Perdagangan"
        verbose_name_plural = "47 Tahun Berkurang PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinPerdagangan(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 Penghapusan PM Perdagangan"
        verbose_name_plural = "47 Penghapusan PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinPerdagangan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Asal PM Perdagangan"
        verbose_name_plural = "47 SKPD Asal PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinPerdagangan(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Tujuan PM Perdagangan"
        verbose_name_plural = "47 SKPD Tujuan PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinPerdagangan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "47 Foto PM Perdagangan"
        verbose_name_plural = "47 Foto PM Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



##BPPD
##model pada app BPPD
class PeralatanMesinBPPD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 PM BPPD"
        verbose_name_plural = "48 PM BPPD"

    def __unicode__(self):
        return self.nama_barang


class PeralatanMesinUsulHapusBPPD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 PM Usul Hapus BPPD"
        verbose_name_plural = "48 PM Usul Hapus BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusPeralatanMesinBPPD(TahunBerkurangUsulHapusPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 Usul Hapus PM BPPD"
        verbose_name_plural = "48 Usul Hapus PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakPeralatanMesinBPPD(KontrakPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 Kontrak PM BPPD"
        verbose_name_plural = "48 Kontrak PM BPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaPeralatanMesinBPPD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 Harga PM BPPD"
        verbose_name_plural = "48 Harga PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)




class PeralatanMesinPenghapusanBPPD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 PM Penghapusan BPPD"
        verbose_name_plural = "48 PM Penghapusan BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangPeralatanMesinBPPD(TahunBerkurangPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 Tahun Berkurang PM BPPD"
        verbose_name_plural = "48 Tahun Berkurang PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanPeralatanMesinBPPD(PenghapusanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 Penghapusan PM BPPD"
        verbose_name_plural = "48 Penghapusan PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalPeralatanMesinBPPD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Asal PM BPPD"
        verbose_name_plural = "48 SKPD Asal PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanPeralatanMesinBPPD(SKPDTujuanPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Tujuan PM BPPD"
        verbose_name_plural = "48 SKPD Tujuan PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinBPPD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "48 Foto PM BPPD"
        verbose_name_plural = "48 Foto PM BPPD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 1 Awayan

class PeralatanMesinDisdikSMPN1Awayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 PM Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN1Awayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Harga PM Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN1Awayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN1Awayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Foto PM Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 1 Batumandi

class PeralatanMesinDisdikSMPN1Batumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 PM Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN1Batumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Harga PM Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN1Batumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN1Batumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Foto PM Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 1 Halong

class PeralatanMesinDisdikSMPN1Halong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 1 Halong"
        verbose_name_plural = "07 PM Disdik SMPN 1 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN1Halong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN1Halong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 1 Halong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN1Halong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 1 Juai

class PeralatanMesinDisdikSMPN1Juai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 1 Juai"
        verbose_name_plural = "07 PM Disdik SMPN 1 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN1Juai(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Harga PM Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN1Juai(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 1 Juai"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN1Juai(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Foto PM Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 1 Lampihong

class PeralatanMesinDisdikSMPN1Lampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 PM Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN1Lampihong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN1Lampihong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN1Lampihong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 1 Paringin

class PeralatanMesinDisdikSMPN1Paringin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 PM Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN1Paringin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Harga PM Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN1Paringin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN1Paringin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Foto PM Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 2 Awayan

class PeralatanMesinDisdikSMPN2Awayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 PM Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN2Awayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Harga PM Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN2Awayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN2Awayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Foto PM Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 2 Batumandi

class PeralatanMesinDisdikSMPN2Batumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 PM Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN2Batumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Harga PM Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN2Batumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN2Batumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Foto PM Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 2 Halong

class PeralatanMesinDisdikSMPN2Halong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 2 Halong"
        verbose_name_plural = "07 PM Disdik SMPN 2 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN2Halong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN2Halong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 2 Halong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN2Halong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 2 Juai

class PeralatanMesinDisdikSMPN2Juai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 2 Juai"
        verbose_name_plural = "07 PM Disdik SMPN 2 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN2Juai(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Harga PM Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN2Juai(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 2 Juai"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN2Juai(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Foto PM Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 2 Lampihong

class PeralatanMesinDisdikSMPN2Lampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 PM Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN2Lampihong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN2Lampihong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN2Lampihong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 2 Paringin

class PeralatanMesinDisdikSMPN2Paringin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 PM Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN2Paringin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Harga PM Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN2Paringin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN2Paringin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Foto PM Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 3 Awayan

class PeralatanMesinDisdikSMPN3Awayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 PM Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN3Awayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Harga PM Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN3Awayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN3Awayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Foto PM Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 3 Batumandi

class PeralatanMesinDisdikSMPN3Batumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 PM Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN3Batumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Harga PM Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN3Batumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN3Batumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Foto PM Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 3 Halong

class PeralatanMesinDisdikSMPN3Halong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 3 Halong"
        verbose_name_plural = "07 PM Disdik SMPN 3 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN3Halong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN3Halong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 3 Halong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN3Halong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 3 Paringin

class PeralatanMesinDisdikSMPN3Paringin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 PM Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN3Paringin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Harga PM Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN3Paringin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN3Paringin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Foto PM Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 4 Awayan

class PeralatanMesinDisdikSMPN4Awayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 PM Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN4Awayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Harga PM Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN4Awayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN4Awayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Foto PM Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 4 Batumandi

class PeralatanMesinDisdikSMPN4Batumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 PM Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN4Batumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Harga PM Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN4Batumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN4Batumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Foto PM Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 4 Halong

class PeralatanMesinDisdikSMPN4Halong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 4 Halong"
        verbose_name_plural = "07 PM Disdik SMPN 4 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN4Halong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN4Halong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 4 Halong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN4Halong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 4 Paringin

class PeralatanMesinDisdikSMPN4Paringin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 PM Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN4Paringin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Harga PM Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN4Paringin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN4Paringin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Foto PM Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 5 Halong

class PeralatanMesinDisdikSMPN5Halong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 5 Halong"
        verbose_name_plural = "07 PM Disdik SMPN 5 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN5Halong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Harga PM Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN5Halong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 5 Halong"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN5Halong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Foto PM Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik SMPN 5 Paringin

class PeralatanMesinDisdikSMPN5Paringin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 PM Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikSMPN5Paringin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Harga PM Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikSMPN5Paringin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 SKPD Asal PM Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikSMPN5Paringin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Foto PM Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Paringin

class PeralatanMesinDinkesParingin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Paringin"
        verbose_name_plural = "05 PM Dinkes Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesParingin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Paringin"
        verbose_name_plural = "05 Harga PM Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesParingin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Paringin"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesParingin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Paringin"
        verbose_name_plural = "05 Foto PM Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Lampihong

class PeralatanMesinDinkesLampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Lampihong"
        verbose_name_plural = "05 PM Dinkes Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesLampihong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Lampihong"
        verbose_name_plural = "05 Harga PM Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesLampihong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Lampihong"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesLampihong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Lampihong"
        verbose_name_plural = "05 Foto PM Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Batumandi

class PeralatanMesinDinkesBatumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Batumandi"
        verbose_name_plural = "05 PM Dinkes Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesBatumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Batumandi"
        verbose_name_plural = "05 Harga PM Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesBatumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Batumandi"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesBatumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Batumandi"
        verbose_name_plural = "05 Foto PM Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Awayan

class PeralatanMesinDinkesAwayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Awayan"
        verbose_name_plural = "05 PM Dinkes Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesAwayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Awayan"
        verbose_name_plural = "05 Harga PM Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesAwayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Awayan"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesAwayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Awayan"
        verbose_name_plural = "05 Foto PM Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Juai

class PeralatanMesinDinkesJuai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Juai"
        verbose_name_plural = "05 PM Dinkes Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesJuai(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Juai"
        verbose_name_plural = "05 Harga PM Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesJuai(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Juai"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesJuai(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Juai"
        verbose_name_plural = "05 Foto PM Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Halong

class PeralatanMesinDinkesHalong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Halong"
        verbose_name_plural = "05 PM Dinkes Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesHalong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Halong"
        verbose_name_plural = "05 Harga PM Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesHalong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Halong"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesHalong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Halong"
        verbose_name_plural = "05 Foto PM Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Lokbatu

class PeralatanMesinDinkesLokbatu(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Lokbatu"
        verbose_name_plural = "05 PM Dinkes Lokbatu"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesLokbatu(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Lokbatu"
        verbose_name_plural = "05 Harga PM Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesLokbatu(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Lokbatu"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesLokbatu(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Lokbatu"
        verbose_name_plural = "05 Foto PM Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Uren

class PeralatanMesinDinkesUren(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Uren"
        verbose_name_plural = "05 PM Dinkes Uren"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesUren(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Uren"
        verbose_name_plural = "05 Harga PM Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesUren(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Uren"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesUren(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Uren"
        verbose_name_plural = "05 Foto PM Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Pirsus

class PeralatanMesinDinkesPirsus(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Pirsus"
        verbose_name_plural = "05 PM Dinkes Pirsus"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesPirsus(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Pirsus"
        verbose_name_plural = "05 Harga PM Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesPirsus(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Pirsus"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesPirsus(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Pirsus"
        verbose_name_plural = "05 Foto PM Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Paringin Selatan

class PeralatanMesinDinkesParinginSelatan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Paringin Selatan"
        verbose_name_plural = "05 PM Dinkes Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesParinginSelatan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Paringin Selatan"
        verbose_name_plural = "05 Harga PM Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesParinginSelatan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Paringin Selatan"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesParinginSelatan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Paringin Selatan"
        verbose_name_plural = "05 Foto PM Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Tebing Tinggi

class PeralatanMesinDinkesTebingTinggi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Tebing Tinggi"
        verbose_name_plural = "05 PM Dinkes Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesTebingTinggi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Harga PM Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesTebingTinggi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Tebing Tinggi"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesTebingTinggi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Foto PM Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Tanah Habang

class PeralatanMesinDinkesTanahHabang(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Tanah Habang"
        verbose_name_plural = "05 PM Dinkes Tanah Habang"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesTanahHabang(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Tanah Habang"
        verbose_name_plural = "05 Harga PM Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesTanahHabang(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Tanah Habang"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesTanahHabang(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Tanah Habang"
        verbose_name_plural = "05 Foto PM Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes RSUD

class PeralatanMesinDinkesRSUD(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes RSUD"
        verbose_name_plural = "05 PM Dinkes RSUD"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesRSUD(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes RSUD"
        verbose_name_plural = "05 Harga PM Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesRSUD(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes RSUD"
        verbose_name_plural = "05 SKPD Asal PM Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesRSUD(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes RSUD"
        verbose_name_plural = "05 Foto PM Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Paringin

class PeralatanMesinDisdikParingin(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Paringin"
        verbose_name_plural = "07 PM Disdik Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikParingin(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Paringin"
        verbose_name_plural = "07 Harga PM Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikParingin(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Paringin"
        verbose_name_plural = "07 SKPD Asal PM Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikParingin(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Paringin"
        verbose_name_plural = "07 Foto PM Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Lampihong

class PeralatanMesinDisdikLampihong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Lampihong"
        verbose_name_plural = "07 PM Disdik Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikLampihong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Lampihong"
        verbose_name_plural = "07 Harga PM Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikLampihong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Lampihong"
        verbose_name_plural = "07 SKPD Asal PM Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikLampihong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Lampihong"
        verbose_name_plural = "07 Foto PM Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Awayan

class PeralatanMesinDisdikAwayan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Awayan"
        verbose_name_plural = "07 PM Disdik Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikAwayan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Awayan"
        verbose_name_plural = "07 Harga PM Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikAwayan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Awayan"
        verbose_name_plural = "07 SKPD Asal PM Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikAwayan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Awayan"
        verbose_name_plural = "07 Foto PM Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Batumandi

class PeralatanMesinDisdikBatumandi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Batumandi"
        verbose_name_plural = "07 PM Disdik Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikBatumandi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Batumandi"
        verbose_name_plural = "07 Harga PM Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikBatumandi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Batumandi"
        verbose_name_plural = "07 SKPD Asal PM Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikBatumandi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Batumandi"
        verbose_name_plural = "07 Foto PM Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Juai

class PeralatanMesinDisdikJuai(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Juai"
        verbose_name_plural = "07 PM Disdik Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikJuai(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Juai"
        verbose_name_plural = "07 Harga PM Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikJuai(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Juai"
        verbose_name_plural = "07 SKPD Asal PM Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikJuai(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Juai"
        verbose_name_plural = "07 Foto PM Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Halong

class PeralatanMesinDisdikHalong(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Halong"
        verbose_name_plural = "07 PM Disdik Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikHalong(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Halong"
        verbose_name_plural = "07 Harga PM Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikHalong(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Halong"
        verbose_name_plural = "07 SKPD Asal PM Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikHalong(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Halong"
        verbose_name_plural = "07 Foto PM Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Tebing Tinggi

class PeralatanMesinDisdikTebingTinggi(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Tebing Tinggi"
        verbose_name_plural = "07 PM Disdik Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikTebingTinggi(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Tebing Tinggi"
        verbose_name_plural = "07 Harga PM Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikTebingTinggi(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Tebing Tinggi"
        verbose_name_plural = "07 SKPD Asal PM Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikTebingTinggi(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Tebing Tinggi"
        verbose_name_plural = "07 Foto PM Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Paringin Selatan

class PeralatanMesinDisdikParinginSelatan(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Paringin Selatan"
        verbose_name_plural = "07 PM Disdik Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikParinginSelatan(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Paringin Selatan"
        verbose_name_plural = "07 Harga PM Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikParinginSelatan(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Paringin Selatan"
        verbose_name_plural = "07 SKPD Asal PM Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikParinginSelatan(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Paringin Selatan"
        verbose_name_plural = "07 Foto PM Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Disdik Kantor

class PeralatanMesinDisdikKantor(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 PM Disdik Kantor"
        verbose_name_plural = "07 PM Disdik Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDisdikKantor(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Harga PM Disdik Kantor"
        verbose_name_plural = "07 Harga PM Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDisdikKantor(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal PM Disdik Kantor"
        verbose_name_plural = "07 SKPD Asal PM Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDisdikKantor(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "07 Foto PM Disdik Kantor"
        verbose_name_plural = "07 Foto PM Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



#Dinkes Kantor

class PeralatanMesinDinkesKantor(PeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 PM Dinkes Kantor"
        verbose_name_plural = "05 PM Dinkes Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaPeralatanMesinDinkesKantor(HargaPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Harga PM Dinkes Kantor"
        verbose_name_plural = "05 Harga PM Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



class SKPDAsalPeralatanMesinDinkesKantor(SKPDAsalPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal PM Dinkes Kantor"
        verbose_name_plural = "05 SKPD Asal PM Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoPeralatanMesinDinkesKantor(FotoPeralatanMesin):
    class Meta:
        proxy = True
        verbose_name = "05 Foto PM Dinkes Kantor"
        verbose_name_plural = "05 Foto PM Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_peralatan_mesin)



