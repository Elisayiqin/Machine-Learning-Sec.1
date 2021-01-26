# A sample driver program
# PLEASE DO NOT SUBMIT


from Assigned import *

q = Assigned('./dataset/training.csv', 'dataset/validation.csv', 7) #column indices start from 0
print(q.Q_01())
# res = q.Q_02()
# print("number of 0 = %d, number of 1 = %d" %(res[0],res[1]))
# print("stdev(second_feature) = %f"%(q.Q_03()))
# print("median(seventh_feature) = %f"%(q.Q_04()))
# conf_mat = q.confusion_matrix([1,1,0,0],[0,1,0,1])
# print("acc = %f"% (q.accuracy(conf_mat)))
# result = q.Q_12()
# print(result)
# print(q.Q_13(result))
# print(q.Q_14(result))
# (X,y) = q.Q_15()
# print(X)
# print(X.shape)
# result = q.Q_16(X,y)
# print(result)
# print(q.Q_17(result))
# print(q.Q_18(result))
# res = q.Q_19()
# print(res)
# # import pandas as pd
# # Q_20_1 = pd.DataFrame(q.Q_20())
# # Q_20_1.to_csv("Q_20_1.csv")
# print(q.Q_20())
# print(q.training)
# print(q.validation)

