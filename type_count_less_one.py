from tools import openData
import numpy as np
import matplotlib.pyplot as plt


def countLessOne():
    """
    prédiction la plus basique.
    prediction(t) = cnt(t-1)

    :return: prediction du jour 2 au jour 731.
    count2 : valeurs réelles / actuelles du nombre de vélos loués.
    """
    variables = openData()
    count = variables[:]["cnt"]  # les valeurs actuelles (dans data)
    prediction = []
    count2 = [x for i, x in enumerate(count) if i != 1]  # enlève la première ligne de count
    for i in range(1, len(count)):
        prediction.append(count[:][i - 1])
    return prediction, count2
