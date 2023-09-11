import polars as pl
import matplotlib.pyplot as plt


def getDescStats():
    df = pl.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )
    answer = df["sepal_length"].describe()
    return answer


def makeGraph():
    df = pl.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )

    groupedDf = df.group_by("species").mean()
    x = groupedDf["species"]
    y = groupedDf["sepal_length"]
    plt.bar(x, y)
    plt.title("Average Sepal Length per Iris Species")
    plt.xlabel("Iris Species")
    plt.ylabel("Average Sepal Length (cm)")

    plt.savefig("graph.png")
