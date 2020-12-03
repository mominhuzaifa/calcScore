#!/usr/bin/python

'''
Author: Momin Huzaifa
email: mominhuzaifa@protonmail.ch
'''


# score predictor of cricket match

def predictor():
    totalOver = int(input('Enter total over of match: '))
    currentOver = float(input('Enter current over of match: '))
    currentScore = int(input('Enter current score of match: '))
    runrate = currentScore/currentOver
    calcScore = runrate * totalOver
    print("\n")
    print("------------------------")
    print("Run rate is: ", round(runrate,2))
    print("Predicted score: ", round(calcScore))
    print("------------------------")

predictor()
