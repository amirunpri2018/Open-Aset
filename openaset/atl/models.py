from django.db import models

from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang

from gedungbangunan.models import Ruangan


### Kumpulan Table KIB E Aset Tetap Lainnya


class ATL(models.Model):
    id = models.AutoField(primary_key=True,
                    verbose_name="Register",
                    db_column="id")
    id_sub_skpd = models.ForeignKey(SUBSKPD,
                    verbose_name="SUB SKPD",
                    db_column="id_sub_skpd")
    id_golongan_barang = models.ForeignKey(GolonganBarang,
                    verbose_name="Golongan Barang",
                    default=5,
                    db_column="id_golongan_barang")
    nama_barang = models.CharField("Nama Barang",
                    max_length=300,
                    db_column="nama_barang")
    id_kode_barang = models.ForeignKey(KodeBarang,
                    verbose_name="Kode Barang",
                    limit_choices_to = {'id__gt': 8252, 'id__lt': 8621},
                    db_column="id_kode_barang")
    id_keadaan_barang = models.ForeignKey(KeadaanBarang,
                    default=1,
                    verbose_name="Keadaan Barang",
                    db_column="id_keadaan_barang")
    judul_pencipta_buku = models.CharField("Judul/Pencipta Buku",
                    max_length=150,
                    null=True, blank=True,
                    db_column="judul_pencipta_buku")
    spesifikasi_buku = models.CharField("Spesifikasi Buku",
                    max_length=150,
                    null=True, blank=True,
                    help_text="Bahan Pembuatan Buku, misal: Kertas, CD, dsb",
                    db_column="spesifikasi_buku")
    asal_daerah_barang_seni = models.CharField(
                    "Asal Daerah Barang Bercorak Kesenian",
                    max_length=150,
                    null=True, blank=True,
                    db_column="asal_daerah_barang_seni")
    pencipta_barang_seni = models.CharField(
                    "Pencipta Barang Bercorak Kesenian",
                    max_length=150,
                    null=True, blank=True,
                    db_column="pencipta_barang_seni")
    bahan_barang_seni = models.CharField("Bahan Barang Bercorak Kesenian",
                    max_length=150,
                    null=True, blank=True,
                    db_column="bahan_barang_seni")
    jenis_hewan_tumbuhan = models.CharField("Jenis Hewan/Tumbuhan",
                    max_length=150,
                    null=True, blank=True,
                    help_text="Diisi mengenai jenis hewan/ternak atau tumbuhan",
                    db_column="jenis_hewan_tumbuhan")
    ukuran_hewan_tumbuhan = models.CharField("Ukuran Hewan/Tumbuhan",
                    max_length=150,
                    null=True, blank=True,
                    help_text="Diisi ukuran (kg, cm, m, dan sebagainya)",
                    db_column="ukuran_hewan_tumbuhan")
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
    id_ruangan = models.ForeignKey(Ruangan,
                    verbose_name="Ruangan",
                    db_column="id_ruangan")
    keterangan = models.TextField("Keterangan",
                    null=True, blank=True,
                    help_text="Tuliskan keterangan yang dianggap perlu yang ada hubungannya dengan barang yang bersangkutan",
                    db_column="keterangan")

    class Meta:
        db_table = "atl"
        verbose_name = "ATL"
        verbose_name_plural = "ATL"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline PenghapusanATL
class ATLPenghapusan(ATL):
    class Meta:
        proxy = True
        verbose_name = "ATL Penghapusan"
        verbose_name_plural = "ATL Penghapusan"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline UsulHapusATL
class ATLUsulHapus(ATL):
    class Meta:
        proxy = True
        verbose_name = "ATL Usul Hapus"
        verbose_name_plural = "ATL Usul Hapus"

    def __unicode__(self):
        return self.nama_barang


#untuk menampung inline PemanfaatanATL
class ATLPemanfaatan(ATL):
    class Meta:
        proxy = True
        verbose_name = "ATL Pemanfaatan"
        verbose_name_plural = "ATL Pemanfaatan"

    def __unicode__(self):
        return self.nama_barang


class KontrakATL(models.Model):
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
        db_table = "kontrak_atl"
	verbose_name = "Kontrak ATL"
        verbose_name_plural = "Kontrak ATL"

    def __unicode__(self):
        return self.nomor_sp2d



class TahunBerkurangATL(models.Model):
    id = models.OneToOneField(ATL, primary_key=True,
                    db_column="id_atl")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang",
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_atl"
	verbose_name = "Tahun Berkurang ATL"
        verbose_name_plural = "Tahun Berkurang ATL"

    def __unicode__(self):
        return "%s" % (self.id)




class TahunBerkurangUsulHapusATL(models.Model):
    id = models.OneToOneField(ATL, primary_key=True,
                    db_column="id_atl")
    tahun_berkurang = models.ForeignKey(Tahun,
                    verbose_name="Tahun Berkurang", null=True, blank=False,
                    db_column="tahun_berkurang")

    class Meta:
        db_table = "tahun_berkurang_usul_hapus_atl"
	verbose_name = "Tahun Berkurang Usul Hapus ATL"
        verbose_name_plural = "Tahun Berkurang Usul Hapus ATL"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATL(models.Model):
    id = models.OneToOneField(ATL, primary_key=True,
                    db_column="id_atl")
    id_sk_penghapusan = models.ForeignKey(SKPenghapusan,
                    verbose_name="SK Penghapusan",
                    db_column="id_sk_penghapusan")

    class Meta:
        db_table = "penghapusan_atl"
	verbose_name = "Penghapusan ATL"
        verbose_name_plural = "Penghapusan ATL"

    def __unicode__(self):
        return "%s" % (self.id)


class PemanfaatanATL(models.Model):
    id = models.OneToOneField(ATL, primary_key=True,
                    db_column="id_atl")
    id_jenis_pemanfaatan = models.ForeignKey(JenisPemanfaatan,
                    verbose_name="Jenis Pemanfaatan",
                    db_column="id_jenis_pemanfaatan")

    class Meta:
        db_table = "pemanfaatan_atl"
	verbose_name = "Pemanfaatan ATL"
        verbose_name_plural = "Pemanfaatan ATL"

    def __unicode__(self):
        return "%s" % (self.id)


class HargaATL(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_atl = models.ForeignKey(ATL,
                    verbose_name="ATL",
                    db_column="id_atl")
    id_asal_usul = models.ForeignKey(AsalUsul,
                    verbose_name="Asal Usul",
                    db_column="id_asal_usul")
    tahun = models.ForeignKey(Tahun,
                    verbose_name="Tahun",
                    help_text="Tahun Anggaran",
                    db_column="tahun")
    id_kontrak_atl = models.ForeignKey(KontrakATL,
                    verbose_name="Kontrak ATL",
                    db_column="id_kontrak_atl")
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
        db_table = "harga_atl"
	verbose_name = "Harga ATL"
        verbose_name_plural = "Harga ATL"

    def __unicode__(self):
        return "%s" % (self.id_atl)




#ATLReklas, untuk melakukan mutasi Antar SKPD
class ATLReklas(ATL):
    class Meta:
        proxy = True
        verbose_name = "ATL Reklas"
        verbose_name_plural = "ATL Reklas"

    def __unicode__(self):
        return self.nama_barang



class SKPDAsalATL(models.Model):
    id = models.OneToOneField(ATL, primary_key=True,
                    db_column="id_atl")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_asal_atl"
	verbose_name = "SKPD Asal ATL"
        verbose_name_plural = "SKPD Asal ATL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATL(models.Model):
    id = models.OneToOneField(ATL, primary_key=True,
                    db_column="id_atl")
    id_skpd = models.ForeignKey(SKPD,
                    verbose_name="SKPD",
                    db_column="id_skpd")

    class Meta:
        db_table = "skpd_tujuan_atl"
	verbose_name = "SKPD Tujuan ATL"
        verbose_name_plural = "SKPD Tujuan ATL"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATL(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    id_atl = models.ForeignKey(ATL,
                    verbose_name="ATL",
                    db_column="id_atl")
    foto = models.FileField("Foto",
                    upload_to='atl/',
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
        db_table = "foto_atl"
	verbose_name = "Foto ATL"
        verbose_name_plural = "Foto ATL"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Setwan
##model pada app Setwan
class ATLSetwan(ATL):
    class Meta:
        proxy = True
        verbose_name = "01 ATL Setwan"
        verbose_name_plural = "01 ATL Setwan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusSetwan(ATL):
    class Meta:
        proxy = True
        verbose_name = "01 ATL Usul Hapus Setwan"
        verbose_name_plural = "01 ATL Usul Hapus Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLSetwan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "01 Usul Hapus ATL Setwan"
        verbose_name_plural = "01 Usul Hapus ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLSetwan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "01 Kontrak ATL Setwan"
        verbose_name_plural = "01 Kontrak ATL Setwan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLSetwan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "01 Harga ATL Setwan"
        verbose_name_plural = "01 Harga ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanSetwan(ATL):
    class Meta:
        proxy = True
        verbose_name = "01 ATL Penghapusan Setwan"
        verbose_name_plural = "01 ATL Penghapusan Setwan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLSetwan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "01 Tahun Berkurang ATL Setwan"
        verbose_name_plural = "01 Tahun Berkurang ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLSetwan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "01 Penghapusan ATL Setwan"
        verbose_name_plural = "01 Penghapusan ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLSetwan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Asal ATL Setwan"
        verbose_name_plural = "01 SKPD Asal ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLSetwan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "01 SKPD Tujuan ATL Setwan"
        verbose_name_plural = "01 SKPD Tujuan ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLSetwan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "01 Foto ATL Setwan"
        verbose_name_plural = "01 Foto ATL Setwan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Setda
##model pada app Setda
class ATLSetda(ATL):
    class Meta:
        proxy = True
        verbose_name = "02 ATL Setda"
        verbose_name_plural = "02 ATL Setda"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusSetda(ATL):
    class Meta:
        proxy = True
        verbose_name = "02 ATL Usul Hapus Setda"
        verbose_name_plural = "02 ATL Usul Hapus Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLSetda(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "02 Usul Hapus ATL Setda"
        verbose_name_plural = "02 Usul Hapus ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLSetda(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "02 Kontrak ATL Setda"
        verbose_name_plural = "02 Kontrak ATL Setda"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLSetda(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "02 Harga ATL Setda"
        verbose_name_plural = "02 Harga ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanSetda(ATL):
    class Meta:
        proxy = True
        verbose_name = "02 ATL Penghapusan Setda"
        verbose_name_plural = "02 ATL Penghapusan Setda"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLSetda(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "02 Tahun Berkurang ATL Setda"
        verbose_name_plural = "02 Tahun Berkurang ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLSetda(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "02 Penghapusan ATL Setda"
        verbose_name_plural = "02 Penghapusan ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLSetda(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Asal ATL Setda"
        verbose_name_plural = "02 SKPD Asal ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLSetda(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "02 SKPD Tujuan ATL Setda"
        verbose_name_plural = "02 SKPD Tujuan ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLSetda(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "02 Foto ATL Setda"
        verbose_name_plural = "02 Foto ATL Setda"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DPUPR
##model pada app DPUPR
class ATLDPUPR(ATL):
    class Meta:
        proxy = True
        verbose_name = "03 ATL DPUPR"
        verbose_name_plural = "03 ATL DPUPR"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDPUPR(ATL):
    class Meta:
        proxy = True
        verbose_name = "03 ATL Usul Hapus DPUPR"
        verbose_name_plural = "03 ATL Usul Hapus DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDPUPR(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "03 Usul Hapus ATL DPUPR"
        verbose_name_plural = "03 Usul Hapus ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDPUPR(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "03 Kontrak ATL DPUPR"
        verbose_name_plural = "03 Kontrak ATL DPUPR"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDPUPR(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "03 Harga ATL DPUPR"
        verbose_name_plural = "03 Harga ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDPUPR(ATL):
    class Meta:
        proxy = True
        verbose_name = "03 ATL Penghapusan DPUPR"
        verbose_name_plural = "03 ATL Penghapusan DPUPR"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDPUPR(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "03 Tahun Berkurang ATL DPUPR"
        verbose_name_plural = "03 Tahun Berkurang ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDPUPR(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "03 Penghapusan ATL DPUPR"
        verbose_name_plural = "03 Penghapusan ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDPUPR(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Asal ATL DPUPR"
        verbose_name_plural = "03 SKPD Asal ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDPUPR(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "03 SKPD Tujuan ATL DPUPR"
        verbose_name_plural = "03 SKPD Tujuan ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDPUPR(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "03 Foto ATL DPUPR"
        verbose_name_plural = "03 Foto ATL DPUPR"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Dishub
##model pada app Dishub
class ATLDishub(ATL):
    class Meta:
        proxy = True
        verbose_name = "04 ATL Dishub"
        verbose_name_plural = "04 ATL Dishub"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDishub(ATL):
    class Meta:
        proxy = True
        verbose_name = "04 ATL Usul Hapus Dishub"
        verbose_name_plural = "04 ATL Usul Hapus Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDishub(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "04 Usul Hapus ATL Dishub"
        verbose_name_plural = "04 Usul Hapus ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDishub(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "04 Kontrak ATL Dishub"
        verbose_name_plural = "04 Kontrak ATL Dishub"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDishub(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "04 Harga ATL Dishub"
        verbose_name_plural = "04 Harga ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDishub(ATL):
    class Meta:
        proxy = True
        verbose_name = "04 ATL Penghapusan Dishub"
        verbose_name_plural = "04 ATL Penghapusan Dishub"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDishub(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "04 Tahun Berkurang ATL Dishub"
        verbose_name_plural = "04 Tahun Berkurang ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDishub(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "04 Penghapusan ATL Dishub"
        verbose_name_plural = "04 Penghapusan ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDishub(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Asal ATL Dishub"
        verbose_name_plural = "04 SKPD Asal ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDishub(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "04 SKPD Tujuan ATL Dishub"
        verbose_name_plural = "04 SKPD Tujuan ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDishub(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "04 Foto ATL Dishub"
        verbose_name_plural = "04 Foto ATL Dishub"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Dinkes
##model pada app Dinkes
class ATLDinkes(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes"
        verbose_name_plural = "05 ATL Dinkes"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDinkes(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Usul Hapus Dinkes"
        verbose_name_plural = "05 ATL Usul Hapus Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDinkes(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "05 Usul Hapus ATL Dinkes"
        verbose_name_plural = "05 Usul Hapus ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDinkes(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "05 Kontrak ATL Dinkes"
        verbose_name_plural = "05 Kontrak ATL Dinkes"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDinkes(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes"
        verbose_name_plural = "05 Harga ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDinkes(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Penghapusan Dinkes"
        verbose_name_plural = "05 ATL Penghapusan Dinkes"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDinkes(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "05 Tahun Berkurang ATL Dinkes"
        verbose_name_plural = "05 Tahun Berkurang ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDinkes(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "05 Penghapusan ATL Dinkes"
        verbose_name_plural = "05 Penghapusan ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDinkes(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDinkes(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Tujuan ATL Dinkes"
        verbose_name_plural = "05 SKPD Tujuan ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkes(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes"
        verbose_name_plural = "05 Foto ATL Dinkes"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##RSUD
##model pada app RSUD
class ATLRSUD(ATL):
    class Meta:
        proxy = True
        verbose_name = "06 ATL RSUD"
        verbose_name_plural = "06 ATL RSUD"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusRSUD(ATL):
    class Meta:
        proxy = True
        verbose_name = "06 ATL Usul Hapus RSUD"
        verbose_name_plural = "06 ATL Usul Hapus RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLRSUD(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "06 Usul Hapus ATL RSUD"
        verbose_name_plural = "06 Usul Hapus ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLRSUD(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "06 Kontrak ATL RSUD"
        verbose_name_plural = "06 Kontrak ATL RSUD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLRSUD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "06 Harga ATL RSUD"
        verbose_name_plural = "06 Harga ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanRSUD(ATL):
    class Meta:
        proxy = True
        verbose_name = "06 ATL Penghapusan RSUD"
        verbose_name_plural = "06 ATL Penghapusan RSUD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLRSUD(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "06 Tahun Berkurang ATL RSUD"
        verbose_name_plural = "06 Tahun Berkurang ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLRSUD(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "06 Penghapusan ATL RSUD"
        verbose_name_plural = "06 Penghapusan ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLRSUD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Asal ATL RSUD"
        verbose_name_plural = "06 SKPD Asal ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLRSUD(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "06 SKPD Tujuan ATL RSUD"
        verbose_name_plural = "06 SKPD Tujuan ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLRSUD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "06 Foto ATL RSUD"
        verbose_name_plural = "06 Foto ATL RSUD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Disdik
##model pada app Disdik
class ATLDisdik(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik"
        verbose_name_plural = "07 ATL Disdik"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDisdik(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Usul Hapus Disdik"
        verbose_name_plural = "07 ATL Usul Hapus Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDisdik(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "07 Usul Hapus ATL Disdik"
        verbose_name_plural = "07 Usul Hapus ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDisdik(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "07 Kontrak ATL Disdik"
        verbose_name_plural = "07 Kontrak ATL Disdik"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDisdik(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik"
        verbose_name_plural = "07 Harga ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDisdik(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Penghapusan Disdik"
        verbose_name_plural = "07 ATL Penghapusan Disdik"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDisdik(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "07 Tahun Berkurang ATL Disdik"
        verbose_name_plural = "07 Tahun Berkurang ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDisdik(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "07 Penghapusan ATL Disdik"
        verbose_name_plural = "07 Penghapusan ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDisdik(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik"
        verbose_name_plural = "07 SKPD Asal ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDisdik(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Tujuan ATL Disdik"
        verbose_name_plural = "07 SKPD Tujuan ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdik(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik"
        verbose_name_plural = "07 Foto ATL Disdik"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Perpustakaan
##model pada app Perpustakaan
class ATLPerpustakaan(ATL):
    class Meta:
        proxy = True
        verbose_name = "08 ATL Perpustakaan"
        verbose_name_plural = "08 ATL Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusPerpustakaan(ATL):
    class Meta:
        proxy = True
        verbose_name = "08 ATL Usul Hapus Perpustakaan"
        verbose_name_plural = "08 ATL Usul Hapus Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLPerpustakaan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "08 Usul Hapus ATL Perpustakaan"
        verbose_name_plural = "08 Usul Hapus ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLPerpustakaan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "08 Kontrak ATL Perpustakaan"
        verbose_name_plural = "08 Kontrak ATL Perpustakaan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLPerpustakaan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "08 Harga ATL Perpustakaan"
        verbose_name_plural = "08 Harga ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanPerpustakaan(ATL):
    class Meta:
        proxy = True
        verbose_name = "08 ATL Penghapusan Perpustakaan"
        verbose_name_plural = "08 ATL Penghapusan Perpustakaan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLPerpustakaan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "08 Tahun Berkurang ATL Perpustakaan"
        verbose_name_plural = "08 Tahun Berkurang ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLPerpustakaan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "08 Penghapusan ATL Perpustakaan"
        verbose_name_plural = "08 Penghapusan ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLPerpustakaan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Asal ATL Perpustakaan"
        verbose_name_plural = "08 SKPD Asal ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLPerpustakaan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "08 SKPD Tujuan ATL Perpustakaan"
        verbose_name_plural = "08 SKPD Tujuan ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLPerpustakaan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "08 Foto ATL Perpustakaan"
        verbose_name_plural = "08 Foto ATL Perpustakaan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Sosial
##model pada app Sosial
class ATLSosial(ATL):
    class Meta:
        proxy = True
        verbose_name = "09 ATL Sosial"
        verbose_name_plural = "09 ATL Sosial"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusSosial(ATL):
    class Meta:
        proxy = True
        verbose_name = "09 ATL Usul Hapus Sosial"
        verbose_name_plural = "09 ATL Usul Hapus Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLSosial(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "09 Usul Hapus ATL Sosial"
        verbose_name_plural = "09 Usul Hapus ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLSosial(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "09 Kontrak ATL Sosial"
        verbose_name_plural = "09 Kontrak ATL Sosial"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLSosial(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "09 Harga ATL Sosial"
        verbose_name_plural = "09 Harga ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanSosial(ATL):
    class Meta:
        proxy = True
        verbose_name = "09 ATL Penghapusan Sosial"
        verbose_name_plural = "09 ATL Penghapusan Sosial"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLSosial(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "09 Tahun Berkurang ATL Sosial"
        verbose_name_plural = "09 Tahun Berkurang ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLSosial(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "09 Penghapusan ATL Sosial"
        verbose_name_plural = "09 Penghapusan ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLSosial(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Asal ATL Sosial"
        verbose_name_plural = "09 SKPD Asal ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLSosial(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "09 SKPD Tujuan ATL Sosial"
        verbose_name_plural = "09 SKPD Tujuan ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLSosial(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "09 Foto ATL Sosial"
        verbose_name_plural = "09 Foto ATL Sosial"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DPMD
##model pada app DPMD
class ATLDPMD(ATL):
    class Meta:
        proxy = True
        verbose_name = "10 ATL DPMD"
        verbose_name_plural = "10 ATL DPMD"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDPMD(ATL):
    class Meta:
        proxy = True
        verbose_name = "10 ATL Usul Hapus DPMD"
        verbose_name_plural = "10 ATL Usul Hapus DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDPMD(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "10 Usul Hapus ATL DPMD"
        verbose_name_plural = "10 Usul Hapus ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDPMD(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "10 Kontrak ATL DPMD"
        verbose_name_plural = "10 Kontrak ATL DPMD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDPMD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "10 Harga ATL DPMD"
        verbose_name_plural = "10 Harga ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDPMD(ATL):
    class Meta:
        proxy = True
        verbose_name = "10 ATL Penghapusan DPMD"
        verbose_name_plural = "10 ATL Penghapusan DPMD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDPMD(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "10 Tahun Berkurang ATL DPMD"
        verbose_name_plural = "10 Tahun Berkurang ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDPMD(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "10 Penghapusan ATL DPMD"
        verbose_name_plural = "10 Penghapusan ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDPMD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Asal ATL DPMD"
        verbose_name_plural = "10 SKPD Asal ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDPMD(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "10 SKPD Tujuan ATL DPMD"
        verbose_name_plural = "10 SKPD Tujuan ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDPMD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "10 Foto ATL DPMD"
        verbose_name_plural = "10 Foto ATL DPMD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DPPPA
##model pada app DPPPA
class ATLDPPPA(ATL):
    class Meta:
        proxy = True
        verbose_name = "11 ATL DPPPA"
        verbose_name_plural = "11 ATL DPPPA"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDPPPA(ATL):
    class Meta:
        proxy = True
        verbose_name = "11 ATL Usul Hapus DPPPA"
        verbose_name_plural = "11 ATL Usul Hapus DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDPPPA(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "11 Usul Hapus ATL DPPPA"
        verbose_name_plural = "11 Usul Hapus ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDPPPA(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "11 Kontrak ATL DPPPA"
        verbose_name_plural = "11 Kontrak ATL DPPPA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDPPPA(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "11 Harga ATL DPPPA"
        verbose_name_plural = "11 Harga ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDPPPA(ATL):
    class Meta:
        proxy = True
        verbose_name = "11 ATL Penghapusan DPPPA"
        verbose_name_plural = "11 ATL Penghapusan DPPPA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDPPPA(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "11 Tahun Berkurang ATL DPPPA"
        verbose_name_plural = "11 Tahun Berkurang ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDPPPA(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "11 Penghapusan ATL DPPPA"
        verbose_name_plural = "11 Penghapusan ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDPPPA(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Asal ATL DPPPA"
        verbose_name_plural = "11 SKPD Asal ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDPPPA(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "11 SKPD Tujuan ATL DPPPA"
        verbose_name_plural = "11 SKPD Tujuan ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDPPPA(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "11 Foto ATL DPPPA"
        verbose_name_plural = "11 Foto ATL DPPPA"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DukCatPil
##model pada app DukCatPil
class ATLDukCatPil(ATL):
    class Meta:
        proxy = True
        verbose_name = "12 ATL DukCatPil"
        verbose_name_plural = "12 ATL DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDukCatPil(ATL):
    class Meta:
        proxy = True
        verbose_name = "12 ATL Usul Hapus DukCatPil"
        verbose_name_plural = "12 ATL Usul Hapus DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDukCatPil(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "12 Usul Hapus ATL DukCatPil"
        verbose_name_plural = "12 Usul Hapus ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDukCatPil(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "12 Kontrak ATL DukCatPil"
        verbose_name_plural = "12 Kontrak ATL DukCatPil"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDukCatPil(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "12 Harga ATL DukCatPil"
        verbose_name_plural = "12 Harga ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDukCatPil(ATL):
    class Meta:
        proxy = True
        verbose_name = "12 ATL Penghapusan DukCatPil"
        verbose_name_plural = "12 ATL Penghapusan DukCatPil"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDukCatPil(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "12 Tahun Berkurang ATL DukCatPil"
        verbose_name_plural = "12 Tahun Berkurang ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDukCatPil(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "12 Penghapusan ATL DukCatPil"
        verbose_name_plural = "12 Penghapusan ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDukCatPil(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Asal ATL DukCatPil"
        verbose_name_plural = "12 SKPD Asal ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDukCatPil(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "12 SKPD Tujuan ATL DukCatPil"
        verbose_name_plural = "12 SKPD Tujuan ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDukCatPil(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "12 Foto ATL DukCatPil"
        verbose_name_plural = "12 Foto ATL DukCatPil"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Pertanian
##model pada app Pertanian
class ATLPertanian(ATL):
    class Meta:
        proxy = True
        verbose_name = "13 ATL Pertanian"
        verbose_name_plural = "13 ATL Pertanian"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusPertanian(ATL):
    class Meta:
        proxy = True
        verbose_name = "13 ATL Usul Hapus Pertanian"
        verbose_name_plural = "13 ATL Usul Hapus Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLPertanian(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "13 Usul Hapus ATL Pertanian"
        verbose_name_plural = "13 Usul Hapus ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLPertanian(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "13 Kontrak ATL Pertanian"
        verbose_name_plural = "13 Kontrak ATL Pertanian"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLPertanian(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "13 Harga ATL Pertanian"
        verbose_name_plural = "13 Harga ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanPertanian(ATL):
    class Meta:
        proxy = True
        verbose_name = "13 ATL Penghapusan Pertanian"
        verbose_name_plural = "13 ATL Penghapusan Pertanian"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLPertanian(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "13 Tahun Berkurang ATL Pertanian"
        verbose_name_plural = "13 Tahun Berkurang ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLPertanian(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "13 Penghapusan ATL Pertanian"
        verbose_name_plural = "13 Penghapusan ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLPertanian(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Asal ATL Pertanian"
        verbose_name_plural = "13 SKPD Asal ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLPertanian(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "13 SKPD Tujuan ATL Pertanian"
        verbose_name_plural = "13 SKPD Tujuan ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLPertanian(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "13 Foto ATL Pertanian"
        verbose_name_plural = "13 Foto ATL Pertanian"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Kehutanan
##model pada app Kehutanan
class ATLKehutanan(ATL):
    class Meta:
        proxy = True
        verbose_name = "14 ATL Kehutanan"
        verbose_name_plural = "14 ATL Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusKehutanan(ATL):
    class Meta:
        proxy = True
        verbose_name = "14 ATL Usul Hapus Kehutanan"
        verbose_name_plural = "14 ATL Usul Hapus Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLKehutanan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "14 Usul Hapus ATL Kehutanan"
        verbose_name_plural = "14 Usul Hapus ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLKehutanan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "14 Kontrak ATL Kehutanan"
        verbose_name_plural = "14 Kontrak ATL Kehutanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLKehutanan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "14 Harga ATL Kehutanan"
        verbose_name_plural = "14 Harga ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanKehutanan(ATL):
    class Meta:
        proxy = True
        verbose_name = "14 ATL Penghapusan Kehutanan"
        verbose_name_plural = "14 ATL Penghapusan Kehutanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLKehutanan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "14 Tahun Berkurang ATL Kehutanan"
        verbose_name_plural = "14 Tahun Berkurang ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLKehutanan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "14 Penghapusan ATL Kehutanan"
        verbose_name_plural = "14 Penghapusan ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLKehutanan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Asal ATL Kehutanan"
        verbose_name_plural = "14 SKPD Asal ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLKehutanan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "14 SKPD Tujuan ATL Kehutanan"
        verbose_name_plural = "14 SKPD Tujuan ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLKehutanan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "14 Foto ATL Kehutanan"
        verbose_name_plural = "14 Foto ATL Kehutanan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DKP
##model pada app DKP
class ATLDKP(ATL):
    class Meta:
        proxy = True
        verbose_name = "15 ATL DKP"
        verbose_name_plural = "15 ATL DKP"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDKP(ATL):
    class Meta:
        proxy = True
        verbose_name = "15 ATL Usul Hapus DKP"
        verbose_name_plural = "15 ATL Usul Hapus DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDKP(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "15 Usul Hapus ATL DKP"
        verbose_name_plural = "15 Usul Hapus ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDKP(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "15 Kontrak ATL DKP"
        verbose_name_plural = "15 Kontrak ATL DKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDKP(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "15 Harga ATL DKP"
        verbose_name_plural = "15 Harga ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDKP(ATL):
    class Meta:
        proxy = True
        verbose_name = "15 ATL Penghapusan DKP"
        verbose_name_plural = "15 ATL Penghapusan DKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDKP(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "15 Tahun Berkurang ATL DKP"
        verbose_name_plural = "15 Tahun Berkurang ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDKP(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "15 Penghapusan ATL DKP"
        verbose_name_plural = "15 Penghapusan ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDKP(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Asal ATL DKP"
        verbose_name_plural = "15 SKPD Asal ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDKP(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "15 SKPD Tujuan ATL DKP"
        verbose_name_plural = "15 SKPD Tujuan ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDKP(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "15 Foto ATL DKP"
        verbose_name_plural = "15 Foto ATL DKP"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DKUKMP
##model pada app DKUKMP
class ATLDKUKMP(ATL):
    class Meta:
        proxy = True
        verbose_name = "16 ATL DKUKMP"
        verbose_name_plural = "16 ATL DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDKUKMP(ATL):
    class Meta:
        proxy = True
        verbose_name = "16 ATL Usul Hapus DKUKMP"
        verbose_name_plural = "16 ATL Usul Hapus DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDKUKMP(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "16 Usul Hapus ATL DKUKMP"
        verbose_name_plural = "16 Usul Hapus ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDKUKMP(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "16 Kontrak ATL DKUKMP"
        verbose_name_plural = "16 Kontrak ATL DKUKMP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDKUKMP(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "16 Harga ATL DKUKMP"
        verbose_name_plural = "16 Harga ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDKUKMP(ATL):
    class Meta:
        proxy = True
        verbose_name = "16 ATL Penghapusan DKUKMP"
        verbose_name_plural = "16 ATL Penghapusan DKUKMP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDKUKMP(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "16 Tahun Berkurang ATL DKUKMP"
        verbose_name_plural = "16 Tahun Berkurang ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDKUKMP(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "16 Penghapusan ATL DKUKMP"
        verbose_name_plural = "16 Penghapusan ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDKUKMP(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Asal ATL DKUKMP"
        verbose_name_plural = "16 SKPD Asal ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDKUKMP(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "16 SKPD Tujuan ATL DKUKMP"
        verbose_name_plural = "16 SKPD Tujuan ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDKUKMP(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "16 Foto ATL DKUKMP"
        verbose_name_plural = "16 Foto ATL DKUKMP"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Distamben
##model pada app Distamben
class ATLDistamben(ATL):
    class Meta:
        proxy = True
        verbose_name = "17 ATL Distamben"
        verbose_name_plural = "17 ATL Distamben"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDistamben(ATL):
    class Meta:
        proxy = True
        verbose_name = "17 ATL Usul Hapus Distamben"
        verbose_name_plural = "17 ATL Usul Hapus Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDistamben(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "17 Usul Hapus ATL Distamben"
        verbose_name_plural = "17 Usul Hapus ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDistamben(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "17 Kontrak ATL Distamben"
        verbose_name_plural = "17 Kontrak ATL Distamben"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDistamben(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "17 Harga ATL Distamben"
        verbose_name_plural = "17 Harga ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDistamben(ATL):
    class Meta:
        proxy = True
        verbose_name = "17 ATL Penghapusan Distamben"
        verbose_name_plural = "17 ATL Penghapusan Distamben"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDistamben(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "17 Tahun Berkurang ATL Distamben"
        verbose_name_plural = "17 Tahun Berkurang ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDistamben(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "17 Penghapusan ATL Distamben"
        verbose_name_plural = "17 Penghapusan ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDistamben(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Asal ATL Distamben"
        verbose_name_plural = "17 SKPD Asal ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDistamben(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "17 SKPD Tujuan ATL Distamben"
        verbose_name_plural = "17 SKPD Tujuan ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDistamben(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "17 Foto ATL Distamben"
        verbose_name_plural = "17 Foto ATL Distamben"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DPMPTSP
##model pada app DPMPTSP
class ATLDPMPTSP(ATL):
    class Meta:
        proxy = True
        verbose_name = "18 ATL DPMPTSP"
        verbose_name_plural = "18 ATL DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDPMPTSP(ATL):
    class Meta:
        proxy = True
        verbose_name = "18 ATL Usul Hapus DPMPTSP"
        verbose_name_plural = "18 ATL Usul Hapus DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDPMPTSP(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "18 Usul Hapus ATL DPMPTSP"
        verbose_name_plural = "18 Usul Hapus ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDPMPTSP(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "18 Kontrak ATL DPMPTSP"
        verbose_name_plural = "18 Kontrak ATL DPMPTSP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDPMPTSP(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "18 Harga ATL DPMPTSP"
        verbose_name_plural = "18 Harga ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDPMPTSP(ATL):
    class Meta:
        proxy = True
        verbose_name = "18 ATL Penghapusan DPMPTSP"
        verbose_name_plural = "18 ATL Penghapusan DPMPTSP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDPMPTSP(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "18 Tahun Berkurang ATL DPMPTSP"
        verbose_name_plural = "18 Tahun Berkurang ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDPMPTSP(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "18 Penghapusan ATL DPMPTSP"
        verbose_name_plural = "18 Penghapusan ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDPMPTSP(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Asal ATL DPMPTSP"
        verbose_name_plural = "18 SKPD Asal ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDPMPTSP(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "18 SKPD Tujuan ATL DPMPTSP"
        verbose_name_plural = "18 SKPD Tujuan ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDPMPTSP(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "18 Foto ATL DPMPTSP"
        verbose_name_plural = "18 Foto ATL DPMPTSP"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##BKD
##model pada app BKD
class ATLBKD(ATL):
    class Meta:
        proxy = True
        verbose_name = "19 ATL BKD"
        verbose_name_plural = "19 ATL BKD"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBKD(ATL):
    class Meta:
        proxy = True
        verbose_name = "19 ATL Usul Hapus BKD"
        verbose_name_plural = "19 ATL Usul Hapus BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBKD(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "19 Usul Hapus ATL BKD"
        verbose_name_plural = "19 Usul Hapus ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBKD(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "19 Kontrak ATL BKD"
        verbose_name_plural = "19 Kontrak ATL BKD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBKD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "19 Harga ATL BKD"
        verbose_name_plural = "19 Harga ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBKD(ATL):
    class Meta:
        proxy = True
        verbose_name = "19 ATL Penghapusan BKD"
        verbose_name_plural = "19 ATL Penghapusan BKD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBKD(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "19 Tahun Berkurang ATL BKD"
        verbose_name_plural = "19 Tahun Berkurang ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBKD(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "19 Penghapusan ATL BKD"
        verbose_name_plural = "19 Penghapusan ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBKD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Asal ATL BKD"
        verbose_name_plural = "19 SKPD Asal ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBKD(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "19 SKPD Tujuan ATL BKD"
        verbose_name_plural = "19 SKPD Tujuan ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBKD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "19 Foto ATL BKD"
        verbose_name_plural = "19 Foto ATL BKD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Inspektorat
##model pada app Inspektorat
class ATLInspektorat(ATL):
    class Meta:
        proxy = True
        verbose_name = "20 ATL Inspektorat"
        verbose_name_plural = "20 ATL Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusInspektorat(ATL):
    class Meta:
        proxy = True
        verbose_name = "20 ATL Usul Hapus Inspektorat"
        verbose_name_plural = "20 ATL Usul Hapus Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLInspektorat(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "20 Usul Hapus ATL Inspektorat"
        verbose_name_plural = "20 Usul Hapus ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLInspektorat(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "20 Kontrak ATL Inspektorat"
        verbose_name_plural = "20 Kontrak ATL Inspektorat"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLInspektorat(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "20 Harga ATL Inspektorat"
        verbose_name_plural = "20 Harga ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanInspektorat(ATL):
    class Meta:
        proxy = True
        verbose_name = "20 ATL Penghapusan Inspektorat"
        verbose_name_plural = "20 ATL Penghapusan Inspektorat"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLInspektorat(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "20 Tahun Berkurang ATL Inspektorat"
        verbose_name_plural = "20 Tahun Berkurang ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLInspektorat(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "20 Penghapusan ATL Inspektorat"
        verbose_name_plural = "20 Penghapusan ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLInspektorat(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Asal ATL Inspektorat"
        verbose_name_plural = "20 SKPD Asal ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLInspektorat(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "20 SKPD Tujuan ATL Inspektorat"
        verbose_name_plural = "20 SKPD Tujuan ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLInspektorat(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "20 Foto ATL Inspektorat"
        verbose_name_plural = "20 Foto ATL Inspektorat"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##BAPPEDA
##model pada app BAPPEDA
class ATLBAPPEDA(ATL):
    class Meta:
        proxy = True
        verbose_name = "21 ATL BAPPEDA"
        verbose_name_plural = "21 ATL BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBAPPEDA(ATL):
    class Meta:
        proxy = True
        verbose_name = "21 ATL Usul Hapus BAPPEDA"
        verbose_name_plural = "21 ATL Usul Hapus BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBAPPEDA(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "21 Usul Hapus ATL BAPPEDA"
        verbose_name_plural = "21 Usul Hapus ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBAPPEDA(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "21 Kontrak ATL BAPPEDA"
        verbose_name_plural = "21 Kontrak ATL BAPPEDA"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBAPPEDA(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "21 Harga ATL BAPPEDA"
        verbose_name_plural = "21 Harga ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBAPPEDA(ATL):
    class Meta:
        proxy = True
        verbose_name = "21 ATL Penghapusan BAPPEDA"
        verbose_name_plural = "21 ATL Penghapusan BAPPEDA"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBAPPEDA(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "21 Tahun Berkurang ATL BAPPEDA"
        verbose_name_plural = "21 Tahun Berkurang ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBAPPEDA(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "21 Penghapusan ATL BAPPEDA"
        verbose_name_plural = "21 Penghapusan ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBAPPEDA(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Asal ATL BAPPEDA"
        verbose_name_plural = "21 SKPD Asal ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBAPPEDA(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "21 SKPD Tujuan ATL BAPPEDA"
        verbose_name_plural = "21 SKPD Tujuan ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBAPPEDA(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "21 Foto ATL BAPPEDA"
        verbose_name_plural = "21 Foto ATL BAPPEDA"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DLH
##model pada app DLH
class ATLDLH(ATL):
    class Meta:
        proxy = True
        verbose_name = "22 ATL DLH"
        verbose_name_plural = "22 ATL DLH"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDLH(ATL):
    class Meta:
        proxy = True
        verbose_name = "22 ATL Usul Hapus DLH"
        verbose_name_plural = "22 ATL Usul Hapus DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDLH(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "22 Usul Hapus ATL DLH"
        verbose_name_plural = "22 Usul Hapus ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDLH(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "22 Kontrak ATL DLH"
        verbose_name_plural = "22 Kontrak ATL DLH"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDLH(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "22 Harga ATL DLH"
        verbose_name_plural = "22 Harga ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDLH(ATL):
    class Meta:
        proxy = True
        verbose_name = "22 ATL Penghapusan DLH"
        verbose_name_plural = "22 ATL Penghapusan DLH"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDLH(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "22 Tahun Berkurang ATL DLH"
        verbose_name_plural = "22 Tahun Berkurang ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDLH(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "22 Penghapusan ATL DLH"
        verbose_name_plural = "22 Penghapusan ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDLH(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Asal ATL DLH"
        verbose_name_plural = "22 SKPD Asal ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDLH(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "22 SKPD Tujuan ATL DLH"
        verbose_name_plural = "22 SKPD Tujuan ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDLH(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "22 Foto ATL DLH"
        verbose_name_plural = "22 Foto ATL DLH"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DKO
##model pada app DKO
class ATLDKO(ATL):
    class Meta:
        proxy = True
        verbose_name = "23 ATL DKO"
        verbose_name_plural = "23 ATL DKO"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDKO(ATL):
    class Meta:
        proxy = True
        verbose_name = "23 ATL Usul Hapus DKO"
        verbose_name_plural = "23 ATL Usul Hapus DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDKO(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "23 Usul Hapus ATL DKO"
        verbose_name_plural = "23 Usul Hapus ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDKO(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "23 Kontrak ATL DKO"
        verbose_name_plural = "23 Kontrak ATL DKO"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDKO(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "23 Harga ATL DKO"
        verbose_name_plural = "23 Harga ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDKO(ATL):
    class Meta:
        proxy = True
        verbose_name = "23 ATL Penghapusan DKO"
        verbose_name_plural = "23 ATL Penghapusan DKO"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDKO(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "23 Tahun Berkurang ATL DKO"
        verbose_name_plural = "23 Tahun Berkurang ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDKO(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "23 Penghapusan ATL DKO"
        verbose_name_plural = "23 Penghapusan ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDKO(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Asal ATL DKO"
        verbose_name_plural = "23 SKPD Asal ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDKO(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "23 SKPD Tujuan ATL DKO"
        verbose_name_plural = "23 SKPD Tujuan ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDKO(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "23 Foto ATL DKO"
        verbose_name_plural = "23 Foto ATL DKO"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##KESBANGPOL
##model pada app KESBANGPOL
class ATLKESBANGPOL(ATL):
    class Meta:
        proxy = True
        verbose_name = "24 ATL KESBANGPOL"
        verbose_name_plural = "24 ATL KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusKESBANGPOL(ATL):
    class Meta:
        proxy = True
        verbose_name = "24 ATL Usul Hapus KESBANGPOL"
        verbose_name_plural = "24 ATL Usul Hapus KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLKESBANGPOL(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "24 Usul Hapus ATL KESBANGPOL"
        verbose_name_plural = "24 Usul Hapus ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLKESBANGPOL(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "24 Kontrak ATL KESBANGPOL"
        verbose_name_plural = "24 Kontrak ATL KESBANGPOL"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLKESBANGPOL(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "24 Harga ATL KESBANGPOL"
        verbose_name_plural = "24 Harga ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanKESBANGPOL(ATL):
    class Meta:
        proxy = True
        verbose_name = "24 ATL Penghapusan KESBANGPOL"
        verbose_name_plural = "24 ATL Penghapusan KESBANGPOL"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLKESBANGPOL(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "24 Tahun Berkurang ATL KESBANGPOL"
        verbose_name_plural = "24 Tahun Berkurang ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLKESBANGPOL(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "24 Penghapusan ATL KESBANGPOL"
        verbose_name_plural = "24 Penghapusan ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLKESBANGPOL(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Asal ATL KESBANGPOL"
        verbose_name_plural = "24 SKPD Asal ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLKESBANGPOL(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "24 SKPD Tujuan ATL KESBANGPOL"
        verbose_name_plural = "24 SKPD Tujuan ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLKESBANGPOL(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "24 Foto ATL KESBANGPOL"
        verbose_name_plural = "24 Foto ATL KESBANGPOL"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##SATPOLPP
##model pada app SATPOLPP
class ATLSATPOLPP(ATL):
    class Meta:
        proxy = True
        verbose_name = "25 ATL SATPOLPP"
        verbose_name_plural = "25 ATL SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusSATPOLPP(ATL):
    class Meta:
        proxy = True
        verbose_name = "25 ATL Usul Hapus SATPOLPP"
        verbose_name_plural = "25 ATL Usul Hapus SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLSATPOLPP(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "25 Usul Hapus ATL SATPOLPP"
        verbose_name_plural = "25 Usul Hapus ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLSATPOLPP(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "25 Kontrak ATL SATPOLPP"
        verbose_name_plural = "25 Kontrak ATL SATPOLPP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLSATPOLPP(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "25 Harga ATL SATPOLPP"
        verbose_name_plural = "25 Harga ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanSATPOLPP(ATL):
    class Meta:
        proxy = True
        verbose_name = "25 ATL Penghapusan SATPOLPP"
        verbose_name_plural = "25 ATL Penghapusan SATPOLPP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLSATPOLPP(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "25 Tahun Berkurang ATL SATPOLPP"
        verbose_name_plural = "25 Tahun Berkurang ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLSATPOLPP(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "25 Penghapusan ATL SATPOLPP"
        verbose_name_plural = "25 Penghapusan ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLSATPOLPP(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Asal ATL SATPOLPP"
        verbose_name_plural = "25 SKPD Asal ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLSATPOLPP(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "25 SKPD Tujuan ATL SATPOLPP"
        verbose_name_plural = "25 SKPD Tujuan ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLSATPOLPP(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "25 Foto ATL SATPOLPP"
        verbose_name_plural = "25 Foto ATL SATPOLPP"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##BKPPD
##model pada app BKPPD
class ATLBKPPD(ATL):
    class Meta:
        proxy = True
        verbose_name = "26 ATL BKPPD"
        verbose_name_plural = "26 ATL BKPPD"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBKPPD(ATL):
    class Meta:
        proxy = True
        verbose_name = "26 ATL Usul Hapus BKPPD"
        verbose_name_plural = "26 ATL Usul Hapus BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBKPPD(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "26 Usul Hapus ATL BKPPD"
        verbose_name_plural = "26 Usul Hapus ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBKPPD(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "26 Kontrak ATL BKPPD"
        verbose_name_plural = "26 Kontrak ATL BKPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBKPPD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "26 Harga ATL BKPPD"
        verbose_name_plural = "26 Harga ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBKPPD(ATL):
    class Meta:
        proxy = True
        verbose_name = "26 ATL Penghapusan BKPPD"
        verbose_name_plural = "26 ATL Penghapusan BKPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBKPPD(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "26 Tahun Berkurang ATL BKPPD"
        verbose_name_plural = "26 Tahun Berkurang ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBKPPD(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "26 Penghapusan ATL BKPPD"
        verbose_name_plural = "26 Penghapusan ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBKPPD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Asal ATL BKPPD"
        verbose_name_plural = "26 SKPD Asal ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBKPPD(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "26 SKPD Tujuan ATL BKPPD"
        verbose_name_plural = "26 SKPD Tujuan ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBKPPD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "26 Foto ATL BKPPD"
        verbose_name_plural = "26 Foto ATL BKPPD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##SekretariatKorpri
##model pada app SekretariatKorpri
class ATLSekretariatKorpri(ATL):
    class Meta:
        proxy = True
        verbose_name = "27 ATL Sekretariat Korpri"
        verbose_name_plural = "27 ATL Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusSekretariatKorpri(ATL):
    class Meta:
        proxy = True
        verbose_name = "27 ATL Usul Hapus Sekretariat Korpri"
        verbose_name_plural = "27 ATL Usul Hapus Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLSekretariatKorpri(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "27 Usul Hapus ATL Sekretariat Korpri"
        verbose_name_plural = "27 Usul Hapus ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLSekretariatKorpri(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "27 Kontrak ATL Sekretariat Korpri"
        verbose_name_plural = "27 Kontrak ATL Sekretariat Korpri"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLSekretariatKorpri(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "27 Harga ATL Sekretariat Korpri"
        verbose_name_plural = "27 Harga ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanSekretariatKorpri(ATL):
    class Meta:
        proxy = True
        verbose_name = "27 ATL Penghapusan Sekretariat Korpri"
        verbose_name_plural = "27 ATL Penghapusan Sekretariat Korpri"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLSekretariatKorpri(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "27 Tahun Berkurang ATL Sekretariat Korpri"
        verbose_name_plural = "27 Tahun Berkurang ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLSekretariatKorpri(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "27 Penghapusan ATL Sekretariat Korpri"
        verbose_name_plural = "27 Penghapusan ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLSekretariatKorpri(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Asal ATL Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Asal ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLSekretariatKorpri(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "27 SKPD Tujuan ATL Sekretariat Korpri"
        verbose_name_plural = "27 SKPD Tujuan ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLSekretariatKorpri(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "27 Foto ATL Sekretariat Korpri"
        verbose_name_plural = "27 Foto ATL Sekretariat Korpri"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Paringin
##model pada app Paringin
class ATLParingin(ATL):
    class Meta:
        proxy = True
        verbose_name = "28 ATL Paringin"
        verbose_name_plural = "28 ATL Paringin"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusParingin(ATL):
    class Meta:
        proxy = True
        verbose_name = "28 ATL Usul Hapus Paringin"
        verbose_name_plural = "28 ATL Usul Hapus Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLParingin(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "28 Usul Hapus ATL Paringin"
        verbose_name_plural = "28 Usul Hapus ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLParingin(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "28 Kontrak ATL Paringin"
        verbose_name_plural = "28 Kontrak ATL Paringin"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLParingin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "28 Harga ATL Paringin"
        verbose_name_plural = "28 Harga ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanParingin(ATL):
    class Meta:
        proxy = True
        verbose_name = "28 ATL Penghapusan Paringin"
        verbose_name_plural = "28 ATL Penghapusan Paringin"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLParingin(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "28 Tahun Berkurang ATL Paringin"
        verbose_name_plural = "28 Tahun Berkurang ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLParingin(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "28 Penghapusan ATL Paringin"
        verbose_name_plural = "28 Penghapusan ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLParingin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Asal ATL Paringin"
        verbose_name_plural = "28 SKPD Asal ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLParingin(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "28 SKPD Tujuan ATL Paringin"
        verbose_name_plural = "28 SKPD Tujuan ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLParingin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "28 Foto ATL Paringin"
        verbose_name_plural = "28 Foto ATL Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##ParinginKota
##model pada app ParinginKota
class ATLParinginKota(ATL):
    class Meta:
        proxy = True
        verbose_name = "29 ATL Paringin Kota"
        verbose_name_plural = "29 ATL Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusParinginKota(ATL):
    class Meta:
        proxy = True
        verbose_name = "29 ATL Usul Hapus Paringin Kota"
        verbose_name_plural = "29 ATL Usul Hapus Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLParinginKota(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "29 Usul Hapus ATL Paringin Kota"
        verbose_name_plural = "29 Usul Hapus ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLParinginKota(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "29 Kontrak ATL Paringin Kota"
        verbose_name_plural = "29 Kontrak ATL Paringin Kota"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLParinginKota(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "29 Harga ATL Paringin Kota"
        verbose_name_plural = "29 Harga ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanParinginKota(ATL):
    class Meta:
        proxy = True
        verbose_name = "29 ATL Penghapusan Paringin Kota"
        verbose_name_plural = "29 ATL Penghapusan Paringin Kota"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLParinginKota(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "29 Tahun Berkurang ATL Paringin Kota"
        verbose_name_plural = "29 Tahun Berkurang ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLParinginKota(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "29 Penghapusan ATL Paringin Kota"
        verbose_name_plural = "29 Penghapusan ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLParinginKota(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Asal ATL Paringin Kota"
        verbose_name_plural = "29 SKPD Asal ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLParinginKota(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "29 SKPD Tujuan ATL Paringin Kota"
        verbose_name_plural = "29 SKPD Tujuan ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLParinginKota(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "29 Foto ATL Paringin Kota"
        verbose_name_plural = "29 Foto ATL Paringin Kota"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##ParinginTimur
##model pada app ParinginTimur
class ATLParinginTimur(ATL):
    class Meta:
        proxy = True
        verbose_name = "30 ATL Paringin Timur"
        verbose_name_plural = "30 ATL Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusParinginTimur(ATL):
    class Meta:
        proxy = True
        verbose_name = "30 ATL Usul Hapus Paringin Timur"
        verbose_name_plural = "30 ATL Usul Hapus Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLParinginTimur(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "30 Usul Hapus ATL Paringin Timur"
        verbose_name_plural = "30 Usul Hapus ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLParinginTimur(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "30 Kontrak ATL Paringin Timur"
        verbose_name_plural = "30 Kontrak ATL Paringin Timur"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLParinginTimur(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "30 Harga ATL Paringin Timur"
        verbose_name_plural = "30 Harga ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanParinginTimur(ATL):
    class Meta:
        proxy = True
        verbose_name = "30 ATL Penghapusan Paringin Timur"
        verbose_name_plural = "30 ATL Penghapusan Paringin Timur"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLParinginTimur(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "30 Tahun Berkurang ATL Paringin Timur"
        verbose_name_plural = "30 Tahun Berkurang ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLParinginTimur(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "30 Penghapusan ATL Paringin Timur"
        verbose_name_plural = "30 Penghapusan ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLParinginTimur(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Asal ATL Paringin Timur"
        verbose_name_plural = "30 SKPD Asal ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLParinginTimur(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "30 SKPD Tujuan ATL Paringin Timur"
        verbose_name_plural = "30 SKPD Tujuan ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLParinginTimur(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "30 Foto ATL Paringin Timur"
        verbose_name_plural = "30 Foto ATL Paringin Timur"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Lampihong
##model pada app Lampihong
class ATLLampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "31 ATL Lampihong"
        verbose_name_plural = "31 ATL Lampihong"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusLampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "31 ATL Usul Hapus Lampihong"
        verbose_name_plural = "31 ATL Usul Hapus Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLLampihong(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "31 Usul Hapus ATL Lampihong"
        verbose_name_plural = "31 Usul Hapus ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLLampihong(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "31 Kontrak ATL Lampihong"
        verbose_name_plural = "31 Kontrak ATL Lampihong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLLampihong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "31 Harga ATL Lampihong"
        verbose_name_plural = "31 Harga ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanLampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "31 ATL Penghapusan Lampihong"
        verbose_name_plural = "31 ATL Penghapusan Lampihong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLLampihong(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "31 Tahun Berkurang ATL Lampihong"
        verbose_name_plural = "31 Tahun Berkurang ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLLampihong(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "31 Penghapusan ATL Lampihong"
        verbose_name_plural = "31 Penghapusan ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLLampihong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Asal ATL Lampihong"
        verbose_name_plural = "31 SKPD Asal ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLLampihong(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "31 SKPD Tujuan ATL Lampihong"
        verbose_name_plural = "31 SKPD Tujuan ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLLampihong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "31 Foto ATL Lampihong"
        verbose_name_plural = "31 Foto ATL Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Batumandi
##model pada app Batumandi
class ATLBatumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "32 ATL Batumandi"
        verbose_name_plural = "32 ATL Batumandi"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBatumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "32 ATL Usul Hapus Batumandi"
        verbose_name_plural = "32 ATL Usul Hapus Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBatumandi(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "32 Usul Hapus ATL Batumandi"
        verbose_name_plural = "32 Usul Hapus ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBatumandi(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "32 Kontrak ATL Batumandi"
        verbose_name_plural = "32 Kontrak ATL Batumandi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBatumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "32 Harga ATL Batumandi"
        verbose_name_plural = "32 Harga ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBatumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "32 ATL Penghapusan Batumandi"
        verbose_name_plural = "32 ATL Penghapusan Batumandi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBatumandi(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "32 Tahun Berkurang ATL Batumandi"
        verbose_name_plural = "32 Tahun Berkurang ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBatumandi(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "32 Penghapusan ATL Batumandi"
        verbose_name_plural = "32 Penghapusan ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBatumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Asal ATL Batumandi"
        verbose_name_plural = "32 SKPD Asal ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBatumandi(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "32 SKPD Tujuan ATL Batumandi"
        verbose_name_plural = "32 SKPD Tujuan ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBatumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "32 Foto ATL Batumandi"
        verbose_name_plural = "32 Foto ATL Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Juai
##model pada app Juai
class ATLJuai(ATL):
    class Meta:
        proxy = True
        verbose_name = "33 ATL Juai"
        verbose_name_plural = "33 ATL Juai"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusJuai(ATL):
    class Meta:
        proxy = True
        verbose_name = "33 ATL Usul Hapus Juai"
        verbose_name_plural = "33 ATL Usul Hapus Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLJuai(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "33 Usul Hapus ATL Juai"
        verbose_name_plural = "33 Usul Hapus ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLJuai(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "33 Kontrak ATL Juai"
        verbose_name_plural = "33 Kontrak ATL Juai"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLJuai(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "33 Harga ATL Juai"
        verbose_name_plural = "33 Harga ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanJuai(ATL):
    class Meta:
        proxy = True
        verbose_name = "33 ATL Penghapusan Juai"
        verbose_name_plural = "33 ATL Penghapusan Juai"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLJuai(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "33 Tahun Berkurang ATL Juai"
        verbose_name_plural = "33 Tahun Berkurang ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLJuai(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "33 Penghapusan ATL Juai"
        verbose_name_plural = "33 Penghapusan ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLJuai(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Asal ATL Juai"
        verbose_name_plural = "33 SKPD Asal ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLJuai(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "33 SKPD Tujuan ATL Juai"
        verbose_name_plural = "33 SKPD Tujuan ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLJuai(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "33 Foto ATL Juai"
        verbose_name_plural = "33 Foto ATL Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Awayan
##model pada app Awayan
class ATLAwayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "34 ATL Awayan"
        verbose_name_plural = "34 ATL Awayan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusAwayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "34 ATL Usul Hapus Awayan"
        verbose_name_plural = "34 ATL Usul Hapus Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLAwayan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "34 Usul Hapus ATL Awayan"
        verbose_name_plural = "34 Usul Hapus ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLAwayan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "34 Kontrak ATL Awayan"
        verbose_name_plural = "34 Kontrak ATL Awayan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLAwayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "34 Harga ATL Awayan"
        verbose_name_plural = "34 Harga ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanAwayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "34 ATL Penghapusan Awayan"
        verbose_name_plural = "34 ATL Penghapusan Awayan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLAwayan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "34 Tahun Berkurang ATL Awayan"
        verbose_name_plural = "34 Tahun Berkurang ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLAwayan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "34 Penghapusan ATL Awayan"
        verbose_name_plural = "34 Penghapusan ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLAwayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Asal ATL Awayan"
        verbose_name_plural = "34 SKPD Asal ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLAwayan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "34 SKPD Tujuan ATL Awayan"
        verbose_name_plural = "34 SKPD Tujuan ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLAwayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "34 Foto ATL Awayan"
        verbose_name_plural = "34 Foto ATL Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Halong
##model pada app Halong
class ATLHalong(ATL):
    class Meta:
        proxy = True
        verbose_name = "35 ATL Halong"
        verbose_name_plural = "35 ATL Halong"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusHalong(ATL):
    class Meta:
        proxy = True
        verbose_name = "35 ATL Usul Hapus Halong"
        verbose_name_plural = "35 ATL Usul Hapus Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLHalong(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "35 Usul Hapus ATL Halong"
        verbose_name_plural = "35 Usul Hapus ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLHalong(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "35 Kontrak ATL Halong"
        verbose_name_plural = "35 Kontrak ATL Halong"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLHalong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "35 Harga ATL Halong"
        verbose_name_plural = "35 Harga ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanHalong(ATL):
    class Meta:
        proxy = True
        verbose_name = "35 ATL Penghapusan Halong"
        verbose_name_plural = "35 ATL Penghapusan Halong"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLHalong(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "35 Tahun Berkurang ATL Halong"
        verbose_name_plural = "35 Tahun Berkurang ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLHalong(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "35 Penghapusan ATL Halong"
        verbose_name_plural = "35 Penghapusan ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLHalong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Asal ATL Halong"
        verbose_name_plural = "35 SKPD Asal ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLHalong(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "35 SKPD Tujuan ATL Halong"
        verbose_name_plural = "35 SKPD Tujuan ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLHalong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "35 Foto ATL Halong"
        verbose_name_plural = "35 Foto ATL Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##ParinginSelatan
##model pada app ParinginSelatan
class ATLParinginSelatan(ATL):
    class Meta:
        proxy = True
        verbose_name = "36 ATL Paringin Selatan"
        verbose_name_plural = "36 ATL Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusParinginSelatan(ATL):
    class Meta:
        proxy = True
        verbose_name = "36 ATL Usul Hapus Paringin Selatan"
        verbose_name_plural = "36 ATL Usul Hapus Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLParinginSelatan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "36 Usul Hapus ATL Paringin Selatan"
        verbose_name_plural = "36 Usul Hapus ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLParinginSelatan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "36 Kontrak ATL Paringin Selatan"
        verbose_name_plural = "36 Kontrak ATL Paringin Selatan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLParinginSelatan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "36 Harga ATL Paringin Selatan"
        verbose_name_plural = "36 Harga ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanParinginSelatan(ATL):
    class Meta:
        proxy = True
        verbose_name = "36 ATL Penghapusan Paringin Selatan"
        verbose_name_plural = "36 ATL Penghapusan Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLParinginSelatan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "36 Tahun Berkurang ATL Paringin Selatan"
        verbose_name_plural = "36 Tahun Berkurang ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLParinginSelatan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "36 Penghapusan ATL Paringin Selatan"
        verbose_name_plural = "36 Penghapusan ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLParinginSelatan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Asal ATL Paringin Selatan"
        verbose_name_plural = "36 SKPD Asal ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLParinginSelatan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "36 SKPD Tujuan ATL Paringin Selatan"
        verbose_name_plural = "36 SKPD Tujuan ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLParinginSelatan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "36 Foto ATL Paringin Selatan"
        verbose_name_plural = "36 Foto ATL Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##BatuPiring
##model pada app BatuPiring
class ATLBatuPiring(ATL):
    class Meta:
        proxy = True
        verbose_name = "37 ATL Batu Piring"
        verbose_name_plural = "37 ATL Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBatuPiring(ATL):
    class Meta:
        proxy = True
        verbose_name = "37 ATL Usul Hapus Batu Piring"
        verbose_name_plural = "37 ATL Usul Hapus Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBatuPiring(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "37 Usul Hapus ATL Batu Piring"
        verbose_name_plural = "37 Usul Hapus ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBatuPiring(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "37 Kontrak ATL Batu Piring"
        verbose_name_plural = "37 Kontrak ATL Batu Piring"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBatuPiring(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "37 Harga ATL Batu Piring"
        verbose_name_plural = "37 Harga ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBatuPiring(ATL):
    class Meta:
        proxy = True
        verbose_name = "37 ATL Penghapusan Batu Piring"
        verbose_name_plural = "37 ATL Penghapusan Batu Piring"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBatuPiring(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "37 Tahun Berkurang ATL Batu Piring"
        verbose_name_plural = "37 Tahun Berkurang ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBatuPiring(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "37 Penghapusan ATL Batu Piring"
        verbose_name_plural = "37 Penghapusan ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBatuPiring(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Asal ATL Batu Piring"
        verbose_name_plural = "37 SKPD Asal ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBatuPiring(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "37 SKPD Tujuan ATL Batu Piring"
        verbose_name_plural = "37 SKPD Tujuan ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBatuPiring(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "37 Foto ATL Batu Piring"
        verbose_name_plural = "37 Foto ATL Batu Piring"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##TebingTinggi
##model pada app TebingTinggi
class ATLTebingTinggi(ATL):
    class Meta:
        proxy = True
        verbose_name = "38 ATL Tebing Tinggi"
        verbose_name_plural = "38 ATL Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusTebingTinggi(ATL):
    class Meta:
        proxy = True
        verbose_name = "38 ATL Usul Hapus Tebing Tinggi"
        verbose_name_plural = "38 ATL Usul Hapus Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLTebingTinggi(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "38 Usul Hapus ATL Tebing Tinggi"
        verbose_name_plural = "38 Usul Hapus ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLTebingTinggi(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "38 Kontrak ATL Tebing Tinggi"
        verbose_name_plural = "38 Kontrak ATL Tebing Tinggi"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLTebingTinggi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "38 Harga ATL Tebing Tinggi"
        verbose_name_plural = "38 Harga ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanTebingTinggi(ATL):
    class Meta:
        proxy = True
        verbose_name = "38 ATL Penghapusan Tebing Tinggi"
        verbose_name_plural = "38 ATL Penghapusan Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLTebingTinggi(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "38 Tahun Berkurang ATL Tebing Tinggi"
        verbose_name_plural = "38 Tahun Berkurang ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLTebingTinggi(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "38 Penghapusan ATL Tebing Tinggi"
        verbose_name_plural = "38 Penghapusan ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLTebingTinggi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Asal ATL Tebing Tinggi"
        verbose_name_plural = "38 SKPD Asal ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLTebingTinggi(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "38 SKPD Tujuan ATL Tebing Tinggi"
        verbose_name_plural = "38 SKPD Tujuan ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLTebingTinggi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "38 Foto ATL Tebing Tinggi"
        verbose_name_plural = "38 Foto ATL Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##BPBD
##model pada app BPBD
class ATLBPBD(ATL):
    class Meta:
        proxy = True
        verbose_name = "39 ATL BPBD"
        verbose_name_plural = "39 ATL BPBD"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBPBD(ATL):
    class Meta:
        proxy = True
        verbose_name = "39 ATL Usul Hapus BPBD"
        verbose_name_plural = "39 ATL Usul Hapus BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBPBD(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "39 Usul Hapus ATL BPBD"
        verbose_name_plural = "39 Usul Hapus ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBPBD(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "39 Kontrak ATL BPBD"
        verbose_name_plural = "39 Kontrak ATL BPBD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBPBD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "39 Harga ATL BPBD"
        verbose_name_plural = "39 Harga ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBPBD(ATL):
    class Meta:
        proxy = True
        verbose_name = "39 ATL Penghapusan BPBD"
        verbose_name_plural = "39 ATL Penghapusan BPBD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBPBD(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "39 Tahun Berkurang ATL BPBD"
        verbose_name_plural = "39 Tahun Berkurang ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBPBD(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "39 Penghapusan ATL BPBD"
        verbose_name_plural = "39 Penghapusan ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBPBD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Asal ATL BPBD"
        verbose_name_plural = "39 SKPD Asal ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBPBD(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "39 SKPD Tujuan ATL BPBD"
        verbose_name_plural = "39 SKPD Tujuan ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBPBD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "39 Foto ATL BPBD"
        verbose_name_plural = "39 Foto ATL BPBD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DPKP
##model pada app DPKP
class ATLDPKP(ATL):
    class Meta:
        proxy = True
        verbose_name = "40 ATL DPKP"
        verbose_name_plural = "40 ATL DPKP"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDPKP(ATL):
    class Meta:
        proxy = True
        verbose_name = "40 ATL Usul Hapus DPKP"
        verbose_name_plural = "40 ATL Usul Hapus DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDPKP(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "40 Usul Hapus ATL DPKP"
        verbose_name_plural = "40 Usul Hapus ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDPKP(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "40 Kontrak ATL DPKP"
        verbose_name_plural = "40 Kontrak ATL DPKP"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDPKP(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "40 Harga ATL DPKP"
        verbose_name_plural = "40 Harga ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDPKP(ATL):
    class Meta:
        proxy = True
        verbose_name = "40 ATL Penghapusan DPKP"
        verbose_name_plural = "40 ATL Penghapusan DPKP"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDPKP(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "40 Tahun Berkurang ATL DPKP"
        verbose_name_plural = "40 Tahun Berkurang ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDPKP(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "40 Penghapusan ATL DPKP"
        verbose_name_plural = "40 Penghapusan ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDPKP(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Asal ATL DPKP"
        verbose_name_plural = "40 SKPD Asal ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDPKP(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "40 SKPD Tujuan ATL DPKP"
        verbose_name_plural = "40 SKPD Tujuan ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDPKP(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "40 Foto ATL DPKP"
        verbose_name_plural = "40 Foto ATL DPKP"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Disnakertrans
##model pada app Disnakertrans
class ATLDisnakertrans(ATL):
    class Meta:
        proxy = True
        verbose_name = "41 ATL Disnakertrans"
        verbose_name_plural = "41 ATL Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDisnakertrans(ATL):
    class Meta:
        proxy = True
        verbose_name = "41 ATL Usul Hapus Disnakertrans"
        verbose_name_plural = "41 ATL Usul Hapus Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDisnakertrans(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "41 Usul Hapus ATL Disnakertrans"
        verbose_name_plural = "41 Usul Hapus ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDisnakertrans(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "41 Kontrak ATL Disnakertrans"
        verbose_name_plural = "41 Kontrak ATL Disnakertrans"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDisnakertrans(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "41 Harga ATL Disnakertrans"
        verbose_name_plural = "41 Harga ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDisnakertrans(ATL):
    class Meta:
        proxy = True
        verbose_name = "41 ATL Penghapusan Disnakertrans"
        verbose_name_plural = "41 ATL Penghapusan Disnakertrans"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDisnakertrans(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "41 Tahun Berkurang ATL Disnakertrans"
        verbose_name_plural = "41 Tahun Berkurang ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDisnakertrans(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "41 Penghapusan ATL Disnakertrans"
        verbose_name_plural = "41 Penghapusan ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDisnakertrans(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Asal ATL Disnakertrans"
        verbose_name_plural = "41 SKPD Asal ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDisnakertrans(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "41 SKPD Tujuan ATL Disnakertrans"
        verbose_name_plural = "41 SKPD Tujuan ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisnakertrans(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "41 Foto ATL Disnakertrans"
        verbose_name_plural = "41 Foto ATL Disnakertrans"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##DPPKB
##model pada app DPPKB
class ATLDPPKB(ATL):
    class Meta:
        proxy = True
        verbose_name = "42 ATL DPPKB"
        verbose_name_plural = "42 ATL DPPKB"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusDPPKB(ATL):
    class Meta:
        proxy = True
        verbose_name = "42 ATL Usul Hapus DPPKB"
        verbose_name_plural = "42 ATL Usul Hapus DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLDPPKB(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "42 Usul Hapus ATL DPPKB"
        verbose_name_plural = "42 Usul Hapus ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLDPPKB(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "42 Kontrak ATL DPPKB"
        verbose_name_plural = "42 Kontrak ATL DPPKB"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLDPPKB(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "42 Harga ATL DPPKB"
        verbose_name_plural = "42 Harga ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanDPPKB(ATL):
    class Meta:
        proxy = True
        verbose_name = "42 ATL Penghapusan DPPKB"
        verbose_name_plural = "42 ATL Penghapusan DPPKB"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLDPPKB(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "42 Tahun Berkurang ATL DPPKB"
        verbose_name_plural = "42 Tahun Berkurang ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLDPPKB(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "42 Penghapusan ATL DPPKB"
        verbose_name_plural = "42 Penghapusan ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLDPPKB(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Asal ATL DPPKB"
        verbose_name_plural = "42 SKPD Asal ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLDPPKB(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "42 SKPD Tujuan ATL DPPKB"
        verbose_name_plural = "42 SKPD Tujuan ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDPPKB(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "42 Foto ATL DPPKB"
        verbose_name_plural = "42 Foto ATL DPPKB"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Kominfo
##model pada app Kominfo
class ATLKominfo(ATL):
    class Meta:
        proxy = True
        verbose_name = "43 ATL Kominfo"
        verbose_name_plural = "43 ATL Kominfo"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusKominfo(ATL):
    class Meta:
        proxy = True
        verbose_name = "43 ATL Usul Hapus Kominfo"
        verbose_name_plural = "43 ATL Usul Hapus Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLKominfo(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "43 Usul Hapus ATL Kominfo"
        verbose_name_plural = "43 Usul Hapus ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLKominfo(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "43 Kontrak ATL Kominfo"
        verbose_name_plural = "43 Kontrak ATL Kominfo"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLKominfo(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "43 Harga ATL Kominfo"
        verbose_name_plural = "43 Harga ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanKominfo(ATL):
    class Meta:
        proxy = True
        verbose_name = "43 ATL Penghapusan Kominfo"
        verbose_name_plural = "43 ATL Penghapusan Kominfo"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLKominfo(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "43 Tahun Berkurang ATL Kominfo"
        verbose_name_plural = "43 Tahun Berkurang ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLKominfo(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "43 Penghapusan ATL Kominfo"
        verbose_name_plural = "43 Penghapusan ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLKominfo(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Asal ATL Kominfo"
        verbose_name_plural = "43 SKPD Asal ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLKominfo(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "43 SKPD Tujuan ATL Kominfo"
        verbose_name_plural = "43 SKPD Tujuan ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLKominfo(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "43 Foto ATL Kominfo"
        verbose_name_plural = "43 Foto ATL Kominfo"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Kearsipan
##model pada app Kearsipan
class ATLKearsipan(ATL):
    class Meta:
        proxy = True
        verbose_name = "44 ATL Kearsipan"
        verbose_name_plural = "44 ATL Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusKearsipan(ATL):
    class Meta:
        proxy = True
        verbose_name = "44 ATL Usul Hapus Kearsipan"
        verbose_name_plural = "44 ATL Usul Hapus Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLKearsipan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "44 Usul Hapus ATL Kearsipan"
        verbose_name_plural = "44 Usul Hapus ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLKearsipan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "44 Kontrak ATL Kearsipan"
        verbose_name_plural = "44 Kontrak ATL Kearsipan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLKearsipan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "44 Harga ATL Kearsipan"
        verbose_name_plural = "44 Harga ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanKearsipan(ATL):
    class Meta:
        proxy = True
        verbose_name = "44 ATL Penghapusan Kearsipan"
        verbose_name_plural = "44 ATL Penghapusan Kearsipan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLKearsipan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "44 Tahun Berkurang ATL Kearsipan"
        verbose_name_plural = "44 Tahun Berkurang ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLKearsipan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "44 Penghapusan ATL Kearsipan"
        verbose_name_plural = "44 Penghapusan ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLKearsipan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Asal ATL Kearsipan"
        verbose_name_plural = "44 SKPD Asal ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLKearsipan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "44 SKPD Tujuan ATL Kearsipan"
        verbose_name_plural = "44 SKPD Tujuan ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLKearsipan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "44 Foto ATL Kearsipan"
        verbose_name_plural = "44 Foto ATL Kearsipan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Perikanan
##model pada app Perikanan
class ATLPerikanan(ATL):
    class Meta:
        proxy = True
        verbose_name = "45 ATL Perikanan"
        verbose_name_plural = "45 ATL Perikanan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusPerikanan(ATL):
    class Meta:
        proxy = True
        verbose_name = "45 ATL Usul Hapus Perikanan"
        verbose_name_plural = "45 ATL Usul Hapus Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLPerikanan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "45 Usul Hapus ATL Perikanan"
        verbose_name_plural = "45 Usul Hapus ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLPerikanan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "45 Kontrak ATL Perikanan"
        verbose_name_plural = "45 Kontrak ATL Perikanan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLPerikanan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "45 Harga ATL Perikanan"
        verbose_name_plural = "45 Harga ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanPerikanan(ATL):
    class Meta:
        proxy = True
        verbose_name = "45 ATL Penghapusan Perikanan"
        verbose_name_plural = "45 ATL Penghapusan Perikanan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLPerikanan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "45 Tahun Berkurang ATL Perikanan"
        verbose_name_plural = "45 Tahun Berkurang ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLPerikanan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "45 Penghapusan ATL Perikanan"
        verbose_name_plural = "45 Penghapusan ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLPerikanan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Asal ATL Perikanan"
        verbose_name_plural = "45 SKPD Asal ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLPerikanan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "45 SKPD Tujuan ATL Perikanan"
        verbose_name_plural = "45 SKPD Tujuan ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLPerikanan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "45 Foto ATL Perikanan"
        verbose_name_plural = "45 Foto ATL Perikanan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Pariwisata
##model pada app Pariwisata
class ATLPariwisata(ATL):
    class Meta:
        proxy = True
        verbose_name = "46 ATL Pariwisata"
        verbose_name_plural = "46 ATL Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusPariwisata(ATL):
    class Meta:
        proxy = True
        verbose_name = "46 ATL Usul Hapus Pariwisata"
        verbose_name_plural = "46 ATL Usul Hapus Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLPariwisata(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "46 Usul Hapus ATL Pariwisata"
        verbose_name_plural = "46 Usul Hapus ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLPariwisata(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "46 Kontrak ATL Pariwisata"
        verbose_name_plural = "46 Kontrak ATL Pariwisata"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLPariwisata(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "46 Harga ATL Pariwisata"
        verbose_name_plural = "46 Harga ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanPariwisata(ATL):
    class Meta:
        proxy = True
        verbose_name = "46 ATL Penghapusan Pariwisata"
        verbose_name_plural = "46 ATL Penghapusan Pariwisata"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLPariwisata(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "46 Tahun Berkurang ATL Pariwisata"
        verbose_name_plural = "46 Tahun Berkurang ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLPariwisata(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "46 Penghapusan ATL Pariwisata"
        verbose_name_plural = "46 Penghapusan ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLPariwisata(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Asal ATL Pariwisata"
        verbose_name_plural = "46 SKPD Asal ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLPariwisata(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "46 SKPD Tujuan ATL Pariwisata"
        verbose_name_plural = "46 SKPD Tujuan ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLPariwisata(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "46 Foto ATL Pariwisata"
        verbose_name_plural = "46 Foto ATL Pariwisata"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##Perdagangan
##model pada app Perdagangan
class ATLPerdagangan(ATL):
    class Meta:
        proxy = True
        verbose_name = "47 ATL Perdagangan"
        verbose_name_plural = "47 ATL Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusPerdagangan(ATL):
    class Meta:
        proxy = True
        verbose_name = "47 ATL Usul Hapus Perdagangan"
        verbose_name_plural = "47 ATL Usul Hapus Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLPerdagangan(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "47 Usul Hapus ATL Perdagangan"
        verbose_name_plural = "47 Usul Hapus ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLPerdagangan(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "47 Kontrak ATL Perdagangan"
        verbose_name_plural = "47 Kontrak ATL Perdagangan"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLPerdagangan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "47 Harga ATL Perdagangan"
        verbose_name_plural = "47 Harga ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanPerdagangan(ATL):
    class Meta:
        proxy = True
        verbose_name = "47 ATL Penghapusan Perdagangan"
        verbose_name_plural = "47 ATL Penghapusan Perdagangan"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLPerdagangan(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "47 Tahun Berkurang ATL Perdagangan"
        verbose_name_plural = "47 Tahun Berkurang ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLPerdagangan(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "47 Penghapusan ATL Perdagangan"
        verbose_name_plural = "47 Penghapusan ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLPerdagangan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Asal ATL Perdagangan"
        verbose_name_plural = "47 SKPD Asal ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLPerdagangan(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "47 SKPD Tujuan ATL Perdagangan"
        verbose_name_plural = "47 SKPD Tujuan ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLPerdagangan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "47 Foto ATL Perdagangan"
        verbose_name_plural = "47 Foto ATL Perdagangan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



##BPPD
##model pada app BPPD
class ATLBPPD(ATL):
    class Meta:
        proxy = True
        verbose_name = "48 ATL BPPD"
        verbose_name_plural = "48 ATL BPPD"

    def __unicode__(self):
        return self.nama_barang


class ATLUsulHapusBPPD(ATL):
    class Meta:
        proxy = True
        verbose_name = "48 ATL Usul Hapus BPPD"
        verbose_name_plural = "48 ATL Usul Hapus BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangUsulHapusATLBPPD(TahunBerkurangUsulHapusATL):
    class Meta:
        proxy = True
        verbose_name = "48 Usul Hapus ATL BPPD"
        verbose_name_plural = "48 Usul Hapus ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id)


class KontrakATLBPPD(KontrakATL):
    class Meta:
        proxy = True
        verbose_name = "48 Kontrak ATL BPPD"
        verbose_name_plural = "48 Kontrak ATL BPPD"

    def __unicode__(self):
        return self.nomor_sp2d


class HargaATLBPPD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "48 Harga ATL BPPD"
        verbose_name_plural = "48 Harga ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id_atl)




class ATLPenghapusanBPPD(ATL):
    class Meta:
        proxy = True
        verbose_name = "48 ATL Penghapusan BPPD"
        verbose_name_plural = "48 ATL Penghapusan BPPD"

    def __unicode__(self):
        return self.nama_barang


class TahunBerkurangATLBPPD(TahunBerkurangATL):
    class Meta:
        proxy = True
        verbose_name = "48 Tahun Berkurang ATL BPPD"
        verbose_name_plural = "48 Tahun Berkurang ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class PenghapusanATLBPPD(PenghapusanATL):
    class Meta:
        proxy = True
        verbose_name = "48 Penghapusan ATL BPPD"
        verbose_name_plural = "48 Penghapusan ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDAsalATLBPPD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Asal ATL BPPD"
        verbose_name_plural = "48 SKPD Asal ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class SKPDTujuanATLBPPD(SKPDTujuanATL):
    class Meta:
        proxy = True
        verbose_name = "48 SKPD Tujuan ATL BPPD"
        verbose_name_plural = "48 SKPD Tujuan ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLBPPD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "48 Foto ATL BPPD"
        verbose_name_plural = "48 Foto ATL BPPD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 1 Awayan


class ATLDisdikSMPN1Awayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 ATL Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN1Awayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN1Awayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN1Awayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 1 Awayan"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 1 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 1 Batumandi


class ATLDisdikSMPN1Batumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 ATL Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN1Batumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN1Batumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN1Batumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 1 Batumandi"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 1 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 1 Halong


class ATLDisdikSMPN1Halong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 1 Halong"
        verbose_name_plural = "07 ATL Disdik SMPN 1 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN1Halong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN1Halong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 1 Halong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN1Halong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 1 Halong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 1 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 1 Juai


class ATLDisdikSMPN1Juai(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 1 Juai"
        verbose_name_plural = "07 ATL Disdik SMPN 1 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN1Juai(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN1Juai(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 1 Juai"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN1Juai(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 1 Juai"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 1 Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 1 Lampihong


class ATLDisdikSMPN1Lampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 ATL Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN1Lampihong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN1Lampihong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN1Lampihong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 1 Lampihong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 1 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 1 Paringin


class ATLDisdikSMPN1Paringin(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 ATL Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN1Paringin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN1Paringin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN1Paringin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 1 Paringin"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 1 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 2 Awayan


class ATLDisdikSMPN2Awayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 ATL Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN2Awayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN2Awayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN2Awayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 2 Awayan"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 2 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 2 Batumandi


class ATLDisdikSMPN2Batumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 ATL Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN2Batumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN2Batumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN2Batumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 2 Batumandi"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 2 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 2 Halong


class ATLDisdikSMPN2Halong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 2 Halong"
        verbose_name_plural = "07 ATL Disdik SMPN 2 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN2Halong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN2Halong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 2 Halong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN2Halong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 2 Halong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 2 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 2 Juai


class ATLDisdikSMPN2Juai(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 2 Juai"
        verbose_name_plural = "07 ATL Disdik SMPN 2 Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN2Juai(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN2Juai(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 2 Juai"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN2Juai(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 2 Juai"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 2 Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 2 Lampihong


class ATLDisdikSMPN2Lampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 ATL Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN2Lampihong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN2Lampihong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN2Lampihong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 2 Lampihong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 2 Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 2 Paringin


class ATLDisdikSMPN2Paringin(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 ATL Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN2Paringin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN2Paringin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN2Paringin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 2 Paringin"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 2 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 3 Awayan


class ATLDisdikSMPN3Awayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 ATL Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN3Awayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN3Awayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN3Awayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 3 Awayan"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 3 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 3 Batumandi


class ATLDisdikSMPN3Batumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 ATL Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN3Batumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN3Batumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN3Batumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 3 Batumandi"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 3 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 3 Halong


class ATLDisdikSMPN3Halong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 3 Halong"
        verbose_name_plural = "07 ATL Disdik SMPN 3 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN3Halong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN3Halong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 3 Halong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN3Halong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 3 Halong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 3 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 3 Paringin


class ATLDisdikSMPN3Paringin(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 ATL Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN3Paringin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN3Paringin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN3Paringin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 3 Paringin"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 3 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 4 Awayan


class ATLDisdikSMPN4Awayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 ATL Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN4Awayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN4Awayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN4Awayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 4 Awayan"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 4 Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 4 Batumandi


class ATLDisdikSMPN4Batumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 ATL Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN4Batumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN4Batumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN4Batumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 4 Batumandi"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 4 Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 4 Halong


class ATLDisdikSMPN4Halong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 4 Halong"
        verbose_name_plural = "07 ATL Disdik SMPN 4 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN4Halong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN4Halong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 4 Halong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN4Halong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 4 Halong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 4 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 4 Paringin


class ATLDisdikSMPN4Paringin(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 ATL Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN4Paringin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN4Paringin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN4Paringin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 4 Paringin"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 4 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 5 Halong


class ATLDisdikSMPN5Halong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 5 Halong"
        verbose_name_plural = "07 ATL Disdik SMPN 5 Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN5Halong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN5Halong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 5 Halong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN5Halong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 5 Halong"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 5 Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik SMPN 5 Paringin


class ATLDisdikSMPN5Paringin(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 ATL Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikSMPN5Paringin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Harga ATL Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikSMPN5Paringin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 SKPD Asal ATL Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikSMPN5Paringin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik SMPN 5 Paringin"
        verbose_name_plural = "07 Foto ATL Disdik SMPN 5 Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Paringin


class ATLDinkesParingin(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Paringin"
        verbose_name_plural = "05 ATL Dinkes Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesParingin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Paringin"
        verbose_name_plural = "05 Harga ATL Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesParingin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Paringin"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesParingin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Paringin"
        verbose_name_plural = "05 Foto ATL Dinkes Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Lampihong


class ATLDinkesLampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Lampihong"
        verbose_name_plural = "05 ATL Dinkes Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesLampihong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Lampihong"
        verbose_name_plural = "05 Harga ATL Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesLampihong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Lampihong"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesLampihong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Lampihong"
        verbose_name_plural = "05 Foto ATL Dinkes Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Batumandi


class ATLDinkesBatumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Batumandi"
        verbose_name_plural = "05 ATL Dinkes Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesBatumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Batumandi"
        verbose_name_plural = "05 Harga ATL Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesBatumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Batumandi"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesBatumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Batumandi"
        verbose_name_plural = "05 Foto ATL Dinkes Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Awayan


class ATLDinkesAwayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Awayan"
        verbose_name_plural = "05 ATL Dinkes Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesAwayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Awayan"
        verbose_name_plural = "05 Harga ATL Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesAwayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Awayan"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesAwayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Awayan"
        verbose_name_plural = "05 Foto ATL Dinkes Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Juai


class ATLDinkesJuai(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Juai"
        verbose_name_plural = "05 ATL Dinkes Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesJuai(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Juai"
        verbose_name_plural = "05 Harga ATL Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesJuai(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Juai"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesJuai(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Juai"
        verbose_name_plural = "05 Foto ATL Dinkes Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Halong


class ATLDinkesHalong(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Halong"
        verbose_name_plural = "05 ATL Dinkes Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesHalong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Halong"
        verbose_name_plural = "05 Harga ATL Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesHalong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Halong"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesHalong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Halong"
        verbose_name_plural = "05 Foto ATL Dinkes Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Lokbatu


class ATLDinkesLokbatu(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Lokbatu"
        verbose_name_plural = "05 ATL Dinkes Lokbatu"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesLokbatu(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Lokbatu"
        verbose_name_plural = "05 Harga ATL Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesLokbatu(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Lokbatu"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesLokbatu(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Lokbatu"
        verbose_name_plural = "05 Foto ATL Dinkes Lokbatu"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Uren


class ATLDinkesUren(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Uren"
        verbose_name_plural = "05 ATL Dinkes Uren"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesUren(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Uren"
        verbose_name_plural = "05 Harga ATL Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesUren(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Uren"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesUren(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Uren"
        verbose_name_plural = "05 Foto ATL Dinkes Uren"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Pirsus


class ATLDinkesPirsus(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Pirsus"
        verbose_name_plural = "05 ATL Dinkes Pirsus"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesPirsus(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Pirsus"
        verbose_name_plural = "05 Harga ATL Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesPirsus(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Pirsus"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesPirsus(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Pirsus"
        verbose_name_plural = "05 Foto ATL Dinkes Pirsus"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Paringin Selatan


class ATLDinkesParinginSelatan(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Paringin Selatan"
        verbose_name_plural = "05 ATL Dinkes Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesParinginSelatan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Paringin Selatan"
        verbose_name_plural = "05 Harga ATL Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesParinginSelatan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Paringin Selatan"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesParinginSelatan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Paringin Selatan"
        verbose_name_plural = "05 Foto ATL Dinkes Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Tebing Tinggi


class ATLDinkesTebingTinggi(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Tebing Tinggi"
        verbose_name_plural = "05 ATL Dinkes Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesTebingTinggi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Harga ATL Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesTebingTinggi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Tebing Tinggi"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesTebingTinggi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Tebing Tinggi"
        verbose_name_plural = "05 Foto ATL Dinkes Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Tanah Habang


class ATLDinkesTanahHabang(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Tanah Habang"
        verbose_name_plural = "05 ATL Dinkes Tanah Habang"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesTanahHabang(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Tanah Habang"
        verbose_name_plural = "05 Harga ATL Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesTanahHabang(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Tanah Habang"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesTanahHabang(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Tanah Habang"
        verbose_name_plural = "05 Foto ATL Dinkes Tanah Habang"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes RSUD


class ATLDinkesRSUD(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes RSUD"
        verbose_name_plural = "05 ATL Dinkes RSUD"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesRSUD(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes RSUD"
        verbose_name_plural = "05 Harga ATL Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesRSUD(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes RSUD"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesRSUD(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes RSUD"
        verbose_name_plural = "05 Foto ATL Dinkes RSUD"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Paringin


class ATLDisdikParingin(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Paringin"
        verbose_name_plural = "07 ATL Disdik Paringin"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikParingin(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Paringin"
        verbose_name_plural = "07 Harga ATL Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikParingin(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Paringin"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikParingin(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Paringin"
        verbose_name_plural = "07 Foto ATL Disdik Paringin"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Lampihong


class ATLDisdikLampihong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Lampihong"
        verbose_name_plural = "07 ATL Disdik Lampihong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikLampihong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Lampihong"
        verbose_name_plural = "07 Harga ATL Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikLampihong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Lampihong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikLampihong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Lampihong"
        verbose_name_plural = "07 Foto ATL Disdik Lampihong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Awayan


class ATLDisdikAwayan(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Awayan"
        verbose_name_plural = "07 ATL Disdik Awayan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikAwayan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Awayan"
        verbose_name_plural = "07 Harga ATL Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikAwayan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Awayan"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikAwayan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Awayan"
        verbose_name_plural = "07 Foto ATL Disdik Awayan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Batumandi


class ATLDisdikBatumandi(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Batumandi"
        verbose_name_plural = "07 ATL Disdik Batumandi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikBatumandi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Batumandi"
        verbose_name_plural = "07 Harga ATL Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikBatumandi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Batumandi"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikBatumandi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Batumandi"
        verbose_name_plural = "07 Foto ATL Disdik Batumandi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Juai


class ATLDisdikJuai(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Juai"
        verbose_name_plural = "07 ATL Disdik Juai"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikJuai(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Juai"
        verbose_name_plural = "07 Harga ATL Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikJuai(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Juai"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikJuai(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Juai"
        verbose_name_plural = "07 Foto ATL Disdik Juai"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Halong


class ATLDisdikHalong(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Halong"
        verbose_name_plural = "07 ATL Disdik Halong"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikHalong(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Halong"
        verbose_name_plural = "07 Harga ATL Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikHalong(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Halong"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikHalong(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Halong"
        verbose_name_plural = "07 Foto ATL Disdik Halong"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Tebing Tinggi


class ATLDisdikTebingTinggi(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Tebing Tinggi"
        verbose_name_plural = "07 ATL Disdik Tebing Tinggi"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikTebingTinggi(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Tebing Tinggi"
        verbose_name_plural = "07 Harga ATL Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikTebingTinggi(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Tebing Tinggi"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikTebingTinggi(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Tebing Tinggi"
        verbose_name_plural = "07 Foto ATL Disdik Tebing Tinggi"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Paringin Selatan


class ATLDisdikParinginSelatan(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Paringin Selatan"
        verbose_name_plural = "07 ATL Disdik Paringin Selatan"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikParinginSelatan(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Paringin Selatan"
        verbose_name_plural = "07 Harga ATL Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikParinginSelatan(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Paringin Selatan"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikParinginSelatan(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Paringin Selatan"
        verbose_name_plural = "07 Foto ATL Disdik Paringin Selatan"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Disdik Kantor


class ATLDisdikKantor(ATL):
    class Meta:
        proxy = True
        verbose_name = "07 ATL Disdik Kantor"
        verbose_name_plural = "07 ATL Disdik Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDisdikKantor(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "07 Harga ATL Disdik Kantor"
        verbose_name_plural = "07 Harga ATL Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDisdikKantor(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "07 SKPD Asal ATL Disdik Kantor"
        verbose_name_plural = "07 SKPD Asal ATL Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDisdikKantor(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "07 Foto ATL Disdik Kantor"
        verbose_name_plural = "07 Foto ATL Disdik Kantor"

    def __unicode__(self):
        return "%s" % (self.id_atl)



#Dinkes Kantor


class ATLDinkesKantor(ATL):
    class Meta:
        proxy = True
        verbose_name = "05 ATL Dinkes Kantor"
        verbose_name_plural = "05 ATL Dinkes Kantor"

    def __unicode__(self):
        return self.nama_barang



class HargaATLDinkesKantor(HargaATL):
    class Meta:
        proxy = True
        verbose_name = "05 Harga ATL Dinkes Kantor"
        verbose_name_plural = "05 Harga ATL Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_atl)



class SKPDAsalATLDinkesKantor(SKPDAsalATL):
    class Meta:
        proxy = True
        verbose_name = "05 SKPD Asal ATL Dinkes Kantor"
        verbose_name_plural = "05 SKPD Asal ATL Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id)



class FotoATLDinkesKantor(FotoATL):
    class Meta:
        proxy = True
        verbose_name = "05 Foto ATL Dinkes Kantor"
        verbose_name_plural = "05 Foto ATL Dinkes Kantor"

    def __unicode__(self):
        return "%s" % (self.id_atl)



