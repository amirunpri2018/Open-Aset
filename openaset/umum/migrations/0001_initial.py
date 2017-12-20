# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsalUsul',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('asal_usul', models.CharField(unique=True, max_length=100, verbose_name=b'Asal Usul', db_column=b'asal_usul')),
            ],
            options={
                'db_table': 'asal_usul',
                'verbose_name': 'Asal Usul',
                'verbose_name_plural': 'Asal Usul',
            },
        ),
        migrations.CreateModel(
            name='FotoTanah',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('foto', models.FileField(help_text=b'PERINGATAN: Hanya Foto Aset dan Hasil Scan File Dokumen Kepemilikan, Bukan Foto Pengguna Aset!!!', upload_to=b'tanah/', verbose_name=b'Foto', db_column=b'foto')),
                ('tanggal', models.DateField(help_text=b'Tanggal Foto yang di Upload', null=True, verbose_name=b'Tanggal', db_column=b'tanggal', blank=True)),
                ('catatan', models.CharField(help_text=b'Catatan Mengenai File yang di Upload', max_length=200, verbose_name=b'Catatan', db_column=b'catatan')),
            ],
            options={
                'db_table': 'foto_tanah',
                'verbose_name': 'Foto Tanah',
                'verbose_name_plural': 'Foto Tanah',
            },
        ),
        migrations.CreateModel(
            name='GolonganBarang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('golongan_barang', models.CharField(unique=True, max_length=100, verbose_name=b'Golongan Barang', db_column=b'golongan_barang')),
            ],
            options={
                'db_table': 'golongan_barang',
                'verbose_name': 'Golongan Barang',
                'verbose_name_plural': 'Golongan Barang',
            },
        ),
        migrations.CreateModel(
            name='HakTanah',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('hak_tanah', models.CharField(unique=True, max_length=100, verbose_name=b'Hak Tanah', db_column=b'hak_tanah')),
            ],
            options={
                'db_table': 'hak_tanah',
                'verbose_name': 'Hak Tanah',
                'verbose_name_plural': 'Hak Tanah',
            },
        ),
        migrations.CreateModel(
            name='HargaTanah',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('luas', models.IntegerField(default=0, verbose_name=b'Luas', db_column=b'luas')),
                ('harga_bertambah', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Bertambah', max_digits=15, db_column=b'harga_bertambah')),
                ('harga_berkurang', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Berkurang', max_digits=15, db_column=b'harga_berkurang')),
                ('catatan', models.CharField(help_text=b'Catatan pada Daftar Pengadaan', max_length=100, verbose_name=b'Catatan', db_column=b'catatan')),
                ('id_asal_usul', models.ForeignKey(db_column=b'id_asal_usul', verbose_name=b'Asal Usul', to='umum.AsalUsul')),
            ],
            options={
                'db_table': 'harga_tanah',
                'verbose_name': 'Harga Tanah',
                'verbose_name_plural': 'Harga Tanah',
            },
        ),
        migrations.CreateModel(
            name='JenisPemanfaatan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('jenis_pemanfaatan', models.CharField(unique=True, max_length=100, verbose_name=b'Jenis Pemanfaatan', db_column=b'jenis_pemanfaatan')),
            ],
            options={
                'db_table': 'jenis_pemanfaatan',
                'verbose_name': 'Jenis Pemanfaatan',
                'verbose_name_plural': 'Jenis Pemanfaatan',
            },
        ),
        migrations.CreateModel(
            name='Kabupaten',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_kabupaten', models.CharField(max_length=20, verbose_name=b'Kode Kabupaten', db_column=b'kode_kabupaten')),
                ('nama_kabupaten', models.CharField(max_length=200, verbose_name=b'Nama Kabupaten', db_column=b'nama_kabupaten')),
            ],
            options={
                'db_table': 'kabupaten',
                'verbose_name': 'Kabupaten',
                'verbose_name_plural': 'Kabupaten',
            },
        ),
        migrations.CreateModel(
            name='KeadaanBarang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('keadaan_barang', models.CharField(unique=True, max_length=100, verbose_name=b'Keadaan Barang', db_column=b'keadaan_barang')),
            ],
            options={
                'db_table': 'keadaan_barang',
                'verbose_name': 'Keadaan Barang',
                'verbose_name_plural': 'Keadaan Barang',
            },
        ),
        migrations.CreateModel(
            name='KodeBarang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_barang', models.CharField(unique=True, max_length=200, verbose_name=b'Kode Barang', db_column=b'kode_barang')),
                ('umur', models.IntegerField(default=0, verbose_name=b'Umur', db_column=b'umur')),
            ],
            options={
                'db_table': 'kode_barang',
                'verbose_name': 'Kode Barang',
                'verbose_name_plural': 'Kode Barang',
            },
        ),
        migrations.CreateModel(
            name='KontrakTanah',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('pihak_ketiga', models.CharField(max_length=200, verbose_name=b'Pihak Ketiga', db_column=b'pihak_ketiga')),
                ('nomor_kontrak', models.CharField(max_length=200, null=True, verbose_name=b'Nomor Kontrak', db_column=b'nomor_kontrak', blank=True)),
                ('tanggal_kontrak', models.DateField(null=True, verbose_name=b'Tanggal Kontrak', db_column=b'tanggal_kontrak', blank=True)),
                ('nomor_sp2d', models.CharField(max_length=200, verbose_name=b'Nomor SP2D', db_column=b'nomor_sp2d')),
                ('tanggal_sp2d', models.DateField(null=True, verbose_name=b'Tanggal SP2D', db_column=b'tanggal_sp2d', blank=True)),
            ],
            options={
                'db_table': 'kontrak_tanah',
                'verbose_name': 'Kontrak Tanah',
                'verbose_name_plural': 'Kontrak Tanah',
            },
        ),
        migrations.CreateModel(
            name='LokasiBidang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_lokasi_bidang', models.CharField(max_length=20, verbose_name=b'Kode Lokasi Bidang', db_column=b'kode_lokasi_bidang')),
                ('nama_lokasi_bidang', models.CharField(max_length=200, verbose_name=b'Nama Lokasi Bidang', db_column=b'nama_lokasi_bidang')),
                ('id_kabupaten', models.ForeignKey(db_column=b'id_kabupaten', verbose_name=b'Kabupaten', to='umum.Kabupaten')),
            ],
            options={
                'db_table': 'lokasi_bidang',
                'verbose_name': 'Lokasi Bidang',
                'verbose_name_plural': 'Lokasi Bidang',
            },
        ),
        migrations.CreateModel(
            name='MutasiBerkurang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('mutasi_berkurang', models.CharField(unique=True, max_length=100, verbose_name=b'Mutasi Berkurang', db_column=b'mutasi_berkurang')),
            ],
            options={
                'db_table': 'mutasi_berkurang',
                'verbose_name': 'Mutasi Berkurang',
                'verbose_name_plural': 'Mutasi Berkurang',
            },
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_provinsi', models.CharField(max_length=20, verbose_name=b'Kode Provinsi', db_column=b'kode_provinsi')),
                ('nama_provinsi', models.CharField(max_length=200, verbose_name=b'Nama Provinsi', db_column=b'nama_provinsi')),
            ],
            options={
                'db_table': 'provinsi',
                'verbose_name': 'Provinsi',
                'verbose_name_plural': 'Provinsi',
            },
        ),
        migrations.CreateModel(
            name='SatuanBarang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('satuan_barang', models.CharField(unique=True, max_length=100, verbose_name=b'Satuan Barang', db_column=b'satuan_barang')),
            ],
            options={
                'db_table': 'satuan_barang',
                'verbose_name': 'Satuan Barang',
                'verbose_name_plural': 'Satuan Barang',
            },
        ),
        migrations.CreateModel(
            name='SKPD',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_skpd', models.CharField(max_length=20, verbose_name=b'Kode SKPD', db_column=b'kode_skpd')),
                ('nama_skpd', models.CharField(max_length=200, verbose_name=b'Nama SKPD', db_column=b'nama_skpd')),
                ('id_lokasi_bidang', models.ForeignKey(db_column=b'id_lokasi_bidang', verbose_name=b'Lokasi Bidang', to='umum.LokasiBidang')),
            ],
            options={
                'db_table': 'skpd',
                'verbose_name': 'SKPD',
                'verbose_name_plural': 'SKPD',
            },
        ),
        migrations.CreateModel(
            name='SKPenghapusan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('tanggal_sk_penghapusan', models.DateField(verbose_name=b'Tanggal SK Penghapusan', db_column=b'tanggal_sk_penghapusan')),
                ('nomor_sk_penghapusan', models.CharField(max_length=100, verbose_name=b'Nomor SK Penghapusan', db_column=b'nomor_sk_penghapusan')),
            ],
            options={
                'db_table': 'sk_penghapusan',
                'verbose_name': 'SK Penghapusan',
                'verbose_name_plural': 'SK Penghapusan',
            },
        ),
        migrations.CreateModel(
            name='SUBSKPD',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('kode_sub_skpd', models.CharField(max_length=20, verbose_name=b'Kode SUB SKPD', db_column=b'kode_sub_skpd')),
                ('nama_sub_skpd', models.CharField(max_length=200, verbose_name=b'Nama SUB SKPD', db_column=b'nama_sub_skpd')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'sub_skpd',
                'verbose_name': 'SUB SKPD',
                'verbose_name_plural': 'SUB SKPD',
            },
        ),
        migrations.CreateModel(
            name='Tahun',
            fields=[
                ('tahun', models.IntegerField(serialize=False, primary_key=True, db_column=b'tahun')),
            ],
            options={
                'ordering': ['tahun'],
                'db_table': 'tahun',
                'verbose_name': 'Tahun',
                'verbose_name_plural': 'Tahun',
            },
        ),
        migrations.CreateModel(
            name='Tanah',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'Register', primary_key=True, db_column=b'id')),
                ('nama_barang', models.CharField(max_length=300, verbose_name=b'Nama Barang', db_column=b'nama_barang')),
                ('letak_alamat', models.CharField(max_length=300, null=True, verbose_name=b'Letak Alamat', db_column=b'letak_alamat', blank=True)),
                ('tanggal_sertifikat', models.DateField(null=True, verbose_name=b'Tanggal Sertifikat', db_column=b'tanggal_sertifikat', blank=True)),
                ('nomor_sertifikat', models.CharField(max_length=100, null=True, verbose_name=b'Nomor Sertifikat', db_column=b'nomor_sertifikat', blank=True)),
                ('penggunaan', models.CharField(max_length=300, null=True, verbose_name=b'Penggunaan', db_column=b'penggunaan', blank=True)),
                ('banyak_barang', models.IntegerField(default=1, verbose_name=b'Banyak Barang', db_column=b'banyak_barang')),
                ('keterangan', models.TextField(null=True, verbose_name=b'Keterangan', db_column=b'keterangan', blank=True)),
            ],
            options={
                'db_table': 'tanah',
                'verbose_name': 'Tanah',
                'verbose_name_plural': 'Tanah',
            },
        ),
        migrations.CreateModel(
            name='PemanfaatanTanah',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_tanah', serialize=False, to='umum.Tanah')),
                ('id_jenis_pemanfaatan', models.ForeignKey(db_column=b'id_jenis_pemanfaatan', verbose_name=b'Jenis Pemanfaatan', to='umum.JenisPemanfaatan')),
            ],
            options={
                'db_table': 'pemanfaatan_tanah',
                'verbose_name': 'Pemanfaatan Tanah',
                'verbose_name_plural': 'Pemanfaatan Tanah',
            },
        ),
        migrations.CreateModel(
            name='PenghapusanTanah',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_tanah', serialize=False, to='umum.Tanah')),
                ('id_sk_penghapusan', models.ForeignKey(db_column=b'id_sk_penghapusan', verbose_name=b'SK Penghapusan', to='umum.SKPenghapusan')),
            ],
            options={
                'db_table': 'penghapusan_tanah',
                'verbose_name': 'Penghapusan Tanah',
                'verbose_name_plural': 'Penghapusan Tanah',
            },
        ),
        migrations.CreateModel(
            name='SKPDAsalTanah',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_tanah', serialize=False, to='umum.Tanah')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_asal_tanah',
                'verbose_name': 'SKPD Asal Tanah',
                'verbose_name_plural': 'SKPD Asal Tanah',
            },
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanah',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_tanah', serialize=False, to='umum.Tanah')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_tujuan_tanah',
                'verbose_name': 'SKPD Tujuan Tanah',
                'verbose_name_plural': 'SKPD Tujuan Tanah',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanah',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_tanah', serialize=False, to='umum.Tanah')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_tanah',
                'verbose_name': 'Tahun Berkurang Tanah',
                'verbose_name_plural': 'Tahun Berkurang Tanah',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanah',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_tanah', serialize=False, to='umum.Tanah')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_usul_hapus_tanah',
                'verbose_name': 'Tahun Berkurang Usul Hapus Tanah',
                'verbose_name_plural': 'Tahun Berkurang Usul Hapus Tanah',
            },
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_golongan_barang',
            field=models.ForeignKey(db_column=b'id_golongan_barang', default=1, verbose_name=b'Golongan Barang', to='umum.GolonganBarang'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_hak_tanah',
            field=models.ForeignKey(db_column=b'id_hak_tanah', verbose_name=b'Hak Tanah', to='umum.HakTanah'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_keadaan_barang',
            field=models.ForeignKey(db_column=b'id_keadaan_barang', default=1, verbose_name=b'Keadaan Barang', to='umum.KeadaanBarang'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_kode_barang',
            field=models.ForeignKey(db_column=b'id_kode_barang', verbose_name=b'Kode Barang', to='umum.KodeBarang'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_mutasi_berkurang',
            field=models.ForeignKey(db_column=b'id_mutasi_berkurang', default=5, verbose_name=b'Mutasi Berkurang', to='umum.MutasiBerkurang'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_satuan_barang',
            field=models.ForeignKey(db_column=b'id_satuan_barang', verbose_name=b'Satuan Barang', to='umum.SatuanBarang'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='id_sub_skpd',
            field=models.ForeignKey(db_column=b'id_sub_skpd', verbose_name=b'SUB SKPD', to='umum.SUBSKPD'),
        ),
        migrations.AddField(
            model_name='tanah',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun Awal', to='umum.Tahun', help_text=b'Tahun Awal Kapitalisasi'),
        ),
        migrations.AddField(
            model_name='kontraktanah',
            name='id_skpd',
            field=models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD'),
        ),
        migrations.AddField(
            model_name='kabupaten',
            name='id_provinsi',
            field=models.ForeignKey(db_column=b'id_provinsi', verbose_name=b'Provinsi', to='umum.Provinsi'),
        ),
        migrations.AddField(
            model_name='hargatanah',
            name='id_kontrak',
            field=models.ForeignKey(db_column=b'id_kontrak', verbose_name=b'Kontrak Tanah', to='umum.KontrakTanah'),
        ),
        migrations.AddField(
            model_name='hargatanah',
            name='id_tanah',
            field=models.ForeignKey(db_column=b'id_tanah', verbose_name=b'Tanah', to='umum.Tanah'),
        ),
        migrations.AddField(
            model_name='hargatanah',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun', to='umum.Tahun', help_text=b'Tahun Anggaran'),
        ),
        migrations.AddField(
            model_name='hargatanah',
            name='tahun_mutasi',
            field=models.ForeignKey(related_name='+', db_column=b'tahun_mutasi', to='umum.Tahun', blank=True, help_text=b'Tahun Mutasi', null=True, verbose_name=b'Tahun Mutasi'),
        ),
        migrations.AddField(
            model_name='fototanah',
            name='id_tanah',
            field=models.ForeignKey(db_column=b'id_tanah', verbose_name=b'Tanah', to='umum.Tanah'),
        ),
        migrations.CreateModel(
            name='FotoTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Foto Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Foto Tanah Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Foto Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Foto Tanah BAPPEDA',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Foto Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Foto Tanah Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Foto Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Foto Tanah Batu Piring',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Foto Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Foto Tanah BKD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Foto Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Foto Tanah BKPPD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Foto Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Foto Tanah BPBD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Foto Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Foto Tanah BPPD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Juai',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Kantor',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Lampihong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Lokbatu',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Paringin Selatan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Pirsus',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes RSUD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Tanah Habang',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Tebing Tinggi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto Tanah Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Foto Tanah Dinkes Uren',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Juai',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Kantor',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Lampihong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Paringin Selatan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 1 Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 1 Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 1 Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 1 Juai',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 1 Lampihong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 1 Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 2 Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 2 Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 2 Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 2 Juai',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 2 Lampihong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 2 Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 3 Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 3 Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 3 Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 3 Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 4 Awayan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 4 Batumandi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 4 Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 4 Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 5 Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik SMPN 5 Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto Tanah Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Foto Tanah Disdik Tebing Tinggi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Foto Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Foto Tanah Dishub',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Foto Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Foto Tanah Disnakertrans',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Foto Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Foto Tanah Distamben',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Foto Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Foto Tanah DKO',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Foto Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Foto Tanah DKP',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Foto Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Foto Tanah DKUKMP',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Foto Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Foto Tanah DLH',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Foto Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Foto Tanah DPKP',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Foto Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Foto Tanah DPMD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Foto Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Foto Tanah DPMPTSP',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Foto Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Foto Tanah DPPKB',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Foto Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Foto Tanah DPPPA',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Foto Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Foto Tanah DPUPR',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Foto Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Foto Tanah DukCatPil',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Foto Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Foto Tanah Halong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Foto Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Foto Tanah Inspektorat',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Foto Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Foto Tanah Juai',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Foto Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Foto Tanah Kearsipan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Foto Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Foto Tanah Kehutanan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Foto Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Foto Tanah KESBANGPOL',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Foto Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Foto Tanah Kominfo',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Foto Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Foto Tanah Lampihong',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Foto Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Foto Tanah Paringin',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Foto Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Foto Tanah Paringin Kota',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Foto Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Foto Tanah Paringin Selatan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Foto Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Foto Tanah Paringin Timur',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Foto Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Foto Tanah Pariwisata',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Foto Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Foto Tanah Perdagangan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Foto Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Foto Tanah Perikanan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Foto Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Foto Tanah Perpustakaan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Foto Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Foto Tanah Pertanian',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Foto Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Foto Tanah RSUD',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Foto Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Foto Tanah SATPOLPP',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Foto Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Foto Tanah Sekretariat Korpri',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Foto Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Foto Tanah Setda',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Foto Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Foto Tanah Setwan',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Foto Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Foto Tanah Sosial',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='FotoTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Foto Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Foto Tanah Tebing Tinggi',
            },
            bases=('umum.fototanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Harga Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Harga Tanah Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Harga Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Harga Tanah BAPPEDA',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Harga Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Harga Tanah Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Harga Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Harga Tanah Batu Piring',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Harga Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Harga Tanah BKD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Harga Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Harga Tanah BKPPD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Harga Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Harga Tanah BPBD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Harga Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Harga Tanah BPPD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Juai',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Kantor',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Lampihong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Lokbatu',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Paringin Selatan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Pirsus',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes RSUD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Tanah Habang',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Tebing Tinggi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga Tanah Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Harga Tanah Dinkes Uren',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Juai',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Kantor',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Lampihong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Paringin Selatan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 1 Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 1 Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 1 Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 1 Juai',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 1 Lampihong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 1 Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 2 Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 2 Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 2 Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 2 Juai',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 2 Lampihong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 2 Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 3 Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 3 Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 3 Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 3 Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 4 Awayan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 4 Batumandi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 4 Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 4 Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 5 Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik SMPN 5 Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga Tanah Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Harga Tanah Disdik Tebing Tinggi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Harga Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Harga Tanah Dishub',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Harga Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Harga Tanah Disnakertrans',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Harga Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Harga Tanah Distamben',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Harga Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Harga Tanah DKO',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Harga Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Harga Tanah DKP',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Harga Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Harga Tanah DKUKMP',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Harga Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Harga Tanah DLH',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Harga Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Harga Tanah DPKP',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Harga Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Harga Tanah DPMD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Harga Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Harga Tanah DPMPTSP',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Harga Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Harga Tanah DPPKB',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Harga Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Harga Tanah DPPPA',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Harga Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Harga Tanah DPUPR',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Harga Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Harga Tanah DukCatPil',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Harga Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Harga Tanah Halong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Harga Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Harga Tanah Inspektorat',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Harga Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Harga Tanah Juai',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Harga Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Harga Tanah Kearsipan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Harga Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Harga Tanah Kehutanan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Harga Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Harga Tanah KESBANGPOL',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Harga Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Harga Tanah Kominfo',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Harga Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Harga Tanah Lampihong',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Harga Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Harga Tanah Paringin',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Harga Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Harga Tanah Paringin Kota',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Harga Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Harga Tanah Paringin Selatan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Harga Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Harga Tanah Paringin Timur',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Harga Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Harga Tanah Pariwisata',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Harga Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Harga Tanah Perdagangan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Harga Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Harga Tanah Perikanan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Harga Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Harga Tanah Perpustakaan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Harga Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Harga Tanah Pertanian',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Harga Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Harga Tanah RSUD',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Harga Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Harga Tanah SATPOLPP',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Harga Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Harga Tanah Sekretariat Korpri',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Harga Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Harga Tanah Setda',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Harga Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Harga Tanah Setwan',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Harga Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Harga Tanah Sosial',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='HargaTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Harga Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Harga Tanah Tebing Tinggi',
            },
            bases=('umum.hargatanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Kontrak Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Kontrak Tanah Awayan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Kontrak Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Kontrak Tanah BAPPEDA',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Kontrak Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Kontrak Tanah Batumandi',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Kontrak Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Kontrak Tanah Batu Piring',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Kontrak Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Kontrak Tanah BKD',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Kontrak Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Kontrak Tanah BKPPD',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Kontrak Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Kontrak Tanah BPBD',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Kontrak Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Kontrak Tanah BPPD',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Kontrak Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Kontrak Tanah Dinkes',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Kontrak Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Kontrak Tanah Disdik',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Kontrak Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Kontrak Tanah Dishub',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Kontrak Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Kontrak Tanah Disnakertrans',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Kontrak Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Kontrak Tanah Distamben',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Kontrak Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Kontrak Tanah DKO',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Kontrak Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Kontrak Tanah DKP',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Kontrak Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Kontrak Tanah DKUKMP',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Kontrak Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Kontrak Tanah DLH',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Kontrak Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Kontrak Tanah DPKP',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Kontrak Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Kontrak Tanah DPMD',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Kontrak Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Kontrak Tanah DPMPTSP',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Kontrak Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Kontrak Tanah DPPKB',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Kontrak Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Kontrak Tanah DPPPA',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Kontrak Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Kontrak Tanah DPUPR',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Kontrak Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Kontrak Tanah DukCatPil',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Kontrak Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Kontrak Tanah Halong',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Kontrak Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Kontrak Tanah Inspektorat',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Kontrak Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Kontrak Tanah Juai',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Kontrak Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Kontrak Tanah Kearsipan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Kontrak Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Kontrak Tanah Kehutanan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Kontrak Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Kontrak Tanah KESBANGPOL',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Kontrak Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Kontrak Tanah Kominfo',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Kontrak Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Kontrak Tanah Lampihong',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Kontrak Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Kontrak Tanah Paringin',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Kontrak Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Kontrak Tanah Paringin Kota',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Kontrak Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Kontrak Tanah Paringin Selatan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Kontrak Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Kontrak Tanah Paringin Timur',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Kontrak Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Kontrak Tanah Pariwisata',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Kontrak Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Kontrak Tanah Perdagangan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Kontrak Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Kontrak Tanah Perikanan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Kontrak Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Kontrak Tanah Perpustakaan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Kontrak Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Kontrak Tanah Pertanian',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Kontrak Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Kontrak Tanah RSUD',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Kontrak Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Kontrak Tanah SATPOLPP',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Kontrak Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Kontrak Tanah Sekretariat Korpri',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Kontrak Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Kontrak Tanah Setda',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Kontrak Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Kontrak Tanah Setwan',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Kontrak Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Kontrak Tanah Sosial',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='KontrakTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Kontrak Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Kontrak Tanah Tebing Tinggi',
            },
            bases=('umum.kontraktanah',),
        ),
        migrations.CreateModel(
            name='TanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tanah Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tanah BAPPEDA',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tanah Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tanah Batu Piring',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tanah BKD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tanah BKPPD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tanah BPBD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tanah BPPD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Kantor',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Lokbatu',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Paringin Selatan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Pirsus',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes RSUD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Tanah Habang',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Tebing Tinggi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Dinkes Uren',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Kantor',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Paringin Selatan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 1 Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 1 Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 1 Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 1 Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 1 Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 1 Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 2 Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 2 Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 2 Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 2 Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 2 Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 2 Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 3 Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 3 Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 3 Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 3 Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 4 Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 4 Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 4 Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 4 Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 5 Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik SMPN 5 Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Disdik Tebing Tinggi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tanah Dishub',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tanah Disnakertrans',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tanah Distamben',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tanah DKO',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tanah DKP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tanah DKUKMP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tanah DLH',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tanah DPKP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tanah DPMD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tanah DPMPTSP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tanah DPPKB',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tanah DPPPA',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tanah DPUPR',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tanah DukCatPil',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tanah Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tanah Inspektorat',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tanah Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tanah Kearsipan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tanah Kehutanan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tanah KESBANGPOL',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tanah Kominfo',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tanah Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tanah Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tanah Paringin Kota',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tanah Paringin Selatan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tanah Paringin Timur',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tanah Pariwisata',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPemanfaatan',
            fields=[
            ],
            options={
                'verbose_name': 'Tanah Pemanfaatan',
                'proxy': True,
                'verbose_name_plural': 'Tanah Pemanfaatan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusan',
            fields=[
            ],
            options={
                'verbose_name': 'Tanah Penghapusan',
                'proxy': True,
                'verbose_name_plural': 'Tanah Penghapusan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tanah Penghapusan Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tanah Penghapusan Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tanah Penghapusan BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tanah Penghapusan BAPPEDA',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tanah Penghapusan Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tanah Penghapusan Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tanah Penghapusan Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tanah Penghapusan Batu Piring',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tanah Penghapusan BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tanah Penghapusan BKD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tanah Penghapusan BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tanah Penghapusan BKPPD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tanah Penghapusan BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tanah Penghapusan BPBD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tanah Penghapusan BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tanah Penghapusan BPPD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Penghapusan Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Penghapusan Dinkes',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Penghapusan Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Penghapusan Disdik',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tanah Penghapusan Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tanah Penghapusan Dishub',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tanah Penghapusan Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tanah Penghapusan Disnakertrans',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tanah Penghapusan Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tanah Penghapusan Distamben',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tanah Penghapusan DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tanah Penghapusan DKO',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tanah Penghapusan DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tanah Penghapusan DKP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tanah Penghapusan DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tanah Penghapusan DKUKMP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tanah Penghapusan DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tanah Penghapusan DLH',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tanah Penghapusan DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tanah Penghapusan DPKP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tanah Penghapusan DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tanah Penghapusan DPMD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tanah Penghapusan DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tanah Penghapusan DPMPTSP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tanah Penghapusan DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tanah Penghapusan DPPKB',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tanah Penghapusan DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tanah Penghapusan DPPPA',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tanah Penghapusan DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tanah Penghapusan DPUPR',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tanah Penghapusan DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tanah Penghapusan DukCatPil',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tanah Penghapusan Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tanah Penghapusan Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tanah Penghapusan Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tanah Penghapusan Inspektorat',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tanah Penghapusan Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tanah Penghapusan Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tanah Penghapusan Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tanah Penghapusan Kearsipan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tanah Penghapusan Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tanah Penghapusan Kehutanan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tanah Penghapusan KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tanah Penghapusan KESBANGPOL',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tanah Penghapusan Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tanah Penghapusan Kominfo',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tanah Penghapusan Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tanah Penghapusan Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tanah Penghapusan Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tanah Penghapusan Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tanah Penghapusan Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tanah Penghapusan Paringin Kota',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tanah Penghapusan Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tanah Penghapusan Paringin Selatan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tanah Penghapusan Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tanah Penghapusan Paringin Timur',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tanah Penghapusan Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tanah Penghapusan Pariwisata',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tanah Penghapusan Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tanah Penghapusan Perdagangan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tanah Penghapusan Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tanah Penghapusan Perikanan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tanah Penghapusan Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tanah Penghapusan Perpustakaan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tanah Penghapusan Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tanah Penghapusan Pertanian',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tanah Penghapusan RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tanah Penghapusan RSUD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tanah Penghapusan SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tanah Penghapusan SATPOLPP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tanah Penghapusan Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tanah Penghapusan Sekretariat Korpri',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tanah Penghapusan Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tanah Penghapusan Setda',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tanah Penghapusan Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tanah Penghapusan Setwan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tanah Penghapusan Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tanah Penghapusan Sosial',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPenghapusanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tanah Penghapusan Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tanah Penghapusan Tebing Tinggi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tanah Perdagangan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tanah Perikanan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tanah Perpustakaan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tanah Pertanian',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahReklas',
            fields=[
            ],
            options={
                'verbose_name': 'Tanah Reklas',
                'proxy': True,
                'verbose_name_plural': 'Tanah Reklas',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tanah RSUD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tanah SATPOLPP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tanah Sekretariat Korpri',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tanah Setda',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tanah Setwan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tanah Sosial',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tanah Tebing Tinggi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapus',
            fields=[
            ],
            options={
                'verbose_name': 'Tanah Usul Hapus',
                'proxy': True,
                'verbose_name_plural': 'Tanah Usul Hapus',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tanah Usul Hapus Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tanah Usul Hapus Awayan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tanah Usul Hapus BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tanah Usul Hapus BAPPEDA',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tanah Usul Hapus Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tanah Usul Hapus Batumandi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tanah Usul Hapus Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tanah Usul Hapus Batu Piring',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tanah Usul Hapus BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tanah Usul Hapus BKD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tanah Usul Hapus BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tanah Usul Hapus BKPPD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tanah Usul Hapus BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tanah Usul Hapus BPBD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tanah Usul Hapus BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tanah Usul Hapus BPPD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tanah Usul Hapus Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tanah Usul Hapus Dinkes',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tanah Usul Hapus Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tanah Usul Hapus Disdik',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tanah Usul Hapus Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tanah Usul Hapus Dishub',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tanah Usul Hapus Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tanah Usul Hapus Disnakertrans',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tanah Usul Hapus Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tanah Usul Hapus Distamben',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tanah Usul Hapus DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tanah Usul Hapus DKO',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tanah Usul Hapus DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tanah Usul Hapus DKP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tanah Usul Hapus DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tanah Usul Hapus DKUKMP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tanah Usul Hapus DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tanah Usul Hapus DLH',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tanah Usul Hapus DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tanah Usul Hapus DPKP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tanah Usul Hapus DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tanah Usul Hapus DPMD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tanah Usul Hapus DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tanah Usul Hapus DPMPTSP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tanah Usul Hapus DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tanah Usul Hapus DPPKB',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tanah Usul Hapus DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tanah Usul Hapus DPPPA',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tanah Usul Hapus DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tanah Usul Hapus DPUPR',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tanah Usul Hapus DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tanah Usul Hapus DukCatPil',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tanah Usul Hapus Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tanah Usul Hapus Halong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tanah Usul Hapus Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tanah Usul Hapus Inspektorat',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tanah Usul Hapus Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tanah Usul Hapus Juai',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tanah Usul Hapus Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tanah Usul Hapus Kearsipan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tanah Usul Hapus Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tanah Usul Hapus Kehutanan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tanah Usul Hapus KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tanah Usul Hapus KESBANGPOL',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tanah Usul Hapus Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tanah Usul Hapus Kominfo',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tanah Usul Hapus Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tanah Usul Hapus Lampihong',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tanah Usul Hapus Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tanah Usul Hapus Paringin',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tanah Usul Hapus Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tanah Usul Hapus Paringin Kota',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tanah Usul Hapus Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tanah Usul Hapus Paringin Selatan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tanah Usul Hapus Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tanah Usul Hapus Paringin Timur',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tanah Usul Hapus Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tanah Usul Hapus Pariwisata',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tanah Usul Hapus Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tanah Usul Hapus Perdagangan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tanah Usul Hapus Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tanah Usul Hapus Perikanan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tanah Usul Hapus Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tanah Usul Hapus Perpustakaan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tanah Usul Hapus Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tanah Usul Hapus Pertanian',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tanah Usul Hapus RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tanah Usul Hapus RSUD',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tanah Usul Hapus SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tanah Usul Hapus SATPOLPP',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tanah Usul Hapus Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tanah Usul Hapus Sekretariat Korpri',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tanah Usul Hapus Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tanah Usul Hapus Setda',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tanah Usul Hapus Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tanah Usul Hapus Setwan',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tanah Usul Hapus Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tanah Usul Hapus Sosial',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='TanahUsulHapusTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tanah Usul Hapus Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tanah Usul Hapus Tebing Tinggi',
            },
            bases=('umum.tanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Penghapusan Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Penghapusan Tanah Awayan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Penghapusan Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Penghapusan Tanah BAPPEDA',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Penghapusan Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Penghapusan Tanah Batumandi',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Penghapusan Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Penghapusan Tanah Batu Piring',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Penghapusan Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Penghapusan Tanah BKD',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Penghapusan Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Penghapusan Tanah BKPPD',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Penghapusan Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Penghapusan Tanah BPBD',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Penghapusan Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Penghapusan Tanah BPPD',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Penghapusan Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Penghapusan Tanah Dinkes',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Penghapusan Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Penghapusan Tanah Disdik',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Penghapusan Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Penghapusan Tanah Dishub',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Penghapusan Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Penghapusan Tanah Disnakertrans',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Penghapusan Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Penghapusan Tanah Distamben',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Penghapusan Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Penghapusan Tanah DKO',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Penghapusan Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Penghapusan Tanah DKP',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Penghapusan Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Penghapusan Tanah DKUKMP',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Penghapusan Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Penghapusan Tanah DLH',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Penghapusan Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Penghapusan Tanah DPKP',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Penghapusan Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Penghapusan Tanah DPMD',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Penghapusan Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Penghapusan Tanah DPMPTSP',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Penghapusan Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Penghapusan Tanah DPPKB',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Penghapusan Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Penghapusan Tanah DPPPA',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Penghapusan Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Penghapusan Tanah DPUPR',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Penghapusan Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Penghapusan Tanah DukCatPil',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Penghapusan Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Penghapusan Tanah Halong',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Penghapusan Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Penghapusan Tanah Inspektorat',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Penghapusan Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Penghapusan Tanah Juai',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Penghapusan Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Penghapusan Tanah Kearsipan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Penghapusan Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Penghapusan Tanah Kehutanan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Penghapusan Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Penghapusan Tanah KESBANGPOL',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Penghapusan Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Penghapusan Tanah Kominfo',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Penghapusan Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Penghapusan Tanah Lampihong',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Penghapusan Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Penghapusan Tanah Paringin',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Penghapusan Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Penghapusan Tanah Paringin Kota',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Penghapusan Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Penghapusan Tanah Paringin Selatan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Penghapusan Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Penghapusan Tanah Paringin Timur',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Penghapusan Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Penghapusan Tanah Pariwisata',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Penghapusan Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Penghapusan Tanah Perdagangan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Penghapusan Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Penghapusan Tanah Perikanan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Penghapusan Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Penghapusan Tanah Perpustakaan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Penghapusan Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Penghapusan Tanah Pertanian',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Penghapusan Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Penghapusan Tanah RSUD',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Penghapusan Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Penghapusan Tanah SATPOLPP',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Penghapusan Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Penghapusan Tanah Sekretariat Korpri',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Penghapusan Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Penghapusan Tanah Setda',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Penghapusan Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Penghapusan Tanah Setwan',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Penghapusan Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Penghapusan Tanah Sosial',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='PenghapusanTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Penghapusan Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Penghapusan Tanah Tebing Tinggi',
            },
            bases=('umum.penghapusantanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Asal Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Asal Tanah Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Asal Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Asal Tanah BAPPEDA',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Asal Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Asal Tanah Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Asal Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Asal Tanah Batu Piring',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Asal Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Asal Tanah BKD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Asal Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Asal Tanah BKPPD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Asal Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Asal Tanah BPBD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Asal Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Asal Tanah BPPD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Juai',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Kantor',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Lampihong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Lokbatu',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Paringin Selatan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Pirsus',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes RSUD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Tanah Habang',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Tebing Tinggi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal Tanah Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal Tanah Dinkes Uren',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Juai',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Kantor',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Lampihong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Paringin Selatan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 1 Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 1 Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 1 Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 1 Juai',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 1 Lampihong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 1 Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 2 Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 2 Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 2 Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 2 Juai',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 2 Lampihong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 2 Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 3 Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 3 Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 3 Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 3 Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 4 Awayan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 4 Batumandi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 4 Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 4 Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 5 Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik SMPN 5 Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal Tanah Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal Tanah Disdik Tebing Tinggi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Asal Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Asal Tanah Dishub',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Asal Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Asal Tanah Disnakertrans',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Asal Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Asal Tanah Distamben',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Asal Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Asal Tanah DKO',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Asal Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Asal Tanah DKP',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Asal Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Asal Tanah DKUKMP',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Asal Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Asal Tanah DLH',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Asal Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Asal Tanah DPKP',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Asal Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Asal Tanah DPMD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Asal Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Asal Tanah DPMPTSP',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Asal Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Asal Tanah DPPKB',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Asal Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Asal Tanah DPPPA',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Asal Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Asal Tanah DPUPR',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Asal Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Asal Tanah DukCatPil',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Asal Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Asal Tanah Halong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Asal Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Asal Tanah Inspektorat',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Asal Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Asal Tanah Juai',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Asal Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Asal Tanah Kearsipan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Asal Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Asal Tanah Kehutanan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Asal Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Asal Tanah KESBANGPOL',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Asal Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Asal Tanah Kominfo',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Asal Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Asal Tanah Lampihong',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Asal Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Asal Tanah Paringin',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Asal Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Asal Tanah Paringin Kota',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Asal Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Asal Tanah Paringin Selatan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Asal Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Asal Tanah Paringin Timur',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Asal Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Asal Tanah Pariwisata',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Asal Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Asal Tanah Perdagangan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Asal Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Asal Tanah Perikanan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Asal Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Asal Tanah Perpustakaan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Asal Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Asal Tanah Pertanian',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Asal Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Asal Tanah RSUD',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Asal Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Asal Tanah SATPOLPP',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Asal Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Asal Tanah Sekretariat Korpri',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Asal Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Asal Tanah Setda',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Asal Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Asal Tanah Setwan',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Asal Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Asal Tanah Sosial',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDAsalTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Asal Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Asal Tanah Tebing Tinggi',
            },
            bases=('umum.skpdasaltanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Tujuan Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Tujuan Tanah Awayan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Tujuan Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Tujuan Tanah BAPPEDA',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Tujuan Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Tujuan Tanah Batumandi',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Tujuan Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Tujuan Tanah Batu Piring',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Tujuan Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Tujuan Tanah BKD',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Tujuan Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Tujuan Tanah BKPPD',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Tujuan Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Tujuan Tanah BPBD',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Tujuan Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Tujuan Tanah BPPD',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Tujuan Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Tujuan Tanah Dinkes',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Tujuan Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Tujuan Tanah Disdik',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Tujuan Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Tujuan Tanah Dishub',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Tujuan Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Tujuan Tanah Disnakertrans',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Tujuan Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Tujuan Tanah Distamben',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Tujuan Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Tujuan Tanah DKO',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Tujuan Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Tujuan Tanah DKP',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Tujuan Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Tujuan Tanah DKUKMP',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Tujuan Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Tujuan Tanah DLH',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Tujuan Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Tujuan Tanah DPKP',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Tujuan Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Tujuan Tanah DPMD',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Tujuan Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Tujuan Tanah DPMPTSP',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Tujuan Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Tujuan Tanah DPPKB',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Tujuan Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Tujuan Tanah DPPPA',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Tujuan Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Tujuan Tanah DPUPR',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Tujuan Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Tujuan Tanah DukCatPil',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Tujuan Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Tujuan Tanah Halong',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Tujuan Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Tujuan Tanah Inspektorat',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Tujuan Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Tujuan Tanah Juai',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Tujuan Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Tujuan Tanah Kearsipan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Tujuan Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Tujuan Tanah Kehutanan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Tujuan Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Tujuan Tanah KESBANGPOL',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Tujuan Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Tujuan Tanah Kominfo',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Tujuan Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Tujuan Tanah Lampihong',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Tujuan Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Tujuan Tanah Paringin',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Tujuan Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Tujuan Tanah Paringin Kota',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Tujuan Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Tujuan Tanah Paringin Selatan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Tujuan Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Tujuan Tanah Paringin Timur',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Tujuan Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Tujuan Tanah Pariwisata',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Tujuan Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Tujuan Tanah Perdagangan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Tujuan Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Tujuan Tanah Perikanan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Tujuan Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Tujuan Tanah Perpustakaan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Tujuan Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Tujuan Tanah Pertanian',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Tujuan Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Tujuan Tanah RSUD',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Tujuan Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Tujuan Tanah SATPOLPP',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Tujuan Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Tujuan Tanah Sekretariat Korpri',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Tujuan Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Tujuan Tanah Setda',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Tujuan Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Tujuan Tanah Setwan',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Tujuan Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Tujuan Tanah Sosial',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Tujuan Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Tujuan Tanah Tebing Tinggi',
            },
            bases=('umum.skpdtujuantanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tahun Berkurang Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tahun Berkurang Tanah Awayan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tahun Berkurang Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tahun Berkurang Tanah BAPPEDA',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tahun Berkurang Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tahun Berkurang Tanah Batumandi',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tahun Berkurang Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tahun Berkurang Tanah Batu Piring',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tahun Berkurang Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tahun Berkurang Tanah BKD',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tahun Berkurang Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tahun Berkurang Tanah BKPPD',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tahun Berkurang Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tahun Berkurang Tanah BPBD',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tahun Berkurang Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tahun Berkurang Tanah BPPD',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tahun Berkurang Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tahun Berkurang Tanah Dinkes',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tahun Berkurang Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tahun Berkurang Tanah Disdik',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tahun Berkurang Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tahun Berkurang Tanah Dishub',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tahun Berkurang Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tahun Berkurang Tanah Disnakertrans',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tahun Berkurang Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tahun Berkurang Tanah Distamben',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tahun Berkurang Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tahun Berkurang Tanah DKO',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tahun Berkurang Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tahun Berkurang Tanah DKP',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tahun Berkurang Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tahun Berkurang Tanah DKUKMP',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tahun Berkurang Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tahun Berkurang Tanah DLH',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tahun Berkurang Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tahun Berkurang Tanah DPKP',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tahun Berkurang Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tahun Berkurang Tanah DPMD',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tahun Berkurang Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tahun Berkurang Tanah DPMPTSP',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tahun Berkurang Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tahun Berkurang Tanah DPPKB',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tahun Berkurang Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tahun Berkurang Tanah DPPPA',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tahun Berkurang Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tahun Berkurang Tanah DPUPR',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tahun Berkurang Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tahun Berkurang Tanah DukCatPil',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tahun Berkurang Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tahun Berkurang Tanah Halong',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tahun Berkurang Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tahun Berkurang Tanah Inspektorat',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tahun Berkurang Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tahun Berkurang Tanah Juai',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tahun Berkurang Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tahun Berkurang Tanah Kearsipan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tahun Berkurang Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tahun Berkurang Tanah Kehutanan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tahun Berkurang Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tahun Berkurang Tanah KESBANGPOL',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tahun Berkurang Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tahun Berkurang Tanah Kominfo',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tahun Berkurang Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tahun Berkurang Tanah Lampihong',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tahun Berkurang Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tahun Berkurang Tanah Paringin',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tahun Berkurang Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tahun Berkurang Tanah Paringin Kota',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tahun Berkurang Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tahun Berkurang Tanah Paringin Selatan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tahun Berkurang Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tahun Berkurang Tanah Paringin Timur',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tahun Berkurang Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tahun Berkurang Tanah Pariwisata',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tahun Berkurang Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tahun Berkurang Tanah Perdagangan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tahun Berkurang Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tahun Berkurang Tanah Perikanan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tahun Berkurang Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tahun Berkurang Tanah Perpustakaan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tahun Berkurang Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tahun Berkurang Tanah Pertanian',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tahun Berkurang Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tahun Berkurang Tanah RSUD',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tahun Berkurang Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tahun Berkurang Tanah SATPOLPP',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tahun Berkurang Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tahun Berkurang Tanah Sekretariat Korpri',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tahun Berkurang Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tahun Berkurang Tanah Setda',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tahun Berkurang Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tahun Berkurang Tanah Setwan',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tahun Berkurang Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tahun Berkurang Tanah Sosial',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tahun Berkurang Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tahun Berkurang Tanah Tebing Tinggi',
            },
            bases=('umum.tahunberkurangtanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Usul Hapus Tanah Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Usul Hapus Tanah Awayan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Usul Hapus Tanah BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Usul Hapus Tanah BAPPEDA',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Usul Hapus Tanah Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Usul Hapus Tanah Batumandi',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Usul Hapus Tanah Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Usul Hapus Tanah Batu Piring',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Usul Hapus Tanah BKD',
                'proxy': True,
                'verbose_name_plural': '19 Usul Hapus Tanah BKD',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Usul Hapus Tanah BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Usul Hapus Tanah BKPPD',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Usul Hapus Tanah BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Usul Hapus Tanah BPBD',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Usul Hapus Tanah BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Usul Hapus Tanah BPPD',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Usul Hapus Tanah Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Usul Hapus Tanah Dinkes',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Usul Hapus Tanah Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Usul Hapus Tanah Disdik',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Usul Hapus Tanah Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Usul Hapus Tanah Dishub',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Usul Hapus Tanah Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Usul Hapus Tanah Disnakertrans',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Usul Hapus Tanah Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Usul Hapus Tanah Distamben',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Usul Hapus Tanah DKO',
                'proxy': True,
                'verbose_name_plural': '23 Usul Hapus Tanah DKO',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Usul Hapus Tanah DKP',
                'proxy': True,
                'verbose_name_plural': '15 Usul Hapus Tanah DKP',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Usul Hapus Tanah DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Usul Hapus Tanah DKUKMP',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Usul Hapus Tanah DLH',
                'proxy': True,
                'verbose_name_plural': '22 Usul Hapus Tanah DLH',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Usul Hapus Tanah DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Usul Hapus Tanah DPKP',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Usul Hapus Tanah DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Usul Hapus Tanah DPMD',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Usul Hapus Tanah DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Usul Hapus Tanah DPMPTSP',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Usul Hapus Tanah DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Usul Hapus Tanah DPPKB',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Usul Hapus Tanah DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Usul Hapus Tanah DPPPA',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Usul Hapus Tanah DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Usul Hapus Tanah DPUPR',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Usul Hapus Tanah DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Usul Hapus Tanah DukCatPil',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Usul Hapus Tanah Halong',
                'proxy': True,
                'verbose_name_plural': '35 Usul Hapus Tanah Halong',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Usul Hapus Tanah Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Usul Hapus Tanah Inspektorat',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Usul Hapus Tanah Juai',
                'proxy': True,
                'verbose_name_plural': '33 Usul Hapus Tanah Juai',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Usul Hapus Tanah Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Usul Hapus Tanah Kearsipan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Usul Hapus Tanah Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Usul Hapus Tanah Kehutanan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Usul Hapus Tanah KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Usul Hapus Tanah KESBANGPOL',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Usul Hapus Tanah Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Usul Hapus Tanah Kominfo',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Usul Hapus Tanah Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Usul Hapus Tanah Lampihong',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Usul Hapus Tanah Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Usul Hapus Tanah Paringin',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Usul Hapus Tanah Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Usul Hapus Tanah Paringin Kota',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Usul Hapus Tanah Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Usul Hapus Tanah Paringin Selatan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Usul Hapus Tanah Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Usul Hapus Tanah Paringin Timur',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Usul Hapus Tanah Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Usul Hapus Tanah Pariwisata',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Usul Hapus Tanah Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Usul Hapus Tanah Perdagangan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Usul Hapus Tanah Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Usul Hapus Tanah Perikanan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Usul Hapus Tanah Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Usul Hapus Tanah Perpustakaan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Usul Hapus Tanah Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Usul Hapus Tanah Pertanian',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Usul Hapus Tanah RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Usul Hapus Tanah RSUD',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Usul Hapus Tanah SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Usul Hapus Tanah SATPOLPP',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Usul Hapus Tanah Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Usul Hapus Tanah Sekretariat Korpri',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Usul Hapus Tanah Setda',
                'proxy': True,
                'verbose_name_plural': '02 Usul Hapus Tanah Setda',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Usul Hapus Tanah Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Usul Hapus Tanah Setwan',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Usul Hapus Tanah Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Usul Hapus Tanah Sosial',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusTanahTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Usul Hapus Tanah Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Usul Hapus Tanah Tebing Tinggi',
            },
            bases=('umum.tahunberkurangusulhapustanah',),
        ),
    ]
