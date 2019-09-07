__author__ = 'chenzhiyuan'

from celery_tasks.main import celery_app
from celery.utils.log import get_task_logger
from DataCollect import Init_StockALL_Sp

logger = get_task_logger('get_dayline')

@celery_app.task(name='')
def get_dayline():
    update_stock = Init_StockALL_Sp.get_dayline()
    print('All Stocks in List %s Are Up-to-date' % (update_stock))