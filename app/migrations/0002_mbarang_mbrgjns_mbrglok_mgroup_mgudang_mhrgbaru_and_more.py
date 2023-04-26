# Generated by Django 4.1.7 on 2023-04-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mbarang',
            fields=[
                ('barangkode', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('barangnama', models.CharField(max_length=50)),
                ('brgjnskode', models.CharField(max_length=4)),
                ('satuankode', models.CharField(max_length=3)),
                ('pabrikkode', models.CharField(max_length=5)),
                ('baranghrgbppn', models.FloatField()),
                ('baranghrgsppn', models.FloatField()),
                ('barangterakhir', models.FloatField()),
                ('barangstokmin', models.FloatField()),
                ('barangaktif', models.CharField(max_length=1)),
                ('barangstokmaks', models.FloatField()),
                ('barangpoinqty', models.FloatField()),
                ('barangpoinomz', models.FloatField()),
                ('barangdscmember', models.FloatField()),
                ('barangstatbonus', models.CharField(max_length=1)),
                ('barangbarcode', models.CharField(max_length=20)),
                ('baranghrgpokok', models.BigIntegerField()),
                ('baranghrgkhusus', models.BigIntegerField()),
                ('barangjumsat', models.IntegerField()),
                ('barangtglbliakh', models.DateField()),
                ('barangdisc', models.FloatField()),
                ('barangupdate', models.DateTimeField()),
                ('barangstatpoin', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'mbarang',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mbrgjns',
            fields=[
                ('brgjnskode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('brgjnsnama', models.CharField(max_length=40)),
                ('groupkode', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'mbrgjns',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mbrglok',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('barangkode', models.CharField(max_length=6)),
                ('lokasikode', models.CharField(max_length=4)),
                ('brglokket', models.CharField(blank=True, max_length=10, null=True)),
                ('gudangkode', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'mbrglok',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mgroup',
            fields=[
                ('groupkode', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('groupnama', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'mgroup',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mgudang',
            fields=[
                ('gudangkode', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('gudangnama', models.CharField(max_length=30)),
                ('gudangstatus', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'mgudang',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mhrgbaru',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('barangkode', models.CharField(max_length=6)),
                ('supplierkode', models.CharField(max_length=4)),
                ('hrgbarutgl', models.DateField()),
                ('hrgbarubppn', models.FloatField()),
                ('hrgbarusppn', models.FloatField()),
            ],
            options={
                'db_table': 'mhrgbaru',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mhrgmod',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('barangkode', models.CharField(max_length=6)),
                ('hrgbarutglnota', models.DateField()),
                ('hrgmodnota', models.FloatField()),
                ('hrgmodppn', models.FloatField()),
                ('hrgmodnppn', models.FloatField()),
                ('hrgmodhrg1', models.FloatField()),
                ('hrgmoddsc1', models.FloatField()),
                ('hrgmodndsc1', models.FloatField()),
                ('hrgmodhrg2', models.FloatField()),
                ('hrgmodds2', models.FloatField()),
                ('hrgmodndsc2', models.FloatField()),
                ('hrgmodhrg3', models.FloatField()),
                ('hrgmoddscfak', models.FloatField()),
                ('hrgmodndscfak', models.FloatField()),
                ('hrgmodhrg4', models.FloatField()),
                ('hrgmodblain', models.FloatField()),
                ('hrgmodqty', models.FloatField()),
                ('hrgmodhblain', models.FloatField()),
                ('hrgmodhmastp', models.FloatField()),
            ],
            options={
                'db_table': 'mhrgmod',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mlokasi',
            fields=[
                ('lokasikode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('lokasinama', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'mlokasi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('modulkode', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('modulnama', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'modul',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mpabrik',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pabrikkode', models.CharField(max_length=5)),
                ('pabriknama', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'mpabrik',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Msatuan',
            fields=[
                ('satuankode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('satuannama', models.CharField(max_length=15)),
                ('satuanlama', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'msatuan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Msupplier',
            fields=[
                ('supplierkode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('suppliernama', models.CharField(max_length=40)),
                ('supplieralamat', models.CharField(max_length=60)),
                ('supplierkota', models.CharField(max_length=30)),
                ('suppliertelp', models.CharField(max_length=20)),
                ('supplierkontak', models.CharField(max_length=20)),
                ('supplierkodeacc', models.CharField(max_length=10)),
                ('supplierstakota', models.CharField(max_length=1)),
                ('suppliernpwp', models.CharField(max_length=20)),
                ('supplierpkp', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'msupplier',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Muser',
            fields=[
                ('userid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('userlevel', models.CharField(max_length=1)),
                ('userimage', models.CharField(max_length=225)),
                ('usertoken', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'muser',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mrangehrg',
            fields=[
                ('barangkode', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('rangehrgqty', models.BigIntegerField()),
                ('rangehrgpokok', models.FloatField()),
                ('rangehrgjual', models.FloatField()),
                ('rangehrgprofit', models.FloatField()),
                ('rangehrgedit', models.CharField(max_length=1)),
                ('rangehrgtgl', models.DateField()),
            ],
            options={
                'db_table': 'mrangehrg',
                'managed': True,
                'unique_together': {('barangkode', 'rangehrgqty')},
            },
        ),
        migrations.CreateModel(
            name='Mhrgcus',
            fields=[
                ('barangkode', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('customerkode', models.CharField(max_length=4)),
                ('hrgcusharga', models.FloatField()),
            ],
            options={
                'db_table': 'mhrgcus',
                'managed': True,
                'unique_together': {('barangkode', 'customerkode')},
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('modulkode', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('menukode', models.CharField(max_length=7)),
                ('menunama', models.CharField(max_length=25)),
                ('menukontroler', models.CharField(max_length=40)),
                ('menuinduk', models.CharField(blank=True, max_length=7, null=True)),
                ('menustatus', models.CharField(max_length=1)),
                ('menulevel', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': True,
                'unique_together': {('modulkode', 'menukode')},
            },
        ),
        migrations.CreateModel(
            name='Mbrgsupp',
            fields=[
                ('supplierkode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('barangkode', models.CharField(max_length=6)),
                ('brgsupphbppn', models.FloatField()),
                ('brgsupphsppn', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mbrgsupp',
                'managed': True,
                'unique_together': {('supplierkode', 'barangkode')},
            },
        ),
        migrations.CreateModel(
            name='Mbrgsat',
            fields=[
                ('barangkode', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('brgsatnourut', models.CharField(max_length=1)),
                ('brgsatbesar', models.CharField(max_length=3)),
                ('brgsatkecil', models.CharField(max_length=3)),
                ('brgsatsatuan', models.CharField(max_length=3)),
                ('brgsathrgbppn', models.FloatField()),
                ('brgsathrgsppn', models.FloatField()),
                ('brgsatqtybrg', models.CharField(max_length=5)),
                ('brgsatbarcode', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'mbrgsat',
                'managed': True,
                'unique_together': {('barangkode', 'brgsatnourut')},
            },
        ),
    ]
