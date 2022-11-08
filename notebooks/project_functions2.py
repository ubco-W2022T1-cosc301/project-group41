import pandas as pd

def load_and_process(file1, file2, file3):

    data1 = (
        pd.read_csv(f"{file1}")
        .drop(columns=['Happiness Rank', 'Family', 'Health (Life Expectancy)', 'Freedom', "Generosity"])
        .rename(columns={"Happiness Score": "2015 Score", "Economy (GDP per Capita)": "2015 GDP", "Trust (Government Corruption)": "2015 Trust", "Dystopia Residual": "2015 Dystopia Residual"})
    )

    data2 = (
        pd.read_csv(f"{file2}")
        .drop(columns=['Happiness Rank', 'Family', 'Health (Life Expectancy)', 'Freedom', "Generosity"])
        .rename(columns={"Happiness Score": "2016 Score", "Economy (GDP per Capita)": "2016 GDP", "Trust (Government Corruption)": "2016 Trust", "Dystopia Residual": "2016 Dystopia Residual"})
    )

    data3 = (
        pd.read_csv(f"{file3}")
        .drop(columns=['Happiness Rank', 'Family', 'Health (Life Expectancy)', 'Freedom', "Generosity"])
        .rename(columns={"Happiness Score": "2017 Score", "Economy (GDP per Capita)": "2017 GDP", "Trust (Government Corruption)": "2017 Trust", "Dystopia Residual": "2017 Dystopia Residual"})
    )

    timeseries = pd.merge(data1, data2, how="left", on="Country")
    timeseries = (
        pd.merge(timeseries, data3, how="left", on="Country")
        .dropna()
        .assign(
            AvgDR = lambda x: (x["2015 Dystopia Residual"] + x["2016 Dystopia Residual"] + x["2017 Dystopia Residual"]) / 3
        )
        .drop(columns=["2015 Dystopia Residual", "2016 Dystopia Residual", "2017 Dystopia Residual"])
    )

    return timeseries