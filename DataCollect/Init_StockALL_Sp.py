import datetime
import tushare as ts
import pymysql
from QFpj.settings import DATABASES

def get_dayline():

    # 设置tushare pro的token并获取连接
    ts.set_token('681d6d0996a1852dd2cc4f3251291339ecabc3d716e69a5ab1a9a83e')
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期，其中初始日期从股票池中的每个股票上次更新时间中获取，终止日期设定为昨天。
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y%m%d')
    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host=DATABASES['default']['HOST'], port=int(DATABASES['default']['PORT']),
                         user=DATABASES['default']['USER'], passwd=DATABASES['default']['PASSWORD'],
                         db=DATABASES['default']['NAME'], charset='utf8')
    cursor = db.cursor()
    # 设定需要获取数据的股票池
    stock_pool = []
    stock_code_list = []
    try:
        get_stockpool = "select * from DataCollect_stock_pool where is_collect=1;"
        cursor.execute(get_stockpool)
        sp_res = cursor.fetchall()
        for sp in sp_res:
            stock_pool.append([sp[0],sp[4]])
            stock_code_list.append(sp[0])
    except Exception as err:
        print(err)
    total = len(stock_pool)
    update_list = "','".join(stock_code_list)
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        try:
            df = pro.daily(ts_code=stock_pool[i][0], start_date=stock_pool[i][1].strftime('%Y%m%d'), end_date=end_dt)
            # 打印进度
            print('Seq: ' + str(i+1) + ' of ' + str(total) + '   Code: ' + str(stock_pool[i][0]))
            c_len = df.shape[0]
        except Exception as aa:
            print(aa)
            print('No DATA Code: ' + str(i))
            continue
        for j in range(c_len):
            resu0 = list(df.iloc[c_len-1-j])
            resu = []
            for k in range(len(resu0)):
                if str(resu0[k]) == 'nan':
                    resu.append(-1)
                else:
                    resu.append(resu0[k])
            state_dt = (datetime.datetime.strptime(resu[1], "%Y%m%d")).strftime('%Y-%m-%d')
            create_time = datetime.datetime.now()
            try:
                sql_insert = "INSERT INTO DataCollect_stock_all(state_dt,stock_code,open,close,high,low,vol,amount,pre_close,amt_change,pct_change,create_time) VALUES ('%s', '%s', '%.2f', '%.2f','%.2f','%.2f','%i','%.2f','%.2f','%.2f','%.2f','%s')" % (state_dt,str(resu[0]),float(resu[2]),float(resu[5]),float(resu[3]),float(resu[4]),float(resu[9]),float(resu[10]),float(resu[6]),float(resu[7]),float(resu[8]),create_time)
                cursor.execute(sql_insert)
            except Exception as err:
                print(err)
                continue
    #更新股票池的最新采集数据时间
    try:
        sql_update = "UPDATE DataCollect_stock_pool set update_time = '%s' WHERE stock_code IN ('%s')" % (datetime.datetime.now(), update_list)
        cursor.execute(sql_update)
        db.commit()
    except Exception as err:
        print(err)

    cursor.close()
    db.close()
    print('All Finished!')

    return stock_code_list
