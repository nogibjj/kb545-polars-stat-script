from src.stat1 import getDescStats, makeGraph
import os


def test_get_stat():
    testDf = getDescStats()
    assert testDf[0, 1] == 150
    assert testDf[4, 1] == 4.3
    assert testDf[5, 1] == 5.1
    assert testDf[6, 1] == 5.8


def test_graph():
    makeGraph()
    assert os.path.isfile("graph.png")
