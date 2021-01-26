def precision(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return precision. It is also known as Positive Predictive Value (PPV).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat
    ## YOUR CODE HERE

    temp = TP+FP
    if temp:
        prec = TP/(TP+FP)
    else:
        prec = -1



    return prec


def Q_07(self):
    # Task 7: Please complete the function "precision" above
    pass