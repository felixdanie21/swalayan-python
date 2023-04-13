# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mbarang(models.Model):
    barangkode = models.CharField(primary_key=True, max_length=6)
    barangnama = models.CharField(max_length=50)
    brgjnskode = models.CharField(max_length=4)
    satuankode = models.CharField(max_length=3)
    pabrikkode = models.CharField(max_length=5)
    baranghrgbppn = models.FloatField()
    baranghrgsppn = models.FloatField()
    barangterakhir = models.FloatField()
    barangstokmin = models.FloatField()
    barangaktif = models.CharField(max_length=1)
    barangstokmaks = models.FloatField()
    barangpoinqty = models.FloatField()
    barangpoinomz = models.FloatField()
    barangdscmember = models.FloatField()
    barangstatbonus = models.CharField(max_length=1)
    barangbarcode = models.CharField(max_length=20)
    baranghrgpokok = models.BigIntegerField()
    baranghrgkhusus = models.BigIntegerField()
    barangjumsat = models.IntegerField()
    barangtglbliakh = models.DateField()
    barangdisc = models.FloatField()
    barangupdate = models.DateTimeField()
    barangstatpoin = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mbarang'


class Mbrgjns(models.Model):
    brgjnskode = models.CharField(primary_key=True, max_length=4)
    brgjnsnama = models.CharField(max_length=40)
    groupkode = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'mbrgjns'


class Mbrglok(models.Model):
    barangkode = models.CharField(max_length=6)
    lokasikode = models.CharField(max_length=4)
    brglokket = models.CharField(max_length=10, blank=True, null=True)
    gudangkode = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'mbrglok'


class Mbrgsat(models.Model):
    barangkode = models.CharField(primary_key=True, max_length=6)
    brgsatnourut = models.CharField(max_length=1)
    brgsatbesar = models.CharField(max_length=3)
    brgsatkecil = models.CharField(max_length=3)
    brgsatsatuan = models.CharField(max_length=3)
    brgsathrgbppn = models.FloatField()
    brgsathrgsppn = models.FloatField()
    brgsatqtybrg = models.CharField(max_length=5)
    brgsatbarcode = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mbrgsat'
        unique_together = (('barangkode', 'brgsatnourut'),)


class Mbrgsupp(models.Model):
    supplierkode = models.CharField(primary_key=True, max_length=4)
    barangkode = models.CharField(max_length=6)
    brgsupphbppn = models.FloatField()
    brgsupphsppn = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mbrgsupp'
        unique_together = (('supplierkode', 'barangkode'),)


class Menu(models.Model):
    modulkode = models.CharField(primary_key=True, max_length=1)
    menukode = models.CharField(max_length=7)
    menunama = models.CharField(max_length=25)
    menukontroler = models.CharField(max_length=40)
    menuinduk = models.CharField(max_length=7, blank=True, null=True)
    menustatus = models.CharField(max_length=1)
    menulevel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'
        unique_together = (('modulkode', 'menukode'),)


class Mgroup(models.Model):
    groupkode = models.CharField(primary_key=True, max_length=2)
    groupnama = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mgroup'


class Mgudang(models.Model):
    gudangkode = models.CharField(primary_key=True, max_length=2)
    gudangnama = models.CharField(max_length=30)
    gudangstatus = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgudang'


class Mhrgbaru(models.Model):
    barangkode = models.CharField(max_length=6)
    supplierkode = models.CharField(max_length=4)
    hrgbarutgl = models.DateField()
    hrgbarubppn = models.FloatField()
    hrgbarusppn = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mhrgbaru'


class Mhrgcus(models.Model):
    barangkode = models.CharField(primary_key=True, max_length=6)
    customerkode = models.CharField(max_length=4)
    hrgcusharga = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mhrgcus'
        unique_together = (('barangkode', 'customerkode'),)


class Mhrgmod(models.Model):
    barangkode = models.CharField(max_length=6)
    hrgbarutglnota = models.DateField()
    hrgmodnota = models.FloatField()
    hrgmodppn = models.FloatField()
    hrgmodnppn = models.FloatField()
    hrgmodhrg1 = models.FloatField()
    hrgmoddsc1 = models.FloatField()
    hrgmodndsc1 = models.FloatField()
    hrgmodhrg2 = models.FloatField()
    hrgmodds2 = models.FloatField()
    hrgmodndsc2 = models.FloatField()
    hrgmodhrg3 = models.FloatField()
    hrgmoddscfak = models.FloatField()
    hrgmodndscfak = models.FloatField()
    hrgmodhrg4 = models.FloatField()
    hrgmodblain = models.FloatField()
    hrgmodqty = models.FloatField()
    hrgmodhblain = models.FloatField()
    hrgmodhmastp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mhrgmod'


class Mlokasi(models.Model):
    lokasikode = models.CharField(primary_key=True, max_length=4)
    lokasinama = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mlokasi'


class Modul(models.Model):
    modulkode = models.CharField(primary_key=True, max_length=1)
    modulnama = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'modul'


class Mpabrik(models.Model):
    pabrikkode = models.CharField(max_length=5)
    pabriknama = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mpabrik'


class Mrangehrg(models.Model):
    barangkode = models.CharField(primary_key=True, max_length=6)
    rangehrgqty = models.BigIntegerField()
    rangehrgpokok = models.FloatField()
    rangehrgjual = models.FloatField()
    rangehrgprofit = models.FloatField()
    rangehrgedit = models.CharField(max_length=1)
    rangehrgtgl = models.DateField()

    class Meta:
        managed = False
        db_table = 'mrangehrg'
        unique_together = (('barangkode', 'rangehrgqty'),)


class Msatuan(models.Model):
    satuankode = models.CharField(primary_key=True, max_length=3)
    satuannama = models.CharField(max_length=15)
    satuanlama = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'msatuan'


class Msupplier(models.Model):
    supplierkode = models.CharField(primary_key=True, max_length=4)
    suppliernama = models.CharField(max_length=40)
    supplieralamat = models.CharField(max_length=60)
    supplierkota = models.CharField(max_length=30)
    suppliertelp = models.CharField(max_length=20)
    supplierkontak = models.CharField(max_length=20)
    supplierkodeacc = models.CharField(max_length=10)
    supplierstakota = models.CharField(max_length=1)
    suppliernpwp = models.CharField(max_length=20)
    supplierpkp = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'msupplier'
