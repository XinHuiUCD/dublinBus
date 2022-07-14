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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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


class HistWeather(models.Model):
    id_hist_weather = models.AutoField(primary_key=True)
    date = models.CharField(unique=True, max_length=45, blank=True, null=True)
    indicator = models.IntegerField(blank=True, null=True)
    precip_amt = models.FloatField(blank=True, null=True)
    indicator2 = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    indicator3 = models.IntegerField(blank=True, null=True)
    wet_bulb_temp = models.FloatField(blank=True, null=True)
    dew_pt_temp = models.FloatField(blank=True, null=True)
    vapor_pressure = models.FloatField(blank=True, null=True)
    relative_humid = models.IntegerField(blank=True, null=True)
    mean_sea_level_pressure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_weather'


class HistWeatherOw(models.Model):
    id_ow = models.IntegerField(blank=True, null=True)
    dt = models.IntegerField(blank=True, null=True)
    dt_iso = models.TextField(blank=True, null=True)
    timezone = models.IntegerField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    dew_point = models.FloatField(blank=True, null=True)
    feels_like = models.FloatField(blank=True, null=True)
    temp_min = models.FloatField(blank=True, null=True)
    temp_max = models.FloatField(blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    sea_level = models.TextField(blank=True, null=True)
    grnd_level = models.TextField(blank=True, null=True)
    humidity = models.IntegerField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_deg = models.IntegerField(blank=True, null=True)
    wind_gust = models.TextField(blank=True, null=True)
    rain_1h = models.TextField(blank=True, null=True)
    rain_3h = models.TextField(blank=True, null=True)
    snow_1h = models.TextField(blank=True, null=True)
    snow_3h = models.TextField(blank=True, null=True)
    clouds_all = models.IntegerField(blank=True, null=True)
    weather_id = models.IntegerField(blank=True, null=True)
    weather_main = models.TextField(blank=True, null=True)
    weather_description = models.TextField(blank=True, null=True)
    weather_icon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hist_weather_ow'


class Import(models.Model):
    id_hist_weather = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    indicator = models.IntegerField(blank=True, null=True)
    precip_amt = models.IntegerField(blank=True, null=True)
    indicator2 = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    indicator3 = models.IntegerField(blank=True, null=True)
    wet_bulb_temp = models.FloatField(blank=True, null=True)
    dew_pt_temp = models.FloatField(blank=True, null=True)
    vapor_pressure = models.FloatField(blank=True, null=True)
    relative_humid = models.IntegerField(blank=True, null=True)
    mean_sea_level_pressure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import'


class Justifications(models.Model):
    justificationid = models.IntegerField(db_column='JUSTIFICATIONID', primary_key=True)  # Field name made lowercase.
    justificationtype = models.CharField(db_column='JUSTIFICATIONTYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.CharField(db_column='OPERATORID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LASTUPDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='NOTE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'justifications'


class Leavetimes(models.Model):
    leaveid = models.IntegerField(db_column='leaveID', primary_key=True)  # Field name made lowercase.
    datasource = models.CharField(db_column='DATASOURCE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dayofservice = models.CharField(db_column='DAYOFSERVICE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tripid = models.IntegerField(db_column='TRIPID', blank=True, null=True)  # Field name made lowercase.
    progrnumber = models.IntegerField(db_column='PROGRNUMBER', blank=True, null=True)  # Field name made lowercase.
    stoppointid = models.IntegerField(db_column='STOPPOINTID', blank=True, null=True)  # Field name made lowercase.
    plannedtime_arr = models.IntegerField(db_column='PLANNEDTIME_ARR', blank=True, null=True)  # Field name made lowercase.
    plannedtime_dep = models.IntegerField(db_column='PLANNEDTIME_DEP', blank=True, null=True)  # Field name made lowercase.
    actualtime_arr = models.IntegerField(db_column='ACTUALTIME_ARR', blank=True, null=True)  # Field name made lowercase.
    actualtime_dep = models.IntegerField(db_column='ACTUALTIME_DEP', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VEHICLEID', blank=True, null=True)  # Field name made lowercase.
    passengers = models.IntegerField(db_column='PASSENGERS', blank=True, null=True)  # Field name made lowercase.
    passengersin = models.IntegerField(db_column='PASSENGERSIN', blank=True, null=True)  # Field name made lowercase.
    passengersout = models.IntegerField(db_column='PASSENGERSOUT', blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='DISTANCE', blank=True, null=True)  # Field name made lowercase.
    suppressed = models.IntegerField(db_column='SUPPRESSED', blank=True, null=True)  # Field name made lowercase.
    justificationid = models.IntegerField(db_column='JUSTIFICATIONID', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.CharField(db_column='LASTUPDATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='NOTE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leavetimes'


class LeavetimesImport(models.Model):
    leaveid = models.IntegerField(db_column='leaveID', blank=True, null=True)  # Field name made lowercase.
    datasource = models.TextField(db_column='DATASOURCE', blank=True, null=True)  # Field name made lowercase.
    dayofservice = models.TextField(db_column='DAYOFSERVICE', blank=True, null=True)  # Field name made lowercase.
    tripid = models.IntegerField(db_column='TRIPID', blank=True, null=True)  # Field name made lowercase.
    progrnumber = models.IntegerField(db_column='PROGRNUMBER', blank=True, null=True)  # Field name made lowercase.
    stoppointid = models.IntegerField(db_column='STOPPOINTID', blank=True, null=True)  # Field name made lowercase.
    plannedtime_arr = models.IntegerField(db_column='PLANNEDTIME_ARR', blank=True, null=True)  # Field name made lowercase.
    plannedtime_dep = models.IntegerField(db_column='PLANNEDTIME_DEP', blank=True, null=True)  # Field name made lowercase.
    actualtime_arr = models.IntegerField(db_column='ACTUALTIME_ARR', blank=True, null=True)  # Field name made lowercase.
    actualtime_dep = models.IntegerField(db_column='ACTUALTIME_DEP', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VEHICLEID', blank=True, null=True)  # Field name made lowercase.
    passengers = models.BigIntegerField(db_column='PASSENGERS', blank=True, null=True)  # Field name made lowercase.
    passengersin = models.BigIntegerField(db_column='PASSENGERSIN', blank=True, null=True)  # Field name made lowercase.
    passengersout = models.BigIntegerField(db_column='PASSENGERSOUT', blank=True, null=True)  # Field name made lowercase.
    distance = models.BigIntegerField(db_column='DISTANCE', blank=True, null=True)  # Field name made lowercase.
    suppressed = models.BigIntegerField(db_column='SUPPRESSED', blank=True, null=True)  # Field name made lowercase.
    justificationid = models.BigIntegerField(db_column='JUSTIFICATIONID', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.TextField(db_column='LASTUPDATE', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leavetimes_import'


class LineStop(models.Model):
    line_stop_id = models.IntegerField(db_column='line_stop_ID', primary_key=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LINEID', blank=True, null=True)  # Field name made lowercase.
    stoppointid = models.IntegerField(db_column='STOPPOINTID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'line_stop'


class RawData(models.Model):
    rawid = models.IntegerField(db_column='rawID', primary_key=True)  # Field name made lowercase.
    datasource = models.CharField(db_column='DATASOURCE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dayofservice = models.CharField(db_column='DAYOFSERVICE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VEHICLEID', blank=True, null=True)  # Field name made lowercase.
    timepos = models.CharField(db_column='TIMEPOS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    posx = models.IntegerField(db_column='POSX', blank=True, null=True)  # Field name made lowercase.
    posy = models.IntegerField(db_column='POSY', blank=True, null=True)  # Field name made lowercase.
    odometer = models.IntegerField(db_column='ODOMETER', blank=True, null=True)  # Field name made lowercase.
    tripid = models.IntegerField(db_column='TRIPID', blank=True, null=True)  # Field name made lowercase.
    tripodometer = models.IntegerField(db_column='TRIPODOMETER', blank=True, null=True)  # Field name made lowercase.
    passengersin = models.IntegerField(db_column='PASSENGERSIN', blank=True, null=True)  # Field name made lowercase.
    passengersout = models.IntegerField(db_column='PASSENGERSOUT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'raw_data'


class Stoprouteinfo(models.Model):
    stopid = models.IntegerField(db_column='stopId', primary_key=True)  # Field name made lowercase.
    routesid = models.CharField(db_column='routesId', max_length=120, blank=True, null=True)  # Field name made lowercase.
    searchname = models.CharField(db_column='searchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.routesid)

    class Meta:
        managed = True
        db_table = 'stopRouteInfo'


class Vehicle(models.Model):
    datasource = models.TextField(db_column='DATASOURCE', blank=True, null=True)  # Field name made lowercase.
    dayofservice = models.TextField(db_column='DAYOFSERVICE', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VEHICLEID', blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='DISTANCE', blank=True, null=True)  # Field name made lowercase.
    minutes = models.IntegerField(db_column='MINUTES', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.TextField(db_column='LASTUPDATE', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'


class XpressbusBus(models.Model):
    id = models.BigAutoField(primary_key=True)
    routeid = models.IntegerField(db_column='routeId')  # Field name made lowercase.
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        managed = False
        db_table = 'xpressbus_bus'
