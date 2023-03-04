class Univariate():
    def SplitDataSet(dataSet):
        Quan = []
        Qual = []
        for column in dataSet.columns:
            if dataSet[column].dtypes == "O":
                Qual.append(column)
            else:
                Quan.append(column)
        return Quan,Qual