def Q_15(self):
    # Task 15: Scale the all the features of the validaton set using the formula, z = (x-m)/s,
    #   where m = mean of a feature in the training set: "dataset/training.csv"
    #         s = standard deviation of the feature in the training set: "dataset/training.csv"
    #  DO NOT SCALE the target feature.
    # At the end, return a tuple (X, y), with X being a numpy array of shape (N,8) and y is an N dim array
    # and N is the total number of samples in the validation set: "dataset/validation.csv".

    ## YOUR CODE HERE ##
    import pandas as pd
    scale_validation = pd.DataFrame()
    for i in range(0,8):
        mean_training = self.training[i].mean()
        std_training = self.training[i].std()
        # print(self.validation[i])
        scale_validation[i] = self.validation[i].apply(lambda x: (x-mean_training)/std_training)

    X = scale_validation.iloc[:,0:8]
    y = self.validation[8]





    return (X, y)
