def MCC(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return Matthews correlation coefficient (MCC).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat

    ## YOUR CODE HERE ##
    import numpy as np
    [TN, FP, FN, TP] = [int(TN), int(FP), int(FN), int(TP)]
    temp = (np.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
    if temp:
        mcc = ((TP*TN) - (FP*FN))/temp
    else:
        mcc = -1


    # can also use
    # try:
    # except ZeroDivisionError:

    return mcc


def Q_10(self):
    # Task 10: Please complete the function "MCC" above
    pass