def accuracy(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return accuracy. In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat

    ## YOUR CODE HERE ##
    temp = TP+FP+FN+TN
    if temp:
        acc = (TP+TN)/(TP+FP+FN+TN)
    else:
        acc = -1



    return acc


def Q_06(self):
    # Task 6: Please complete the function "accuracy" above
    pass