from django.db import models

# Create your models here.


class DBG(models.Model):
    # id = models.IntegerField()
    name_group_full = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name_group_full
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    #     ordering = ['-create_at']



class DBC(models.Model):
    # id = models.IntegerField()
    name_counter_full = models.CharField(max_length=50, verbose_name='Наименование счетчика', blank=False, default="")  # обязательное поле для формы (blank=False) 
    group = models.ManyToManyField(DBG, through="DBGC", verbose_name='Наименование группы')
    schem = models.CharField(max_length=20, default="", blank=True)                                                     # НЕобязательное поле для формы
    # net_adress = models.CharField(max_length=20)
    net_adress = models.IntegerField(verbose_name='Сетевой адрес', blank=False, default=0) # обязательное поле для формы (blank=False)
    # manuf_number = models.CharField(max_length=20)
    manuf_number = models.IntegerField(verbose_name='Заводской номер', default=0, blank=True)
    manuf_data = models.DateTimeField(verbose_name='Дата изготовление', default='2000-01-01T00:00', blank=True)
    version_data = models.BigIntegerField(blank=True, default=0)             # вариант исполнения счетчика (6+2 = 8 байт в виде одного числа) (стр.77)
    # klass_react = models.CharField(max_length=20)   
    klass_react = models.FloatField(blank=True, default=0)                   # класс точности по реактивной энергии (стр.75)
    # klass_act = models.CharField(max_length=20)
    klass_act = models.FloatField(blank=True, default=0)                     # класс точности по активной энергии (стр.75)
    nom_u = models.IntegerField(blank=True, default=0)
    nom_i = models.IntegerField(blank=True, default=0)
    # ku = models.CharField(max_length=20)   
    # ki = models.CharField(max_length=20)
    ku = models.IntegerField(blank=True, default=0)                  # коэф трансформации 
    ki = models.IntegerField(blank=True, default=0)
    koefA = models.IntegerField(blank=True, default=0)               #
    datetime = models.DateTimeField(blank=True, default='2000-01-01T00:00')           # текущее время и дата счетчика
    adress_last_record = models.IntegerField(blank=True, default=0)  # адрес последней записи массива средних мощностей (стр.78)
    datetime_adr0 = models.DateTimeField(blank=True, default='2000-01-01T00:00')      # дата и время последней записи массива средних мощностей (стр.79)
    # comment = models.TextField()

    def __str__(self) -> str:
        return self.name_counter_full
    
    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчики'
        # ordering = ['-create_at']



class DBGC(models.Model):
        # id = models.IntegerField()
        group = models.ForeignKey(DBG, on_delete = models.CASCADE)
        counter = models.ForeignKey(DBC, on_delete = models.CASCADE)

# мгновенные значения (стр.69)
class DBIC(models.Model):
    # id = models.IntegerField()
    counter = models.ForeignKey(DBC, on_delete = models.CASCADE)
    # name_counter_full = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    CurrentFaze1    = models.IntegerField()  
    CurrentFaze2    = models.IntegerField()
    CurrentFaze3    = models.IntegerField()
    CurrentSum      = models.IntegerField()
    PowerPFaze1     = models.IntegerField()
    PowerPFaze2     = models.IntegerField()
    PowerPFaze3     = models.IntegerField()
    PowerPFazeSum   = models.IntegerField()
    PowerQFaze1     = models.IntegerField()
    PowerQFaze1     = models.IntegerField()
    PowerQFaze2     = models.IntegerField()
    PowerQFaze3     = models.IntegerField()
    PowerQFazeSum   = models.IntegerField()
    PowerSFaze1     = models.IntegerField()
    PowerSFaze2     = models.IntegerField()
    PowerSFaze3     = models.IntegerField()
    PowerSFazeSum   = models.IntegerField()
    KPowerFaze1     = models.IntegerField()
    KPowerFaze2     = models.IntegerField()
    KPowerFaze3     = models.IntegerField()
    KPowerFazeSum   = models.IntegerField()
    EnergyTarif1    = models.IntegerField()
    EnergyTarif2    = models.IntegerField()
    EnergyTarif3    = models.IntegerField()
    EnergyTarif4    = models.IntegerField()
    EnergyTarifSum  = models.IntegerField()

# профиль мощности
class DBPP(models.Model):
    # id = models.IntegerField()
    counter = models.ForeignKey(DBC, on_delete = models.CASCADE)
    # name_counter_full   = models.CharField(max_length=50)
    datetime            = models.DateTimeField()
    write_status_byte     = models.IntegerField()           # байт состояня записи  (стр.79 и 97)
    period_int          = models.IntegerField()
    P_plus              = models.IntegerField()
    P_minus             = models.IntegerField()
    Q_plus              = models.IntegerField()
    Q_minus             = models.IntegerField()

# потерянные данные профиля мощности
class LDPP(models.Model):
    # id = models.IntegerField()
    counter = models.ForeignKey(DBC, on_delete = models.CASCADE)
    # name_counter_full   = models.CharField(max_length=50)
    datetime            = models.DateTimeField()

        