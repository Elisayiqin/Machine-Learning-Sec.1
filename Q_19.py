def Q_19(self, model_file="models/Model_1.pkl"):
    # Task 19: Flip the prediction of Model 1, and then compute and
    #  return as a dataframe containing:
    #      {acc,prec,rec,f1,mcc,FDR} on the
    #   original (i.e., not-scaled) validation dataset: "dataset/validation.csv"
    #     # You can load the pretrained model via pickle library. Here is an example use:
    #     # infile = open('pickle-file.pkl','rb')
    #     # model = pickle.load(infile)
    #     # infile.close()
    #     # y_pred = model.predict(X) #to get the predictions of all the X samples using the model
    import pickle
    import sys
    import os
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn import tree
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier

    ## YOUR CODE HERE ##
    #result = pd.DataFrame({'Accuracy': [acc], 'Precision': [prec], 'Recall': [rec], 'F1': [f1], 'MCC': [mcc], 'FDR': [fdr]})
    result = pd.DataFrame(columns=['Accuracy', 'Precision', 'Recall', 'F1', 'MCC', 'FDR'])

    infile = open(model_file, 'rb')
    model = pickle.load(infile)
    infile.close()
    data_validation = self.validation.drop([8],axis=1)
    y_pred = model.predict(data_validation) # to get the predictions of all the X samples using the model
    y_pred = y_pred ^ 1
    y_actual = self.validation[8]
    con = self.confusion_matrix(y_actual,y_pred)
    result.loc[0] = [self.accuracy(con), self.precision(con), self.recall(con), self.F1(con),
                         self.MCC(con), self.FDR(con)]





    return result