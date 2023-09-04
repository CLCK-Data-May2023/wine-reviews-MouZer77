import pandas as pd
import zipfile
from tabulate import tabulate


zf = zipfile.ZipFile('C:/Users/idfap/Documents/Projects/Wine Review/wine-reviews-MouZer77/data/winemag-data-130k-v2.csv.zip') #Unzips

df = pd.read_csv(zf.open('winemag-data-130k-v2.csv')) #Reads

average_points = df.groupby("country")["points"].mean() #Find the average points of countries
total_reviews = df.groupby("country")["Unnamed: 0"].nunique() #How many reviews per country
df_merged = pd.merge(total_reviews, average_points, on="country") #Merge to 1 output

df_merged = df_merged.rename(columns={"Unnamed: 0": "count"}) #Name Change

df_merged = df_merged.sort_values(by="count", ascending=False) #Sorts by Count

df_merged['points'] = df_merged['points'].round(1) #Rounded float

print(tabulate(df_merged, headers=df_merged.columns, tablefmt="fancy_grid")) #Oh, you fancy, huh?


path = "C:\\Users\\idfap\\Documents\\Projects\\Wine Review\\wine-reviews-MouZer77\\data\\" #Where to
df_merged.to_csv(path + "reviews-per-country.csv") #Saves as CSV