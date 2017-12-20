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
            name='FotoPeralatanMesin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('foto', models.FileField(help_text=b'PERINGATAN: Hanya Foto Aset dan Hasil Scan File Dokumen Kepemilikan, Bukan Foto Pengguna Aset!!!', upload_to=b'peralatan_mesin/', verbose_name=b'Foto', db_column=b'foto')),
                ('tanggal', models.DateField(help_text=b'Tanggal Foto yang di Upload', null=True, verbose_name=b'Tanggal', db_column=b'tanggal', blank=True)),
                ('catatan', models.CharField(help_text=b'Catatan Mengenai File yang di Upload', max_length=200, verbose_name=b'Catatan', db_column=b'catatan')),
            ],
            options={
                'db_table': 'foto_peralatan_mesin',
                'verbose_name': 'Foto Peralatan Mesin',
                'verbose_name_plural': 'Foto Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('harga_bertambah', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Bertambah', max_digits=15, db_column=b'harga_bertambah')),
                ('harga_berkurang', models.DecimalField(default=0, decimal_places=0, verbose_name=b'Harga Berkurang', max_digits=15, db_column=b'harga_berkurang')),
                ('catatan', models.CharField(help_text=b'Catatan pada Daftar Pengadaan', max_length=250, verbose_name=b'Catatan', db_column=b'catatan')),
                ('id_asal_usul', models.ForeignKey(db_column=b'id_asal_usul', verbose_name=b'Asal Usul', to='umum.AsalUsul')),
            ],
            options={
                'db_table': 'harga_peralatan_mesin',
                'verbose_name': 'Harga Peralatan Mesin',
                'verbose_name_plural': 'Harga Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesin',
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
                'db_table': 'kontrak_peralatan_mesin',
                'verbose_name': 'Kontrak Peralatan Mesin',
                'verbose_name_plural': 'Kontrak Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='PeralatanMesin',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'Register', primary_key=True, db_column=b'id')),
                ('nama_barang', models.CharField(max_length=300, verbose_name=b'Nama Barang', db_column=b'nama_barang')),
                ('merk_type', models.CharField(max_length=150, null=True, verbose_name=b'Merk / Type', db_column=b'merk_type', blank=True)),
                ('ukuran_cc', models.CharField(max_length=100, null=True, verbose_name=b'Ukuran / CC', db_column=b'ukuran_cc', blank=True)),
                ('bahan', models.CharField(max_length=100, null=True, verbose_name=b'Bahan', db_column=b'bahan', blank=True)),
                ('nomor_pabrik', models.CharField(max_length=100, null=True, verbose_name=b'Nomor Pabrik', db_column=b'nomor_pabrik', blank=True)),
                ('nomor_rangka', models.CharField(max_length=100, verbose_name=b'Nomor Rangka', db_column=b'nomor_rangka')),
                ('nomor_mesin', models.CharField(max_length=100, verbose_name=b'Nomor Mesin', db_column=b'nomor_mesin')),
                ('nomor_polisi', models.CharField(max_length=100, verbose_name=b'Nomor Polisi', db_column=b'nomor_polisi')),
                ('nomor_bpkb', models.CharField(max_length=100, verbose_name=b'Nomor BPKB', db_column=b'nomor_bpkb')),
                ('banyak_barang', models.IntegerField(default=1, verbose_name=b'Banyak Barang', db_column=b'banyak_barang')),
                ('keterangan', models.TextField(null=True, verbose_name=b'Keterangan', db_column=b'keterangan', blank=True)),
            ],
            options={
                'db_table': 'peralatan_mesin',
                'verbose_name': 'Peralatan Mesin',
                'verbose_name_plural': 'Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='PemanfaatanPeralatanMesin',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_peralatan_mesin', serialize=False, to='peralatanmesin.PeralatanMesin')),
                ('id_jenis_pemanfaatan', models.ForeignKey(db_column=b'id_jenis_pemanfaatan', verbose_name=b'Jenis Pemanfaatan', to='umum.JenisPemanfaatan')),
            ],
            options={
                'db_table': 'pemanfaatan_peralatan_mesin',
                'verbose_name': 'Pemanfaatan Peralatan Mesin',
                'verbose_name_plural': 'Pemanfaatan Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesin',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_peralatan_mesin', serialize=False, to='peralatanmesin.PeralatanMesin')),
                ('id_sk_penghapusan', models.ForeignKey(db_column=b'id_sk_penghapusan', verbose_name=b'SK Penghapusan', to='umum.SKPenghapusan')),
            ],
            options={
                'db_table': 'penghapusan_peralatan_mesin',
                'verbose_name': 'Penghapusan Peralatan Mesin',
                'verbose_name_plural': 'Penghapusan Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesin',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_peralatan_mesin', serialize=False, to='peralatanmesin.PeralatanMesin')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_asal_peralatan_mesin',
                'verbose_name': 'SKPD Asal Peralatan Mesin',
                'verbose_name_plural': 'SKPD Asal Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesin',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_peralatan_mesin', serialize=False, to='peralatanmesin.PeralatanMesin')),
                ('id_skpd', models.ForeignKey(db_column=b'id_skpd', verbose_name=b'SKPD', to='umum.SKPD')),
            ],
            options={
                'db_table': 'skpd_tujuan_peralatan_mesin',
                'verbose_name': 'SKPD Tujuan Peralatan Mesin',
                'verbose_name_plural': 'SKPD Tujuan Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesin',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_peralatan_mesin', serialize=False, to='peralatanmesin.PeralatanMesin')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_peralatan_mesin',
                'verbose_name': 'Tahun Berkurang Peralatan Mesin',
                'verbose_name_plural': 'Tahun Berkurang Peralatan Mesin',
            },
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesin',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id_peralatan_mesin', serialize=False, to='peralatanmesin.PeralatanMesin')),
                ('tahun_berkurang', models.ForeignKey(db_column=b'tahun_berkurang', verbose_name=b'Tahun Berkurang', to='umum.Tahun')),
            ],
            options={
                'db_table': 'tahun_berkurang_usul_hapus_pm',
                'verbose_name': 'Tahun Berkurang Usul Hapus PM',
                'verbose_name_plural': 'Tahun Berkurang Usul Hapus PM',
            },
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_golongan_barang',
            field=models.ForeignKey(db_column=b'id_golongan_barang', default=2, verbose_name=b'Golongan Barang', to='umum.GolonganBarang'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_keadaan_barang',
            field=models.ForeignKey(db_column=b'id_keadaan_barang', default=1, verbose_name=b'Keadaan Barang', to='umum.KeadaanBarang'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_kode_barang',
            field=models.ForeignKey(db_column=b'id_kode_barang', verbose_name=b'Kode Barang', to='umum.KodeBarang'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_mutasi_berkurang',
            field=models.ForeignKey(db_column=b'id_mutasi_berkurang', default=5, verbose_name=b'Mutasi Berkurang', to='umum.MutasiBerkurang'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_ruangan',
            field=models.ForeignKey(db_column=b'id_ruangan', verbose_name=b'Ruangan', to='gedungbangunan.Ruangan'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_satuan_barang',
            field=models.ForeignKey(db_column=b'id_satuan_barang', verbose_name=b'Satuan Barang', to='umum.SatuanBarang'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='id_sub_skpd',
            field=models.ForeignKey(db_column=b'id_sub_skpd', verbose_name=b'SUB SKPD', to='umum.SUBSKPD'),
        ),
        migrations.AddField(
            model_name='peralatanmesin',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun Awal', to='umum.Tahun', help_text=b'Tahun Awal Kapitalisasi'),
        ),
        migrations.AddField(
            model_name='hargaperalatanmesin',
            name='id_kontrak_peralatan_mesin',
            field=models.ForeignKey(db_column=b'id_kontrak_peralatan_mesin', verbose_name=b'Kontrak Peralatan Mesin', to='peralatanmesin.KontrakPeralatanMesin'),
        ),
        migrations.AddField(
            model_name='hargaperalatanmesin',
            name='id_peralatan_mesin',
            field=models.ForeignKey(db_column=b'id_peralatan_mesin', verbose_name=b'Peralatan Mesin', to='peralatanmesin.PeralatanMesin'),
        ),
        migrations.AddField(
            model_name='hargaperalatanmesin',
            name='tahun',
            field=models.ForeignKey(db_column=b'tahun', verbose_name=b'Tahun', to='umum.Tahun', help_text=b'Tahun Anggaran'),
        ),
        migrations.AddField(
            model_name='hargaperalatanmesin',
            name='tahun_mutasi',
            field=models.ForeignKey(related_name='+', db_column=b'tahun_mutasi', to='umum.Tahun', blank=True, help_text=b'Tahun Mutasi', null=True, verbose_name=b'Tahun Mutasi'),
        ),
        migrations.AddField(
            model_name='fotoperalatanmesin',
            name='id_peralatan_mesin',
            field=models.ForeignKey(db_column=b'id_peralatan_mesin', verbose_name=b'Peralatan Mesin', to='peralatanmesin.PeralatanMesin'),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Foto PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Foto PM Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Foto PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Foto PM BAPPEDA',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Foto PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Foto PM Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Foto PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Foto PM Batu Piring',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Foto PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 Foto PM BKD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Foto PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Foto PM BKPPD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Foto PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Foto PM BPBD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Foto PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Foto PM BPPD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Juai',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Kantor',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Lampihong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Lokbatu',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Paringin Selatan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Pirsus',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes RSUD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Tanah Habang',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Tebing Tinggi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Foto PM Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Foto PM Dinkes Uren',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Juai',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Kantor',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Lampihong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Paringin Selatan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 1 Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 1 Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 1 Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 1 Juai',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 1 Lampihong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 1 Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 2 Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 2 Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 2 Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 2 Juai',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 2 Lampihong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 2 Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 3 Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 3 Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 3 Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 3 Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 4 Awayan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 4 Batumandi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 4 Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 4 Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 5 Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik SMPN 5 Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Foto PM Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Foto PM Disdik Tebing Tinggi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Foto PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Foto PM Dishub',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Foto PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Foto PM Disnakertrans',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Foto PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Foto PM Distamben',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Foto PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 Foto PM DKO',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Foto PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 Foto PM DKP',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Foto PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Foto PM DKUKMP',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Foto PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 Foto PM DLH',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Foto PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Foto PM DPKP',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Foto PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Foto PM DPMD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Foto PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Foto PM DPMPTSP',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Foto PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Foto PM DPPKB',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Foto PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Foto PM DPPPA',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Foto PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Foto PM DPUPR',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Foto PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Foto PM DukCatPil',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Foto PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 Foto PM Halong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Foto PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Foto PM Inspektorat',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Foto PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 Foto PM Juai',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Foto PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Foto PM Kearsipan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Foto PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Foto PM Kehutanan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Foto PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Foto PM KESBANGPOL',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Foto PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Foto PM Kominfo',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Foto PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Foto PM Lampihong',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Foto PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Foto PM Paringin',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Foto PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Foto PM Paringin Kota',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Foto PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Foto PM Paringin Selatan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Foto PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Foto PM Paringin Timur',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Foto PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Foto PM Pariwisata',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Foto PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Foto PM Perdagangan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Foto PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Foto PM Perikanan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Foto PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Foto PM Perpustakaan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Foto PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Foto PM Pertanian',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Foto PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Foto PM RSUD',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Foto PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Foto PM SATPOLPP',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Foto PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Foto PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Foto PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 Foto PM Setda',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Foto PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Foto PM Setwan',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Foto PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Foto PM Sosial',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='FotoPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Foto PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Foto PM Tebing Tinggi',
            },
            bases=('peralatanmesin.fotoperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Harga PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Harga PM Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Harga PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Harga PM BAPPEDA',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Harga PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Harga PM Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Harga PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Harga PM Batu Piring',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Harga PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 Harga PM BKD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Harga PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Harga PM BKPPD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Harga PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Harga PM BPBD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Harga PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Harga PM BPPD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Juai',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Kantor',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Lampihong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Lokbatu',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Paringin Selatan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Pirsus',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes RSUD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Tanah Habang',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Tebing Tinggi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 Harga PM Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 Harga PM Dinkes Uren',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Juai',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Kantor',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Lampihong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Paringin Selatan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 1 Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 1 Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 1 Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 1 Juai',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 1 Lampihong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 1 Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 2 Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 2 Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 2 Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 2 Juai',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 2 Lampihong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 2 Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 3 Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 3 Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 3 Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 3 Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 4 Awayan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 4 Batumandi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 4 Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 4 Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 5 Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik SMPN 5 Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 Harga PM Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 Harga PM Disdik Tebing Tinggi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Harga PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Harga PM Dishub',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Harga PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Harga PM Disnakertrans',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Harga PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Harga PM Distamben',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Harga PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 Harga PM DKO',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Harga PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 Harga PM DKP',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Harga PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Harga PM DKUKMP',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Harga PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 Harga PM DLH',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Harga PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Harga PM DPKP',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Harga PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Harga PM DPMD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Harga PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Harga PM DPMPTSP',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Harga PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Harga PM DPPKB',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Harga PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Harga PM DPPPA',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Harga PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Harga PM DPUPR',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Harga PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Harga PM DukCatPil',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Harga PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 Harga PM Halong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Harga PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Harga PM Inspektorat',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Harga PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 Harga PM Juai',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Harga PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Harga PM Kearsipan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Harga PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Harga PM Kehutanan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Harga PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Harga PM KESBANGPOL',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Harga PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Harga PM Kominfo',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Harga PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Harga PM Lampihong',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Harga PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Harga PM Paringin',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Harga PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Harga PM Paringin Kota',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Harga PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Harga PM Paringin Selatan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Harga PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Harga PM Paringin Timur',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Harga PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Harga PM Pariwisata',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Harga PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Harga PM Perdagangan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Harga PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Harga PM Perikanan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Harga PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Harga PM Perpustakaan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Harga PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Harga PM Pertanian',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Harga PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Harga PM RSUD',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Harga PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Harga PM SATPOLPP',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Harga PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Harga PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Harga PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 Harga PM Setda',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Harga PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Harga PM Setwan',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Harga PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Harga PM Sosial',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='HargaPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Harga PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Harga PM Tebing Tinggi',
            },
            bases=('peralatanmesin.hargaperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Kontrak PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Kontrak PM Awayan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Kontrak PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Kontrak PM BAPPEDA',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Kontrak PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Kontrak PM Batumandi',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Kontrak PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Kontrak PM Batu Piring',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Kontrak PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 Kontrak PM BKD',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Kontrak PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Kontrak PM BKPPD',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Kontrak PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Kontrak PM BPBD',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Kontrak PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Kontrak PM BPPD',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Kontrak PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Kontrak PM Dinkes',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Kontrak PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Kontrak PM Disdik',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Kontrak PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Kontrak PM Dishub',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Kontrak PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Kontrak PM Disnakertrans',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Kontrak PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Kontrak PM Distamben',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Kontrak PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 Kontrak PM DKO',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Kontrak PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 Kontrak PM DKP',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Kontrak PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Kontrak PM DKUKMP',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Kontrak PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 Kontrak PM DLH',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Kontrak PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Kontrak PM DPKP',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Kontrak PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Kontrak PM DPMD',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Kontrak PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Kontrak PM DPMPTSP',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Kontrak PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Kontrak PM DPPKB',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Kontrak PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Kontrak PM DPPPA',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Kontrak PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Kontrak PM DPUPR',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Kontrak PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Kontrak PM DukCatPil',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Kontrak PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 Kontrak PM Halong',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Kontrak PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Kontrak PM Inspektorat',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Kontrak PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 Kontrak PM Juai',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Kontrak PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Kontrak PM Kearsipan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Kontrak PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Kontrak PM Kehutanan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Kontrak PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Kontrak PM KESBANGPOL',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Kontrak PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Kontrak PM Kominfo',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Kontrak PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Kontrak PM Lampihong',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Kontrak PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Kontrak PM Paringin',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Kontrak PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Kontrak PM Paringin Kota',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Kontrak PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Kontrak PM Paringin Selatan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Kontrak PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Kontrak PM Paringin Timur',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Kontrak PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Kontrak PM Pariwisata',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Kontrak PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Kontrak PM Perdagangan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Kontrak PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Kontrak PM Perikanan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Kontrak PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Kontrak PM Perpustakaan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Kontrak PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Kontrak PM Pertanian',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Kontrak PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Kontrak PM RSUD',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Kontrak PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Kontrak PM SATPOLPP',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Kontrak PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Kontrak PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Kontrak PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 Kontrak PM Setda',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Kontrak PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Kontrak PM Setwan',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Kontrak PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Kontrak PM Sosial',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='KontrakPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Kontrak PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Kontrak PM Tebing Tinggi',
            },
            bases=('peralatanmesin.kontrakperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 PM Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 PM BAPPEDA',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 PM Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 PM Batu Piring',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 PM BKD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 PM BKPPD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 PM BPBD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 PM BPPD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Kantor',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Lokbatu',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Paringin Selatan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Pirsus',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes RSUD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Tanah Habang',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Tebing Tinggi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 PM Dinkes Uren',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Kantor',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Paringin Selatan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 1 Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 1 Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 1 Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 1 Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 1 Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 1 Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 2 Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 2 Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 2 Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 2 Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 2 Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 2 Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 3 Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 3 Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 3 Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 3 Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 4 Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 4 Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 4 Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 4 Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 5 Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik SMPN 5 Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 PM Disdik Tebing Tinggi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 PM Dishub',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 PM Disnakertrans',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 PM Distamben',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 PM DKO',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 PM DKP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 PM DKUKMP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 PM DLH',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 PM DPKP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 PM DPMD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 PM DPMPTSP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 PM DPPKB',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 PM DPPPA',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 PM DPUPR',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 PM DukCatPil',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 PM Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 PM Inspektorat',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 PM Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 PM Kearsipan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 PM Kehutanan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 PM KESBANGPOL',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 PM Kominfo',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 PM Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 PM Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 PM Paringin Kota',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 PM Paringin Selatan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 PM Paringin Timur',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 PM Pariwisata',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPemanfaatan',
            fields=[
            ],
            options={
                'verbose_name': 'Peralatan Mesin Pemanfaatan',
                'proxy': True,
                'verbose_name_plural': 'Peralatan Mesin Pemanfaatan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusan',
            fields=[
            ],
            options={
                'verbose_name': 'Peralatan Mesin Penghapusan',
                'proxy': True,
                'verbose_name_plural': 'Peralatan Mesin Penghapusan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 PM Penghapusan Awayan',
                'proxy': True,
                'verbose_name_plural': '34 PM Penghapusan Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 PM Penghapusan BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 PM Penghapusan BAPPEDA',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 PM Penghapusan Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 PM Penghapusan Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 PM Penghapusan Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 PM Penghapusan Batu Piring',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 PM Penghapusan BKD',
                'proxy': True,
                'verbose_name_plural': '19 PM Penghapusan BKD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 PM Penghapusan BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 PM Penghapusan BKPPD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 PM Penghapusan BPBD',
                'proxy': True,
                'verbose_name_plural': '39 PM Penghapusan BPBD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 PM Penghapusan BPPD',
                'proxy': True,
                'verbose_name_plural': '48 PM Penghapusan BPPD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Penghapusan Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 PM Penghapusan Dinkes',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Penghapusan Disdik',
                'proxy': True,
                'verbose_name_plural': '07 PM Penghapusan Disdik',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 PM Penghapusan Dishub',
                'proxy': True,
                'verbose_name_plural': '04 PM Penghapusan Dishub',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 PM Penghapusan Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 PM Penghapusan Disnakertrans',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 PM Penghapusan Distamben',
                'proxy': True,
                'verbose_name_plural': '17 PM Penghapusan Distamben',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 PM Penghapusan DKO',
                'proxy': True,
                'verbose_name_plural': '23 PM Penghapusan DKO',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 PM Penghapusan DKP',
                'proxy': True,
                'verbose_name_plural': '15 PM Penghapusan DKP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 PM Penghapusan DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 PM Penghapusan DKUKMP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 PM Penghapusan DLH',
                'proxy': True,
                'verbose_name_plural': '22 PM Penghapusan DLH',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 PM Penghapusan DPKP',
                'proxy': True,
                'verbose_name_plural': '40 PM Penghapusan DPKP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 PM Penghapusan DPMD',
                'proxy': True,
                'verbose_name_plural': '10 PM Penghapusan DPMD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 PM Penghapusan DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 PM Penghapusan DPMPTSP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 PM Penghapusan DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 PM Penghapusan DPPKB',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 PM Penghapusan DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 PM Penghapusan DPPPA',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 PM Penghapusan DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 PM Penghapusan DPUPR',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 PM Penghapusan DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 PM Penghapusan DukCatPil',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 PM Penghapusan Halong',
                'proxy': True,
                'verbose_name_plural': '35 PM Penghapusan Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 PM Penghapusan Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 PM Penghapusan Inspektorat',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 PM Penghapusan Juai',
                'proxy': True,
                'verbose_name_plural': '33 PM Penghapusan Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 PM Penghapusan Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 PM Penghapusan Kearsipan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 PM Penghapusan Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 PM Penghapusan Kehutanan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 PM Penghapusan KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 PM Penghapusan KESBANGPOL',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 PM Penghapusan Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 PM Penghapusan Kominfo',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 PM Penghapusan Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 PM Penghapusan Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 PM Penghapusan Paringin',
                'proxy': True,
                'verbose_name_plural': '28 PM Penghapusan Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 PM Penghapusan Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 PM Penghapusan Paringin Kota',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 PM Penghapusan Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 PM Penghapusan Paringin Selatan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 PM Penghapusan Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 PM Penghapusan Paringin Timur',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 PM Penghapusan Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 PM Penghapusan Pariwisata',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 PM Penghapusan Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 PM Penghapusan Perdagangan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 PM Penghapusan Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 PM Penghapusan Perikanan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 PM Penghapusan Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 PM Penghapusan Perpustakaan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 PM Penghapusan Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 PM Penghapusan Pertanian',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 PM Penghapusan RSUD',
                'proxy': True,
                'verbose_name_plural': '06 PM Penghapusan RSUD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 PM Penghapusan SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 PM Penghapusan SATPOLPP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 PM Penghapusan Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 PM Penghapusan Sekretariat Korpri',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 PM Penghapusan Setda',
                'proxy': True,
                'verbose_name_plural': '02 PM Penghapusan Setda',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 PM Penghapusan Setwan',
                'proxy': True,
                'verbose_name_plural': '01 PM Penghapusan Setwan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 PM Penghapusan Sosial',
                'proxy': True,
                'verbose_name_plural': '09 PM Penghapusan Sosial',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPenghapusanTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 PM Penghapusan Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 PM Penghapusan Tebing Tinggi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 PM Perdagangan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 PM Perikanan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 PM Perpustakaan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 PM Pertanian',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinReklas',
            fields=[
            ],
            options={
                'verbose_name': 'Peralatan Mesin Reklas',
                'proxy': True,
                'verbose_name_plural': 'Peralatan Mesin Reklas',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 PM RSUD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 PM SATPOLPP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 PM Setda',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 PM Setwan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 PM Sosial',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 PM Tebing Tinggi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapus',
            fields=[
            ],
            options={
                'verbose_name': 'Peralatan Mesin Usul Hapus',
                'proxy': True,
                'verbose_name_plural': 'Peralatan Mesin Usul Hapus',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 PM Usul Hapus Awayan',
                'proxy': True,
                'verbose_name_plural': '34 PM Usul Hapus Awayan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 PM Usul Hapus BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 PM Usul Hapus BAPPEDA',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 PM Usul Hapus Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 PM Usul Hapus Batumandi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 PM Usul Hapus Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 PM Usul Hapus Batu Piring',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 PM Usul Hapus BKD',
                'proxy': True,
                'verbose_name_plural': '19 PM Usul Hapus BKD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 PM Usul Hapus BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 PM Usul Hapus BKPPD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 PM Usul Hapus BPBD',
                'proxy': True,
                'verbose_name_plural': '39 PM Usul Hapus BPBD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 PM Usul Hapus BPPD',
                'proxy': True,
                'verbose_name_plural': '48 PM Usul Hapus BPPD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 PM Usul Hapus Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 PM Usul Hapus Dinkes',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 PM Usul Hapus Disdik',
                'proxy': True,
                'verbose_name_plural': '07 PM Usul Hapus Disdik',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 PM Usul Hapus Dishub',
                'proxy': True,
                'verbose_name_plural': '04 PM Usul Hapus Dishub',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 PM Usul Hapus Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 PM Usul Hapus Disnakertrans',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 PM Usul Hapus Distamben',
                'proxy': True,
                'verbose_name_plural': '17 PM Usul Hapus Distamben',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 PM Usul Hapus DKO',
                'proxy': True,
                'verbose_name_plural': '23 PM Usul Hapus DKO',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 PM Usul Hapus DKP',
                'proxy': True,
                'verbose_name_plural': '15 PM Usul Hapus DKP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 PM Usul Hapus DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 PM Usul Hapus DKUKMP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 PM Usul Hapus DLH',
                'proxy': True,
                'verbose_name_plural': '22 PM Usul Hapus DLH',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 PM Usul Hapus DPKP',
                'proxy': True,
                'verbose_name_plural': '40 PM Usul Hapus DPKP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 PM Usul Hapus DPMD',
                'proxy': True,
                'verbose_name_plural': '10 PM Usul Hapus DPMD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 PM Usul Hapus DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 PM Usul Hapus DPMPTSP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 PM Usul Hapus DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 PM Usul Hapus DPPKB',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 PM Usul Hapus DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 PM Usul Hapus DPPPA',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 PM Usul Hapus DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 PM Usul Hapus DPUPR',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 PM Usul Hapus DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 PM Usul Hapus DukCatPil',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 PM Usul Hapus Halong',
                'proxy': True,
                'verbose_name_plural': '35 PM Usul Hapus Halong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 PM Usul Hapus Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 PM Usul Hapus Inspektorat',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 PM Usul Hapus Juai',
                'proxy': True,
                'verbose_name_plural': '33 PM Usul Hapus Juai',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 PM Usul Hapus Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 PM Usul Hapus Kearsipan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 PM Usul Hapus Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 PM Usul Hapus Kehutanan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 PM Usul Hapus KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 PM Usul Hapus KESBANGPOL',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 PM Usul Hapus Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 PM Usul Hapus Kominfo',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 PM Usul Hapus Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 PM Usul Hapus Lampihong',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 PM Usul Hapus Paringin',
                'proxy': True,
                'verbose_name_plural': '28 PM Usul Hapus Paringin',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 PM Usul Hapus Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 PM Usul Hapus Paringin Kota',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 PM Usul Hapus Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 PM Usul Hapus Paringin Selatan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 PM Usul Hapus Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 PM Usul Hapus Paringin Timur',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 PM Usul Hapus Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 PM Usul Hapus Pariwisata',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 PM Usul Hapus Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 PM Usul Hapus Perdagangan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 PM Usul Hapus Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 PM Usul Hapus Perikanan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 PM Usul Hapus Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 PM Usul Hapus Perpustakaan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 PM Usul Hapus Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 PM Usul Hapus Pertanian',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 PM Usul Hapus RSUD',
                'proxy': True,
                'verbose_name_plural': '06 PM Usul Hapus RSUD',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 PM Usul Hapus SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 PM Usul Hapus SATPOLPP',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 PM Usul Hapus Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 PM Usul Hapus Sekretariat Korpri',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 PM Usul Hapus Setda',
                'proxy': True,
                'verbose_name_plural': '02 PM Usul Hapus Setda',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 PM Usul Hapus Setwan',
                'proxy': True,
                'verbose_name_plural': '01 PM Usul Hapus Setwan',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 PM Usul Hapus Sosial',
                'proxy': True,
                'verbose_name_plural': '09 PM Usul Hapus Sosial',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PeralatanMesinUsulHapusTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 PM Usul Hapus Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 PM Usul Hapus Tebing Tinggi',
            },
            bases=('peralatanmesin.peralatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Penghapusan PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Penghapusan PM Awayan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Penghapusan PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Penghapusan PM BAPPEDA',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Penghapusan PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Penghapusan PM Batumandi',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Penghapusan PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Penghapusan PM Batu Piring',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Penghapusan PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 Penghapusan PM BKD',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Penghapusan PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Penghapusan PM BKPPD',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Penghapusan PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Penghapusan PM BPBD',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Penghapusan PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Penghapusan PM BPPD',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Penghapusan PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Penghapusan PM Dinkes',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Penghapusan PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Penghapusan PM Disdik',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Penghapusan PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Penghapusan PM Dishub',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Penghapusan PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Penghapusan PM Disnakertrans',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Penghapusan PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Penghapusan PM Distamben',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Penghapusan PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 Penghapusan PM DKO',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Penghapusan PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 Penghapusan PM DKP',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Penghapusan PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Penghapusan PM DKUKMP',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Penghapusan PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 Penghapusan PM DLH',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Penghapusan PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Penghapusan PM DPKP',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Penghapusan PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Penghapusan PM DPMD',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Penghapusan PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Penghapusan PM DPMPTSP',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Penghapusan PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Penghapusan PM DPPKB',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Penghapusan PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Penghapusan PM DPPPA',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Penghapusan PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Penghapusan PM DPUPR',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Penghapusan PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Penghapusan PM DukCatPil',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Penghapusan PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 Penghapusan PM Halong',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Penghapusan PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Penghapusan PM Inspektorat',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Penghapusan PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 Penghapusan PM Juai',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Penghapusan PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Penghapusan PM Kearsipan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Penghapusan PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Penghapusan PM Kehutanan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Penghapusan PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Penghapusan PM KESBANGPOL',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Penghapusan PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Penghapusan PM Kominfo',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Penghapusan PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Penghapusan PM Lampihong',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Penghapusan PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Penghapusan PM Paringin',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Penghapusan PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Penghapusan PM Paringin Kota',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Penghapusan PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Penghapusan PM Paringin Selatan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Penghapusan PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Penghapusan PM Paringin Timur',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Penghapusan PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Penghapusan PM Pariwisata',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Penghapusan PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Penghapusan PM Perdagangan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Penghapusan PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Penghapusan PM Perikanan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Penghapusan PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Penghapusan PM Perpustakaan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Penghapusan PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Penghapusan PM Pertanian',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Penghapusan PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Penghapusan PM RSUD',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Penghapusan PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Penghapusan PM SATPOLPP',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Penghapusan PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Penghapusan PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Penghapusan PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 Penghapusan PM Setda',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Penghapusan PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Penghapusan PM Setwan',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Penghapusan PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Penghapusan PM Sosial',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='PenghapusanPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Penghapusan PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Penghapusan PM Tebing Tinggi',
            },
            bases=('peralatanmesin.penghapusanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Asal PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Asal PM Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Asal PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Asal PM BAPPEDA',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Asal PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Asal PM Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Asal PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Asal PM Batu Piring',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Asal PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Asal PM BKD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Asal PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Asal PM BKPPD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Asal PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Asal PM BPBD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Asal PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Asal PM BPPD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesAwayan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Awayan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Batumandi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesHalong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Halong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesJuai',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Juai',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Juai',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesKantor',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Kantor',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Kantor',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesLampihong',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Lampihong',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Lampihong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesLokbatu',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Lokbatu',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Lokbatu',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesParingin',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Paringin',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Paringin Selatan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesPirsus',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Pirsus',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Pirsus',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesRSUD',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes RSUD',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes RSUD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesTanahHabang',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Tanah Habang',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Tanah Habang',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Tebing Tinggi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDinkesUren',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Asal PM Dinkes Uren',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Asal PM Dinkes Uren',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikAwayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikHalong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikJuai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Juai',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikKantor',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Kantor',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Kantor',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikLampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Lampihong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikParingin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Paringin Selatan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN1Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 1 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 1 Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN1Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 1 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 1 Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN1Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 1 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 1 Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN1Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 1 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 1 Juai',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN1Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 1 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 1 Lampihong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN1Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 1 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 1 Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN2Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 2 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 2 Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN2Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 2 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 2 Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN2Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 2 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 2 Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN2Juai',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 2 Juai',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 2 Juai',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN2Lampihong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 2 Lampihong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 2 Lampihong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN2Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 2 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 2 Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN3Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 3 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 3 Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN3Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 3 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 3 Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN3Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 3 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 3 Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN3Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 3 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 3 Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN4Awayan',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 4 Awayan',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 4 Awayan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN4Batumandi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 4 Batumandi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 4 Batumandi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN4Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 4 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 4 Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN4Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 4 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 4 Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN5Halong',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 5 Halong',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 5 Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikSMPN5Paringin',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik SMPN 5 Paringin',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik SMPN 5 Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisdikTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Asal PM Disdik Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Asal PM Disdik Tebing Tinggi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Asal PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Asal PM Dishub',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Asal PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Asal PM Disnakertrans',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Asal PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Asal PM Distamben',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Asal PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Asal PM DKO',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Asal PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Asal PM DKP',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Asal PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Asal PM DKUKMP',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Asal PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Asal PM DLH',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Asal PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Asal PM DPKP',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Asal PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Asal PM DPMD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Asal PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Asal PM DPMPTSP',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Asal PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Asal PM DPPKB',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Asal PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Asal PM DPPPA',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Asal PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Asal PM DPUPR',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Asal PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Asal PM DukCatPil',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Asal PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Asal PM Halong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Asal PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Asal PM Inspektorat',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Asal PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Asal PM Juai',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Asal PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Asal PM Kearsipan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Asal PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Asal PM Kehutanan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Asal PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Asal PM KESBANGPOL',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Asal PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Asal PM Kominfo',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Asal PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Asal PM Lampihong',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Asal PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Asal PM Paringin',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Asal PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Asal PM Paringin Kota',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Asal PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Asal PM Paringin Selatan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Asal PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Asal PM Paringin Timur',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Asal PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Asal PM Pariwisata',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Asal PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Asal PM Perdagangan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Asal PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Asal PM Perikanan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Asal PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Asal PM Perpustakaan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Asal PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Asal PM Pertanian',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Asal PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Asal PM RSUD',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Asal PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Asal PM SATPOLPP',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Asal PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Asal PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Asal PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Asal PM Setda',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Asal PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Asal PM Setwan',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Asal PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Asal PM Sosial',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDAsalPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Asal PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Asal PM Tebing Tinggi',
            },
            bases=('peralatanmesin.skpdasalperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 SKPD Tujuan PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 SKPD Tujuan PM Awayan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 SKPD Tujuan PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 SKPD Tujuan PM BAPPEDA',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 SKPD Tujuan PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 SKPD Tujuan PM Batumandi',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 SKPD Tujuan PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 SKPD Tujuan PM Batu Piring',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 SKPD Tujuan PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 SKPD Tujuan PM BKD',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 SKPD Tujuan PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 SKPD Tujuan PM BKPPD',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 SKPD Tujuan PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 SKPD Tujuan PM BPBD',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 SKPD Tujuan PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 SKPD Tujuan PM BPPD',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 SKPD Tujuan PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 SKPD Tujuan PM Dinkes',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 SKPD Tujuan PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 SKPD Tujuan PM Disdik',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 SKPD Tujuan PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 SKPD Tujuan PM Dishub',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 SKPD Tujuan PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 SKPD Tujuan PM Disnakertrans',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 SKPD Tujuan PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 SKPD Tujuan PM Distamben',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 SKPD Tujuan PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 SKPD Tujuan PM DKO',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 SKPD Tujuan PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 SKPD Tujuan PM DKP',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 SKPD Tujuan PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 SKPD Tujuan PM DKUKMP',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 SKPD Tujuan PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 SKPD Tujuan PM DLH',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 SKPD Tujuan PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 SKPD Tujuan PM DPKP',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 SKPD Tujuan PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 SKPD Tujuan PM DPMD',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 SKPD Tujuan PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 SKPD Tujuan PM DPMPTSP',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 SKPD Tujuan PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 SKPD Tujuan PM DPPKB',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 SKPD Tujuan PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 SKPD Tujuan PM DPPPA',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 SKPD Tujuan PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 SKPD Tujuan PM DPUPR',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 SKPD Tujuan PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 SKPD Tujuan PM DukCatPil',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 SKPD Tujuan PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 SKPD Tujuan PM Halong',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 SKPD Tujuan PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 SKPD Tujuan PM Inspektorat',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 SKPD Tujuan PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 SKPD Tujuan PM Juai',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 SKPD Tujuan PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 SKPD Tujuan PM Kearsipan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 SKPD Tujuan PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 SKPD Tujuan PM Kehutanan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 SKPD Tujuan PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 SKPD Tujuan PM KESBANGPOL',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 SKPD Tujuan PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 SKPD Tujuan PM Kominfo',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 SKPD Tujuan PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 SKPD Tujuan PM Lampihong',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 SKPD Tujuan PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 SKPD Tujuan PM Paringin',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 SKPD Tujuan PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 SKPD Tujuan PM Paringin Kota',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 SKPD Tujuan PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 SKPD Tujuan PM Paringin Selatan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 SKPD Tujuan PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 SKPD Tujuan PM Paringin Timur',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 SKPD Tujuan PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 SKPD Tujuan PM Pariwisata',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 SKPD Tujuan PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 SKPD Tujuan PM Perdagangan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 SKPD Tujuan PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 SKPD Tujuan PM Perikanan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 SKPD Tujuan PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 SKPD Tujuan PM Perpustakaan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 SKPD Tujuan PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 SKPD Tujuan PM Pertanian',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 SKPD Tujuan PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 SKPD Tujuan PM RSUD',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 SKPD Tujuan PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 SKPD Tujuan PM SATPOLPP',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 SKPD Tujuan PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 SKPD Tujuan PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 SKPD Tujuan PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 SKPD Tujuan PM Setda',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 SKPD Tujuan PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 SKPD Tujuan PM Setwan',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 SKPD Tujuan PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 SKPD Tujuan PM Sosial',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='SKPDTujuanPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 SKPD Tujuan PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 SKPD Tujuan PM Tebing Tinggi',
            },
            bases=('peralatanmesin.skpdtujuanperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Tahun Berkurang PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Tahun Berkurang PM Awayan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Tahun Berkurang PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Tahun Berkurang PM BAPPEDA',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Tahun Berkurang PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Tahun Berkurang PM Batumandi',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Tahun Berkurang PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Tahun Berkurang PM Batu Piring',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Tahun Berkurang PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 Tahun Berkurang PM BKD',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Tahun Berkurang PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Tahun Berkurang PM BKPPD',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Tahun Berkurang PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Tahun Berkurang PM BPBD',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Tahun Berkurang PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Tahun Berkurang PM BPPD',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Tahun Berkurang PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Tahun Berkurang PM Dinkes',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Tahun Berkurang PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Tahun Berkurang PM Disdik',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Tahun Berkurang PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Tahun Berkurang PM Dishub',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Tahun Berkurang PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Tahun Berkurang PM Disnakertrans',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Tahun Berkurang PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Tahun Berkurang PM Distamben',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Tahun Berkurang PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 Tahun Berkurang PM DKO',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Tahun Berkurang PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 Tahun Berkurang PM DKP',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Tahun Berkurang PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Tahun Berkurang PM DKUKMP',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Tahun Berkurang PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 Tahun Berkurang PM DLH',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Tahun Berkurang PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Tahun Berkurang PM DPKP',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Tahun Berkurang PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Tahun Berkurang PM DPMD',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Tahun Berkurang PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Tahun Berkurang PM DPMPTSP',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Tahun Berkurang PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Tahun Berkurang PM DPPKB',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Tahun Berkurang PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Tahun Berkurang PM DPPPA',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Tahun Berkurang PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Tahun Berkurang PM DPUPR',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Tahun Berkurang PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Tahun Berkurang PM DukCatPil',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Tahun Berkurang PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 Tahun Berkurang PM Halong',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Tahun Berkurang PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Tahun Berkurang PM Inspektorat',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Tahun Berkurang PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 Tahun Berkurang PM Juai',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Tahun Berkurang PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Tahun Berkurang PM Kearsipan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Tahun Berkurang PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Tahun Berkurang PM Kehutanan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Tahun Berkurang PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Tahun Berkurang PM KESBANGPOL',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Tahun Berkurang PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Tahun Berkurang PM Kominfo',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Tahun Berkurang PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Tahun Berkurang PM Lampihong',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Tahun Berkurang PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Tahun Berkurang PM Paringin',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Tahun Berkurang PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Tahun Berkurang PM Paringin Kota',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Tahun Berkurang PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Tahun Berkurang PM Paringin Selatan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Tahun Berkurang PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Tahun Berkurang PM Paringin Timur',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Tahun Berkurang PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Tahun Berkurang PM Pariwisata',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Tahun Berkurang PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Tahun Berkurang PM Perdagangan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Tahun Berkurang PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Tahun Berkurang PM Perikanan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Tahun Berkurang PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Tahun Berkurang PM Perpustakaan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Tahun Berkurang PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Tahun Berkurang PM Pertanian',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Tahun Berkurang PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Tahun Berkurang PM RSUD',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Tahun Berkurang PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Tahun Berkurang PM SATPOLPP',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Tahun Berkurang PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Tahun Berkurang PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Tahun Berkurang PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 Tahun Berkurang PM Setda',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Tahun Berkurang PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Tahun Berkurang PM Setwan',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Tahun Berkurang PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Tahun Berkurang PM Sosial',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Tahun Berkurang PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Tahun Berkurang PM Tebing Tinggi',
            },
            bases=('peralatanmesin.tahunberkurangperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinAwayan',
            fields=[
            ],
            options={
                'verbose_name': '34 Usul Hapus PM Awayan',
                'proxy': True,
                'verbose_name_plural': '34 Usul Hapus PM Awayan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBAPPEDA',
            fields=[
            ],
            options={
                'verbose_name': '21 Usul Hapus PM BAPPEDA',
                'proxy': True,
                'verbose_name_plural': '21 Usul Hapus PM BAPPEDA',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBatumandi',
            fields=[
            ],
            options={
                'verbose_name': '32 Usul Hapus PM Batumandi',
                'proxy': True,
                'verbose_name_plural': '32 Usul Hapus PM Batumandi',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBatuPiring',
            fields=[
            ],
            options={
                'verbose_name': '37 Usul Hapus PM Batu Piring',
                'proxy': True,
                'verbose_name_plural': '37 Usul Hapus PM Batu Piring',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBKD',
            fields=[
            ],
            options={
                'verbose_name': '19 Usul Hapus PM BKD',
                'proxy': True,
                'verbose_name_plural': '19 Usul Hapus PM BKD',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBKPPD',
            fields=[
            ],
            options={
                'verbose_name': '26 Usul Hapus PM BKPPD',
                'proxy': True,
                'verbose_name_plural': '26 Usul Hapus PM BKPPD',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBPBD',
            fields=[
            ],
            options={
                'verbose_name': '39 Usul Hapus PM BPBD',
                'proxy': True,
                'verbose_name_plural': '39 Usul Hapus PM BPBD',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinBPPD',
            fields=[
            ],
            options={
                'verbose_name': '48 Usul Hapus PM BPPD',
                'proxy': True,
                'verbose_name_plural': '48 Usul Hapus PM BPPD',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDinkes',
            fields=[
            ],
            options={
                'verbose_name': '05 Usul Hapus PM Dinkes',
                'proxy': True,
                'verbose_name_plural': '05 Usul Hapus PM Dinkes',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDisdik',
            fields=[
            ],
            options={
                'verbose_name': '07 Usul Hapus PM Disdik',
                'proxy': True,
                'verbose_name_plural': '07 Usul Hapus PM Disdik',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDishub',
            fields=[
            ],
            options={
                'verbose_name': '04 Usul Hapus PM Dishub',
                'proxy': True,
                'verbose_name_plural': '04 Usul Hapus PM Dishub',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDisnakertrans',
            fields=[
            ],
            options={
                'verbose_name': '41 Usul Hapus PM Disnakertrans',
                'proxy': True,
                'verbose_name_plural': '41 Usul Hapus PM Disnakertrans',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDistamben',
            fields=[
            ],
            options={
                'verbose_name': '17 Usul Hapus PM Distamben',
                'proxy': True,
                'verbose_name_plural': '17 Usul Hapus PM Distamben',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDKO',
            fields=[
            ],
            options={
                'verbose_name': '23 Usul Hapus PM DKO',
                'proxy': True,
                'verbose_name_plural': '23 Usul Hapus PM DKO',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDKP',
            fields=[
            ],
            options={
                'verbose_name': '15 Usul Hapus PM DKP',
                'proxy': True,
                'verbose_name_plural': '15 Usul Hapus PM DKP',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDKUKMP',
            fields=[
            ],
            options={
                'verbose_name': '16 Usul Hapus PM DKUKMP',
                'proxy': True,
                'verbose_name_plural': '16 Usul Hapus PM DKUKMP',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDLH',
            fields=[
            ],
            options={
                'verbose_name': '22 Usul Hapus PM DLH',
                'proxy': True,
                'verbose_name_plural': '22 Usul Hapus PM DLH',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDPKP',
            fields=[
            ],
            options={
                'verbose_name': '40 Usul Hapus PM DPKP',
                'proxy': True,
                'verbose_name_plural': '40 Usul Hapus PM DPKP',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDPMD',
            fields=[
            ],
            options={
                'verbose_name': '10 Usul Hapus PM DPMD',
                'proxy': True,
                'verbose_name_plural': '10 Usul Hapus PM DPMD',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDPMPTSP',
            fields=[
            ],
            options={
                'verbose_name': '18 Usul Hapus PM DPMPTSP',
                'proxy': True,
                'verbose_name_plural': '18 Usul Hapus PM DPMPTSP',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDPPKB',
            fields=[
            ],
            options={
                'verbose_name': '42 Usul Hapus PM DPPKB',
                'proxy': True,
                'verbose_name_plural': '42 Usul Hapus PM DPPKB',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDPPPA',
            fields=[
            ],
            options={
                'verbose_name': '11 Usul Hapus PM DPPPA',
                'proxy': True,
                'verbose_name_plural': '11 Usul Hapus PM DPPPA',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDPUPR',
            fields=[
            ],
            options={
                'verbose_name': '03 Usul Hapus PM DPUPR',
                'proxy': True,
                'verbose_name_plural': '03 Usul Hapus PM DPUPR',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinDukCatPil',
            fields=[
            ],
            options={
                'verbose_name': '12 Usul Hapus PM DukCatPil',
                'proxy': True,
                'verbose_name_plural': '12 Usul Hapus PM DukCatPil',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinHalong',
            fields=[
            ],
            options={
                'verbose_name': '35 Usul Hapus PM Halong',
                'proxy': True,
                'verbose_name_plural': '35 Usul Hapus PM Halong',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinInspektorat',
            fields=[
            ],
            options={
                'verbose_name': '20 Usul Hapus PM Inspektorat',
                'proxy': True,
                'verbose_name_plural': '20 Usul Hapus PM Inspektorat',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinJuai',
            fields=[
            ],
            options={
                'verbose_name': '33 Usul Hapus PM Juai',
                'proxy': True,
                'verbose_name_plural': '33 Usul Hapus PM Juai',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinKearsipan',
            fields=[
            ],
            options={
                'verbose_name': '44 Usul Hapus PM Kearsipan',
                'proxy': True,
                'verbose_name_plural': '44 Usul Hapus PM Kearsipan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinKehutanan',
            fields=[
            ],
            options={
                'verbose_name': '14 Usul Hapus PM Kehutanan',
                'proxy': True,
                'verbose_name_plural': '14 Usul Hapus PM Kehutanan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinKESBANGPOL',
            fields=[
            ],
            options={
                'verbose_name': '24 Usul Hapus PM KESBANGPOL',
                'proxy': True,
                'verbose_name_plural': '24 Usul Hapus PM KESBANGPOL',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinKominfo',
            fields=[
            ],
            options={
                'verbose_name': '43 Usul Hapus PM Kominfo',
                'proxy': True,
                'verbose_name_plural': '43 Usul Hapus PM Kominfo',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinLampihong',
            fields=[
            ],
            options={
                'verbose_name': '31 Usul Hapus PM Lampihong',
                'proxy': True,
                'verbose_name_plural': '31 Usul Hapus PM Lampihong',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinParingin',
            fields=[
            ],
            options={
                'verbose_name': '28 Usul Hapus PM Paringin',
                'proxy': True,
                'verbose_name_plural': '28 Usul Hapus PM Paringin',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinParinginKota',
            fields=[
            ],
            options={
                'verbose_name': '29 Usul Hapus PM Paringin Kota',
                'proxy': True,
                'verbose_name_plural': '29 Usul Hapus PM Paringin Kota',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinParinginSelatan',
            fields=[
            ],
            options={
                'verbose_name': '36 Usul Hapus PM Paringin Selatan',
                'proxy': True,
                'verbose_name_plural': '36 Usul Hapus PM Paringin Selatan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinParinginTimur',
            fields=[
            ],
            options={
                'verbose_name': '30 Usul Hapus PM Paringin Timur',
                'proxy': True,
                'verbose_name_plural': '30 Usul Hapus PM Paringin Timur',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinPariwisata',
            fields=[
            ],
            options={
                'verbose_name': '46 Usul Hapus PM Pariwisata',
                'proxy': True,
                'verbose_name_plural': '46 Usul Hapus PM Pariwisata',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinPerdagangan',
            fields=[
            ],
            options={
                'verbose_name': '47 Usul Hapus PM Perdagangan',
                'proxy': True,
                'verbose_name_plural': '47 Usul Hapus PM Perdagangan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinPerikanan',
            fields=[
            ],
            options={
                'verbose_name': '45 Usul Hapus PM Perikanan',
                'proxy': True,
                'verbose_name_plural': '45 Usul Hapus PM Perikanan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinPerpustakaan',
            fields=[
            ],
            options={
                'verbose_name': '08 Usul Hapus PM Perpustakaan',
                'proxy': True,
                'verbose_name_plural': '08 Usul Hapus PM Perpustakaan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinPertanian',
            fields=[
            ],
            options={
                'verbose_name': '13 Usul Hapus PM Pertanian',
                'proxy': True,
                'verbose_name_plural': '13 Usul Hapus PM Pertanian',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinRSUD',
            fields=[
            ],
            options={
                'verbose_name': '06 Usul Hapus PM RSUD',
                'proxy': True,
                'verbose_name_plural': '06 Usul Hapus PM RSUD',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinSATPOLPP',
            fields=[
            ],
            options={
                'verbose_name': '25 Usul Hapus PM SATPOLPP',
                'proxy': True,
                'verbose_name_plural': '25 Usul Hapus PM SATPOLPP',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinSekretariatKorpri',
            fields=[
            ],
            options={
                'verbose_name': '27 Usul Hapus PM Sekretariat Korpri',
                'proxy': True,
                'verbose_name_plural': '27 Usul Hapus PM Sekretariat Korpri',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinSetda',
            fields=[
            ],
            options={
                'verbose_name': '02 Usul Hapus PM Setda',
                'proxy': True,
                'verbose_name_plural': '02 Usul Hapus PM Setda',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinSetwan',
            fields=[
            ],
            options={
                'verbose_name': '01 Usul Hapus PM Setwan',
                'proxy': True,
                'verbose_name_plural': '01 Usul Hapus PM Setwan',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinSosial',
            fields=[
            ],
            options={
                'verbose_name': '09 Usul Hapus PM Sosial',
                'proxy': True,
                'verbose_name_plural': '09 Usul Hapus PM Sosial',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
        migrations.CreateModel(
            name='TahunBerkurangUsulHapusPeralatanMesinTebingTinggi',
            fields=[
            ],
            options={
                'verbose_name': '38 Usul Hapus PM Tebing Tinggi',
                'proxy': True,
                'verbose_name_plural': '38 Usul Hapus PM Tebing Tinggi',
            },
            bases=('peralatanmesin.tahunberkurangusulhapusperalatanmesin',),
        ),
    ]
