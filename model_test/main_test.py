# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC


"""
import sys
sys.path.append("..")
sys.path.append('load_data')
sys.path.append('generate_dataSet')
sys.path.append('generate_feature')
sys.path.append('combine_neg_pos')
sys.path.append('model_test')
import load_data
import generate_dataSet
import combine_feature_dataSet
import main_generate_feature
import model_rf
import ceshiyanzheng

# 装载数据 
month_3_data_path = 'input/JData_Action_201603.csv' 
month_3_extra_data_path = 'input/JData_Action_201603_extra.csv'
month_4_data_path = 'input/JData_Action_201604.csv'
month_34_all_data_path = 'data/month_34_all_data.csv'
all_dataSet_path = 'data/all_dataSet.csv'

# 生成不同数据集 
all_dataSet_path = 'data/all_dataSet.csv'
one_dataSet_train_path = 'data/one_dataSet_train.csv'
one_dataSet_test_path = 'data/one_dataSet_test.csv'
two_dataSet_train_path = 'data/two_dataSet_train.csv'
two_dataSet_test_path = 'data/two_dataSet_test.csv'
three_dataSet_train_path = 'data/three_dataSet_train.csv'

# 合并正负数据集
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

#  特征生成
all_dataSet_path = 'data/all_dataSet.csv'
one_dataSet_path_train = 'data/one_dataSet_train.csv'
two_dataSet_path_train = 'data/two_dataSet_train.csv'
three_dataSet_path_train = 'data/three_dataSet_train.csv'

train_one_train_feature_path_pre1 = 'data/train_one_train_feature_pre1.csv'
train_one_train_feature_path = 'data/train_one_train_feature.csv'

train_two_train_feature_path_pre1 = 'data/train_two_train_feature_pre1.csv'
train_two_train_feature_path = 'data/train_two_train_feature.csv'

train_three_train_feature_path_pre1='data/train_three_train_feature_pre1.csv'
train_three_train_feature_path = 'data/train_three_train_feature.csv'

#  模型预估  
# one_train_dataSet_final_path = 'data/one_train_dataSet_final.csv'
# two_train_dataSet_final_path = 'data/two_train_dataSet_final.csv'
train_one_and_two_result_as_proba_path = 'data/train_one_and_two_result_as_proba.csv'
# train_two_train_feature_path = 'data/train_two_train_feature.csv'
# train_three_train_feature_path = 'data/train_three_train_feature.csv'
three_train_dataSet_path =train_three_train_feature_path

train_three_result_as_proba_path = 'data/train_three_result_as_proba.csv'
three_before_answer_path = 'data/three_before_answer.csv'
three_rf_answer_path = 'data/three_answer_rf.csv'

train_two_result_as_proba_path = 'data/train_two_result_as_proba.csv'
two_before_answer_path = 'data/two_before_answer.csv'
two_answer_path = 'data/two_answer.csv'

train_one_result_as_proba_path = 'data/train_one_result_as_proba.csv'
one_before_answer_path = 'data/one_before_answer.csv'
one_answer_path = 'data/one_answer.csv'


two_real_path = 'data/two_real.csv'
one_real_path = 'data/one_real.csv'





if __name__=='__main__':
    ###############################################################################
    #                               装载数据                                       #
    ###############################################################################
    load_data.load_data(month_3_data_path, month_3_extra_data_path, month_4_data_path,month_34_all_data_path)
    load_data.clean_unNormal_data(all_dataSet_path,month_34_all_data_path)
    
    ###############################################################################
    #                            生成不同数据集                                    #
    ###############################################################################
    generate_dataSet.generate_dataSet()
    
    
    ###############################################################################
    #                              特征生成                                        #
    ###############################################################################
    main_generate_feature.generate_all_feature()
    # 结束后生成如下名称feature_dataSet-->'data/train_three_train_feature.csv'
    
    ###############################################################################
    #                合并正负数据集(打标签，负样本抽样，正负样本合并)               #
    ###############################################################################
    # 通过打标签和正负样本均衡合并，最后形成：'data/one_train_dataSet_final.csv'
    combine_feature_dataSet.main_combine()
    
    
    one_train_dataSet_final_path = 'data/one_train_dataSet_final.csv'
    two_train_dataSet_final_path = 'data/two_train_dataSet_final.csv'
    two_train_dataSet_final_path = 'data/two_train_dataSet_final.csv'    
    # 通过清理不用用户和商品，最后形成：如下特征集：
    one_train_dataSet_after_clean_path = 'data/one_train_dataSet_after_clean.csv'
    two_train_dataSet_after_clean_path = 'data/two_train_dataSet_after_clean.csv'
    three_train_dataSet_after_clean_path  = 'data/three_train_dataSet_after_clean.csv'
    load_data.clean_data(one_train_dataSet_final_path, one_train_dataSet_after_clean_path, '_one')
    load_data.clean_data(two_train_dataSet_final_path, two_train_dataSet_after_clean_path, '_two')
    load_data.clean_data(three_train_dataSet_path, three_train_dataSet_after_clean_path, '_three')
    
    ###############################################################################
    #                              模型预估  RF                                   #
    ###############################################################################

    # 特征筛选后：
    one_train_dataSet_after_clean_path = 'data/one_train_dataSet_after_clean.csv'
    two_train_dataSet_after_clean_path = 'data/two_train_dataSet_after_clean.csv'
    three_train_dataSet_after_clean_path  = 'data/three_train_dataSet_after_clean.csv'
    three_train_dataSet_path

    clf = model_rf.classify_user_item(one_train_dataSet_after_clean_path, two_train_dataSet_after_clean_path, 
                             train_one_and_two_result_as_proba_path)

    # 预测第一数据集：                      
    model_rf.classify(clf, one_train_dataSet_after_clean_path, train_one_result_as_proba_path)      
    model_rf.output_answer(one_train_dataSet_after_clean_path, train_one_result_as_proba_path, 
                  one_before_answer_path, one_answer_path)
    # 第一数据集结果分数：
    ceshiyanzheng.evl(one_real_path, one_answer_path)    
       
    # 预测第二数据集：                      
    model_rf.classify(clf, train_two_train_feature_path, train_two_result_as_proba_path)      
    model_rf.output_answer(train_two_train_feature_path, train_two_result_as_proba_path, 
                  two_before_answer_path, two_answer_path)
    # 第二数据集结果分数：
    ceshiyanzheng.evl(two_real_path, two_answer_path)
    
    # 最终预测第三数据集：
    model_rf.classify(clf, three_train_dataSet_after_clean_path, train_three_result_as_proba_path)
    model_rf.output_answer(three_train_dataSet_after_clean_path, train_three_result_as_proba_path,
                  three_before_answer_path, three_rf_answer_path)