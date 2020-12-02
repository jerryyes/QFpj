# -*- coding: utf-8 -*-
# @Author  : chenzhiyuan

from QFpj.dataComparison.basic_compare import BasicCompare
import datetime
import decimal
import logging


class MysqlCompare(BasicCompare):
    def __init__(self, old, new, params, filters, save_detail):
        BasicCompare.__init__(self, save_detail)
        self.old = old
        self.new = new
        self.params = params
        self.filters = filters

    def common(self, _mysql, table, special_filter):
        fields_idx = _mysql.fieldIdx(table)
        fields = self.toLower([key for key in fields_idx.keys()])
        fields = self.listSort(self.listFilter(fields, special_filter))
        count = _mysql.count(table)
        return fields_idx, fields, count

    def LoadData(self, sql, _mysql, fields):
        all_data = []
        rsp = _mysql.excute(sql)
        if rsp is None:
            pass
        else:
            for sin_tup in rsp:
                ary = []
                for index in range(len(fields)):
                    value = sin_tup[index]
                    if value is None:
                        ary.append('')
                    elif isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
                        ary.append(value.isoformat())
                    elif isinstance(value, decimal.Decimal):
                        ary.append(str(float(value)))
                    else:
                        ary.append(str(value))
                all_data.append(self.md5('|'.join(ary)))
        return all_data

    def loadAllDataDict(self, table, fields, _mysql):
        sql = 'select %s from %s' % (','.join(fields), table)
        all_data = self.LoadData(sql, _mysql, fields)
        logging.info('len_%s' % len(all_data))
        return self.listToDict(all_data)

    def loadPartDataDict(self, table, fields, _mysql, special_filter, idx):
        if len(idx) <= 0:
            idx = self.loadIndex(table, _mysql)
            idx = self.listFilter(idx, special_filter)
        if len(idx) >= 0:
            sql = 'select %s from %s order by %s desc limit 0,5000000' % (','.join(fields), table, idx[0])
        else:
            sql = 'select %s from %s limit 0,5000000' % (','.join(fields), table)
        all_data = self.LoadData(sql, _mysql, fields)
        logging.info('len_%s' % len(all_data))
        return self.listToDict(all_data), len(idx) >= 0

    def loadIndex(self, table, _mysql):
        # Column_name is in the 5th
        # Key_name is in the 3rd
        sql = 'show index from %s' % table
        rsp = _mysql.excute(sql)
        idx = []
        if rsp is None:
            pass
        else:
            for single in rsp:
                if len(single) >= 5:
                    if str(single[2]) == 'PRIMARY' and str(single[4]) != '':
                        idx = [str(single[4])] + idx
                    else:
                        idx.append(str(single[4]))
        return idx

    def run(self):
        mysql_result = {}
        for db in self.params.keys():
            for part in self.params[db]:
                for table in self.params[db][part]:
                    # both all use
                    special_filter = self.loadFilter(db, part, table)
                    index_idx = self.loadIdx(db, part, table)
                    try:

                        diff = {}
                        diff['time'] = {'btime': datetime.datetime.now().isoformat()}
                        # old part
                        old_fields_idx, old_fields, old_count = self.common(self.old, table, special_filter)
                        logging.info(
                            'old part table[%s] count[%s] fields[%s]' % (table, old_count, ','.join(old_fields)))
                        # new part
                        new_fields_idx, new_fields, new_count = self.common(self.new, table, special_filter)
                        logging.info(
                            'new part table[%s] count[%s] fields[%s]' % (table, new_count, ','.join(new_fields)))

                        diff['count'] = self.compareCount(old_count, new_count)
                        diff['field'] = self.compreFields(old_fields, new_fields)
                        if diff['field']['isSame'] is True:
                            diff['field_idx'] = self.compareType(old_fields, old_fields_idx, new_fields_idx)
                        if diff['field']['isSame'] is True and 'field_idx' in diff.keys() and diff['field_idx'][
                            'isSame'] is True:
                            mini_count = min(old_count, new_count)
                            old_possess_idx = True
                            new_possess_idx = True
                            if mini_count <= 500 * 10000:
                                # 当数据量比较小的时候全量数据
                                old_data = self.loadAllDataDict(table, old_fields, self.old)
                                new_data = self.loadAllDataDict(table, new_fields, self.new)
                            else:
                                # 当数据量比较大的时候则是截取一部分比较即可
                                old_data, old_possess_idx = self.loadPartDataDict(table, old_fields, self.old,
                                                                                  special_filter, index_idx)
                                new_data, new_possess_idx = self.loadPartDataDict(table, new_fields, self.new,
                                                                                  special_filter, index_idx)
                            diff['data'] = self.compareDetail(old_data, new_data)
                            diff['data']['old_possess_idx'] = old_possess_idx
                            diff['data']['new_possess_idx'] = new_possess_idx
                        diff['time']['etime'] = datetime.datetime.now().isoformat()
                        mysql_result[table] = diff

                    except Exception as e:
                        logging.error('call db[%s] part[%s] table[%s] error[%s]' % (db, part, table, e))
        logging.info('compre result %s' % (mysql_result))

        self.saveData(datas=mysql_result)
        self.saveReport(datas=mysql_result)


if __name__ == '__main__':
    pass
