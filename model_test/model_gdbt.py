# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC


"""
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_fscore_support
 
 

one_train_dataSet_final_path = 'data/one_train_dataSet_final.csv'
two_train_dataSet_final_path = 'data/two_train_dataSet_final.csv'
train_one_and_two_result_as_proba_path = 'data/train_one_and_two_result_as_proba.csv'

train_two_train_feature_path = 'data/train_two_train_feature.csv'

train_three_train_feature_path = 'data/train_three_train_feature.csv'
three_train_dataSet_path =train_three_train_feature_path
train_three_result_as_proba_path = 'data/train_three_result_as_proba.csv'
three_before_answer_path = 'data/three_before_answer.csv'
three_answer_path = 'data/three_answer.csv'

two_before_answer_path = 'data/two_before_answer.csv'
two_answer_path = 'data/two_answer.csv'

train_two_result_as_proba_path = 'data/train_two_result_as_proba.csv'

# GBDT_classify(one_train_dataSet_final_path, two_train_dataSet_final_path, train_one_and_two_result_as_proba_path)
# classify_user_item(one_train_dataSet_path, 
#                    two_train_dataSet_path, 
#                    train_one_and_two_result_as_proba_path)
one_train_dataSet_path = 'data/one_train_dataSet.csv'
two_train_dataSet_path = 'data/two_train_dataSet.csv'
def GBDT_classify(train_dataSet_path, test_dataSet_path, train_one_and_two_result_as_proba_path):
    
    train_data = pd.read_csv(train_dataSet_path)
    train_data = train_data.as_matrix()
    X_train = train_data[:, 2:-1]  # select columns 0 through end-1
    y_train = train_data[:, -1]  # select column end

    test_data = pd.read_csv(test_dataSet_path)
    test_data = test_data.as_matrix()
    X_test = test_data[:, 2:-1]  # select columns 0 through end-1
    y_test = test_data[:, -1]  # select column end 
    
    clf = GradientBoostingClassifier(n_estimators=200)
    clf.fit(X_train, y_train)
    pre_y_test = clf.predict_proba(X_test)
    print pre_y_test
    print("GBDT Metrics : {0}".format(precision_recall_fscore_support(y_test, pre_y_test)))
    
    print u'保存结果.....'
    f_result = open(test_dataSet_prob_path, 'w')
    for i in range(0, len(pre_y_test)):
        if i==0:
            print str(pre_y_test[i][0])
        if i==len(pre_y_test)-1:
            print str(pre_y_test[i][0])
        f_result.write(str(pre_y_test[i][0]) + '\n')   

    return clf
    
def classify(clf, train_dataSet_path, result_proba_path):
    data1 = pd.read_csv(train_dataSet_path)
    data1 = data1.as_matrix()
    X_test = data1[:, 2:]
    result = clf.predict_proba(X_test)
    print u'预测结束.....'

    f_result = open( result_proba_path, 'w')
    print 'len(result):', len(result)
    for i in range(0, len(result)):
        f_result.write(str(result[i][0]) + '\n')
        
        
        
'''
接收数据集和对应的target概率，返回的是[user_id, sku_id, pre]   pre为概率
'''
def combine_tar_and_pre(dataSet_path, proba_path, before_answer_path):
    data = pd.read_csv(dataSet_path)
    target = pd.read_csv(proba_path, names='p')

    combine_tar_pre = pd.concat([data,target],axis=1)
    s = pd.concat([combine_tar_pre.user_id, combine_tar_pre.sku_id,combine_tar_pre.p], axis=1)
    ss = s[s.p <= 0.3]
    ss.to_csv(before_answer_path)

# 根据各个概率值选择合适的用户商品对，作为最后答案
def get_final_answer(before_answer_path, answer_path):
    data = open(before_answer_path)
    user_list = []
    data.readline()
    temp = {}
    lines = data.readlines()
    for line in lines:
        # 10,16579,66638,0,0.29\n
        info = []
        arr = line.strip().split(',')
        if arr[1] not in user_list:
            user_list.append(arr[1])
            info.append(arr[2])
            info.append(arr[-1])
            temp[arr[1]] = info
        else:
            info_set = temp[arr[1]]
            if info_set[-1] > arr[-1]:
                new_info = []
                new_info.append(arr[2])
                new_info.append(arr[-1])
                temp[arr[1]] = new_info

    answer = open(answer_path,'w')
    string = ('user_id'+","+'sku_id'+'\n')
    answer.write(string)
    for key in temp.keys():
        sss = key+',' +temp[key][0]+'\n'
        answer.write(sss)
    answer.close()

# 最终得出用户商品键值对
# (three_train_dataSet_path, train_three_result_as_proba_path, three_before_answer_path, three_answer_path)
def output_answer(dataSet_path, proba_path, before_answer_path, answer_path):
    combine_tar_and_pre(dataSet_path, proba_path, before_answer_path)
    get_final_answer(before_answer_path, answer_path)
        