def Q_18(self, performance_result_dataframe):
    # Task 18: Return the model name with path which is performing the worst in terms of recall, given the
    #  performance result dataframe from Q_16


    ## YOUR CODE HERE
    row_min = performance_result_dataframe.loc[performance_result_dataframe['Recall'].idxmin()]
    name_min = row_min["model_name"]
    name = f'models/{name_min}.pkl'

    return name