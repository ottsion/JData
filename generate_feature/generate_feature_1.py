#!/usr/bin/env python2
# -*- coding: utf-8-*-
'''

    抽取如下特征,  浏览数、收藏数、购物车、购买数、平均活跃天数、最后活跃天数距离最终时间的天数
    列表：
    用户名, 商品名,平均活跃天数、最后活跃天数距离最终时间的天数、
    年龄段、性别、用户等级、用户注册时间长度、
    商品属性1、商品属性2、商品属性3、品类、 品牌  -->协同过滤算法得到相关系数亦可
    累计评分数、是否有差评、差评比率、平均累计评分数、平均是否有差评、平均差评比率

    加入预测前一天时各个商品的:
        comment_num             评价数目
        has_bad_comment         差评数目
        bad_comment_rate        差评率
        avg_comment_num         平均累计评分数
        avg_bad_comment         平均是否有差评
        avg_bad_comment_rate    平均差评比率
    用户信息：
        age	         年龄段	 -1表示未知
        sex	         性别	 0表示男，1表示女，2表示保密
        user_lv_cd	 用户等级	 有顺序的级别枚举，越高级别数字越大
        user_reg_dt	 用户注册日期	 粒度到天
'''

import csv
import pandas as pd
from  datetime import *



# 数据路径
comment_data_path = 'input/JData_Comment.csv';
product_data_path = 'input/JData_Product.csv';
user_data_path = 'input/JData_User.csv';
all_user_behave_data_path = 'data/all_behave.csv';
train_user_behave_data_path = 'data/train_behave.csv';



user_data_utf8_path = 'data/JData_User.csv';
user_data_utf8_after_path = 'data/JData_User_after.csv';
user_data_final_path = 'data/user_data_final.csv'
user_data_final_path_new = 'data/user_final_data.csv'      #新增，删除上表中错误信息
comment_data_final_path = 'data/comment_final_data.csv'


# 解析日期
def parse_date(raw_date):
    entry_date = raw_date
    year, month, day = entry_date.split(" ")[0].split("/")
    return int(year), int(month), int(day)


###############################################################################
#                         处理用户信息                                         #
###############################################################################
#user_data = pd.read_csv(user_data_path, encoding='gbk')
#user_data.to_csv(user_data_utf8_path, encoding='utf-8', index=False)
def deal_with_user_data():

    # 将用户的注册日期改为距离预测日期的时间长度，又称为注册时长
    csvfile = file(user_data_utf8_after_path, 'wb')
    writer = csv.writer(csvfile)
    reader = open(user_data_utf8_path)
    writer.writerow(('user_id','age','sex','user_lv_cd','reg_long1','reg_long2','reg_long3'))    
    reader.readline()
    for line in reader.readlines():
        # ',user_id,age,sex,user_lv_cd,user_reg_dt\n'

        if line[4]=='user_reg_dt':
            print 'user_reg_dt'
            continue
        line = line.strip().split(',')
        reg_time = date(*parse_date(line[4]))
        timeSeprate1 = date(2016,04,05)
        timeSeprate2 = date(2016,04,10)
        timeSeprate3 = date(2016,04,15)
        reg_long1 = (timeSeprate1 - reg_time).days
        reg_long2 = (timeSeprate2 - reg_time).days
        reg_long3 = (timeSeprate3 - reg_time).days
        writer.writerow((line[0],line[1],line[2],line[3],reg_long1,reg_long2,reg_long2+5))
    
    #  1  79  36-45岁  2  2   69  74  79
    # 将年龄、性别、等级dummies化
    user_data = pd.read_csv(user_data_utf8_after_path)
    newdf = pd.get_dummies(user_data,columns=["age","sex",'user_lv_cd'],dummy_na=True)
    newdf.to_csv(user_data_final_path, index=False)
    
###############################################################################
#                         处理评论信息                                         #
###############################################################################
def deal_with_comment_data():
    comment_data = pd.read_csv(comment_data_path, parse_dates =[0])
    #  原 dt  sku_id  comment_num  has_bad_comment  bad_comment_rate
    # 转换为 sku_id  
    # avg_comment_num  avg_have_bad_comment_sku_mean avg_bad_comment_rate
    
    # 2016-02-01到2016-03-07数据 
    avg_comment_num = comment_data.groupby('sku_id').comment_num.mean()
    std_comment_num = comment_data.groupby('sku_id').comment_num.std()
    avg_have_bad_comment = comment_data.groupby('sku_id').has_bad_comment.mean()
    std_have_bad_comment = comment_data.groupby('sku_id').has_bad_comment.std()
    avg_bad_comment_rate = comment_data.groupby('sku_id').bad_comment_rate.mean()
    std_bad_comment_rate = comment_data.groupby('sku_id').bad_comment_rate.std()
    
    data = pd.DataFrame({'avg_comment_num':avg_comment_num,'std_comment_num':std_comment_num,
        'avg_have_bad_comment':avg_have_bad_comment,'std_have_bad_comment':std_have_bad_comment,
        'avg_bad_comment_rate':avg_bad_comment_rate,'std_bad_comment_rate':std_bad_comment_rate
    })
    data.to_csv(comment_data_final_path)
    
''''    #发现用户表首列有错误，列名为空，是序号，这里删除一下
def delete_user_info_no_1():
    user_info = pd.read_csv(user_data_final_path)
    user_info = user_info.as_matrix()[:,1:]
    user_info = pd.DataFrame(user_info, columns=['user_id', 'reg_long1', 'reg_long2', 'reg_long3',
       'age_-1', 'age_15', 'age_16_25', 'age_26_35', 'age_36_45',
       'age_46_55', 'age_56', 'age_nan', 'sex_0.0', 'sex_1.0',
       'sex_2.0', 'sex_nan', 'user_lv_cd_1.0', 'user_lv_cd_2.0',
       'user_lv_cd_3.0', 'user_lv_cd_4.0', 'user_lv_cd_5.0',
       'user_lv_cd_nan'])
    return user_info
'''    



    

def fetch_feature_1(train_feature_path, finnal_feature_data_path):
    import pandas as pd
    train_feature_data = pd.read_csv(train_feature_path)
    print u'处理用户和评论信息....'
    deal_with_user_data()
    deal_with_comment_data()
    #user_info = delete_user_info_no_1()
    user_info = pd.read_csv(user_data_final_path)
    comment_info = pd.read_csv(comment_data_final_path)
    print u'开始融合特征....'
    merge_feature_and_user_info = pd.merge(train_feature_data,user_info, on='user_id')
    merge_feature_and_user_info_and_comment = pd.merge(merge_feature_and_user_info,comment_info, on='sku_id')
    merge_feature_and_user_info_and_comment.to_csv(finnal_feature_data_path, index=False)
    print u'一次特征选择完成，存入:',finnal_feature_data_path
    
    #generate_feature_1.fetch_feature_1(train_one_train_feature_path_pre1, 
    #                                   train_one_train_feature_path_pre2)
    

    

    
    
    
 
    

    

    
 
    

