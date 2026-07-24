import os
import pandas as pd

path = r"C:\Users\yash6\.cache\kagglehub\datasets\imdevskp\corona-virus-report\versions\166"

for file in os.listdir(path):
    print(file)