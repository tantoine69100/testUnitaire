import joblib
import statistics

def testPositivePredict():
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import joblib

    X = [[205.9991686803,2,1]]

    model = joblib.load('regression.joblib')

    actual_result = model.predict(X)

    assert actual_result > 0

def testAccuracyModel():

    X =  [  [186.5591664373, 2, 0],
             [187.1437846716, 1, 1],
             [83.3153631652, 2, 1],
             [161.7815803479, 2, 1],
             [165.0130482406, 2, 1],
             [193.7314621901, 3, 1],
             [94.650536354, 2, 0],
             [237.8816666324, 2, 1]]

    Y = [   256534.245748472,
            282674.291716703,
            266555.384156006,
            319158.41869534,
            320042.987510679,
            324222.967162171,
            222231.558650076,
            317418.57397821]

    model = joblib.load('regression.joblib')

    yPredict = model.predict(X)

    diff = [abs(yChap - y) for yChap, y  in zip(yPredict, Y)]

    assert statistics.mean(diff) < 40000
