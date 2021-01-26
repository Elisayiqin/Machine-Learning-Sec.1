def Q_20(self):
    # Task 20: Say, in a confusion matrix, the values of the four metrics are: TP=90, TN=1, FP=4, FN=5.
    # Compute F1_original and MCC_original.
    # Now, flip the predictions, i.e., positives are now will be predicted as negative,
    # and negatives are going to be predicted as positive.
    # Then, compute F1_flipped and MCC_flipped.
    # Return the new TP, TN, FP, FN, F1_original,MCC_original,F1_flipped, MCC_flipped, COMMENT
    # as a dataframe, where
    # The COMMENT is a string that will be no longer than 200 characters but is
    #   going to be your comment about the F1 and MCC values for the two cases.

    ## YOUR CODE HERE ##
    import pandas as pd
    import numpy as np
    TP = 90
    TN = 1
    FP = 4
    FN = 5
    COMMENT = "Due to the flip, MCC becomes the opposite of MCC, F1 score changed from good to bad. Incorrectly defining" \
              " the positive class will affect F1 score value instead of MCC value."
    F1_original = (2*TP) /(2*TP+FN+FP)
    temp = (np.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)))
    if temp:
        MCC_original = ((TP * TN) - (FP * FN)) / temp
    else:
        MCC_original = -1
    # Here, due to the flip, correct predictions are incorrectly seem as false predictions, so the true positive
    # and false negative swap, true negative and false positive swap.
    TP, FN = FN, TP
    TN, FP = FP, TN

    F1_flipped = (2*TP) /(2*TP+FN+FP)
    temp = (np.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)))
    if temp:
        MCC_flipped = ((TP * TN) - (FP * FN)) / temp
    else:
        MCC_flipped = -1


    result = pd.DataFrame({'TP': [5], 'TN': [4], 'FP': [1], \
                           'FN': [90], 'F1_original': [F1_original], \
                           'MCC_original': [MCC_original],'F1_flipped':[F1_flipped],\
                           'MCC_flipped':[MCC_flipped],'COMMENT':[COMMENT]})
    return result
