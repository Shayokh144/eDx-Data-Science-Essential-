# eDx-Data-Science-Essential-

## pandas merge :
* https://stackoverflow.com/questions/20375561/joining-pandas-dataframes-by-column-names

## pandas drop duplicate: 
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop_duplicates.html

## handling missing data: 
* https://www.oreilly.com/learning/handling-missing-data

* https://pandas.pydata.org/pandas-docs/stable/missing_data.html

* https://chrisalbon.com/python/pandas_missing_data.html

* df.fillna(0) returns a new dataframe; it does not alter df.

So either use

df = df.fillna(0)           # assigns df to a new dataframe
or

df.fillna(0, inplace=True)  # modifies df inplace 
