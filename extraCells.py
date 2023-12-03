import csv
import pandas as pd
from datetime import *




  
def convert(list):
  return tuple(list)



def realVsPred():
  data= pd.read_csv("export.csv")
  predTime = data.PredictedTime
  realTime = data.TotalTime
  lastPred = predTime.tail(1)
  lastReal = realTime.tail(1)
  predString = lastPred.to_string()
  realString = lastReal.to_string()
  print(realString, sep=' ')
realVsPred()