#used methods: df.max() - df.min() from columns, sort_values, first_valid_index()

import pandas as pd
censusDF = pd.read_csv('census.csv')
censusDF.head()

#Which county has had the largest absolute change in population within the period 2010-2015?
#e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.

def answer_seven():
    filtered_columns = ["POPESTIMATE2015", "POPESTIMATE2014", "POPESTIMATE2013", "POPESTIMATE2012", "POPESTIMATE2011",
                        "POPESTIMATE2010"] #Auswahl der Spalten für die Berechnung
    filtered_rows = censusDF[censusDF["SUMLEV"] == 50] # Auswahl der Counties jedoch auf Basis eines DataFrames
    filtered_df = filtered_rows[filtered_columns] # Erstellung des geeigneten DataFrames

    max_diff_country = (filtered_df.max(axis='columns') - filtered_df.min(axis='columns'))  # Max und Min Funktion gehen alle Spalten pro Zeile durch. mit (axis='columns' oder 1) wird die der höchste Wert
                                                                                            # pro Zeile gesucht. mit (axis='index' or 0) wird der höchste Wert der Spalte gesucht
    sort_diff_country = max_diff_country.sort_values(ascending=False)

    index_of_max_diff_country = sort_diff_country.first_valid_index() # Gibt  den ersten Index Eintrag des Dataframes wider

    return censusDF["CTYNAME"][index_of_max_diff_country] # Verknüpfung des Indexeintrages mit dem Citynamen.


print(answer_seven())