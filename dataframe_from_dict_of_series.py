import pandas as pd

# example 1: series without index
s = {"a": pd.Series(range(1, 3)), "b": pd.Series(range(2, 4))}

df = pd.DataFrame(s)
print("dataframe created from dict of series")
print(df)
print("--------------------")

# example 2: series with index
s = {
    "a": pd.Series(range(1, 3), index=["a", "b"]),
    "b": pd.Series(range(2, 4), index=["b", "c"])
}
df = pd.DataFrame(s)
print("dataframe created from dict of series with index")
print(df)


"""
dataframe created from dict of series
   a  b
0  1  2
1  2  3
--------------------
dataframe created from dict of series with index
     a    b
a  1.0  NaN
b  2.0  2.0
c  NaN  3.0
"""


d = {"a": [1, 2, 3, 4], "b": [2, 4, 6, 8]}
df = pd.DataFrame.from_dict(d)
print("dataframe created from from_dict")
print(df)
print("--------------------")

df = pd.DataFrame.from_dict(d, orient="index")
print("dataframe created from from_dict and set the orient")
print(df)
"""
dataframe created from from_dict
0  1  2
1  2  4
2  3  6
3  4  8
--------------------
dataframe created from from_dict and set the orient
   0  1  2  3
b  2  4  6  8
a  1  2  3  4
"""