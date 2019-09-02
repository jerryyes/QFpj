from django.contrib import admin
from DataCollect.models import stock_pool,stock_all

# Register your models here.
class StockPoolAdmin(admin.ModelAdmin):
    fields = ('stock_code','stock_name')
    search_fields = ('stock_name',)
    list_display = ('stock_code','stock_name','create_time')

class StockAllAdmin(admin.ModelAdmin):
    search_fields = ('stock_code',)
    list_display = ('state_dt','stock_code','open','close','high','low','vol','amount','pre_close','amt_change','pct_change')


admin.site.site_header = '量化分析平台-后台管理'
admin.site.site_title = '量化分析平台'
admin.site.register(stock_pool,StockPoolAdmin)
admin.site.register(stock_all,StockAllAdmin)
