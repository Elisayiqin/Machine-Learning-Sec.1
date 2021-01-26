def F1(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return F1 score. It is the harmonic mean of precision and recall.
    #  In case of Division by Zero error, return -1.

    ## YOUR CODE HERE ##
    [TN, FP, FN, TP] = conf_mat
    temp = 2*TP+FN+FP
    if temp:
        f1 = (2*TP) /(2*TP+FN+FP)
    else:
        f1 = -1




    return f1


def Q_09(self):
    # Task 9: Please complete the function "F1" above
    pass