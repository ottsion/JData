# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:20:40 2017

@author: SUNFC

完成 解析字符串转化为时间
     合并3.4月行为数据
     按照时间段取出数据集
     找出异常用户并返回用户集合
"""
import pandas as pd
from datetime import *

'''
# 数据路径
month_3_data_path = 'input/JData_Action_201603.csv' 
month_3_extra_data_path = 'input/JData_Action_201603_extra.csv'
month_4_data_path = 'input/JData_Action_201604.csv'
month_34_all_data_path = 'data/month_34_all_data.csv'
all_dataSet_path = 'data/all_dataSet.csv'
load_data.py
'''

# 需自备表格如下：
# 数据路径
data_02_month_path = 'input/JData_Action_201602.csv'
data_03_month_path = 'input/JData_Action_201603.csv'
data_03_month_extra_path = 'input/JData_Action_201603_extra.csv'
data_04_month_path = 'input/JData_Action_201604.csv'
Product_data_path = 'input/JData_Product.csv'
User_data_path = 'input/JData_User.csv'
Comment_data_path = 'input/JData_Comment.csv'

# 解析日期
def parse_date(raw_date):
    entry_date = raw_date
    year, month, day = entry_date.split(" ")[0].split("-")
    return int(year), int(month), int(day)


# 将行为数据表进行合并，不包含二月信息
def load_data(month_3_data_path, month_3_extra_data_path, month_4_data_path,month_34_all_data_path):
    month_3_data = open(month_3_data_path)
    month_3_extra_data = open(month_3_extra_data_path)
    month_4_data = open(month_4_data_path)
    month_34_all_data = open(month_34_all_data_path,'w')
    for line in month_3_data.readlines():
        month_34_all_data.write(line)
    month_3_extra_data.readline()
    for line in month_3_extra_data.readlines():
        month_34_all_data.write(line)   
    month_4_data.readline()
    for line in month_4_data.readlines():
        month_34_all_data.write(line)  
    month_4_data.close()
    month_3_data.close()
    month_3_extra_data.close()
    month_34_all_data.close()
    print u'将三月四月行为数据合并完成....'
    
# 删除异常用户信息
def clean_unNormal_user_data(all_dataSet_path, month_34_all_data_path):
    unNormai_user = find_unNormal_user(month_34_all_data_path)
    data = pd.read_csv(month_34_all_data_path)
    new_data = data[~data.user_id.isin(unNormai_user)]
    new_data.to_csv(all_dataSet_path, index=False)
    print u'将删除异常用户后的数据集合存入:',all_dataSet_path


  
'''
用户的行为如下，根据行为去删除异常用户
 1.浏览（指浏览商品详情页）；2.加入购物车；3.购物车删除；4.下单；5.关注；6.点击
返回需要删除的用户名列表
''' 
def find_unNormal_user(month_34_all_data_path): 
    user_view = dict()    # 构建用户对商品的浏览总数，以便异常浏览的用户可以剔除
    user_basket = dict()  # 构建用户加入购物车总数，以便异常加入购物车的用户可以剔除
    user_follow = dict()  # 构建用户关注总数，以便异常关注的用户可以剔除
    user_click = dict()   # 构建用户对商品的点击总数，以便异常点击的用户可以剔除
    user_list = []
    all_data = open(month_34_all_data_path)
    all_data.readline()
    for line in all_data.readlines():
        entry = line.strip().split(",")
        user_list.append(entry[0])
        if entry[4] == '1':
            if entry[0] not in user_view:
                user_view[entry[0]] = 1
            else:
                user_view[entry[0]] = user_view[entry[0]] + 1
        if entry[4] == '2':
            if entry[0] not in user_basket:
                user_basket[entry[0]] = 1
            else:
                user_basket[entry[0]] = user_basket[entry[0]] + 1
        if entry[4] == '5':
            if entry[0] not in user_follow:
                user_follow[entry[0]] = 1
            else:
                user_follow[entry[0]] = user_follow[entry[0]] + 1
        if entry[4] == '6':
            if entry[0] not in user_click:
                user_click[entry[0]] = 1
            else:
                user_click[entry[0]] = user_click[entry[0]] + 1
    # 处理异常浏览用户信息
    need_delete_user = []
    view_count = 0.0
    for (k, v) in user_view.items():
        view_count = view_count + user_view[k]
    view_mean = view_count/len(user_view)
    for (k, v) in user_view.items():
        if user_view[k] > 3*view_mean:
            need_delete_user.append(k)
    print u'总计view用户:',len(user_view),' 需要删除个数:',len(need_delete_user)
    # 处理异常加入购物车用户信息
    view_count = 0.0
    for (k, v) in user_basket.items():
        view_count = view_count + user_basket[k]
    view_mean = view_count/len(user_basket)
    for (k, v) in user_basket.items():
        if user_basket[k] > 3*view_mean:
            need_delete_user.append(k)
    print u'总计view用户:',len(user_basket),' 需要删除个数:',len(need_delete_user)
    # 处理异常关注 用户信息
    view_count = 0.0
    for (k, v) in user_follow.items():
        view_count = view_count + user_follow[k]
    view_mean = view_count/len(user_follow)
    for (k, v) in user_follow.items():
        if user_follow[k] > 3*view_mean:
            need_delete_user.append(k)
    print u'总计view用户:',len(user_follow),' 需要删除个数:',len(need_delete_user)
    # 处理异常关注 用户信息
    view_count = 0.0
    for (k, v) in user_click.items():
        view_count = view_count + user_click[k]
    view_mean = view_count/len(user_click)
    for (k, v) in user_click.items():
        if user_click[k] > 3*view_mean:
            need_delete_user.append(k)
    print u'总计view用户:',len(user_click),' 需要删除个数:',len(need_delete_user)
    temp = set(need_delete_user)
    need_delete_user = list(temp)
    print u'总计有',len(need_delete_user),'个异常用户被删除'
    return  need_delete_user
    
    





# 清理不需要出现的用户和不需要出现的商品
def clean_noUse_user_and_noUser_product(dataSet_path, after_dataSet_path):
    # 清理不需要的商品  下单商品必须为P中商品
    train_data = pd.read_csv( dataSet_path)
    product_data = pd.read_csv( Product_data_path)
    sku_all = product_data.sku_id
    new_train_data = train_data[train_data.sku_id.isin(sku_all)]
    new_train_data.to_csv( after_dataSet_path, index=False)

    
# 清理异常数据
def clean_unNormal_data(after_dataSet_path,code):
    train_data = pd.read_csv( after_dataSet_path)
    train_data.describe()
    train_data = train_data[train_data['user_item_click'+code]<54] 
    train_data = train_data[train_data['user_click'+code]<1500] 
    train_data = train_data[train_data['usr_item_hide'+code]<18] 
    
    train_data = train_data[train_data['user_hide'+code]<20] 
    train_data = train_data[train_data['usr_item_shop_basket'+code]<15] 
    train_data = train_data[train_data['user_basket'+code]<50] 

    train_data = train_data[train_data['user_view'+code]<1000] 
    
    train_data.to_csv( after_dataSet_path, index=False)
    

#load_data.clean_data(one_train_dataSet_final_path, one_train_dataSet_after_clean_path)   
# 最后阶段用来除去不需要的商品
def clean_data(dataSet_path, after_dataSet_path, code):
    clean_noUse_user_and_noUser_product(dataSet_path, after_dataSet_path)
    clean_unNormal_data(after_dataSet_path,code)

    
    

    
    
if __name__=='__main__':
    # 运行第一次时操作
    load_data(month_3_data_path, month_3_extra_data_path, month_4_data_path, month_34_all_data_path)
    clean_unNormal_user_data(all_dataSet_path,month_34_all_data_path)
    