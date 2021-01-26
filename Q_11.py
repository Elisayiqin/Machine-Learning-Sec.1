def FDR(self,conf_mat):
    # Given a confusion matrix, i.e. the list of four metrics: [TN,FP, FN, TP], in this order
    # return False Discovery Rate (FDR).
    #  In case of Division by Zero error, return -1.
    [TN, FP, FN, TP] = conf_mat

    ## YOUR CODE HERE ###
    temp = FP+TP
    if temp:
        fdr = FP/(FP+TP)
    else:
        fdr = -1


    return fdr


def Q_11(self):
    # Task 11: Please complete the function "FDR" above
    pass