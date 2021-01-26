# Machine-Learning

复现机器学习的算法原理-第一节

主要知识点包括：dataset的行列数，dataframe的取数，标准差，中位数，混淆矩阵的计算，模型预测的好坏使用指标的计算原理：accuracy，f1, precision, recall, FDR, MCC，学会怎么评价模型好坏

Q_01.py

Return total number of samples in the validation dataset: "dataset/validation.csv"
   
Q_02.py

Return a list of two numbers: [n0, n1], where
n0 represents number of class=0 (negative) samples and n1 represents number of class=1 (positive) samples in the validation dataset: "dataset/validation.csv"

Q_03.py

Return standard deviation of the second feature: "The length of shorter sequence" of the validation dataset: "dataset/validation.csv"

Q_04.py

Return median (i.e., 50% percentile) of the seventh feature: "'U' frequencies of sequence 2" of the validation dataset: "dataset/validation.csv"

Q_05.py

This function does nothing, but you need to complete the function "confusion_matrix" defined in the file that takes two arrays of target variable "y": y_actual and y_pred denoting ground truth class labels and predicted class labels for the N samples when N is the length of both the arrays. The function should return a list of 4 metrics: TN, FP, FN, TP (in this order).

Q_06.py

You need to complete the accuracy function defined in the file that takes a confusion matrix, i.e. the list of the four metrics: [TN, FP, FN, TP], in this order, and return accuracy. In case of Division by Zero error, return -1.

Q_07.py

You need to complete the precision function defined in the file that takes a confusion matrix, i.e. the list of the four metrics: [TN, FP, FN, TP], in this order, and return precision. It is also known as Positive Predictive Value (PPV). In case of Division by Zero error, return -1.

Q_08.py

You need to complete the recall function defined in the file that takes a confusion matrix, i.e. the list of the four metrics: [TN, FP, FN, TP], in this order, and return recall. It is also known as Sensitivity, or True Positive Rate (TPR). In case of Division by Zero error, return -1.

Q_09.py

You need to complete the F1 function defined in the file that takes a confusion matrix, i.e. the list of the four metrics: [TN, FP, FN, TP], in this order, and return F1. It is the harmonic mean of precision and recall. In case of Division by Zero error, return -1.

Q_10.py

You need to complete the MCC function defined in the file that takes a confusion matrix, i.e. the list of the four metrics: [TN, FP, FN, TP], in this order, and return Matthews Correlation Coefficient (MCC). In case of Division by Zero error, return -1.

Q_11.py

You need to complete the FDR function defined in the file that takes a confusion matrix, i.e. the list of the four metrics: [TN, FP, FN, TP], in this order, and return False Discovery Rate (FDR). In case of Division by Zero error, return -1

Q_12.py

Return as a dataframe containing: {model_name,acc,prec,rec,f1,mcc,FDR} for each of the N models (listed in model_files) after predicting the target variables of the validation data: "dataset/validation.csv"

Q_13.py

Return the model name with path which is performing superior among the 6 pretrained models in terms of accuracy, given the performance result dataframe from Q_12

Q_14.py

Return the model name with path which is performing the worst among the 6 pretrained models in terms of recall, given the performance result dataframe from Q_12

Q_15.py

Scale the all the features of the validation set using the formula, z = (x-m)/s, where m = mean of a feature in the training set: "dataset/training.csv"
s = standard deviation of the feature in the training set: "dataset/training.csv"
\# DO NOT SCALE the target feature.
\# At the end, return a tuple (X, y), with X being a numpy array of shape (N,8) and y is an N dim array and N is the total number of samples in the validation set: "dataset/validation.csv".

Q_16.py

Return as a dataframe containing: {model_name,acc,prec,rec,f1,mcc,FDR} for each of the N models (listed in model_files) after predicting the target variables "y" (given) for "X" (also given as arguments to this function.

Q_17.py

Return the model name with path which is performing superior in terms of accuracy, given the performance result dataframe from Q_16

Q_18.py

Return the model name with path which is performing the worst in terms of recall, given the performance result dataframe from Q_16

Q_19.py

Flip the prediction of Model 1, and then compute and return as a dataframe containing: {acc,prec,rec,f1,mcc,FDR} on the original (i.e., not-scaled) validation dataset: "dataset/validation.csv"

Q_20.py

In a confusion matrix, the values of the four metrics are: TP=90, TN=1, FP=4, FN=5. Compute F1_original and MCC_original denoting the F1 and MCC scores. Now, flip the predictions, i.e., positives are now will be predicted as negative, and negatives are going to be predicted as positive. Then, compute F1_flipped and MCC_flipped, denoting corresponding F1 and MCC scores. Return the new {TP, TN, FP, FN, F1_original,MCC_original,F1_flipped, MCC_flipped, COMMENT} as a dataframe, where the COMMENT is a string that will be no longer than 200 characters but is going to be your comment about the F1 and MCC values for the two cases.

训练集和测试集皆在file内，并包含models。
