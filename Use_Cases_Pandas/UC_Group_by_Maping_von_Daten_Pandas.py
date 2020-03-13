#used methods: pd.read_csv, replace(), pd.merge(), map()Zuordnung von Kategorien auf Zeileneinträge einer Spalte,
# set.index(), groupby().count, groupby().mean, groupby().std, groupby().sum

import pandas as pd
import numpy as np


def energy_data():
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17, skipfooter=38)

    energy = energy[["Unnamed: 1", "Petajoules", "Gigajoules", "%"]]
    energy.columns = ["Country", "Energy Supply", "Energy Supply per Capita", "% Renewable"]

    energy = energy.replace("...", np.NaN)

    energy["Energy Supply"] = energy["Energy Supply"] * 1000000

    energy["Country"] = energy["Country"].replace(
        {"Iran (Islamic Republic of)": "Iran", "Republic of Korea": "South Korea",
         "United States of America": "United States",
         "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
         "China, Hong Kong Special Administrative Region": "Hong Kong"})

    energy["Country"] = energy["Country"].replace({"[0-9]": "", " \(.*\)": ""})
    return energy


def gdp_data():
    gdp = pd.read_csv("world_bank.csv", skiprows=4)
    gdp["Country Name"] = gdp["Country Name"].replace(
        {"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"})
    gdp = gdp[["Country Name", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]
    return gdp


def scim_en_data():
    ScimEn = pd.read_excel("scimagojr-3.xlsx")
    ScimEn = ScimEn[0:15]
    return ScimEn


def answer_one():
    energy = energy_data()
    gdp = gdp_data()
    ScimEn = scim_en_data()

    years = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]

    df = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
    df = pd.merge(df, gdp, how='inner', left_on='Country', right_on='Country Name').set_index(
        'Country')  # merge data, inner method takes intersection, and finally only 15 countries
    df = df[
        ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index',
         'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015']]
    return df


answer_one()


Top15 = answer_one()
Top15 = Top15.reset_index() # Methodenliste Reset Index. Index Parameter werden gelöscht vom Dataframe Top15

ContinentDict  = {'China':'Asia',
              'United States':'North America',
              'Japan':'Asia',
              'United Kingdom':'Europe',
              'Russian Federation':'Europe',
              'Canada':'North America',
              'Germany':'Europe',
              'India':'Asia',
              'France':'Europe',
              'South Korea':'Asia',
              'Italy':'Europe',
              'Spain':'Europe',
              'Iran':'Asia',
              'Australia':'Australia',
              'Brazil':'South America'}

Top15["Continent"] = Top15["Country"].map(ContinentDict) # Map Funktion Zuordnung von Kategorien auf Zeileneinträge einer Spalte.
size = Top15.groupby("Continent")["Country"].count() # Groupy Funktion wird zum zählen der Länder pro Kontinent verwendet
Top15["Population"]=Top15["Energy Supply"]/Top15["Energy Supply per Capita"]


pop_sum = Top15.groupby("Continent")["Population"].sum() # Summe berechnen von 2 Spalten
pop_mean = Top15.groupby("Continent")["Population"].mean() # Median berechnen von 2 Spalten
pop_std = Top15.groupby("Continent")["Population"].std() # Standardabweichung berechnen von 2 Spalten

new_df = pd.concat([size, pop_sum, pop_mean, pop_std], axis = 1) # concat funktion. Verketten von Listen
new_df.columns = ["size", "sum", "mean", "std"] # erstellen eine dataframes aus den Berechnungen

print(new_df)