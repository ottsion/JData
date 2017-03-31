#!/usr/bin/env python2
# -*- coding: utf-8-*-
"""
created on 
@author: sunfc
------------------

"""


from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cross_validation, metrics
import numpy as np
import pandas as pd
from sklearn.grid_search import GridSearchCV

def classify_user_item(train_data_path, test_data_path, result_as_proba_path):
    data = pd.read_csv(train_data_path)
    data = data.as_matrix()
    X = data[:, 2:-1]  # select columns 0 through end-1
    y = data[:, -1]  # select column end
    print 'len(X):',len(X)
    print 'len(y):',len(y)
    print u'开始训练数据.....'
    clf2 = RandomForestClassifier(oob_score=True, random_state=10)
    # clf2=GradientBoostingClassifier()
    clf2.fit(X, y)
    # clf2 = LogisticRegression().fit(X, y)
    print clf2.oob_score_
    
    y_predprob = clf2.predict_proba(X)[:,1]
    print "AUC Score (Train): %f" % metrics.roc_auc_score(y, y_predprob)
    print clf2.classes_
    
    print u'结束训练数据.....'
    print u'载入测试数据.....'
    data1 = pd.read_csv(test_data_path)
    data1 = data1.as_matrix()
    X_test = data1[:, 2:-1]
    print len(X_test)
    print u'开始测试.....'
    result = clf2.predict_proba(X_test)
    print u'测试结束.....'

    print u'保存结果.....'
    f_result = open(result_as_proba_path, 'w')
    print 'len(result):',len(result)
    for i in range(0, len(result)):
        if i==0:
            print str(result[i][0])
        if i==len(result)-1:
            print str(result[i][0])
        f_result.write(str(result[i][0]) + '\n')
    return clf2
    
    
    
# two_train_dataSet_path
def RF_tiaocan(train_data_path, test_data_path, result_as_proba_path):
    data = pd.read_csv(train_data_path)

    data = data.as_matrix()
    X = data[:, 2:-1]  # select columns 0 through end-1
    y = data[:, -1]  # select column end
    print 'len(X):',len(X)
    print 'len(y):',len(y)
    print u'开始训练数据.....'
    ###############################################################################
    # 对n_estimators进行网格搜索  
    ###############################################################################
    param_test1 = {'n_estimators':range(70,150,10)}
    gsearch1 = GridSearchCV(estimator = RandomForestClassifier(min_samples_split=100,
                                      min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10), 
                           param_grid = param_test1, scoring='roc_auc',cv=5)
    gsearch1.fit(X,y)
    gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_   
    
    ###############################################################################
    # 对max_depth进行网格搜索  
    ###############################################################################
    param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(50,201,20)}
    gsearch2 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 130, 
                                  min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10),
    param_grid = param_test2, scoring='roc_auc',iid=False, cv=5)
    gsearch2.fit(X,y)
    gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_


    # 测试是否有效提高
    rf1 = RandomForestClassifier(n_estimators= 130, max_depth=11, min_samples_split=110,
                                  min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10)
    rf1.fit(X,y)
    print rf1.oob_score_
    # 0.899313350059
    
    ###############################################################################
    # 对min_samples_split、min_samples_leaf进行网格搜索    
    ###############################################################################    
    param_test3 = {'min_samples_split':range(80,150,20), 'min_samples_leaf':range(10,60,10)}
    gsearch3 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 130, max_depth=11,
                                  max_features='sqrt' ,oob_score=True, random_state=10),
    param_grid = param_test3, scoring='roc_auc',iid=False, cv=5)
    gsearch3.fit(X,y)
    gsearch3.grid_scores_, gsearch2.best_params_, gsearch2.best_score_
    
    
    ###############################################################################
    # 最大特征数max_features做调参 
    ###############################################################################      
    param_test4 = {'max_features':range(30,70,5)}
    gsearch4 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 130, max_depth=11, min_samples_split=80,
                                      min_samples_leaf=10 ,oob_score=True, random_state=10),
    param_grid = param_test4, scoring='roc_auc',iid=False, cv=5)
    gsearch4.fit(X,y)
    gsearch4.grid_scores_, gsearch4.best_params_, gsearch4.best_score_
    
    
    # 测试
    rf2 = RandomForestClassifier(n_estimators= 130, max_depth=11, min_samples_split=80,
                                  min_samples_leaf=10,max_features=30 ,oob_score=True, random_state=10)
    rf2.fit(X,y)
    print rf2.oob_score_
    # 0.906245873498
    ###############################################################################
    
    
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
    ss = s[s.p <= 0.7]
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
    
if __name__=='__main__':
    
    clf = classify_user_item(one_train_dataSet_final_path, two_train_dataSet_final_path, 
                             train_one_and_two_result_as_proba_path)
                             
    classify(clf, train_two_train_feature_path, train_two_result_as_proba_path)      
    output_answer(train_two_train_feature_path, train_two_result_as_proba_path, 
                  two_before_answer_path, two_answer_path)
    
    classify(clf, three_train_dataSet_path, train_three_result_as_proba_path)
    output_answer(train_three_train_feature_path, train_three_result_as_proba_path,
                  three_before_answer_path, three_answer_path)