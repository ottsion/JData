#!/usr/bin/env python2
# -*- coding: utf-8-*-
"""
created on 
@author: sunfc
------------------
负样本太大,抽取部分负样本作为训练数据集

"""

import csv



'''
# train_one_label_data_path, train_one_train_feature_path, 'one_'
# ['user_id', 'sku_id', 'time', 'model_id', 'type', 'cate', 'brand']
# 1.浏览（指浏览商品详情页）；2.加入购物车；3.购物车删除；4.下单；5.关注；6.点击
'''
# fetch_sample(one_dataSet_test_path, train_one_train_feature_path, one_negative_data_path,one_positive_data_path)
# 获得正负样本，并且为每个样本添加target，分别保存在正样本、负样本文本中
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
    print u'正负样本分类并打好标签，分别存入:',negative_data_path,positive_data_path



# 抽取部分负样本作为训练数据集
def fetch_negative_sample(negative_data_path, new_negative_data_path):
    num = 1
    csvfile = file(new_negative_data_path, 'wb')
    writer = csv.writer(csvfile)
    for line in csv.reader(file(negative_data_path, 'r')):
        if num==1:
            writer.writerow(line)
        elif num % 200 == 0:
            writer.writerow(line)
        num = num + 1
    print num
    print u'挑选部分负样本，存入:',new_negative_data_path

# 正负样本融合在一起构成训练集
def combine_neg_and_posi(negative_data_path, positive_data_path, train_dataSet_path):
    negative_data = open(negative_data_path, 'r')
    positive_data = open(positive_data_path, 'r')
    train_dataSet = open(train_dataSet_path, 'wb') 
    train_dataSet.write(negative_data.readline())
    for line in negative_data.readlines():
        if line.strip().split(',')[0] =='user_id':
            continue
        else:
            train_dataSet.write(line)
    for line in positive_data.readlines():
        if line.strip().split(',')[0] =='user_id':
            continue
        else:
            train_dataSet.write(line)
    print u'正负样本融合，存入:',train_dataSet_path
            
            
            

train_one_train_feature_path = 'data/train_one_train_feature.csv'
train_two_train_feature_path = 'data/train_two_train_feature.csv'
train_three_train_feature_path = 'data/train_three_train_feature.csv' 

one_dataSet_test_path = 'data/one_dataSet_test.csv'
two_dataSet_test_path = 'data/two_dataSet_test.csv'

one_negative_data_path = 'data/one_negative.csv'
one_negative_data_after_sampling_path = 'data/one_negative_data_after_sampling.csv'
one_positive_data_path = 'data/one_positive.csv'
one_train_dataSet_final_path = 'data/one_train_dataSet_final.csv'

two_negative_data_path = 'data/two_negative.csv'
two_negative_data_after_sampling_path = 'data/two_negative_data_after_sampling.csv'
two_positive_data_path = 'data/two_positive.csv'
two_train_dataSet_final_path = 'data/two_train_dataSet_final.csv'
         
def main_combine():
    ####################################################################
    #                           打上标签                                #
    ####################################################################
    print u'开始打上标签.....'
    # 以2016-03-01到2016-04-05数据   预测2016-04-06到2016-04-10某用户是否下单某商品
    fetch_sample(one_dataSet_test_path, train_one_train_feature_path, one_negative_data_path,one_positive_data_path)
    print u'第一数据集标签完成.....'
    # 以2016-03-06到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
    fetch_sample(two_dataSet_test_path, train_two_train_feature_path, two_negative_data_path,two_positive_data_path)
    print u'第二数据集标签完成.....'
    print u'成功打上标签.....'
    ####################################################################
    #                      抽取正负样本组成训练集                       #
    ####################################################################
    print u'开始抽取正负样本组成训练集.....one'
    # 抽取部分负数据集作为负样本
    fetch_negative_sample(one_negative_data_path, one_negative_data_after_sampling_path)
    # 融合正负样本数据作为训练集
    combine_neg_and_posi(one_negative_data_after_sampling_path, one_positive_data_path,
                                                    one_train_dataSet_final_path)
    print u'成功抽取正负样本组成训练集.....one'
    print u'开始抽取正负样本组成训练集.....two'
    # 抽取部分负数据集作为负样本
    fetch_negative_sample(two_negative_data_path, two_negative_data_after_sampling_path)
    # 融合正负样本数据作为训练集
    combine_neg_and_posi(two_negative_data_after_sampling_path, two_positive_data_path,
                                                    two_train_dataSet_final_path)
    print u'成功抽取正负样本组成训练集.....two'
            
            
 

################################################################################
#             根据各个数据集正样本抽取出真实答案样本
################################################################################
one_dataSet_test_path = 'data/one_dataSet_test.csv'
one_test_positive_data_path = 'data/one_test_positive.csv'

two_dataSet_test_path = 'data/two_dataSet_test.csv'
two_test_positive_data_path = 'data/two_test_positive.csv'
one_test_real_path = 'data/one_real.csv'
two_test_real_path = 'data/two_real1.csv'


def fetch_sample_test_for_real_answer(test_data_path, positive_data_path):
    positive_data = open(positive_data_path, 'w')

    for line in csv.reader(file(test_data_path, 'rb')):
        if line[0]=='user_id':
            lineStr = 'user_id, sku_id  \n'
            positive_data.write(lineStr)
        if line[4] == '4':
            lineStr = line[0] +","+line[1]+"\n"
            positive_data.write(lineStr)  
def get_real_answer():
    fetch_sample_test_for_real_answer(one_dataSet_test_path, one_test_real_path)
    fetch_sample_test_for_real_answer(two_dataSet_test_path, two_test_real_path)




    
    
    
