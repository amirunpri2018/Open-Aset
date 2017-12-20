# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umum', '0001_initial'),
        ('gedungbangunan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATL',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'Register', primary_key=True, db_column=b'id')),
                ('nama_barang', models.CharField(max_length=300, verbose_name=b'Nama Barang', db_column=b'nama_barang')),
                ('judul_pencipta_buku', models.CharField(max_length=150, null=True, verbose_name=b'Judul/Pencipta Buku', db_column=b'judul_pencipta_buku', blank=True)),
                ('spesifikasi_buku', models.CharField(db_column=b'spesifikasi_buku', max_length=150, blank=True, help_text=b'Bahan Pembuatan Buku, misal: Kertas, CD, dsb', null=True, verbose_name=b'Spesifikasi Buku')),
                ('asal_daerah_barang_seni', models.CharField(max_length=150, null=True, verbose_name=b'Asal Daerah Barang Bercorak Kesenian', db_column=b'asal_daerah_barang_seni', blank=True)),
                ('pencipta_barang_seni', models.CharField(max_length=150, null=True, verbose_name=b'Pencipta Barang Bercorak Kesenian', db_column=b'pencipta_barang_seni', blank=True)),
                ('bahan_barang_seni', models.CharField(max_length=150, null=True, verbose_name=b'Bahan Barang Bercorak Kesenian', db_column=b'bahan_barang_seni', blank=True)),
                ('jenis_hewan_tumbuhan', models.CharField(db_column=b'jenis_hewan_tumbuhan', max_length=150, blank=True, help_text=b'Diisi mengenai jenis hewan/ternak atau tumbuhan', null=True, verbose_name=b'Jenis Hewan/Tumbuhan')),
                ('ukuran_hewan_tumbuhan', models.CharField(db_column=b'ukuran_hewan_tumbuhan', max_length=150, blank=True, help_text=b'Diisi ukuran (kg, cm, m, dan sebagainya)', null=True, verbose_name=b'Ukuran Hewan/Tumbuhan')),
                ('banyak_barang', models.IntegerField(default=1, verbose_name=b'Banyak Barang', db_column=b'banyak_barang')),
                ('keterangan', models.TextField(help_text=b'Tuliskan keterangan yang dianggap perlu yang ada hubungannya dengan barang yang bersangkutan', null=True, verbose_name=b'Keterangan', db_column=b'keterangan', blank=True)),
            ],
            options={
                'db_table': 'atl',
                'verbose_name': 'ATL',
                'verbose_name_plural': 'ATL',
            },
        ),
        migrations.CreateModel(
            name='FotoATL',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('foto', models.FileField(help_text=b'PERINGATAN: Hanya Foto Aset dan Hasil Scan File Dokumen Kepemilikan, Bukan Foto Pengguna Aset!!!', upload_to=b'atl/', verbose_name=b'Foto', db_column=b'foto')),
                ('tanggal', models.DateField(help_text=b'Tanggal Foto yang di Upload', null=True, verbose_name=b'Tanggal', db_column=b'tanggal', blank=True)),
                ('catatan', models.CharField(help_text=b'Catatan Mengenai File yang di Upload', max_length=200, verbose_name=b'Catatan', db_column=b'catatan')),
            ],
            options={
                'db_table': 'foto_atl',
                'verbose_name': 'Foto ATL',
                'verbose_name_plural': 'Foto ATL',
            },
        ),
        migrations.CreateModel(
            name='HargaATL',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('harga_bertambah', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Bertambah', max_digits=15, db_column=b'harga_bertambah')),
                ('harga_berkurang', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Berkurang', max_digits=15, db_column=b'harga_berkurang')),
                ('catatan', models.CharField(help_text=b'Catatan pada Daftar Pengadaan', max_length=250, verbose_name=b'Catatan', db_column=b'catatan')),
                ('id_asal_usul', models.ForeignKey(db_column=b'id_asal_usul', verbose_name=b'Asal Usul', to='umum.AsalUsul')),
            ],
            options={
                'db_table': 'harga_atl',
                'verbose_name': 'Harga ATL',
                'verbose_name_plural': 'Harga ATL',
            },
        ),
        migrations.CreateModel(
            name='KontrakATL',
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
                'db_table': 'kontrak_atl',
                'verbose_name': 'Kontrak ATL',
                'verbose_name_plural': 'Kontrak ATL',
            },
        ),
        migrations.CreateModel(
            name='PemanfaatanATL',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_atl', serialize=False, to='atl.ATL')),
                ('id_jenis_pemanfaatan', models.ForeignKey(db_column=b'id_jenis_pemanfaatan', verbose_name=b'Jenis Pemanfaatan', to='umum.JenisPemanfaatan')),
            ],
            options={
                'db_table': 'pemanfaatan_atl',
                'verbose_name': 'Pemanfaatan ATL',
                'verbose_name_plural': 'Pemanfaatan ATL',
            },
        ),
        migrations.CreateModel(
            name='PenghapusanATL',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_atl', serialize=False, to='atl.ATL')),
                ('id_sk_penghapusan', models.ForeignKey(db_column=b'id_sk_penghapusan', verbose_name=b'SK Penghapusan', to='umum.SKPenghapusan')),
            ],
            options={
                'db_table': 'penghapusan_atl',
                'verbose_name': 'Penghapusan ATL',
                'verbose_name_plural': 'Penghapusan ATL',
            },
        ),
        migrations.CreateModel(
            name='SKPDAsalATL',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_atl', serialize=False, to='atl.ATL')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_asal_atl',
                'verbose_name': 'SKPD Asal ATL',
                'verbose_name_plural': 'SKPD Asal ATL',
            },
        ),
        migrations.CreateModel(
            name='SKPDTujuanATL',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_atl', serialize=False, to='atl.ATL')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_tujuan_atl',
                'verbose_name': 'SKPD Tujuan ATL',
                'verbose_name_plural': 'SKPD Tujuan ATL',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangATL',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_atl', serialize=False, to='atl.ATL')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_atl',
                'verbose_name': 'Tahun Berkurang ATL',
                'verbose_name_plural': 'Tahun Berkurang ATL',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATL',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_atl', serialize=False, to='atl.ATL')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun', null=True)),
            ],
            options={
                'db_table': 'tahun_berkurang_usul_hapus_atl',
                'verbose_name': 'Tahun Berkurang Usul Hapus ATL',
                'verbose_name_plural': 'Tahun Berkurang Usul Hapus ATL',
            },
        ),
        migrations.AddField(
            model_name='hargaatl',
            name='id_atl',
            field=models.ForeignKey(db_column=b'id_atl', verbose_name=b'ATL', to='atl.ATL'),
        ),
        migrations.AddField(
            model_name='hargaatl',
            name='id_kontrak_atl',
            field=models.ForeignKey(db_column=b'id_kontrak_atl', verbose_name=b'Kontrak ATL', to='atl.KontrakATL'),
        ),
        migrations.AddField(
            model_name='hargaatl',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun', to='umum.Tahun', help_text=b'Tahun Anggaran'),
        ),
        migrations.AddField(
            model_name='hargaatl',
            name='tahun_mutasi',
            field=models.ForeignKey(related_name='+', db_column=b'tahun_mutasi', to='umum.Tahun', blank=True, help_text=b'Tahun Mutasi', null=True, verbose_name=b'Tahun Mutasi'),
        ),
        migrations.AddField(
            model_name='fotoatl',
            name='id_atl',
            field=models.ForeignKey(db_column=b'id_atl', verbose_name=b'ATL', to='atl.ATL'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_golongan_barang',
            field=models.ForeignKey(db_column=b'id_golongan_barang', default=5, verbose_name=b'Golongan Barang', to='umum.GolonganBarang'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_keadaan_barang',
            field=models.ForeignKey(db_column=b'id_keadaan_barang', default=1, verbose_name=b'Keadaan Barang', to='umum.KeadaanBarang'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_kode_barang',
            field=models.ForeignKey(db_column=b'id_kode_barang', verbose_name=b'Kode Barang', to='umum.KodeBarang'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_mutasi_berkurang',
            field=models.ForeignKey(db_column=b'id_mutasi_berkurang', default=5, verbose_name=b'Mutasi Berkurang', to='umum.MutasiBerkurang'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_ruangan',
            field=models.ForeignKey(db_column=b'id_ruangan', verbose_name=b'Ruangan', to='gedungbangunan.Ruangan'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_satuan_barang',
            field=models.ForeignKey(db_column=b'id_satuan_barang', verbose_name=b'Satuan Barang', to='umum.SatuanBarang'),
        ),
        migrations.AddField(
            model_name='atl',
            name='id_sub_skpd',
            field=models.ForeignKey(db_column=b'id_sub_skpd', verbose_name=b'SUB SKPD', to='umum.SUBSKPD'),
        ),
        migrations.AddField(
            model_name='atl',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun Awal', to='umum.Tahun', help_text=b'Tahun Awal Kapitalisasi'),
        ),
        migrations.CreateModel(
            name='ATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 ATL Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 ATL BAPPEDA',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 ATL Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 ATL Batu Piring',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 ATL BKD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 ATL BKPPD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 ATL BPBD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 ATL BPPD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Kantor',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Lokbatu',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Paringin Selatan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Pirsus',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes RSUD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Tanah Habang',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Tebing Tinggi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 ATL Dinkes Uren',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Kantor',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Paringin Selatan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 1 Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 1 Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 1 Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 1 Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 1 Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 1 Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 2 Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 2 Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 2 Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 2 Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 2 Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 2 Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 3 Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 3 Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 3 Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 3 Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 4 Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 4 Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 4 Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 4 Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 5 Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik SMPN 5 Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 ATL Disdik Tebing Tinggi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 ATL Dishub',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 ATL Disnakertrans',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 ATL Distamben',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 ATL DKO',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 ATL DKP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 ATL DKUKMP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 ATL DLH',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 ATL DPKP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 ATL DPMD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 ATL DPMPTSP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 ATL DPPKB',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 ATL DPPPA',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 ATL DPUPR',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 ATL DukCatPil',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 ATL Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 ATL Inspektorat',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 ATL Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 ATL Kearsipan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 ATL Kehutanan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 ATL KESBANGPOL',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 ATL Kominfo',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 ATL Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 ATL Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 ATL Paringin Kota',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 ATL Paringin Selatan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 ATL Paringin Timur',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 ATL Pariwisata',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPemanfaatan',
            fields=[
            ],
            options={
                'verbose_name': 'ATL Pemanfaatan',
                'proxy': True,
                'verbose_name_plural': 'ATL Pemanfaatan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusan',
            fields=[
            ],
            options={
                'verbose_name': 'ATL Penghapusan',
                'proxy': True,
                'verbose_name_plural': 'ATL Penghapusan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 ATL Penghapusan Awayan',
                'proxy': True,
                'verbose_name_plural': '34 ATL Penghapusan Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 ATL Penghapusan BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 ATL Penghapusan BAPPEDA',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 ATL Penghapusan Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 ATL Penghapusan Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 ATL Penghapusan Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 ATL Penghapusan Batu Piring',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 ATL Penghapusan BKD',
                'proxy': True,
                'verbose_name_plural': '19 ATL Penghapusan BKD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 ATL Penghapusan BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 ATL Penghapusan BKPPD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 ATL Penghapusan BPBD',
                'proxy': True,
                'verbose_name_plural': '39 ATL Penghapusan BPBD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 ATL Penghapusan BPPD',
                'proxy': True,
                'verbose_name_plural': '48 ATL Penghapusan BPPD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Penghapusan Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 ATL Penghapusan Dinkes',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Penghapusan Disdik',
                'proxy': True,
                'verbose_name_plural': '07 ATL Penghapusan Disdik',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 ATL Penghapusan Dishub',
                'proxy': True,
                'verbose_name_plural': '04 ATL Penghapusan Dishub',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 ATL Penghapusan Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 ATL Penghapusan Disnakertrans',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 ATL Penghapusan Distamben',
                'proxy': True,
                'verbose_name_plural': '17 ATL Penghapusan Distamben',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 ATL Penghapusan DKO',
                'proxy': True,
                'verbose_name_plural': '23 ATL Penghapusan DKO',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 ATL Penghapusan DKP',
                'proxy': True,
                'verbose_name_plural': '15 ATL Penghapusan DKP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 ATL Penghapusan DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 ATL Penghapusan DKUKMP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 ATL Penghapusan DLH',
                'proxy': True,
                'verbose_name_plural': '22 ATL Penghapusan DLH',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 ATL Penghapusan DPKP',
                'proxy': True,
                'verbose_name_plural': '40 ATL Penghapusan DPKP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 ATL Penghapusan DPMD',
                'proxy': True,
                'verbose_name_plural': '10 ATL Penghapusan DPMD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 ATL Penghapusan DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 ATL Penghapusan DPMPTSP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 ATL Penghapusan DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 ATL Penghapusan DPPKB',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 ATL Penghapusan DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 ATL Penghapusan DPPPA',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 ATL Penghapusan DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 ATL Penghapusan DPUPR',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 ATL Penghapusan DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 ATL Penghapusan DukCatPil',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 ATL Penghapusan Halong',
                'proxy': True,
                'verbose_name_plural': '35 ATL Penghapusan Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 ATL Penghapusan Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 ATL Penghapusan Inspektorat',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 ATL Penghapusan Juai',
                'proxy': True,
                'verbose_name_plural': '33 ATL Penghapusan Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 ATL Penghapusan Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 ATL Penghapusan Kearsipan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 ATL Penghapusan Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 ATL Penghapusan Kehutanan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 ATL Penghapusan KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 ATL Penghapusan KESBANGPOL',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 ATL Penghapusan Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 ATL Penghapusan Kominfo',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 ATL Penghapusan Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 ATL Penghapusan Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 ATL Penghapusan Paringin',
                'proxy': True,
                'verbose_name_plural': '28 ATL Penghapusan Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 ATL Penghapusan Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 ATL Penghapusan Paringin Kota',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 ATL Penghapusan Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 ATL Penghapusan Paringin Selatan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 ATL Penghapusan Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 ATL Penghapusan Paringin Timur',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 ATL Penghapusan Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 ATL Penghapusan Pariwisata',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 ATL Penghapusan Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 ATL Penghapusan Perdagangan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 ATL Penghapusan Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 ATL Penghapusan Perikanan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 ATL Penghapusan Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 ATL Penghapusan Perpustakaan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 ATL Penghapusan Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 ATL Penghapusan Pertanian',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 ATL Penghapusan RSUD',
                'proxy': True,
                'verbose_name_plural': '06 ATL Penghapusan RSUD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 ATL Penghapusan SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 ATL Penghapusan SATPOLPP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 ATL Penghapusan Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 ATL Penghapusan Sekretariat Korpri',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 ATL Penghapusan Setda',
                'proxy': True,
                'verbose_name_plural': '02 ATL Penghapusan Setda',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 ATL Penghapusan Setwan',
                'proxy': True,
                'verbose_name_plural': '01 ATL Penghapusan Setwan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 ATL Penghapusan Sosial',
                'proxy': True,
                'verbose_name_plural': '09 ATL Penghapusan Sosial',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPenghapusanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 ATL Penghapusan Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 ATL Penghapusan Tebing Tinggi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 ATL Perdagangan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 ATL Perikanan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 ATL Perpustakaan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 ATL Pertanian',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLReklas',
            fields=[
            ],
            options={
                'verbose_name': 'ATL Reklas',
                'proxy': True,
                'verbose_name_plural': 'ATL Reklas',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 ATL RSUD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 ATL SATPOLPP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 ATL Sekretariat Korpri',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 ATL Setda',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 ATL Setwan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 ATL Sosial',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 ATL Tebing Tinggi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapus',
            fields=[
            ],
            options={
                'verbose_name': 'ATL Usul Hapus',
                'proxy': True,
                'verbose_name_plural': 'ATL Usul Hapus',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 ATL Usul Hapus Awayan',
                'proxy': True,
                'verbose_name_plural': '34 ATL Usul Hapus Awayan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 ATL Usul Hapus BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 ATL Usul Hapus BAPPEDA',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 ATL Usul Hapus Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 ATL Usul Hapus Batumandi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 ATL Usul Hapus Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 ATL Usul Hapus Batu Piring',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 ATL Usul Hapus BKD',
                'proxy': True,
                'verbose_name_plural': '19 ATL Usul Hapus BKD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 ATL Usul Hapus BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 ATL Usul Hapus BKPPD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 ATL Usul Hapus BPBD',
                'proxy': True,
                'verbose_name_plural': '39 ATL Usul Hapus BPBD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 ATL Usul Hapus BPPD',
                'proxy': True,
                'verbose_name_plural': '48 ATL Usul Hapus BPPD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 ATL Usul Hapus Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 ATL Usul Hapus Dinkes',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 ATL Usul Hapus Disdik',
                'proxy': True,
                'verbose_name_plural': '07 ATL Usul Hapus Disdik',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 ATL Usul Hapus Dishub',
                'proxy': True,
                'verbose_name_plural': '04 ATL Usul Hapus Dishub',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 ATL Usul Hapus Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 ATL Usul Hapus Disnakertrans',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 ATL Usul Hapus Distamben',
                'proxy': True,
                'verbose_name_plural': '17 ATL Usul Hapus Distamben',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 ATL Usul Hapus DKO',
                'proxy': True,
                'verbose_name_plural': '23 ATL Usul Hapus DKO',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 ATL Usul Hapus DKP',
                'proxy': True,
                'verbose_name_plural': '15 ATL Usul Hapus DKP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 ATL Usul Hapus DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 ATL Usul Hapus DKUKMP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 ATL Usul Hapus DLH',
                'proxy': True,
                'verbose_name_plural': '22 ATL Usul Hapus DLH',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 ATL Usul Hapus DPKP',
                'proxy': True,
                'verbose_name_plural': '40 ATL Usul Hapus DPKP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 ATL Usul Hapus DPMD',
                'proxy': True,
                'verbose_name_plural': '10 ATL Usul Hapus DPMD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 ATL Usul Hapus DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 ATL Usul Hapus DPMPTSP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 ATL Usul Hapus DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 ATL Usul Hapus DPPKB',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 ATL Usul Hapus DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 ATL Usul Hapus DPPPA',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 ATL Usul Hapus DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 ATL Usul Hapus DPUPR',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 ATL Usul Hapus DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 ATL Usul Hapus DukCatPil',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 ATL Usul Hapus Halong',
                'proxy': True,
                'verbose_name_plural': '35 ATL Usul Hapus Halong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 ATL Usul Hapus Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 ATL Usul Hapus Inspektorat',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 ATL Usul Hapus Juai',
                'proxy': True,
                'verbose_name_plural': '33 ATL Usul Hapus Juai',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 ATL Usul Hapus Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 ATL Usul Hapus Kearsipan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 ATL Usul Hapus Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 ATL Usul Hapus Kehutanan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 ATL Usul Hapus KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 ATL Usul Hapus KESBANGPOL',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 ATL Usul Hapus Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 ATL Usul Hapus Kominfo',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 ATL Usul Hapus Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 ATL Usul Hapus Lampihong',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 ATL Usul Hapus Paringin',
                'proxy': True,
                'verbose_name_plural': '28 ATL Usul Hapus Paringin',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 ATL Usul Hapus Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 ATL Usul Hapus Paringin Kota',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 ATL Usul Hapus Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 ATL Usul Hapus Paringin Selatan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 ATL Usul Hapus Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 ATL Usul Hapus Paringin Timur',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 ATL Usul Hapus Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 ATL Usul Hapus Pariwisata',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 ATL Usul Hapus Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 ATL Usul Hapus Perdagangan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 ATL Usul Hapus Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 ATL Usul Hapus Perikanan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 ATL Usul Hapus Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 ATL Usul Hapus Perpustakaan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 ATL Usul Hapus Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 ATL Usul Hapus Pertanian',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 ATL Usul Hapus RSUD',
                'proxy': True,
                'verbose_name_plural': '06 ATL Usul Hapus RSUD',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 ATL Usul Hapus SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 ATL Usul Hapus SATPOLPP',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 ATL Usul Hapus Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 ATL Usul Hapus Sekretariat Korpri',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 ATL Usul Hapus Setda',
                'proxy': True,
                'verbose_name_plural': '02 ATL Usul Hapus Setda',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 ATL Usul Hapus Setwan',
                'proxy': True,
                'verbose_name_plural': '01 ATL Usul Hapus Setwan',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 ATL Usul Hapus Sosial',
                'proxy': True,
                'verbose_name_plural': '09 ATL Usul Hapus Sosial',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='ATLUsulHapusTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 ATL Usul Hapus Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 ATL Usul Hapus Tebing Tinggi',
            },
            bases=('atl.atl',),
        ),
        migrations.CreateModel(
            name='FotoATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Foto ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Foto ATL Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Foto ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Foto ATL BAPPEDA',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Foto ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Foto ATL Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Foto ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Foto ATL Batu Piring',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Foto ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 Foto ATL BKD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Foto ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Foto ATL BKPPD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Foto ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Foto ATL BPBD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Foto ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Foto ATL BPPD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Juai',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Kantor',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Lampihong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Lokbatu',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Paringin Selatan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Pirsus',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes RSUD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Tanah Habang',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Tebing Tinggi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto ATL Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Foto ATL Dinkes Uren',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Juai',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Kantor',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Lampihong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Paringin Selatan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 1 Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 1 Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 1 Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 1 Juai',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 1 Lampihong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 1 Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 2 Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 2 Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 2 Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 2 Juai',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 2 Lampihong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 2 Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 3 Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 3 Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 3 Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 3 Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 4 Awayan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 4 Batumandi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 4 Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 4 Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 5 Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik SMPN 5 Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto ATL Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Foto ATL Disdik Tebing Tinggi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Foto ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Foto ATL Dishub',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Foto ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Foto ATL Disnakertrans',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Foto ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Foto ATL Distamben',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Foto ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 Foto ATL DKO',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Foto ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 Foto ATL DKP',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Foto ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Foto ATL DKUKMP',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Foto ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 Foto ATL DLH',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Foto ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Foto ATL DPKP',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Foto ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Foto ATL DPMD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Foto ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Foto ATL DPMPTSP',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Foto ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Foto ATL DPPKB',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Foto ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Foto ATL DPPPA',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Foto ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Foto ATL DPUPR',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Foto ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Foto ATL DukCatPil',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Foto ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 Foto ATL Halong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Foto ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Foto ATL Inspektorat',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Foto ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 Foto ATL Juai',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Foto ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Foto ATL Kearsipan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Foto ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Foto ATL Kehutanan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Foto ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Foto ATL KESBANGPOL',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Foto ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Foto ATL Kominfo',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Foto ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Foto ATL Lampihong',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Foto ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Foto ATL Paringin',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Foto ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Foto ATL Paringin Kota',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Foto ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Foto ATL Paringin Selatan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Foto ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Foto ATL Paringin Timur',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Foto ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Foto ATL Pariwisata',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Foto ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Foto ATL Perdagangan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Foto ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Foto ATL Perikanan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Foto ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Foto ATL Perpustakaan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Foto ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Foto ATL Pertanian',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Foto ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Foto ATL RSUD',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Foto ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Foto ATL SATPOLPP',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Foto ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Foto ATL Sekretariat Korpri',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Foto ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 Foto ATL Setda',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Foto ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Foto ATL Setwan',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Foto ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Foto ATL Sosial',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='FotoATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Foto ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Foto ATL Tebing Tinggi',
            },
            bases=('atl.fotoatl',),
        ),
        migrations.CreateModel(
            name='HargaATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Harga ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Harga ATL Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Harga ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Harga ATL BAPPEDA',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Harga ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Harga ATL Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Harga ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Harga ATL Batu Piring',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Harga ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 Harga ATL BKD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Harga ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Harga ATL BKPPD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Harga ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Harga ATL BPBD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Harga ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Harga ATL BPPD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Juai',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Kantor',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Lampihong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Lokbatu',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Paringin Selatan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Pirsus',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes RSUD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Tanah Habang',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Tebing Tinggi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga ATL Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Harga ATL Dinkes Uren',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Juai',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Kantor',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Lampihong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Paringin Selatan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 1 Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 1 Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 1 Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 1 Juai',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 1 Lampihong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 1 Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 2 Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 2 Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 2 Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 2 Juai',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 2 Lampihong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 2 Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 3 Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 3 Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 3 Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 3 Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 4 Awayan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 4 Batumandi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 4 Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 4 Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 5 Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik SMPN 5 Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga ATL Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Harga ATL Disdik Tebing Tinggi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Harga ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Harga ATL Dishub',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Harga ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Harga ATL Disnakertrans',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Harga ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Harga ATL Distamben',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Harga ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 Harga ATL DKO',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Harga ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 Harga ATL DKP',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Harga ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Harga ATL DKUKMP',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Harga ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 Harga ATL DLH',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Harga ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Harga ATL DPKP',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Harga ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Harga ATL DPMD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Harga ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Harga ATL DPMPTSP',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Harga ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Harga ATL DPPKB',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Harga ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Harga ATL DPPPA',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Harga ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Harga ATL DPUPR',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Harga ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Harga ATL DukCatPil',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Harga ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 Harga ATL Halong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Harga ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Harga ATL Inspektorat',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Harga ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 Harga ATL Juai',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Harga ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Harga ATL Kearsipan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Harga ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Harga ATL Kehutanan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Harga ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Harga ATL KESBANGPOL',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Harga ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Harga ATL Kominfo',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Harga ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Harga ATL Lampihong',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Harga ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Harga ATL Paringin',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Harga ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Harga ATL Paringin Kota',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Harga ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Harga ATL Paringin Selatan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Harga ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Harga ATL Paringin Timur',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Harga ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Harga ATL Pariwisata',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Harga ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Harga ATL Perdagangan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Harga ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Harga ATL Perikanan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Harga ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Harga ATL Perpustakaan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Harga ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Harga ATL Pertanian',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Harga ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Harga ATL RSUD',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Harga ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Harga ATL SATPOLPP',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Harga ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Harga ATL Sekretariat Korpri',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Harga ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 Harga ATL Setda',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Harga ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Harga ATL Setwan',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Harga ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Harga ATL Sosial',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='HargaATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Harga ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Harga ATL Tebing Tinggi',
            },
            bases=('atl.hargaatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Kontrak ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Kontrak ATL Awayan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Kontrak ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Kontrak ATL BAPPEDA',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Kontrak ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Kontrak ATL Batumandi',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Kontrak ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Kontrak ATL Batu Piring',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Kontrak ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 Kontrak ATL BKD',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Kontrak ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Kontrak ATL BKPPD',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Kontrak ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Kontrak ATL BPBD',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Kontrak ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Kontrak ATL BPPD',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Kontrak ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Kontrak ATL Dinkes',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Kontrak ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Kontrak ATL Disdik',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Kontrak ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Kontrak ATL Dishub',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Kontrak ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Kontrak ATL Disnakertrans',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Kontrak ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Kontrak ATL Distamben',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Kontrak ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 Kontrak ATL DKO',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Kontrak ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 Kontrak ATL DKP',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Kontrak ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Kontrak ATL DKUKMP',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Kontrak ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 Kontrak ATL DLH',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Kontrak ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Kontrak ATL DPKP',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Kontrak ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Kontrak ATL DPMD',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Kontrak ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Kontrak ATL DPMPTSP',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Kontrak ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Kontrak ATL DPPKB',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Kontrak ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Kontrak ATL DPPPA',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Kontrak ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Kontrak ATL DPUPR',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Kontrak ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Kontrak ATL DukCatPil',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Kontrak ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 Kontrak ATL Halong',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Kontrak ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Kontrak ATL Inspektorat',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Kontrak ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 Kontrak ATL Juai',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Kontrak ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Kontrak ATL Kearsipan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Kontrak ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Kontrak ATL Kehutanan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Kontrak ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Kontrak ATL KESBANGPOL',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Kontrak ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Kontrak ATL Kominfo',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Kontrak ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Kontrak ATL Lampihong',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Kontrak ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Kontrak ATL Paringin',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Kontrak ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Kontrak ATL Paringin Kota',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Kontrak ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Kontrak ATL Paringin Selatan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Kontrak ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Kontrak ATL Paringin Timur',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Kontrak ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Kontrak ATL Pariwisata',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Kontrak ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Kontrak ATL Perdagangan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Kontrak ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Kontrak ATL Perikanan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Kontrak ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Kontrak ATL Perpustakaan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Kontrak ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Kontrak ATL Pertanian',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Kontrak ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Kontrak ATL RSUD',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Kontrak ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Kontrak ATL SATPOLPP',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Kontrak ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Kontrak ATL Sekretariat Korpri',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Kontrak ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 Kontrak ATL Setda',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Kontrak ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Kontrak ATL Setwan',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Kontrak ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Kontrak ATL Sosial',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='KontrakATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Kontrak ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Kontrak ATL Tebing Tinggi',
            },
            bases=('atl.kontrakatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Penghapusan ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Penghapusan ATL Awayan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Penghapusan ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Penghapusan ATL BAPPEDA',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Penghapusan ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Penghapusan ATL Batumandi',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Penghapusan ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Penghapusan ATL Batu Piring',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Penghapusan ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 Penghapusan ATL BKD',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Penghapusan ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Penghapusan ATL BKPPD',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Penghapusan ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Penghapusan ATL BPBD',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Penghapusan ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Penghapusan ATL BPPD',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Penghapusan ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Penghapusan ATL Dinkes',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Penghapusan ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Penghapusan ATL Disdik',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Penghapusan ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Penghapusan ATL Dishub',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Penghapusan ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Penghapusan ATL Disnakertrans',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Penghapusan ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Penghapusan ATL Distamben',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Penghapusan ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 Penghapusan ATL DKO',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Penghapusan ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 Penghapusan ATL DKP',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Penghapusan ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Penghapusan ATL DKUKMP',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Penghapusan ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 Penghapusan ATL DLH',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Penghapusan ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Penghapusan ATL DPKP',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Penghapusan ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Penghapusan ATL DPMD',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Penghapusan ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Penghapusan ATL DPMPTSP',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Penghapusan ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Penghapusan ATL DPPKB',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Penghapusan ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Penghapusan ATL DPPPA',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Penghapusan ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Penghapusan ATL DPUPR',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Penghapusan ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Penghapusan ATL DukCatPil',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Penghapusan ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 Penghapusan ATL Halong',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Penghapusan ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Penghapusan ATL Inspektorat',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Penghapusan ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 Penghapusan ATL Juai',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Penghapusan ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Penghapusan ATL Kearsipan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Penghapusan ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Penghapusan ATL Kehutanan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Penghapusan ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Penghapusan ATL KESBANGPOL',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Penghapusan ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Penghapusan ATL Kominfo',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Penghapusan ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Penghapusan ATL Lampihong',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Penghapusan ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Penghapusan ATL Paringin',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Penghapusan ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Penghapusan ATL Paringin Kota',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Penghapusan ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Penghapusan ATL Paringin Selatan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Penghapusan ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Penghapusan ATL Paringin Timur',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Penghapusan ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Penghapusan ATL Pariwisata',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Penghapusan ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Penghapusan ATL Perdagangan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Penghapusan ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Penghapusan ATL Perikanan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Penghapusan ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Penghapusan ATL Perpustakaan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Penghapusan ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Penghapusan ATL Pertanian',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Penghapusan ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Penghapusan ATL RSUD',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Penghapusan ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Penghapusan ATL SATPOLPP',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Penghapusan ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Penghapusan ATL Sekretariat Korpri',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Penghapusan ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 Penghapusan ATL Setda',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Penghapusan ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Penghapusan ATL Setwan',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Penghapusan ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Penghapusan ATL Sosial',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='PenghapusanATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Penghapusan ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Penghapusan ATL Tebing Tinggi',
            },
            bases=('atl.penghapusanatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Asal ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Asal ATL Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Asal ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Asal ATL BAPPEDA',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Asal ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Asal ATL Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Asal ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Asal ATL Batu Piring',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Asal ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Asal ATL BKD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Asal ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Asal ATL BKPPD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Asal ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Asal ATL BPBD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Asal ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Asal ATL BPPD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Juai',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Kantor',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Lampihong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Lokbatu',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Paringin Selatan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Pirsus',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes RSUD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Tanah Habang',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Tebing Tinggi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal ATL Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal ATL Dinkes Uren',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Juai',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Kantor',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Lampihong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Paringin Selatan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 1 Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 1 Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 1 Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 1 Juai',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 1 Lampihong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 1 Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 2 Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 2 Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 2 Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 2 Juai',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 2 Lampihong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 2 Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 3 Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 3 Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 3 Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 3 Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 4 Awayan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 4 Batumandi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 4 Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 4 Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 5 Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik SMPN 5 Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal ATL Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal ATL Disdik Tebing Tinggi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Asal ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Asal ATL Dishub',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Asal ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Asal ATL Disnakertrans',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Asal ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Asal ATL Distamben',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Asal ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Asal ATL DKO',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Asal ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Asal ATL DKP',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Asal ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Asal ATL DKUKMP',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Asal ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Asal ATL DLH',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Asal ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Asal ATL DPKP',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Asal ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Asal ATL DPMD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Asal ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Asal ATL DPMPTSP',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Asal ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Asal ATL DPPKB',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Asal ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Asal ATL DPPPA',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Asal ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Asal ATL DPUPR',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Asal ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Asal ATL DukCatPil',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Asal ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Asal ATL Halong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Asal ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Asal ATL Inspektorat',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Asal ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Asal ATL Juai',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Asal ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Asal ATL Kearsipan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Asal ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Asal ATL Kehutanan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Asal ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Asal ATL KESBANGPOL',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Asal ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Asal ATL Kominfo',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Asal ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Asal ATL Lampihong',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Asal ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Asal ATL Paringin',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Asal ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Asal ATL Paringin Kota',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Asal ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Asal ATL Paringin Selatan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Asal ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Asal ATL Paringin Timur',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Asal ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Asal ATL Pariwisata',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Asal ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Asal ATL Perdagangan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Asal ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Asal ATL Perikanan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Asal ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Asal ATL Perpustakaan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Asal ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Asal ATL Pertanian',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Asal ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Asal ATL RSUD',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Asal ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Asal ATL SATPOLPP',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Asal ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Asal ATL Sekretariat Korpri',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Asal ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Asal ATL Setda',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Asal ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Asal ATL Setwan',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Asal ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Asal ATL Sosial',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDAsalATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Asal ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Asal ATL Tebing Tinggi',
            },
            bases=('atl.skpdasalatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Tujuan ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Tujuan ATL Awayan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Tujuan ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Tujuan ATL BAPPEDA',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Tujuan ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Tujuan ATL Batumandi',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Tujuan ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Tujuan ATL Batu Piring',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Tujuan ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Tujuan ATL BKD',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Tujuan ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Tujuan ATL BKPPD',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Tujuan ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Tujuan ATL BPBD',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Tujuan ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Tujuan ATL BPPD',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Tujuan ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Tujuan ATL Dinkes',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Tujuan ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Tujuan ATL Disdik',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Tujuan ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Tujuan ATL Dishub',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Tujuan ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Tujuan ATL Disnakertrans',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Tujuan ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Tujuan ATL Distamben',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Tujuan ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Tujuan ATL DKO',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Tujuan ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Tujuan ATL DKP',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Tujuan ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Tujuan ATL DKUKMP',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Tujuan ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Tujuan ATL DLH',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Tujuan ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Tujuan ATL DPKP',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Tujuan ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Tujuan ATL DPMD',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Tujuan ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Tujuan ATL DPMPTSP',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Tujuan ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Tujuan ATL DPPKB',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Tujuan ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Tujuan ATL DPPPA',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Tujuan ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Tujuan ATL DPUPR',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Tujuan ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Tujuan ATL DukCatPil',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Tujuan ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Tujuan ATL Halong',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Tujuan ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Tujuan ATL Inspektorat',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Tujuan ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Tujuan ATL Juai',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Tujuan ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Tujuan ATL Kearsipan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Tujuan ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Tujuan ATL Kehutanan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Tujuan ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Tujuan ATL KESBANGPOL',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Tujuan ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Tujuan ATL Kominfo',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Tujuan ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Tujuan ATL Lampihong',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Tujuan ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Tujuan ATL Paringin',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Tujuan ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Tujuan ATL Paringin Kota',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Tujuan ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Tujuan ATL Paringin Selatan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Tujuan ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Tujuan ATL Paringin Timur',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Tujuan ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Tujuan ATL Pariwisata',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Tujuan ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Tujuan ATL Perdagangan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Tujuan ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Tujuan ATL Perikanan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Tujuan ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Tujuan ATL Perpustakaan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Tujuan ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Tujuan ATL Pertanian',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Tujuan ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Tujuan ATL RSUD',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Tujuan ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Tujuan ATL SATPOLPP',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Tujuan ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Tujuan ATL Sekretariat Korpri',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Tujuan ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Tujuan ATL Setda',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Tujuan ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Tujuan ATL Setwan',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Tujuan ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Tujuan ATL Sosial',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Tujuan ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Tujuan ATL Tebing Tinggi',
            },
            bases=('atl.skpdtujuanatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tahun Berkurang ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tahun Berkurang ATL Awayan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tahun Berkurang ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tahun Berkurang ATL BAPPEDA',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tahun Berkurang ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tahun Berkurang ATL Batumandi',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tahun Berkurang ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tahun Berkurang ATL Batu Piring',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tahun Berkurang ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tahun Berkurang ATL BKD',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tahun Berkurang ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tahun Berkurang ATL BKPPD',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tahun Berkurang ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tahun Berkurang ATL BPBD',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tahun Berkurang ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tahun Berkurang ATL BPPD',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tahun Berkurang ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tahun Berkurang ATL Dinkes',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tahun Berkurang ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tahun Berkurang ATL Disdik',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tahun Berkurang ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tahun Berkurang ATL Dishub',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tahun Berkurang ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tahun Berkurang ATL Disnakertrans',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tahun Berkurang ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tahun Berkurang ATL Distamben',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tahun Berkurang ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tahun Berkurang ATL DKO',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tahun Berkurang ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tahun Berkurang ATL DKP',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tahun Berkurang ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tahun Berkurang ATL DKUKMP',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tahun Berkurang ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tahun Berkurang ATL DLH',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tahun Berkurang ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tahun Berkurang ATL DPKP',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tahun Berkurang ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tahun Berkurang ATL DPMD',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tahun Berkurang ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tahun Berkurang ATL DPMPTSP',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tahun Berkurang ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tahun Berkurang ATL DPPKB',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tahun Berkurang ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tahun Berkurang ATL DPPPA',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tahun Berkurang ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tahun Berkurang ATL DPUPR',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tahun Berkurang ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tahun Berkurang ATL DukCatPil',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tahun Berkurang ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tahun Berkurang ATL Halong',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tahun Berkurang ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tahun Berkurang ATL Inspektorat',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tahun Berkurang ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tahun Berkurang ATL Juai',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tahun Berkurang ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tahun Berkurang ATL Kearsipan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tahun Berkurang ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tahun Berkurang ATL Kehutanan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tahun Berkurang ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tahun Berkurang ATL KESBANGPOL',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tahun Berkurang ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tahun Berkurang ATL Kominfo',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tahun Berkurang ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tahun Berkurang ATL Lampihong',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tahun Berkurang ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tahun Berkurang ATL Paringin',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tahun Berkurang ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tahun Berkurang ATL Paringin Kota',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tahun Berkurang ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tahun Berkurang ATL Paringin Selatan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tahun Berkurang ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tahun Berkurang ATL Paringin Timur',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tahun Berkurang ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tahun Berkurang ATL Pariwisata',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tahun Berkurang ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tahun Berkurang ATL Perdagangan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tahun Berkurang ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tahun Berkurang ATL Perikanan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tahun Berkurang ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tahun Berkurang ATL Perpustakaan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tahun Berkurang ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tahun Berkurang ATL Pertanian',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tahun Berkurang ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tahun Berkurang ATL RSUD',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tahun Berkurang ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tahun Berkurang ATL SATPOLPP',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tahun Berkurang ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tahun Berkurang ATL Sekretariat Korpri',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tahun Berkurang ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tahun Berkurang ATL Setda',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tahun Berkurang ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tahun Berkurang ATL Setwan',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tahun Berkurang ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tahun Berkurang ATL Sosial',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tahun Berkurang ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tahun Berkurang ATL Tebing Tinggi',
            },
            bases=('atl.tahunberkurangatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Usul Hapus ATL Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Usul Hapus ATL Awayan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Usul Hapus ATL BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Usul Hapus ATL BAPPEDA',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Usul Hapus ATL Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Usul Hapus ATL Batumandi',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Usul Hapus ATL Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Usul Hapus ATL Batu Piring',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Usul Hapus ATL BKD',
                'proxy': True,
                'verbose_name_plural': '19 Usul Hapus ATL BKD',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Usul Hapus ATL BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Usul Hapus ATL BKPPD',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Usul Hapus ATL BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Usul Hapus ATL BPBD',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Usul Hapus ATL BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Usul Hapus ATL BPPD',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Usul Hapus ATL Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Usul Hapus ATL Dinkes',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Usul Hapus ATL Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Usul Hapus ATL Disdik',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Usul Hapus ATL Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Usul Hapus ATL Dishub',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Usul Hapus ATL Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Usul Hapus ATL Disnakertrans',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Usul Hapus ATL Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Usul Hapus ATL Distamben',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Usul Hapus ATL DKO',
                'proxy': True,
                'verbose_name_plural': '23 Usul Hapus ATL DKO',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Usul Hapus ATL DKP',
                'proxy': True,
                'verbose_name_plural': '15 Usul Hapus ATL DKP',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Usul Hapus ATL DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Usul Hapus ATL DKUKMP',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Usul Hapus ATL DLH',
                'proxy': True,
                'verbose_name_plural': '22 Usul Hapus ATL DLH',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Usul Hapus ATL DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Usul Hapus ATL DPKP',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Usul Hapus ATL DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Usul Hapus ATL DPMD',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Usul Hapus ATL DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Usul Hapus ATL DPMPTSP',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Usul Hapus ATL DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Usul Hapus ATL DPPKB',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Usul Hapus ATL DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Usul Hapus ATL DPPPA',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Usul Hapus ATL DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Usul Hapus ATL DPUPR',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Usul Hapus ATL DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Usul Hapus ATL DukCatPil',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Usul Hapus ATL Halong',
                'proxy': True,
                'verbose_name_plural': '35 Usul Hapus ATL Halong',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Usul Hapus ATL Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Usul Hapus ATL Inspektorat',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Usul Hapus ATL Juai',
                'proxy': True,
                'verbose_name_plural': '33 Usul Hapus ATL Juai',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Usul Hapus ATL Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Usul Hapus ATL Kearsipan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Usul Hapus ATL Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Usul Hapus ATL Kehutanan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Usul Hapus ATL KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Usul Hapus ATL KESBANGPOL',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Usul Hapus ATL Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Usul Hapus ATL Kominfo',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Usul Hapus ATL Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Usul Hapus ATL Lampihong',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Usul Hapus ATL Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Usul Hapus ATL Paringin',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Usul Hapus ATL Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Usul Hapus ATL Paringin Kota',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Usul Hapus ATL Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Usul Hapus ATL Paringin Selatan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Usul Hapus ATL Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Usul Hapus ATL Paringin Timur',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Usul Hapus ATL Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Usul Hapus ATL Pariwisata',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Usul Hapus ATL Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Usul Hapus ATL Perdagangan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Usul Hapus ATL Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Usul Hapus ATL Perikanan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Usul Hapus ATL Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Usul Hapus ATL Perpustakaan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Usul Hapus ATL Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Usul Hapus ATL Pertanian',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Usul Hapus ATL RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Usul Hapus ATL RSUD',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Usul Hapus ATL SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Usul Hapus ATL SATPOLPP',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Usul Hapus ATL Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Usul Hapus ATL Sekretariat Korpri',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Usul Hapus ATL Setda',
                'proxy': True,
                'verbose_name_plural': '02 Usul Hapus ATL Setda',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Usul Hapus ATL Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Usul Hapus ATL Setwan',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Usul Hapus ATL Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Usul Hapus ATL Sosial',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusATLTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Usul Hapus ATL Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Usul Hapus ATL Tebing Tinggi',
            },
            bases=('atl.tahunberkurangusulhapusatl',),
        ),
    ]
