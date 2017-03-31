# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC

"""

import sys
sys.path.append("..")
sys.path.append('generate_feature')
import generate_feature
import generate_feature_1
import generate_feature_2
import pandas as pd


all_dataSet_path = 'data/all_dataSet.csv'
one_dataSet_path_train = 'data/one_dataSet_train.csv'
two_dataSet_path_train = 'data/two_dataSet_train.csv'
three_dataSet_path_train = 'data/three_dataSet_train.csv'

train_one_train_feature_path_pre1 = 'data/train_one_train_feature_pre1.csv'
train_one_train_feature_path_pre2 = 'data/train_one_train_feature_pre2.csv'
train_one_train_feature_path = 'data/train_one_train_feature.csv'

train_two_train_feature_path_pre1 = 'data/train_two_train_feature_pre1.csv'
train_two_train_feature_path_pre2 = 'data/train_two_train_feature_pre2.csv'
train_two_train_feature_path = 'data/train_two_train_feature.csv'

train_three_train_feature_path_pre1='data/train_three_train_feature_pre1.csv'
train_three_train_feature_path_pre2='data/train_three_train_feature_pre2.csv'
train_three_train_feature_path = 'data/train_three_train_feature.csv'


####################################################################
#                         生成特征维度集                            #
####################################################################
def generate_all_feature():
    print u'开始生成特征维度集.....'
    # 以2016-03-10到2016-04-05数据   预测2016-04-06到2016-04-10某用户是否下单某商品
    item_brand = dict()
    generate_feature.fetch_feature(one_dataSet_path_train, train_one_train_feature_path_pre1, item_brand,'')
    generate_feature_1.fetch_feature_1(train_one_train_feature_path_pre1, train_one_train_feature_path)  
    #generate_feature_2.fetch_feature_2(train_one_train_feature_path_pre2,train_one_train_feature_path,1)
    print u'第一数据集完成.....'
    # 以2016-03-15到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
    item_brand = dict()
    generate_feature.fetch_feature(two_dataSet_path_train, train_two_train_feature_path_pre1, item_brand,'')
    generate_feature_1.fetch_feature_1(train_two_train_feature_path_pre1, train_two_train_feature_path)
    #generate_feature_2.fetch_feature_2(train_two_train_feature_path_pre2,train_two_train_feature_path,2)
    print u'第二数据集完成.....'
    # 以2016-03-20到2016-04-15数据   预测2016-04-16到2016-04-20某用户是否下单某商品
    item_brand = dict()
    generate_feature.fetch_feature(three_dataSet_path_train, train_three_train_feature_path_pre1,item_brand,'')
    generate_feature_1.fetch_feature_1(train_three_train_feature_path_pre1, train_three_train_feature_path)
    #generate_feature_2.fetch_feature_2(train_three_train_feature_path_pre2,train_three_train_feature_path,3)
    print u'第三数据集完成.....'
    print u'成功生成特征维度集(部分数据附带NaN,已做0处理 ).....'
    