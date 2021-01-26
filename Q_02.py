def Q_02(self):
    #Task 2: Return a list of of two numbers: [n0, n1], where
    # n0 represents number of class=0 (negative) samples and n1 represents number of class=1 (positive) samples
    # in the validation dataset: "dataset/validation.csv"
    data_validation = self.validation
    n0 = data_validation[8][data_validation[8]==0].count()

    n1 = data_validation[8][data_validation[8]==1].count()



    return [n0, n1]