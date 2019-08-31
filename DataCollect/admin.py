from django.contrib import admin
from DataCollect.models import stock_pool,stock_all

# Register your models here.
class StockPoolAdmin(admin.ModelAdmin):
    fields = ('stock_code','stock_name')
    search_fields = ('stock_name',)
    list_display = ('stock_code','stock_name','create_time')


admin.site.register(stock_pool,StockPoolAdmin)
admin.site.register(stock_all)
