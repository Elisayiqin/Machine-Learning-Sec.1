def confusion_matrix(self,y_actual, y_pred):
    # Task 5: the function takes two arrays of target variable "y": y_actual and y_pred
    #    denoting ground truth class labels and predicted class labels for the N samples
    #    when N is the length of both the arrays.
    # The function should return a list of 4 metrics: TN, FP, FN, TP (in this order).
    assert(len(y_actual)==len(y_pred))
    import numpy as np
    y_actual = np.array(y_actual)
    y_pred = np.array(y_pred)
    TP = sum((y_actual == y_pred) * (y_actual == [1]*len(y_actual)))
    FP = sum((y_actual != y_pred) * (y_actual == [0]*len(y_actual)))
    TN = sum((y_actual == y_pred) * (y_actual == [0]*len(y_actual)))
    FN = sum((y_actual != y_pred) * (y_actual == [1]*len(y_actual)))



    return [TN,FP, FN, TP]

# def confusion_matrix(self,TP, TN, FP, FN):
#     return [TN, FP, FN, TP]

def Q_05(self):
    # Task 5: This function does nothing, but you need to complete the two functions "confusion_matrix" above
    #   First "confusion_matrix" takes two arguments: y_actual and y_pred
    # And the second overloaded version of the function takes 4 arguments: TP, TN, FP, FN
    pass


