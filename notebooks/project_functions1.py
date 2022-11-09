import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def landp(f1, f2, f3):

    data1 = (
        pd.read_csv(f"{f1}")
        .drop(columns=['Trust (Government Corruption)','Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', "Generosity"])
        .rename(columns={"Happiness Score": "2015 HS", "Happiness Rank": "2015 Rank", "Freedom": "15Free", "Dystopia Residual": "2015 DysRes"})
    )

    data2 = (
        pd.read_csv(f"{f2}")
        .drop(columns=['Trust (Government Corruption)','Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', "Generosity"])
        .rename(columns={"Happiness Score": "2016 HS", "Happiness Rank": "2016 Rank", "Freedom": "16Free", "Dystopia Residual": "2016 DysRes"})
    )

    data3 = (
        pd.read_csv(f"{f3}")
        .drop(columns=['Trust (Government Corruption)','Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', "Generosity"])
        .rename(columns={"Happiness Score": "2017 HS", "Happiness Rank": "2017 Rank", "Freedom": "17Free", "Dystopia Residual": "2017 DysRes"})
    )

    timeseries = pd.merge(data1, data2, how="left", on="Country")
    timeseries = (
        pd.merge(timeseries, data3, how="left", on="Country")
        .dropna()
        .assign(
            AvgDR = lambda x: (x["2015 DysRes"] + x["2016 DysRes"] + x["2017 DysRes"]) / 3
        )
        .drop(columns=["2015 DysRes", "2016 DysRes", "2017 DysRes"])
    )

    return timeseries