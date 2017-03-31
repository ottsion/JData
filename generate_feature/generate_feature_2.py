# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC

提取特征
    切片数据分为最后 2/4/6/8天
"""

import sys
sys.path.append("..")
sys.path.append('generate_dataSet')
sys.path.append('generate_feature')
sys.path.append('load_data')
from datetime import *
import generate_dataSet
import generate_feature
import pandas as pd

one_dataSet_train_path = 'data/one_dataSet_train.csv'
one_before_2_days_path = 'data/one_before_2_days.csv'
one_before_4_days_path = 'data/one_before_4_days.csv'
one_before_6_days_path = 'data/one_before_6_days.csv'
one_before_8_days_path = 'data/one_before_8_days.csv'

one_before_2_days_feature_path = 'data/one_before_2_days_feature.csv'
one_before_4_days_feature_path = 'data/one_before_4_days_feature.csv'
one_before_6_days_feature_path = 'data/one_before_6_days_feature.csv'
one_before_8_days_feature_path = 'data/one_before_8_days_feature.csv'

two_dataSet_train_path = 'data/two_dataSet_train.csv'
two_before_2_days_path = 'data/two_before_2_days.csv'
two_before_4_days_path = 'data/two_before_4_days.csv'
two_before_6_days_path = 'data/two_before_6_days.csv'
two_before_8_days_path = 'data/two_before_8_days.csv'

two_before_2_days_feature_path = 'data/two_before_2_days_feature.csv'
two_before_4_days_feature_path = 'data/two_before_4_days_feature.csv'
two_before_6_days_feature_path = 'data/two_before_6_days_feature.csv'
two_before_8_days_feature_path = 'data/two_before_8_days_feature.csv'

three_dataSet_train_path = 'data/three_dataSet_train.csv'
three_before_2_days_path = 'data/three_before_2_days.csv'
three_before_4_days_path = 'data/three_before_4_days.csv'
three_before_6_days_path = 'data/three_before_6_days.csv'
three_before_8_days_path = 'data/three_before_8_days.csv'

three_before_2_days_feature_path = 'data/three_before_2_days_feature.csv'
three_before_4_days_feature_path = 'data/three_before_4_days_feature.csv'
three_before_6_days_feature_path = 'data/three_before_6_days_feature.csv'
three_before_8_days_feature_path = 'data/three_before_8_days_feature.csv'


##############################################################################
#                   切片数据分为最后 2//4/6/8/10天                            #
##############################################################################
# 1. 切分数据集
# 2. 获得特征
def split_dataSet_and_generate_feature():
    #=============================第一数据集===================================
    #最后两天
    print u'处理第一数据集...' 
    begin_day = date(2016, 04, 04)
    end_day = date(2016, 04, 05)
    generate_dataSet.cut_data_as_time(one_dataSet_train_path, one_before_2_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(one_before_2_days_path, one_before_2_days_feature_path, item_brand,'_2')
    #最后四天
    begin_day = date(2016, 04, 02)
    end_day = date(2016, 04, 05)
    generate_dataSet.cut_data_as_time(one_dataSet_train_path, one_before_4_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(one_before_4_days_path, one_before_4_days_feature_path, item_brand,'_4')    
    #最后六天
    begin_day = date(2016, 03, 31)
    end_day = date(2016, 04, 05)
    generate_dataSet.cut_data_as_time(one_dataSet_train_path, one_before_6_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(one_before_6_days_path, one_before_6_days_feature_path, item_brand,'_6')    
    #最后八天
    begin_day = date(2016, 03, 29)
    end_day = date(2016, 04, 05)
    generate_dataSet.cut_data_as_time(one_dataSet_train_path, one_before_8_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(one_before_8_days_path, one_before_8_days_feature_path, item_brand,'_8')    
    #=============================第二数据集===================================
    #最后两天
    print u'处理第二数据集...' 
    begin_day = date(2016, 04, 9)
    end_day = date(2016, 04, 10)
    generate_dataSet.cut_data_as_time(two_dataSet_train_path, two_before_2_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(two_before_2_days_path, two_before_2_days_feature_path, item_brand,"_2")    
    #最后四天
    begin_day = date(2016, 04, 07)
    end_day = date(2016, 04, 10)
    generate_dataSet.cut_data_as_time(two_dataSet_train_path, two_before_4_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(two_before_4_days_path, two_before_4_days_feature_path, item_brand,"_4")    
    #最后六天
    begin_day = date(2016, 04, 05)
    end_day = date(2016, 04, 10)
    generate_dataSet.cut_data_as_time(two_dataSet_train_path, two_before_6_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(two_before_6_days_path, two_before_6_days_feature_path, item_brand,"_6")   
    #最后八天
    begin_day = date(2016, 04, 03)
    end_day = date(2016, 04, 10)
    generate_dataSet.cut_data_as_time(two_dataSet_train_path, two_before_8_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(two_before_8_days_path, two_before_8_days_feature_path, item_brand,"_8")    
    #=============================第三数据集===================================
    #最后两天
    print u'处理第三数据集...' 
    begin_day = date(2016, 04, 14)
    end_day = date(2016, 04, 15)
    generate_dataSet.cut_data_as_time(three_dataSet_train_path, three_before_2_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(three_before_2_days_path, three_before_2_days_feature_path, item_brand,'_2')    
    #最后四天
    begin_day = date(2016, 04, 12)
    end_day = date(2016, 04, 15)
    generate_dataSet.cut_data_as_time(three_dataSet_train_path, three_before_4_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(three_before_4_days_path, three_before_4_days_feature_path, item_brand,'_4')    
    #最后六天
    begin_day = date(2016, 04, 10)
    end_day = date(2016, 04, 15)
    generate_dataSet.cut_data_as_time(three_dataSet_train_path, three_before_6_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(three_before_6_days_path, three_before_6_days_feature_path, item_brand,'_6')    
    #最后八天
    begin_day = date(2016, 04, 8)
    end_day = date(2016, 04, 15)
    generate_dataSet.cut_data_as_time(three_dataSet_train_path, three_before_8_days_path , begin_day, end_day)
    item_brand = dict()
    generate_feature.fetch_feature(three_before_8_days_path, three_before_8_days_feature_path, item_brand,'_8')


# train_feature_path已有的   finnal_feature_data_path 最终的
def fetch_feature_2(train_feature_path, finnal_feature_data_path, index):
    

    train_feature_data = pd.read_csv(train_feature_path)
    print u'生成特征.....'
    # 先将新生成的特征存到一起：
    if index == 1:
        before_2_days_feature = pd.read_csv(one_before_2_days_feature_path)
        before_4_days_feature = pd.read_csv(one_before_4_days_feature_path)
        before_6_days_feature = pd.read_csv(one_before_6_days_feature_path)
        before_8_days_feature = pd.read_csv(one_before_8_days_feature_path)
    elif index == 2:
        before_2_days_feature = pd.read_csv(two_before_2_days_feature_path)
        before_4_days_feature = pd.read_csv(two_before_4_days_feature_path)
        before_6_days_feature = pd.read_csv(two_before_6_days_feature_path)
        before_8_days_feature = pd.read_csv(two_before_8_days_feature_path)
    else:
        before_2_days_feature = pd.read_csv(three_before_2_days_feature_path)
        before_4_days_feature = pd.read_csv(three_before_4_days_feature_path)
        before_6_days_feature = pd.read_csv(three_before_6_days_feature_path)
        before_8_days_feature = pd.read_csv(three_before_8_days_feature_path)
        
    new_data_df1 = pd.merge(before_2_days_feature, before_4_days_feature, on=['user_id','sku_id'], how='outer')
    new_data_df2 = pd.merge(before_6_days_feature, before_8_days_feature, on=['user_id','sku_id'], how='outer')
    new_data_df = pd.merge(new_data_df1, new_data_df2, on=['user_id','sku_id'], how='outer')
    
    print u'开始融合特征....'
    new_data = pd.merge(train_feature_data,new_data_df,on=['user_id','sku_id'],how='outer')  
    new_data.fillna(0)
    new_data.to_csv(finnal_feature_data_path, index=False)
    print u'fetch_feature_2 特征选择完成......存入:',finnal_feature_data_path
    
    
    
    
    
    
    
    
    
    
########################################################################################################
#                    好像没有正样本，这里测试看看
########################################################################################################
    
def fetch_sample(test_data_path, feature_data_path, negative_data_path,positive_data_path):
    buy = set()
    for line in csv.reader(file(test_data_path, 'rb')):
        if line[4] == '4':
            buy.add((line[0], line[1]))  # 正例集


    negative_file = file(negative_data_path, 'wb')
    negative_writer = csv.writer(negative_file)

    positive_file = file(positive_data_path, 'wb')
    positive_writer = csv.writer(positive_file)

    print 'open ',feature_data_path,'to add label'
    print len(buy)
    for line in csv.reader(file(feature_data_path, 'rb')):
        if line[0]=='user_id':
            line.extend('r')
            negative_writer.writerow((line))
            positive_writer.writerow((line))
        elif (line[0], line[1]) not in buy:
            line.append(0)
            negative_writer.writerow(line)  # 负例特征
        elif (line[0], line[1]) in buy:
            line.append(1)
            positive_writer.writerow(line)  # 正例特征
            print 'write positive'
    print u'正负样本分类并打好标签，分别存入:',one_negative_data_path,one_positive_data_path
    
def test():
    #测试第一数据集整理后正负样本情况，数据集情况
    before_2_days_feature = pd.read_csv(one_before_2_days_feature_path)
    before_4_days_feature = pd.read_csv(one_before_4_days_feature_path)
    before_6_days_feature = pd.read_csv(one_before_6_days_feature_path)
    before_8_days_feature = pd.read_csv(one_before_8_days_feature_path)
    # 大小情况
    print u'前两天的数据集大小：',before_2_days_feature.shape
    print u'前两天的数据集大小：',before_4_days_feature.shape
    print u'前两天的数据集大小：',before_6_days_feature.shape
    print u'前两天的数据集大小：',before_8_days_feature.shape
    
    # 查看各数据集正负样本情况
    
    
    new_data_df1 = pd.merge(before_2_days_feature, before_4_days_feature, on=['user_id','sku_id'], how='outer')
    new_data_df2 = pd.merge(before_6_days_feature, before_8_days_feature, on=['user_id','sku_id'], how='outer')
    new_data_df = pd.merge(new_data_df1, new_data_df2, on=['user_id','sku_id'], how='outer')