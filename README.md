# eDx-Data-Science-Essential-

## pandas merge :
* https://stackoverflow.com/questions/20375561/joining-pandas-dataframes-by-column-names

## pandas drop duplicate: 
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop_duplicates.html

## handling missing data: 
* https://www.oreilly.com/learning/handling-missing-data

* https://pandas.pydata.org/pandas-docs/stable/missing_data.html

* https://chrisalbon.com/python/pandas_missing_data.html

* df.fillna(0) returns a new dataframe; it does not alter df. So either use:
    * dataframe['col_xyz'] = dataframe['col_xyz'].fillna(0)           #  for exact column
    * dataframe = dataframe.fillna(0)                                 # for all column     
    * or
    * dataframe['col_name'].fillna(0, inplace=True)                   # for exact column
    * dataframe.fillna(0, inplace=True)                               # for all column
