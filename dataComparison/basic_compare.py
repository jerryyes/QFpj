# -*- coding: utf-8 -*-
# @Author  : chenzhiyuan


import json
import hashlib
import csv
import logging


class BasicCompare:
    def __init__(self, save_detail):
        self.save_detail = save_detail

    def md5(self, msg):
        _md5 = hashlib.md5()
        _md5.update(msg.encode(encoding='utf-8'))
        return _md5.hexdigest()

    def compareList(self, from_list, target_list):
        if len(from_list) != len(target_list):
            return False
        for single in from_list:
            if single not in target_list:
                return False
        return True

    # 比较大小
    def compareCount(self, old_count, new_count):
        ret = {
            'old_count': old_count,
            'new_count': new_count,
        }

        if old_count != new_count:
            ret['isSame'] = False
        else:
            ret['isSame'] = True
        return ret

    # 比较字段内容
    def compreFields(self, old_fields, new_fields):
        if self.compareList(old_fields, new_fields) is False:
            return {
                'old_field': old_fields,
                'new_field': new_fields,
                'isSame': False,
            }
        return {'isSame': True}

    # 比较字段类型
    def compareType(self, fields, old_fields_idx, new_fields_idx):
        def toLowerDict(idx):
            ret = {}
            for key, value in idx.items():
                ret[key.lower()] = value
            return ret

        old_fields_idx = toLowerDict(old_fields_idx)
        new_fields_idx = toLowerDict(new_fields_idx)
        for field in fields:
            if old_fields_idx[field].strip(' ') != new_fields_idx[field].strip(' '):
                return {
                    'key': field,
                    'old_idx': old_fields_idx[field],
                    'new_idx': new_fields_idx[field],
                    'isSame': False,
                }
        return {'isSame': True}

    # 比较文本内容
    def compareDetail(self, old_data, new_data):
        both = 0
        not_equal = 0
        new_own = {}
        old_own = {}

        for _md5 in old_data.keys():
            if _md5 in new_data.keys():
                both += 1
                if old_data[_md5] != new_data[_md5]:
                    not_equal += 1
            else:
                old_own[_md5] = old_data[_md5]

        for _md5 in new_data.keys():
            if _md5 not in old_data.keys():
                new_own[_md5] = new_data[_md5]

        ret = {
            'both': both,
            'not_equal': not_equal,
            'new_own': new_own,
            'old_own': old_own,
            'new_own_len': len(new_own),
            'old_own_len': len(old_own),
        }

        if self.save_detail is False:
            del ret['new_own']
            del ret['old_own']

        return ret

    def saveData(self, filename='save.csv', datas={}):
        def formateDict(dict_tmp):
            ret = {}
            for key, value in dict_tmp.items():
                ret[key] = json.dumps(value)
            return ret

        fieldnamesIdx = {}
        for key, value_dict in datas.items():
            for key in value_dict.keys():
                fieldnamesIdx[key] = 1
        fieldnames = ['table'] + [key for key in fieldnamesIdx.keys()]
        with open(filename, 'w', newline='') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for table, data in datas.items():
                tmp = formateDict(data)
                tmp['table'] = table
                writer.writerow(tmp)

    def saveReport(self, filename='report.csv', datas={}, t='mysql'):
        fieldnames = ['table', 'type', 'old_count', 'new_count', 'field', 'field_idx', 'both', 'not_equal', 'old_own',
                      'new_own', 'btime', 'etime']

        def val(data, val1, val2):
            try:
                return data[val1][val2]
            except:
                return ''

        def formate(table, data):
            logging.info('formate %s' % data)
            ret = {}
            ret['type'] = t
            ret['table'] = table
            ret['old_count'] = val(data, 'count', 'old_count')
            ret['new_count'] = val(data, 'count', 'new_count')
            ret['field'] = val(data, 'field', 'isSame')
            ret['field_idx'] = val(data, 'field_idx', 'isSame')
            ret['both'] = val(data, 'data', 'both')
            ret['not_equal'] = val(data, 'data', 'not_equal')
            ret['old_own'] = val(data, 'data', 'old_own_len')
            ret['new_own'] = val(data, 'data', 'new_own_len')
            ret['btime'] = val(data, 'time', 'btime')
            ret['etime'] = val(data, 'time', 'etime')
            logging.info('formate2 %s' % ret)
            return ret

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for table, data in datas.items():
                writer.writerow(formate(table, data))

    def listFilter(self, from_list, filter_list):
        ret_list = []
        for single in from_list:
            if single not in filter_list:
                ret_list.append(single)
        return ret_list

    def listSort(self, list1):
        return sorted(list1, reverse=True)

    def toLower(self, p):
        ret = []
        if p is None:
            ret = []
        if isinstance(p, list):
            for single in p:
                ret.append(str(single).lower())
        else:
            return ret.append(str(p).lower())
        return ret

    def listToDict(self, all_data):
        ret_dict = {}
        for single in all_data:
            if single in ret_dict.keys():
                ret_dict[single] += 1
            else:
                ret_dict[single] = 1
        return ret_dict

    def loadFilter(self, db, part, table):
        try:
            special_filter = self.params[db][part][table]['filter_field'] + self.filters
        except:
            special_filter = self.filters
        return special_filter

    def loadIdx(self, db, part, table):
        try:
            index_idx = self.params[db][part][table]['idx']
        except:
            index_idx = []
        return index_idx


if __name__ == '__main__':
    import time

    action_time = int(time.time() * 1000)
    b = BasicCompare(False)
    dict_1 = {}
    for i in range(0, 3000):
        dict_1[b.md5(str(i))] = 1
    dict_2 = {}
    for i in range(1501, 4500):
        dict_2[b.md5(str(i))] = 1

    own_1 = 0
    own_2 = 0
    both = 0
    for key in dict_1.keys():
        if key not in dict_2.keys():
            own_1 += 1
        else:
            both += 1
    for key in dict_2.keys():
        if key not in dict_1.keys():
            own_2 += 1
    print('own_1[%s] own_2[%s] both[%s]' % (own_1, own_2, both))

    end_time = int(time.time() * 1000)

    print('cost %s seconds' % ((end_time - action_time) / 1000))

    pass
