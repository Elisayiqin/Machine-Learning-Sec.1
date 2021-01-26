def Q_16(self, X, y, model_files=["models/Model_1.pkl","models/Model_2.pkl","models/Model_3.pkl",\
                            "models/Model_4.pkl","models/Model_5.pkl","models/Model_6.pkl"]):
    # Task 16: Return as a dataframe containing:
    # {model_name,acc,prec,rec,f1,mcc,FDR} for each of the N models (listed in model_files)
    # predicting the target variables "y" (given) for "X" (also given as arguments to this function.
    # You can load the pretrained model via pickle library. Here is an example use:
    # infile = open('pickle-file.pkl','rb')
    # model = pickle.load(infile)
    # infile.close()
    # y_pred = model.predict(X) #to get the predictions of all the X samples using the model
    import pickle
    import numpy as np
    import pandas as pd
    import sys
    import os
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn import tree
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier
    result = pd.DataFrame(columns=['model_name','Accuracy','Precision','Recall','F1','MCC','FDR'])


    ## YOUR CODE HERE ###
    for i in range(1,7):
        infile = open(f'models/Model_{i}.pkl', 'rb')
        model = pickle.load(infile)
        infile.close()
        y_pred = model.predict(X)  # to get the predictions of all the X samples using the model
        y_actual = y
        con = self.confusion_matrix(y_actual,y_pred)

        result.loc[i-1] = [f"Model_{i}", self.accuracy(con), self.precision(con), self.recall(con), self.F1(con),
                         self.MCC(con), self.FDR(con)]


    return result