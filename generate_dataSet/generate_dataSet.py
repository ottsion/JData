# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC

用来提取数据：
1.全部数据
2.只包含在P中的数据

generate_dataSet.py
"""


from datetime import *

all_dataSet_path = 'data/all_dataSet.csv'
one_dataSet_train_path = 'data/one_dataSet_train.csv'
one_dataSet_test_path = 'data/one_dataSet_test.csv'
two_dataSet_train_path = 'data/two_dataSet_train.csv'
two_dataSet_test_path = 'data/two_dataSet_test.csv'
three_dataSet_train_path = 'data/three_dataSet_train.csv'

# 切分三个数据集
# 以2016-03-10到2016-04-05数据   预测2016-04-06到2016-04-10某用户是否下单某商品
# 以2016-03-15到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
# 以2016-03-20到2016-04-15数据   预测2016-04-16到2016-04-20某用户是否下单某商品


def generate_dataSet():
    print u'开始划分数据集.....'
    # 以2016-03-10到2016-04-05数据   预测2016-04-06到2016-04-10某用户是否下单某商品
    # begin_day = date(2016, 03, 10)
    begin_day = date(2016, 03, 17)
    end_day = date(2016, 04, 05)
    cut_data_as_time(all_dataSet_path, one_dataSet_train_path , begin_day, end_day)
    # begin_day = date(2016, 04, 06)
    begin_day = date(2016, 04, 06)
    end_day = date(2016, 04, 10)
    cut_data_as_time(all_dataSet_path, one_dataSet_test_path , begin_day, end_day)    
    print u'第一数据集(包括数据集和结果集)划分完成.....'
    # 以2016-03-15到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
    # begin_day = date(2016, 03, 15)
    begin_day = date(2016, 03, 22)
    end_day = date(2016, 04, 10)
    cut_data_as_time(all_dataSet_path, two_dataSet_train_path , begin_day, end_day)
    begin_day = date(2016, 04, 11)
    end_day = date(2016, 04, 15)
    cut_data_as_time(all_dataSet_path, two_dataSet_test_path , begin_day, end_day)
    print u'第二数据集(包括数据集和结果集)划分完成.....'
    # 以2016-03-20到2016-04-15数据   预测2016-04-16到2016-04-20某用户是否下单某商品
    # begin_day = date(2016, 03, 20)
    begin_day = date(2016, 03, 27)
    end_day = date(2016, 04, 15)
    cut_data_as_time(all_dataSet_path, three_dataSet_train_path , begin_day, end_day)
    print u'第三数据集(包括数据集和结果集)划分完成......'
    print u'成功划分三个数据集.....'
    
'''
# 从dataSet_path中按照 BEGINDAY, ENDDAY 拆分数据集
    #以2016-03-17到2016-04-05数据   预测2016-04-06到2016-04-10某用户是否下单某商品
    #以2016-03-22到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
    #以2016-03-27到2016-04-15数据   预测2016-04-16到2016-04-20某用户是否下单某商品
    
    # 以2016-03-10到2016-04-05数据   预测2016-04-06到2016-04-10某用户是否下单某商品
    # 以2016-03-15到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
    # 以2016-03-20到2016-04-15数据   预测2016-04-16到2016-04-20某用户是否下单某商品
'''
def cut_data_as_time(dataSet_path, new_dataSet_path , begin_day, end_day):
    raw_file = open(dataSet_path)
    t_all = open(new_dataSet_path, 'w')
    column_name = raw_file.readline()  # 读出栏位名
    t_all.write(column_name)
    for line in raw_file:

        entry = line.split(",")
        # user_id, sku_id, time, model_id, type, cate, brand,
        entry_date = date(*parse_date(entry[2]))
        if entry_date <= end_day and entry_date >= begin_day:
            t_all.write(line)
    t_all.close()
    raw_file.close()
    print u'根据起始和结束时间将数据集取出完成，存入:',new_dataSet_path
# 解析日期
def parse_date(raw_date):
    entry_date = raw_date
    year, month, day = entry_date.split(" ")[0].split("-")
    return int(year), int(month), int(day)
    
    
    

    
    
    