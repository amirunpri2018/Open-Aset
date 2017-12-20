# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoGedungBangunan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('foto', models.FileField(help_text=b'PERINGATAN: Hanya Foto Aset dan Hasil Scan File Dokumen Kepemilikan, Bukan Foto Pengguna Aset!!!', upload_to=b'gedung_bangunan/', verbose_name=b'Foto', db_column=b'foto')),
                ('tanggal', models.DateField(help_text=b'Tanggal Foto yang di Upload', null=True, verbose_name=b'Tanggal', db_column=b'tanggal', blank=True)),
                ('catatan', models.CharField(help_text=b'Catatan Mengenai File yang di Upload', max_length=200, verbose_name=b'Catatan', db_column=b'catatan')),
            ],
            options={
                'db_table': 'foto_gedung_bangunan',
                'verbose_name': 'Foto Gedung Bangunan',
                'verbose_name_plural': 'Foto Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='GedungBangunan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'Register', primary_key=True, db_column=b'id')),
                ('nama_barang', models.CharField(max_length=300, verbose_name=b'Nama Barang', db_column=b'nama_barang')),
                ('tanggal_dokumen_gedung', models.DateField(null=True, verbose_name=b'Tanggal Dokumen Gedung', db_column=b'tanggal_dokumen_gedung', blank=True)),
                ('nomor_dokumen_gedung', models.CharField(max_length=300, null=True, verbose_name=b'Nomor Dokumen Gedung', db_column=b'nomor_dokumen_gedung', blank=True)),
                ('banyak_barang', models.IntegerField(default=1, verbose_name=b'Banyak Barang', db_column=b'banyak_barang')),
                ('keterangan', models.TextField(null=True, verbose_name=b'Keterangan', db_column=b'keterangan', blank=True)),
            ],
            options={
                'db_table': 'gedung_bangunan',
                'verbose_name': 'Gedung Bangunan',
                'verbose_name_plural': 'Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='HargaGedungBangunan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('luas_lantai', models.DecimalField(default=0, decimal_places=1, verbose_name=b'Luas Lantai (m2)', max_digits=10, db_column=b'luas_lantai')),
                ('harga_bertambah', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Bertambah', max_digits=15, db_column=b'harga_bertambah')),
                ('harga_berkurang', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Berkurang', max_digits=15, db_column=b'harga_berkurang')),
                ('catatan', models.CharField(help_text=b'Catatan pada Daftar Pengadaan', max_length=250, verbose_name=b'Catatan', db_column=b'catatan')),
                ('id_asal_usul', models.ForeignKey(db_column=b'id_asal_usul', verbose_name=b'Asal Usul', to='umum.AsalUsul')),
            ],
            options={
                'db_table': 'harga_gedung_bangunan',
                'verbose_name': 'Harga Gedung Bangunan',
                'verbose_name_plural': 'Harga Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('pihak_ketiga', models.CharField(max_length=200, verbose_name=b'Pihak Ketiga', db_column=b'pihak_ketiga')),
                ('nomor_kontrak', models.CharField(max_length=200, null=True, verbose_name=b'Nomor Kontrak', db_column=b'nomor_kontrak', blank=True)),
                ('tanggal_kontrak', models.DateField(null=True, verbose_name=b'Tanggal Kontrak', db_column=b'tanggal_kontrak', blank=True)),
                ('nomor_sp2d', models.CharField(max_length=200, verbose_name=b'Nomor SP2D', db_column=b'nomor_sp2d')),
                ('tanggal_sp2d', models.DateField(null=True, verbose_name=b'Tanggal SP2D', db_column=b'tanggal_sp2d', blank=True)),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'kontrak_gedung_bangunan',
                'verbose_name': 'Kontrak Gedung Bangunan',
                'verbose_name_plural': 'Kontrak Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='PenambahanUmur',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_barang', models.CharField(max_length=50, verbose_name=b'Kode Barang', db_column=b'kode_barang')),
                ('umur', models.IntegerField(verbose_name=b'Umur', db_column=b'umur')),
            ],
            options={
                'ordering': ['kode_barang', 'persen'],
                'db_table': 'penambahan_umur',
                'verbose_name': 'Penambahan Umur',
                'verbose_name_plural': 'Penambahan Umur',
            },
        ),
        migrations.CreateModel(
            name='Persen',
            fields=[
                ('persen', models.IntegerField(serialize=False, primary_key=True, db_column=b'persen')),
            ],
            options={
                'ordering': ['persen'],
                'db_table': 'persen',
                'verbose_name': 'Persen',
                'verbose_name_plural': 'Persen',
            },
        ),
        migrations.CreateModel(
            name='Ruangan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_ruangan', models.CharField(max_length=10, verbose_name=b'Kode Ruangan', db_column=b'kode_ruangan')),
                ('nama_ruangan', models.CharField(max_length=250, verbose_name=b'Nama Ruangan', db_column=b'nama_ruangan')),
            ],
            options={
                'ordering': ['id_gedung_bangunan', 'kode_ruangan'],
                'db_table': 'ruangan',
                'verbose_name': 'Ruangan',
                'verbose_name_plural': 'Ruangan',
            },
        ),
        migrations.CreateModel(
            name='StatusBeton',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('status_beton', models.CharField(unique=True, max_length=100, verbose_name=b'Status Beton', db_column=b'status_beton')),
            ],
            options={
                'db_table': 'status_beton',
                'verbose_name': 'Status Beton',
                'verbose_name_plural': 'Status Beton',
            },
        ),
        migrations.CreateModel(
            name='StatusTingkat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('status_tingkat', models.CharField(unique=True, max_length=100, verbose_name=b'Status Tingkat', db_column=b'status_tingkat')),
            ],
            options={
                'db_table': 'status_tingkat',
                'verbose_name': 'Status Tingkat',
                'verbose_name_plural': 'Status Tingkat',
            },
        ),
        migrations.CreateModel(
            name='PemanfaatanGedungBangunan',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_gedung_bangunan', serialize=False, to='gedungbangunan.GedungBangunan')),
                ('id_jenis_pemanfaatan', models.ForeignKey(db_column=b'id_jenis_pemanfaatan', verbose_name=b'Jenis Pemanfaatan', to='umum.JenisPemanfaatan')),
            ],
            options={
                'db_table': 'pemanfaatan_gedung_bangunan',
                'verbose_name': 'Pemanfaatan Gedung Bangunan',
                'verbose_name_plural': 'Pemanfaatan Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunan',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_gedung_bangunan', serialize=False, to='gedungbangunan.GedungBangunan')),
                ('id_sk_penghapusan', models.ForeignKey(db_column=b'id_sk_penghapusan', verbose_name=b'SK Penghapusan', to='umum.SKPenghapusan')),
            ],
            options={
                'db_table': 'penghapusan_gedung_bangunan',
                'verbose_name': 'Penghapusan Gedung Bangunan',
                'verbose_name_plural': 'Penghapusan Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunan',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_gedung_bangunan', serialize=False, to='gedungbangunan.GedungBangunan')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_asal_gedung_bangunan',
                'verbose_name': 'SKPD Asal Gedung Bangunan',
                'verbose_name_plural': 'SKPD Asal Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunan',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_gedung_bangunan', serialize=False, to='gedungbangunan.GedungBangunan')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_tujuan_gedung_bangunan',
                'verbose_name': 'SKPD Tujuan Gedung Bangunan',
                'verbose_name_plural': 'SKPD Tujuan Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunan',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_gedung_bangunan', serialize=False, to='gedungbangunan.GedungBangunan')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_gedung_bangunan',
                'verbose_name': 'Tahun Berkurang Gedung Bangunan',
                'verbose_name_plural': 'Tahun Berkurang Gedung Bangunan',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedung',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_gedung_bangunan', serialize=False, to='gedungbangunan.GedungBangunan')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_usul_hapus_gedung',
                'verbose_name': 'Tahun Berkurang Usul Hapus Gedung',
                'verbose_name_plural': 'Tahun Berkurang Usul Hapus Gedung',
            },
        ),
        migrations.AddField(
            model_name='ruangan',
            name='id_gedung_bangunan',
            field=models.ForeignKey(db_column=b'id_gedung_bangunan', verbose_name=b'Gedung Bangunan', to='gedungbangunan.GedungBangunan'),
        ),
        migrations.AddField(
            model_name='penambahanumur',
            name='persen',
            field=models.ForeignKey(db_column=b'persen', verbose_name=b'Persen', to='gedungbangunan.Persen'),
        ),
        migrations.AddField(
            model_name='hargagedungbangunan',
            name='id_gedung_bangunan',
            field=models.ForeignKey(db_column=b'id_gedung_bangunan', verbose_name=b'Gedung Bangunan', to='gedungbangunan.GedungBangunan'),
        ),
        migrations.AddField(
            model_name='hargagedungbangunan',
            name='id_kontrak_gedung_bangunan',
            field=models.ForeignKey(db_column=b'id_kontrak_gedung_bangunan', verbose_name=b'Kontrak Gedung Bangunan', to='gedungbangunan.KontrakGedungBangunan'),
        ),
        migrations.AddField(
            model_name='hargagedungbangunan',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun', to='umum.Tahun', help_text=b'Tahun Anggaran'),
        ),
        migrations.AddField(
            model_name='hargagedungbangunan',
            name='tahun_mutasi',
            field=models.ForeignKey(related_name='+', db_column=b'tahun_mutasi', to='umum.Tahun', blank=True, help_text=b'Tahun Mutasi', null=True, verbose_name=b'Tahun Mutasi'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_golongan_barang',
            field=models.ForeignKey(db_column=b'id_golongan_barang', default=3, verbose_name=b'Golongan Barang', to='umum.GolonganBarang'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_keadaan_barang',
            field=models.ForeignKey(db_column=b'id_keadaan_barang', default=1, verbose_name=b'Keadaan Barang', to='umum.KeadaanBarang'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_kode_barang',
            field=models.ForeignKey(db_column=b'id_kode_barang', verbose_name=b'Kode Barang', to='umum.KodeBarang'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_mutasi_berkurang',
            field=models.ForeignKey(db_column=b'id_mutasi_berkurang', default=5, verbose_name=b'Mutasi Berkurang', to='umum.MutasiBerkurang'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_satuan_barang',
            field=models.ForeignKey(db_column=b'id_satuan_barang', verbose_name=b'Satuan Barang', to='umum.SatuanBarang'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_status_beton',
            field=models.ForeignKey(db_column=b'id_status_beton', verbose_name=b'Status Beton', to='gedungbangunan.StatusBeton'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_status_tingkat',
            field=models.ForeignKey(db_column=b'id_status_tingkat', verbose_name=b'Status Tingkat', to='gedungbangunan.StatusTingkat'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_sub_skpd',
            field=models.ForeignKey(db_column=b'id_sub_skpd', verbose_name=b'SUB SKPD', to='umum.SUBSKPD'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='id_tanah',
            field=models.ForeignKey(db_column=b'id_tanah', verbose_name=b'Tanah', to='umum.Tanah'),
        ),
        migrations.AddField(
            model_name='gedungbangunan',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun Awal', to='umum.Tahun', help_text=b'Tahun Awal Kapitalisasi'),
        ),
        migrations.AddField(
            model_name='fotogedungbangunan',
            name='id_gedung_bangunan',
            field=models.ForeignKey(db_column=b'id_gedung_bangunan', verbose_name=b'Gedung Bangunan', to='gedungbangunan.GedungBangunan'),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Foto Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Foto Gedung Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Foto Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Foto Gedung BAPPEDA',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Foto Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Foto Gedung Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Foto Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Foto Gedung Batu Piring',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Foto Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Foto Gedung BKD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Foto Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Foto Gedung BKPPD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Foto Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Foto Gedung BPBD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Foto Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Foto Gedung BPPD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Juai',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Kantor',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Lampihong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Lokbatu',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Paringin Selatan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Pirsus',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes RSUD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Tanah Habang',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Tebing Tinggi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Gedung Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Foto Gedung Dinkes Uren',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Juai',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Kantor',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Lampihong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Paringin Selatan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 1 Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 1 Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 1 Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 1 Juai',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 1 Lampihong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 1 Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 2 Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 2 Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 2 Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 2 Juai',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 2 Lampihong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 2 Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 3 Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 3 Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 3 Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 3 Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 4 Awayan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 4 Batumandi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 4 Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 4 Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 5 Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik SMPN 5 Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Gedung Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Gedung Disdik Tebing Tinggi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Foto Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Foto Gedung Dishub',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Foto Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Foto Gedung Disnakertrans',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Foto Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Foto Gedung Distamben',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Foto Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Foto Gedung DKO',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Foto Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Foto Gedung DKP',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Foto Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Foto Gedung DKUKMP',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Foto Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Foto Gedung DLH',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Foto Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Foto Gedung DPKP',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Foto Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Foto Gedung DPMD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Foto Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Foto Gedung DPMPTSP',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Foto Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Foto Gedung DPPKB',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Foto Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Foto Gedung DPPPA',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Foto Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Foto Gedung DPUPR',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Foto Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Foto Gedung DukCatPil',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Foto Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Foto Gedung Halong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Foto Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Foto Gedung Inspektorat',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Foto Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Foto Gedung Juai',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Foto Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Foto Gedung Kearsipan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Foto Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Foto Gedung Kehutanan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Foto Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Foto Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Foto Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Foto Gedung Kominfo',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Foto Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Foto Gedung Lampihong',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Foto Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Foto Gedung Paringin',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Foto Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Foto Gedung Paringin Kota',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Foto Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Foto Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Foto Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Foto Gedung Paringin Timur',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Foto Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Foto Gedung Pariwisata',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Foto Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Foto Gedung Perdagangan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Foto Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Foto Gedung Perikanan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Foto Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Foto Gedung Perpustakaan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Foto Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Foto Gedung Pertanian',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Foto Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Foto Gedung RSUD',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Foto Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Foto Gedung SATPOLPP',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Foto Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Foto Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Foto Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Foto Gedung Setda',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Foto Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Foto Gedung Setwan',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Foto Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Foto Gedung Sosial',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='FotoGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Foto Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Foto Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.fotogedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Gedung Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Gedung BAPPEDA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Gedung Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Gedung Batu Piring',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Gedung BKD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Gedung BKPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Gedung BPBD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Gedung BPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Kantor',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Lokbatu',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Pirsus',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Tanah Habang',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Dinkes Uren',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Kantor',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 1 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 1 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 1 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 1 Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 1 Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 1 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 2 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 2 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 2 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 2 Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 2 Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 2 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 3 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 3 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 3 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 3 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 4 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 4 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 4 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 4 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 5 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik SMPN 5 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Disdik Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Gedung Dishub',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Gedung Disnakertrans',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Gedung Distamben',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Gedung DKO',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Gedung DKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Gedung DKUKMP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Gedung DLH',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Gedung DPKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Gedung DPMD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Gedung DPMPTSP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Gedung DPPKB',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Gedung DPPPA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Gedung DPUPR',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Gedung DukCatPil',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Gedung Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Gedung Inspektorat',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Gedung Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Gedung Kearsipan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Gedung Kehutanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Gedung Kominfo',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Gedung Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Gedung Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Gedung Paringin Kota',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Gedung Paringin Timur',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Gedung Pariwisata',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPemanfaatan',
            fields=[
            ],
            options={
                'verbose_name': 'Gedung Bangunan Pemanfaatan',
                'proxy': True,
                'verbose_name_plural': 'Gedung Bangunan Pemanfaatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusan',
            fields=[
            ],
            options={
                'verbose_name': 'Gedung Bangunan Penghapusan',
                'proxy': True,
                'verbose_name_plural': 'Gedung Bangunan Penghapusan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Gedung Penghapusan Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Gedung Penghapusan Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Gedung Penghapusan BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Gedung Penghapusan BAPPEDA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Gedung Penghapusan Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Gedung Penghapusan Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Gedung Penghapusan Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Gedung Penghapusan Batu Piring',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Gedung Penghapusan BKD',
                'proxy': True,
                'verbose_name_plural': '19 Gedung Penghapusan BKD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Gedung Penghapusan BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Gedung Penghapusan BKPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Gedung Penghapusan BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Gedung Penghapusan BPBD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Gedung Penghapusan BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Gedung Penghapusan BPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Penghapusan Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Penghapusan Dinkes',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Penghapusan Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Penghapusan Disdik',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Gedung Penghapusan Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Gedung Penghapusan Dishub',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Gedung Penghapusan Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Gedung Penghapusan Disnakertrans',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Gedung Penghapusan Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Gedung Penghapusan Distamben',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Gedung Penghapusan DKO',
                'proxy': True,
                'verbose_name_plural': '23 Gedung Penghapusan DKO',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Gedung Penghapusan DKP',
                'proxy': True,
                'verbose_name_plural': '15 Gedung Penghapusan DKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Gedung Penghapusan DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Gedung Penghapusan DKUKMP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Gedung Penghapusan DLH',
                'proxy': True,
                'verbose_name_plural': '22 Gedung Penghapusan DLH',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Gedung Penghapusan DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Gedung Penghapusan DPKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Gedung Penghapusan DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Gedung Penghapusan DPMD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Gedung Penghapusan DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Gedung Penghapusan DPMPTSP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Gedung Penghapusan DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Gedung Penghapusan DPPKB',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Gedung Penghapusan DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Gedung Penghapusan DPPPA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Gedung Penghapusan DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Gedung Penghapusan DPUPR',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Gedung Penghapusan DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Gedung Penghapusan DukCatPil',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Gedung Penghapusan Halong',
                'proxy': True,
                'verbose_name_plural': '35 Gedung Penghapusan Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Gedung Penghapusan Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Gedung Penghapusan Inspektorat',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Gedung Penghapusan Juai',
                'proxy': True,
                'verbose_name_plural': '33 Gedung Penghapusan Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Gedung Penghapusan Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Gedung Penghapusan Kearsipan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Gedung Penghapusan Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Gedung Penghapusan Kehutanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Gedung Penghapusan KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Gedung Penghapusan KESBANGPOL',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Gedung Penghapusan Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Gedung Penghapusan Kominfo',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Gedung Penghapusan Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Gedung Penghapusan Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Gedung Penghapusan Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Gedung Penghapusan Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Gedung Penghapusan Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Gedung Penghapusan Paringin Kota',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Gedung Penghapusan Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Gedung Penghapusan Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Gedung Penghapusan Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Gedung Penghapusan Paringin Timur',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Gedung Penghapusan Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Gedung Penghapusan Pariwisata',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Gedung Penghapusan Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Gedung Penghapusan Perdagangan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Gedung Penghapusan Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Gedung Penghapusan Perikanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Gedung Penghapusan Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Gedung Penghapusan Perpustakaan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Gedung Penghapusan Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Gedung Penghapusan Pertanian',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Gedung Penghapusan RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Gedung Penghapusan RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Gedung Penghapusan SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Gedung Penghapusan SATPOLPP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Gedung Penghapusan Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Gedung Penghapusan Sekretariat Korpri',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Gedung Penghapusan Setda',
                'proxy': True,
                'verbose_name_plural': '02 Gedung Penghapusan Setda',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Gedung Penghapusan Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Gedung Penghapusan Setwan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Gedung Penghapusan Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Gedung Penghapusan Sosial',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPenghapusanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Gedung Penghapusan Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Gedung Penghapusan Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Gedung Perdagangan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Gedung Perikanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Gedung Perpustakaan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Gedung Pertanian',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Gedung RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuangan',
            fields=[
            ],
            options={
                'verbose_name': 'Gedung Bangunan Ruangan',
                'proxy': True,
                'verbose_name_plural': 'Gedung Bangunan Ruangan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Gedung Ruangan Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Gedung Ruangan Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Gedung Ruangan BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Gedung Ruangan BAPPEDA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Gedung Ruangan Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Gedung Ruangan Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Gedung Ruangan Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Gedung Ruangan Batu Piring',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Gedung Ruangan BKD',
                'proxy': True,
                'verbose_name_plural': '19 Gedung Ruangan BKD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Gedung Ruangan BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Gedung Ruangan BKPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Gedung Ruangan BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Gedung Ruangan BPBD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Gedung Ruangan BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Gedung Ruangan BPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Kantor',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Lokbatu',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Pirsus',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Tanah Habang',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Ruangan Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Ruangan Dinkes Uren',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Kantor',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 1 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 1 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 1 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 1 Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 1 Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 1 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 2 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 2 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 2 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 2 Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 2 Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 2 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 3 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 3 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 3 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 3 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 4 Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 4 Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 4 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 4 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 5 Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik SMPN 5 Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Ruangan Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Ruangan Disdik Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Gedung Ruangan Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Gedung Ruangan Dishub',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Gedung Ruangan Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Gedung Ruangan Disnakertrans',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Gedung Ruangan Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Gedung Ruangan Distamben',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Gedung Ruangan DKO',
                'proxy': True,
                'verbose_name_plural': '23 Gedung Ruangan DKO',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Gedung Ruangan DKP',
                'proxy': True,
                'verbose_name_plural': '15 Gedung Ruangan DKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Gedung Ruangan DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Gedung Ruangan DKUKMP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Gedung Ruangan DLH',
                'proxy': True,
                'verbose_name_plural': '22 Gedung Ruangan DLH',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Gedung Ruangan DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Gedung Ruangan DPKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Gedung Ruangan DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Gedung Ruangan DPMD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Gedung Ruangan DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Gedung Ruangan DPMPTSP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Gedung Ruangan DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Gedung Ruangan DPPKB',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Gedung Ruangan DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Gedung Ruangan DPPPA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Gedung Ruangan DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Gedung Ruangan DPUPR',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Gedung Ruangan DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Gedung Ruangan DukCatPil',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Gedung Ruangan Halong',
                'proxy': True,
                'verbose_name_plural': '35 Gedung Ruangan Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Gedung Ruangan Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Gedung Ruangan Inspektorat',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Gedung Ruangan Juai',
                'proxy': True,
                'verbose_name_plural': '33 Gedung Ruangan Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Gedung Ruangan Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Gedung Ruangan Kearsipan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Gedung Ruangan Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Gedung Ruangan Kehutanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Gedung Ruangan KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Gedung Ruangan KESBANGPOL',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Gedung Ruangan Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Gedung Ruangan Kominfo',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Gedung Ruangan Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Gedung Ruangan Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Gedung Ruangan Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Gedung Ruangan Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Gedung Ruangan Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Gedung Ruangan Paringin Kota',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Gedung Ruangan Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Gedung Ruangan Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Gedung Ruangan Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Gedung Ruangan Paringin Timur',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Gedung Ruangan Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Gedung Ruangan Pariwisata',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Gedung Ruangan Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Gedung Ruangan Perdagangan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Gedung Ruangan Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Gedung Ruangan Perikanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Gedung Ruangan Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Gedung Ruangan Perpustakaan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Gedung Ruangan Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Gedung Ruangan Pertanian',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Gedung Ruangan RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Gedung Ruangan RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Gedung Ruangan SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Gedung Ruangan SATPOLPP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Gedung Ruangan Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Gedung Ruangan Sekretariat Korpri',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Gedung Ruangan Setda',
                'proxy': True,
                'verbose_name_plural': '02 Gedung Ruangan Setda',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Gedung Ruangan Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Gedung Ruangan Setwan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Gedung Ruangan Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Gedung Ruangan Sosial',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanRuanganTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Gedung Ruangan Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Gedung Ruangan Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Gedung SATPOLPP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Gedung Setda',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Gedung Setwan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Gedung Sosial',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapus',
            fields=[
            ],
            options={
                'verbose_name': 'Gedung Bangunan Usul Hapus',
                'proxy': True,
                'verbose_name_plural': 'Gedung Bangunan Usul Hapus',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Gedung Usul Hapus Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Gedung Usul Hapus Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Gedung Usul Hapus BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Gedung Usul Hapus BAPPEDA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Gedung Usul Hapus Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Gedung Usul Hapus Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Gedung Usul Hapus Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Gedung Usul Hapus Batu Piring',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Gedung Usul Hapus BKD',
                'proxy': True,
                'verbose_name_plural': '19 Gedung Usul Hapus BKD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Gedung Usul Hapus BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Gedung Usul Hapus BKPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Gedung Usul Hapus BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Gedung Usul Hapus BPBD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Gedung Usul Hapus BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Gedung Usul Hapus BPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Gedung Usul Hapus Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Gedung Usul Hapus Dinkes',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Gedung Usul Hapus Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Gedung Usul Hapus Disdik',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Gedung Usul Hapus Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Gedung Usul Hapus Dishub',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Gedung Usul Hapus Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Gedung Usul Hapus Disnakertrans',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Gedung Usul Hapus Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Gedung Usul Hapus Distamben',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Gedung Usul Hapus DKO',
                'proxy': True,
                'verbose_name_plural': '23 Gedung Usul Hapus DKO',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Gedung Usul Hapus DKP',
                'proxy': True,
                'verbose_name_plural': '15 Gedung Usul Hapus DKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Gedung Usul Hapus DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Gedung Usul Hapus DKUKMP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Gedung Usul Hapus DLH',
                'proxy': True,
                'verbose_name_plural': '22 Gedung Usul Hapus DLH',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Gedung Usul Hapus DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Gedung Usul Hapus DPKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Gedung Usul Hapus DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Gedung Usul Hapus DPMD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Gedung Usul Hapus DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Gedung Usul Hapus DPMPTSP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Gedung Usul Hapus DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Gedung Usul Hapus DPPKB',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Gedung Usul Hapus DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Gedung Usul Hapus DPPPA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Gedung Usul Hapus DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Gedung Usul Hapus DPUPR',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Gedung Usul Hapus DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Gedung Usul Hapus DukCatPil',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Gedung Usul Hapus Halong',
                'proxy': True,
                'verbose_name_plural': '35 Gedung Usul Hapus Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Gedung Usul Hapus Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Gedung Usul Hapus Inspektorat',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Gedung Usul Hapus Juai',
                'proxy': True,
                'verbose_name_plural': '33 Gedung Usul Hapus Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Gedung Usul Hapus Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Gedung Usul Hapus Kearsipan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Gedung Usul Hapus Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Gedung Usul Hapus Kehutanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Gedung Usul Hapus KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Gedung Usul Hapus KESBANGPOL',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Gedung Usul Hapus Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Gedung Usul Hapus Kominfo',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Gedung Usul Hapus Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Gedung Usul Hapus Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Gedung Usul Hapus Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Gedung Usul Hapus Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Gedung Usul Hapus Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Gedung Usul Hapus Paringin Kota',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Gedung Usul Hapus Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Gedung Usul Hapus Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Gedung Usul Hapus Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Gedung Usul Hapus Paringin Timur',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Gedung Usul Hapus Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Gedung Usul Hapus Pariwisata',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Gedung Usul Hapus Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Gedung Usul Hapus Perdagangan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Gedung Usul Hapus Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Gedung Usul Hapus Perikanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Gedung Usul Hapus Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Gedung Usul Hapus Perpustakaan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Gedung Usul Hapus Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Gedung Usul Hapus Pertanian',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Gedung Usul Hapus RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Gedung Usul Hapus RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Gedung Usul Hapus SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Gedung Usul Hapus SATPOLPP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Gedung Usul Hapus Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Gedung Usul Hapus Sekretariat Korpri',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Gedung Usul Hapus Setda',
                'proxy': True,
                'verbose_name_plural': '02 Gedung Usul Hapus Setda',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Gedung Usul Hapus Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Gedung Usul Hapus Setwan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Gedung Usul Hapus Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Gedung Usul Hapus Sosial',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='GedungBangunanUsulHapusTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Gedung Usul Hapus Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Gedung Usul Hapus Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Harga Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Harga Gedung Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Harga Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Harga Gedung BAPPEDA',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Harga Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Harga Gedung Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Harga Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Harga Gedung Batu Piring',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Harga Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Harga Gedung BKD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Harga Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Harga Gedung BKPPD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Harga Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Harga Gedung BPBD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Harga Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Harga Gedung BPPD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Juai',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Kantor',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Lampihong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Lokbatu',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Paringin Selatan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Pirsus',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes RSUD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Tanah Habang',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Tebing Tinggi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Gedung Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Harga Gedung Dinkes Uren',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Juai',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Kantor',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Lampihong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Paringin Selatan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 1 Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 1 Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 1 Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 1 Juai',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 1 Lampihong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 1 Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 2 Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 2 Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 2 Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 2 Juai',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 2 Lampihong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 2 Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 3 Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 3 Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 3 Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 3 Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 4 Awayan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 4 Batumandi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 4 Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 4 Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 5 Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik SMPN 5 Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Gedung Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Gedung Disdik Tebing Tinggi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Harga Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Harga Gedung Dishub',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Harga Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Harga Gedung Disnakertrans',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Harga Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Harga Gedung Distamben',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Harga Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Harga Gedung DKO',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Harga Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Harga Gedung DKP',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Harga Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Harga Gedung DKUKMP',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Harga Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Harga Gedung DLH',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Harga Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Harga Gedung DPKP',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Harga Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Harga Gedung DPMD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Harga Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Harga Gedung DPMPTSP',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Harga Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Harga Gedung DPPKB',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Harga Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Harga Gedung DPPPA',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Harga Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Harga Gedung DPUPR',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Harga Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Harga Gedung DukCatPil',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Harga Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Harga Gedung Halong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Harga Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Harga Gedung Inspektorat',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Harga Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Harga Gedung Juai',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Harga Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Harga Gedung Kearsipan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Harga Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Harga Gedung Kehutanan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Harga Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Harga Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Harga Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Harga Gedung Kominfo',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Harga Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Harga Gedung Lampihong',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Harga Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Harga Gedung Paringin',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Harga Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Harga Gedung Paringin Kota',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Harga Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Harga Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Harga Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Harga Gedung Paringin Timur',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Harga Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Harga Gedung Pariwisata',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Harga Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Harga Gedung Perdagangan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Harga Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Harga Gedung Perikanan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Harga Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Harga Gedung Perpustakaan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Harga Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Harga Gedung Pertanian',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Harga Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Harga Gedung RSUD',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Harga Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Harga Gedung SATPOLPP',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Harga Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Harga Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Harga Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Harga Gedung Setda',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Harga Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Harga Gedung Setwan',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Harga Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Harga Gedung Sosial',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='HargaGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Harga Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Harga Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.hargagedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunan',
            fields=[
            ],
            options={
                'verbose_name': 'KDP Gedung Bangunan',
                'proxy': True,
                'verbose_name_plural': 'KDP Gedung Bangunan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 KDP Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 KDP Gedung Awayan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 KDP Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 KDP Gedung BAPPEDA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 KDP Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 KDP Gedung Batumandi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 KDP Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 KDP Gedung Batu Piring',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 KDP Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 KDP Gedung BKD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 KDP Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 KDP Gedung BKPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 KDP Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 KDP Gedung BPBD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 KDP Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 KDP Gedung BPPD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 KDP Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 KDP Gedung Dinkes',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 KDP Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 KDP Gedung Disdik',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 KDP Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 KDP Gedung Dishub',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 KDP Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 KDP Gedung Disnakertrans',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 KDP Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 KDP Gedung Distamben',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 KDP Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 KDP Gedung DKO',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 KDP Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 KDP Gedung DKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 KDP Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 KDP Gedung DKUKMP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 KDP Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 KDP Gedung DLH',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 KDP Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 KDP Gedung DPKP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 KDP Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 KDP Gedung DPMD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 KDP Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 KDP Gedung DPMPTSP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 KDP Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 KDP Gedung DPPKB',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 KDP Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 KDP Gedung DPPPA',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 KDP Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 KDP Gedung DPUPR',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 KDP Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 KDP Gedung DukCatPil',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 KDP Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 KDP Gedung Halong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 KDP Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 KDP Gedung Inspektorat',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 KDP Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 KDP Gedung Juai',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 KDP Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 KDP Gedung Kearsipan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 KDP Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 KDP Gedung Kehutanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 KDP Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 KDP Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 KDP Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 KDP Gedung Kominfo',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 KDP Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 KDP Gedung Lampihong',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 KDP Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 KDP Gedung Paringin',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 KDP Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 KDP Gedung Paringin Kota',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 KDP Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 KDP Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 KDP Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 KDP Gedung Paringin Timur',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 KDP Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 KDP Gedung Pariwisata',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 KDP Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 KDP Gedung Perdagangan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 KDP Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 KDP Gedung Perikanan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 KDP Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 KDP Gedung Perpustakaan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 KDP Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 KDP Gedung Pertanian',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanReklas',
            fields=[
            ],
            options={
                'verbose_name': 'KDP Gedung Bangunan Reklas',
                'proxy': True,
                'verbose_name_plural': 'KDP Gedung Bangunan Reklas',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 KDP Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 KDP Gedung RSUD',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 KDP Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 KDP Gedung SATPOLPP',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 KDP Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 KDP Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 KDP Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 KDP Gedung Setda',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 KDP Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 KDP Gedung Setwan',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 KDP Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 KDP Gedung Sosial',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KDPGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 KDP Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 KDP Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.gedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Kontrak Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Kontrak Gedung Awayan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Kontrak Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Kontrak Gedung BAPPEDA',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Kontrak Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Kontrak Gedung Batumandi',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Kontrak Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Kontrak Gedung Batu Piring',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Kontrak Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Kontrak Gedung BKD',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Kontrak Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Kontrak Gedung BKPPD',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Kontrak Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Kontrak Gedung BPBD',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Kontrak Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Kontrak Gedung BPPD',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Kontrak Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Kontrak Gedung Dinkes',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Kontrak Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Kontrak Gedung Disdik',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Kontrak Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Kontrak Gedung Dishub',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Kontrak Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Kontrak Gedung Disnakertrans',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Kontrak Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Kontrak Gedung Distamben',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Kontrak Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Kontrak Gedung DKO',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Kontrak Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Kontrak Gedung DKP',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Kontrak Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Kontrak Gedung DKUKMP',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Kontrak Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Kontrak Gedung DLH',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Kontrak Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Kontrak Gedung DPKP',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Kontrak Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Kontrak Gedung DPMD',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Kontrak Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Kontrak Gedung DPMPTSP',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Kontrak Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Kontrak Gedung DPPKB',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Kontrak Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Kontrak Gedung DPPPA',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Kontrak Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Kontrak Gedung DPUPR',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Kontrak Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Kontrak Gedung DukCatPil',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Kontrak Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Kontrak Gedung Halong',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Kontrak Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Kontrak Gedung Inspektorat',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Kontrak Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Kontrak Gedung Juai',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Kontrak Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Kontrak Gedung Kearsipan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Kontrak Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Kontrak Gedung Kehutanan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Kontrak Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Kontrak Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Kontrak Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Kontrak Gedung Kominfo',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Kontrak Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Kontrak Gedung Lampihong',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Kontrak Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Kontrak Gedung Paringin',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Kontrak Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Kontrak Gedung Paringin Kota',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Kontrak Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Kontrak Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Kontrak Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Kontrak Gedung Paringin Timur',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Kontrak Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Kontrak Gedung Pariwisata',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Kontrak Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Kontrak Gedung Perdagangan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Kontrak Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Kontrak Gedung Perikanan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Kontrak Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Kontrak Gedung Perpustakaan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Kontrak Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Kontrak Gedung Pertanian',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Kontrak Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Kontrak Gedung RSUD',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Kontrak Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Kontrak Gedung SATPOLPP',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Kontrak Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Kontrak Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Kontrak Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Kontrak Gedung Setda',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Kontrak Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Kontrak Gedung Setwan',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Kontrak Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Kontrak Gedung Sosial',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='KontrakGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Kontrak Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Kontrak Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.kontrakgedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Penghapusan Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Penghapusan Gedung Awayan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Penghapusan Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Penghapusan Gedung BAPPEDA',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Penghapusan Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Penghapusan Gedung Batumandi',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Penghapusan Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Penghapusan Gedung Batu Piring',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Penghapusan Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Penghapusan Gedung BKD',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Penghapusan Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Penghapusan Gedung BKPPD',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Penghapusan Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Penghapusan Gedung BPBD',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Penghapusan Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Penghapusan Gedung BPPD',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Penghapusan Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Penghapusan Gedung Dinkes',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Penghapusan Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Penghapusan Gedung Disdik',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Penghapusan Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Penghapusan Gedung Dishub',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Penghapusan Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Penghapusan Gedung Disnakertrans',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Penghapusan Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Penghapusan Gedung Distamben',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Penghapusan Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Penghapusan Gedung DKO',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Penghapusan Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Penghapusan Gedung DKP',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Penghapusan Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Penghapusan Gedung DKUKMP',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Penghapusan Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Penghapusan Gedung DLH',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Penghapusan Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Penghapusan Gedung DPKP',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Penghapusan Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Penghapusan Gedung DPMD',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Penghapusan Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Penghapusan Gedung DPMPTSP',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Penghapusan Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Penghapusan Gedung DPPKB',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Penghapusan Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Penghapusan Gedung DPPPA',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Penghapusan Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Penghapusan Gedung DPUPR',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Penghapusan Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Penghapusan Gedung DukCatPil',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Penghapusan Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Penghapusan Gedung Halong',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Penghapusan Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Penghapusan Gedung Inspektorat',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Penghapusan Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Penghapusan Gedung Juai',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Penghapusan Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Penghapusan Gedung Kearsipan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Penghapusan Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Penghapusan Gedung Kehutanan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Penghapusan Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Penghapusan Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Penghapusan Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Penghapusan Gedung Kominfo',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Penghapusan Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Penghapusan Gedung Lampihong',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Penghapusan Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Penghapusan Gedung Paringin',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Penghapusan Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Penghapusan Gedung Paringin Kota',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Penghapusan Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Penghapusan Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Penghapusan Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Penghapusan Gedung Paringin Timur',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Penghapusan Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Penghapusan Gedung Pariwisata',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Penghapusan Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Penghapusan Gedung Perdagangan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Penghapusan Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Penghapusan Gedung Perikanan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Penghapusan Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Penghapusan Gedung Perpustakaan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Penghapusan Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Penghapusan Gedung Pertanian',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Penghapusan Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Penghapusan Gedung RSUD',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Penghapusan Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Penghapusan Gedung SATPOLPP',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Penghapusan Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Penghapusan Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Penghapusan Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Penghapusan Gedung Setda',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Penghapusan Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Penghapusan Gedung Setwan',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Penghapusan Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Penghapusan Gedung Sosial',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='PenghapusanGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Penghapusan Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Penghapusan Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.penghapusangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Asal Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Asal Gedung Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Asal Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Asal Gedung BAPPEDA',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Asal Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Asal Gedung Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Asal Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Asal Gedung Batu Piring',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Asal Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Asal Gedung BKD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Asal Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Asal Gedung BKPPD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Asal Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Asal Gedung BPBD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Asal Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Asal Gedung BPPD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Juai',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Kantor',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Lampihong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Lokbatu',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Paringin Selatan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Pirsus',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes RSUD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Tanah Habang',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Tebing Tinggi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Gedung Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Gedung Dinkes Uren',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Juai',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Kantor',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Lampihong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Paringin Selatan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 1 Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 1 Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 1 Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 1 Juai',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 1 Lampihong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 1 Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 2 Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 2 Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 2 Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 2 Juai',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 2 Lampihong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 2 Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 3 Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 3 Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 3 Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 3 Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 4 Awayan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 4 Batumandi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 4 Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 4 Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 5 Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik SMPN 5 Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Gedung Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Gedung Disdik Tebing Tinggi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Asal Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Asal Gedung Dishub',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Asal Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Asal Gedung Disnakertrans',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Asal Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Asal Gedung Distamben',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Asal Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Asal Gedung DKO',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Asal Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Asal Gedung DKP',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Asal Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Asal Gedung DKUKMP',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Asal Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Asal Gedung DLH',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Asal Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Asal Gedung DPKP',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Asal Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Asal Gedung DPMD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Asal Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Asal Gedung DPMPTSP',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Asal Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Asal Gedung DPPKB',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Asal Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Asal Gedung DPPPA',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Asal Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Asal Gedung DPUPR',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Asal Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Asal Gedung DukCatPil',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Asal Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Asal Gedung Halong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Asal Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Asal Gedung Inspektorat',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Asal Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Asal Gedung Juai',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Asal Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Asal Gedung Kearsipan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Asal Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Asal Gedung Kehutanan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Asal Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Asal Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Asal Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Asal Gedung Kominfo',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Asal Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Asal Gedung Lampihong',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Asal Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Asal Gedung Paringin',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Asal Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Asal Gedung Paringin Kota',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Asal Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Asal Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Asal Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Asal Gedung Paringin Timur',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Asal Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Asal Gedung Pariwisata',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Asal Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Asal Gedung Perdagangan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Asal Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Asal Gedung Perikanan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Asal Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Asal Gedung Perpustakaan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Asal Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Asal Gedung Pertanian',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Asal Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Asal Gedung RSUD',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Asal Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Asal Gedung SATPOLPP',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Asal Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Asal Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Asal Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Asal Gedung Setda',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Asal Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Asal Gedung Setwan',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Asal Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Asal Gedung Sosial',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDAsalGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Asal Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Asal Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.skpdasalgedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Tujuan Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Tujuan Gedung Awayan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Tujuan Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Tujuan Gedung BAPPEDA',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Tujuan Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Tujuan Gedung Batumandi',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Tujuan Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Tujuan Gedung Batu Piring',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Tujuan Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Tujuan Gedung BKD',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Tujuan Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Tujuan Gedung BKPPD',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Tujuan Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Tujuan Gedung BPBD',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Tujuan Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Tujuan Gedung BPPD',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Tujuan Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Tujuan Gedung Dinkes',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Tujuan Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Tujuan Gedung Disdik',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Tujuan Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Tujuan Gedung Dishub',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Tujuan Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Tujuan Gedung Disnakertrans',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Tujuan Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Tujuan Gedung Distamben',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Tujuan Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Tujuan Gedung DKO',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Tujuan Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Tujuan Gedung DKP',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Tujuan Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Tujuan Gedung DKUKMP',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Tujuan Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Tujuan Gedung DLH',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Tujuan Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Tujuan Gedung DPKP',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Tujuan Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Tujuan Gedung DPMD',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Tujuan Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Tujuan Gedung DPMPTSP',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Tujuan Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Tujuan Gedung DPPKB',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Tujuan Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Tujuan Gedung DPPPA',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Tujuan Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Tujuan Gedung DPUPR',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Tujuan Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Tujuan Gedung DukCatPil',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Tujuan Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Tujuan Gedung Halong',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Tujuan Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Tujuan Gedung Inspektorat',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Tujuan Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Tujuan Gedung Juai',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Tujuan Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Tujuan Gedung Kearsipan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Tujuan Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Tujuan Gedung Kehutanan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Tujuan Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Tujuan Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Tujuan Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Tujuan Gedung Kominfo',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Tujuan Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Tujuan Gedung Lampihong',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Tujuan Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Tujuan Gedung Paringin',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Tujuan Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Tujuan Gedung Paringin Kota',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Tujuan Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Tujuan Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Tujuan Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Tujuan Gedung Paringin Timur',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Tujuan Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Tujuan Gedung Pariwisata',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Tujuan Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Tujuan Gedung Perdagangan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Tujuan Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Tujuan Gedung Perikanan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Tujuan Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Tujuan Gedung Perpustakaan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Tujuan Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Tujuan Gedung Pertanian',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Tujuan Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Tujuan Gedung RSUD',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Tujuan Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Tujuan Gedung SATPOLPP',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Tujuan Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Tujuan Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Tujuan Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Tujuan Gedung Setda',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Tujuan Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Tujuan Gedung Setwan',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Tujuan Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Tujuan Gedung Sosial',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Tujuan Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Tujuan Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.skpdtujuangedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tahun Berkurang Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tahun Berkurang Gedung Awayan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tahun Berkurang Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tahun Berkurang Gedung BAPPEDA',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tahun Berkurang Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tahun Berkurang Gedung Batumandi',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tahun Berkurang Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tahun Berkurang Gedung Batu Piring',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tahun Berkurang Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tahun Berkurang Gedung BKD',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tahun Berkurang Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tahun Berkurang Gedung BKPPD',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tahun Berkurang Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tahun Berkurang Gedung BPBD',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tahun Berkurang Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tahun Berkurang Gedung BPPD',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tahun Berkurang Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tahun Berkurang Gedung Dinkes',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tahun Berkurang Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tahun Berkurang Gedung Disdik',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tahun Berkurang Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tahun Berkurang Gedung Dishub',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tahun Berkurang Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tahun Berkurang Gedung Disnakertrans',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tahun Berkurang Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tahun Berkurang Gedung Distamben',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tahun Berkurang Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tahun Berkurang Gedung DKO',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tahun Berkurang Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tahun Berkurang Gedung DKP',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tahun Berkurang Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tahun Berkurang Gedung DKUKMP',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tahun Berkurang Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tahun Berkurang Gedung DLH',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tahun Berkurang Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tahun Berkurang Gedung DPKP',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tahun Berkurang Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tahun Berkurang Gedung DPMD',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tahun Berkurang Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tahun Berkurang Gedung DPMPTSP',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tahun Berkurang Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tahun Berkurang Gedung DPPKB',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tahun Berkurang Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tahun Berkurang Gedung DPPPA',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tahun Berkurang Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tahun Berkurang Gedung DPUPR',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tahun Berkurang Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tahun Berkurang Gedung DukCatPil',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tahun Berkurang Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tahun Berkurang Gedung Halong',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tahun Berkurang Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tahun Berkurang Gedung Inspektorat',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tahun Berkurang Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tahun Berkurang Gedung Juai',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tahun Berkurang Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tahun Berkurang Gedung Kearsipan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tahun Berkurang Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tahun Berkurang Gedung Kehutanan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tahun Berkurang Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tahun Berkurang Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tahun Berkurang Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tahun Berkurang Gedung Kominfo',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tahun Berkurang Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tahun Berkurang Gedung Lampihong',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tahun Berkurang Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tahun Berkurang Gedung Paringin',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tahun Berkurang Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tahun Berkurang Gedung Paringin Kota',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tahun Berkurang Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tahun Berkurang Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tahun Berkurang Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tahun Berkurang Gedung Paringin Timur',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tahun Berkurang Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tahun Berkurang Gedung Pariwisata',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tahun Berkurang Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tahun Berkurang Gedung Perdagangan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tahun Berkurang Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tahun Berkurang Gedung Perikanan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tahun Berkurang Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tahun Berkurang Gedung Perpustakaan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tahun Berkurang Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tahun Berkurang Gedung Pertanian',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tahun Berkurang Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tahun Berkurang Gedung RSUD',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tahun Berkurang Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tahun Berkurang Gedung SATPOLPP',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tahun Berkurang Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tahun Berkurang Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tahun Berkurang Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tahun Berkurang Gedung Setda',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tahun Berkurang Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tahun Berkurang Gedung Setwan',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tahun Berkurang Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tahun Berkurang Gedung Sosial',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangGedungBangunanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tahun Berkurang Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tahun Berkurang Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.tahunberkuranggedungbangunan',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Usul Hapus Gedung Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Usul Hapus Gedung Awayan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Usul Hapus Gedung BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Usul Hapus Gedung BAPPEDA',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Usul Hapus Gedung Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Usul Hapus Gedung Batumandi',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Usul Hapus Gedung Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Usul Hapus Gedung Batu Piring',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Usul Hapus Gedung BKD',
                'proxy': True,
                'verbose_name_plural': '19 Usul Hapus Gedung BKD',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Usul Hapus Gedung BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Usul Hapus Gedung BKPPD',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Usul Hapus Gedung BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Usul Hapus Gedung BPBD',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Usul Hapus Gedung BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Usul Hapus Gedung BPPD',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Usul Hapus Gedung Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Usul Hapus Gedung Dinkes',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Usul Hapus Gedung Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Usul Hapus Gedung Disdik',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Usul Hapus Gedung Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Usul Hapus Gedung Dishub',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Usul Hapus Gedung Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Usul Hapus Gedung Disnakertrans',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Usul Hapus Gedung Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Usul Hapus Gedung Distamben',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Usul Hapus Gedung DKO',
                'proxy': True,
                'verbose_name_plural': '23 Usul Hapus Gedung DKO',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Usul Hapus Gedung DKP',
                'proxy': True,
                'verbose_name_plural': '15 Usul Hapus Gedung DKP',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Usul Hapus Gedung DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Usul Hapus Gedung DKUKMP',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Usul Hapus Gedung DLH',
                'proxy': True,
                'verbose_name_plural': '22 Usul Hapus Gedung DLH',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Usul Hapus Gedung DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Usul Hapus Gedung DPKP',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Usul Hapus Gedung DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Usul Hapus Gedung DPMD',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Usul Hapus Gedung DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Usul Hapus Gedung DPMPTSP',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Usul Hapus Gedung DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Usul Hapus Gedung DPPKB',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Usul Hapus Gedung DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Usul Hapus Gedung DPPPA',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Usul Hapus Gedung DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Usul Hapus Gedung DPUPR',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Usul Hapus Gedung DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Usul Hapus Gedung DukCatPil',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Usul Hapus Gedung Halong',
                'proxy': True,
                'verbose_name_plural': '35 Usul Hapus Gedung Halong',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Usul Hapus Gedung Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Usul Hapus Gedung Inspektorat',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Usul Hapus Gedung Juai',
                'proxy': True,
                'verbose_name_plural': '33 Usul Hapus Gedung Juai',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Usul Hapus Gedung Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Usul Hapus Gedung Kearsipan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Usul Hapus Gedung Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Usul Hapus Gedung Kehutanan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Usul Hapus Gedung KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Usul Hapus Gedung KESBANGPOL',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Usul Hapus Gedung Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Usul Hapus Gedung Kominfo',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Usul Hapus Gedung Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Usul Hapus Gedung Lampihong',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Usul Hapus Gedung Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Usul Hapus Gedung Paringin',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Usul Hapus Gedung Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Usul Hapus Gedung Paringin Kota',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Usul Hapus Gedung Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Usul Hapus Gedung Paringin Selatan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Usul Hapus Gedung Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Usul Hapus Gedung Paringin Timur',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Usul Hapus Gedung Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Usul Hapus Gedung Pariwisata',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Usul Hapus Gedung Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Usul Hapus Gedung Perdagangan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Usul Hapus Gedung Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Usul Hapus Gedung Perikanan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Usul Hapus Gedung Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Usul Hapus Gedung Perpustakaan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Usul Hapus Gedung Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Usul Hapus Gedung Pertanian',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Usul Hapus Gedung RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Usul Hapus Gedung RSUD',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Usul Hapus Gedung SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Usul Hapus Gedung SATPOLPP',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Usul Hapus Gedung Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Usul Hapus Gedung Sekretariat Korpri',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Usul Hapus Gedung Setda',
                'proxy': True,
                'verbose_name_plural': '02 Usul Hapus Gedung Setda',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Usul Hapus Gedung Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Usul Hapus Gedung Setwan',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Usul Hapus Gedung Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Usul Hapus Gedung Sosial',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusGedungTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Usul Hapus Gedung Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Usul Hapus Gedung Tebing Tinggi',
            },
            bases=('gedungbangunan.tahunberkurangusulhapusgedung',),
        ),
    ]
