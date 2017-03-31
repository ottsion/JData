


## load_data.py ##

- 装载三月四月份数据，保存在'data/month_34_all_data.csv'位置：

         load_data(month_3_data_path, month_3_extra_data_path, month_4_data_path,month_34_all_data_path)

- 发现异常用户，返回need_delete_user的list集合：

         find_unNormal_user(month_34_all_data_path)

- 删除异常用户，将所有行为数据保存至'data/all_dataSet.csv'

         clean_unNormal_data(all_dataSet_path, month_34_all_data_path)


----------
## generate_dataSet.py ##


-  以2016-03-17到2016-04-05数据 预测2016-04-06到2016-04-10某用户是否下单某商品
- 以2016-03-22到2016-04-10数据   预测2016-04-11到2016-04-15某用户是否下单某商品
- 以2016-03-27到2016-04-15数据   预测2016-04-16到2016-04-20某用户是否下单某商品

        all_dataSet_path = 'data/all_dataSet.csv'
        one_dataSet_train_path = 'data/one_dataSet_train.csv'
        one_dataSet_test_path = 'data/one_dataSet_test.csv'
        two_dataSet_train_path = 'data/two_dataSet_train.csv'
        two_dataSet_test_path = 'data/two_dataSet_test.csv'
        three_dataSet_train_path = 'data/three_dataSet_train.csv'

    从总表中按上面时间截取部分数据作为数据集 : generate_dataSet()
    切分方法函数：

    	cut_data_as_time(dataSet_path, new_dataSet_path , begin_day, end_day)


----------


##  generate_all_feature.py ##


    train_one_train_feature_path = 'data/train_one_train_feature.csv'
    train_two_train_feature_path = 'data/train_two_train_feature.csv'
    train_three_train_feature_path = 'data/train_three_train_feature.csv'


总的合并各种特征，最终结果保存在上面地址：generate_all_feature()
1.  generate_feature.py

         fetch_feature(sample_filename, feature_filename, item_brand, code)
         - sample_filename:样本信息地址
            - feature_filename：提取出的特征地址
            - code : 针对不同信息样本，表征下不同的特证名
            - 此处48维特征

2. generate_feature_1.py
   处理用户信息特征：deal_with_user_data()
   处理商品评价特征：deal_with_comment_data()
   将上述特征加入到目前的特征中：

         fetch_feature_1(train_feature_path, finnal_feature_data_path)

3. generate_feature_2.py
   自动生成当前数据集最近2\4\6\8天的特征：

       split_dataSet_and_generate_feature()

   将上述特征加入到目前的特征中：

       fetch_feature_2(train_feature_path, finnal_feature_data_path, index)


----------

## combine_feature_dataSet.py ##

之前的特征位置

    train_one_train_feature_path = 'data/train_one_train_feature.csv'
    train_two_train_feature_path = 'data/train_two_train_feature.csv'
    train_three_train_feature_path = 'data/train_three_train_feature.csv' 

源数据集：

    one_dataSet_test_path = 'data/one_dataSet_test.csv'
    two_dataSet_test_path = 'data/two_dataSet_test.csv'

合并后保存的位置：

    one_train_dataSet_final_path = 'data/one_train_dataSet_final.csv'
    two_train_dataSet_final_path = 'data/two_train_dataSet_final.csv'

核心函数包括 main_combine()：
1. 从最开始划分的不同时间数据集中找出正样本信息，与之对应到特征数据集中对相应样本进行正负样本标注：

        fetch_sample(test_data_path, feature_data_path, negative_data_path,positive_data_path)

2. 负样本太多，进行抽取部分作为负样本：

        fetch_negative_sample(negative_data_path, new_negative_data_path)

3. 将现有正负样本（经过标注）合并成训练集测试集等，用于最终测试

        combine_neg_and_posi(negative_data_path, positive_data_path, train_dataSet_path)


----------

## ceshiyanzheng.py ##

1. 用来计算AB值，输入为（user_id,sku_id）格式

        evl(two_real_path, two_answer_path)

2. 用来输出测试后的答案

        output_answer(dataSet_path, proba_path, before_answer_path, answer_path)
        - dataSet_path   训练集
        - proba_path    预测结果
        - before_answer_path  将结果标准化(user_id,sku_id)格式
        - answer_path    去除before_answer_path中重复的数据，为最终结果

----------

##　load_data.py ##

一般来说此时数据集准备就绪，但是按题意所有预测商品均在Ｐ中，我们需要删除一部分数据集中不属于这些商品的数据

    　clean_data(dataSet_path, after_dataSet_path)
    　-　dataSet_path　输入为　特征数据集，用来训练或者预测的特征集，未清洗
    　-　 after_dataSet_path　　　合理的，将直接用于ｍｏｄｅｌ的特征数据集

----------

##　main_test.py ##

这里选用ＲＦ测试：

    clf = model_rf.classify_user_item(train_feature_dataSet, test_feature_dataSet, 
                             proba_path)
                             
    model_rf.classify(clf, test_feature_dataSet, proba_path)      
    model_rf.output_answer(feature_path, proba_path, two_before_answer_path, two_answer_path)
    
    ceshiyanzheng.evl(two_real_path, two_answer_path)