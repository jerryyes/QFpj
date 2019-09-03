from django.db import models

# Create your models here.
class stock_pool(models.Model):
    stock_code = models.CharField('股票代码', max_length=200, primary_key=True)
    stock_name = models.CharField('股票名称', max_length=200)
    is_collect = models.BooleanField('是否采集数据',default=False)
    create_time = models.DateTimeField('创建时间', auto_now=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '股票池'
        verbose_name_plural = '股票池'

    def __str__(self):
        return self.stock_name

class stock_all(models.Model):
    state_dt = models.DateTimeField('交易日期', auto_now=False)
    stock_code = models.CharField('股票代码', max_length=200)
    open = models.DecimalField('开盘价', max_digits=20, decimal_places=2)
    close = models.DecimalField('收盘价', max_digits=20, decimal_places=2)
    high = models.DecimalField('最高价', max_digits=20, decimal_places=2)
    low = models.DecimalField('最低价', max_digits=20, decimal_places=2)
    vol = models.DecimalField('成交量（手）', max_digits=20, decimal_places=2)
    amount = models.DecimalField('成交额', max_digits=20, decimal_places=2)
    pre_close = models.DecimalField('昨收价', max_digits=20, decimal_places=2)
    amt_change = models.DecimalField('涨跌额', max_digits=20, decimal_places=2)
    pct_change = models.DecimalField('涨跌幅 （未复权）', max_digits=20, decimal_places=2)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '日线行情'
        verbose_name_plural = '日线行情'

    def __str__(self):
        return self.stock_code
