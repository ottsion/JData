# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC


"""

import pandas as pd


###############################################################################
#                    输入只包含user_id和sku_id的真实表和预测表                  #
###############################################################################
def evl(two_real_path, two_answer_path):
    preds = pd.read_csv(two_answer_path)
    real = pd.read_csv(two_real_path)
    lenReal = len(real)
    lenPreds = len(preds)
    
    TP1 = float(len(set(real.user_id).intersection(set(preds.user_id))))
    P11 = TP1/lenPreds
    R11 = TP1/lenReal
    F11 = 6 * R11 / (5 * R11 + P11)

    TP2 = float(len(real.append(preds)[real.append(preds).duplicated()]))
    P12 = TP2/lenPreds
    R12 = TP2/lenReal
    F12 = 5 * R12 * R12 / (2 * R12 + 3 * P12)
    Score = 0.4 * F11 + 0.6 * F12
    print 'P11 = %f | R11 = %f | F11 = %f' % (P11,R11,F11)
    print 'P12 = %f | R12 = %f | F12 = %f' % (P12,R12,F12)
    print 'Score = %f' % Score
    
    
    
###############################################################################
#                    以下函数是为了在真实值中取出user_id和sku_id键值对          #
###############################################################################
two_positive_path = 'data/two_positive.csv'
two_real_path = 'data/two_real.csv'
# two_positive_path 真实数据，包含其他数据, two_real_path  真实数据，只包含user_id,sku_id
def get_two_real_answer(two_positive_path, two_real_path):
    real_data = pd.read_csv(two_positive_path)
    data = pd.DataFrame([real_data.user_id,real_data.sku_id])
    data = data.T
    data.to_csv(two_real_path, index=False,columns=['user_id','sku_id'])
    
    
    
    
    
if __name__=='__main__':
    # 处理得到正确值，（user_id，sku_id）格式
    two_real_path = 'data/two_real.csv'
    two_positive_path = 'data/two_positive.csv'
    get_two_real_answer(two_positive_path, two_real_path)
    
    # 一下分别是真实数据和预测数据
    two_real_path = 'data/two_real.csv'
    two_answer_path = 'data/two_answer.csv'
    evl(two_real_path, two_answer_path)
    
    
    
    
    
# 规则
#  最后四天加入购物车，却未购买的用户-商品对    如果出现在预测结果中，则优先于概率最大值成为预测结果
#  最后四天数据：three_before_4_days.csv
def regular_may_shop():
    three_before_4_days_path = 'data/three_before_4_days.csv'
    regular_may_shop_path = 'data/regular_may_shop.csv'
    # 加入购物车的用户-商品对dict : user_item_basket
    # 购买的用户商品 dict  user_item_shop
    user_item_basket = set()
    user_item_shop = set()
    three_before_4_days_data = open(three_before_4_days_path)
    three_before_4_days_data.readline()
    for line in three_before_4_days_data.readlines():
        lineArr = line.strip().split(',')
        if lineArr[0] > 0:      #加入购物车过
            user_item_basket.add((lineArr[0],lineArr[1]))
        if lineArr[0] > 0:
            user_item_shop.add((lineArr[0],lineArr[1]))
    # 对user_item_basket中的每一个键值对观察是否包含在user_item_shop中，没有的话就单独保存list：may_shop
    may_shop = set()
    for k in user_item_basket:
        if k not in user_item_shop:
            may_shop.add((k[0], k[1]))
    may_shap_list = list(may_shop)
    import pandas as pd
    may_shop_df = pd.DataFrame(may_shap_list)
    may_shop_df.to_csv(regular_may_shop_path, index=False)
    
    
# 此处数据集应该是预测结果集（user_id,sku_id,prob）与规则优先集（user_id,sku_id）
# 如果预测结果集中出现规则优先级的键值对，则对此键值对prob提升0.3%
# 最后将预测结果集user_id数据唯一化
def get_regular_answer(before_answer_path, regular_may_shop_path):
    before_answer = open(before_answer_path)
    regular_may_shop = open(regular_may_shop_path)
    before_answer.readline()
    for line in before_answer.readlines():
        lineArr = line.strip().split(',')





'''
接收数据集和对应的target概率，返回的是[user_id, sku_id, pre]   pre为概率
'''
def combine_tar_and_pre(dataSet_path, proba_path, before_answer_path):
    data = pd.read_csv(dataSet_path)
    target = pd.read_csv(proba_path, names='p')

    combine_tar_pre = pd.concat([data,target],axis=1)
    s = pd.concat([combine_tar_pre.user_id, combine_tar_pre.sku_id,combine_tar_pre.p], axis=1)
    ss = s[s.p <= 0.5]
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



    
    
    
    