#used methods: median(), astype, Vergleichsoperatoren mit pandas


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

Top15 = answer_one() # Dataframe Zugriff

# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15
# The Value 0 if the country's % Renewable value is below the median.
Top15['HighRenewe'] = (Top15['% Renewable'] >= Top15['% Renewable'].median()).astype(int) # Vergleich der Renewable mit dem Median der Renewable.
# Daraus ergeben sich Booleans (True or False). Mit Funktion astype(int) werden sie in Zahlen umbenannt.

Top15['HighRenewe'].sort_values(ascending=False)

