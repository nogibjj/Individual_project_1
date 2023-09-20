"""
Main cli or app entry point
"""
# import lib
import pandas as pd

file = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"

data_frame = pd.read_csv(file)

print(data_frame)
