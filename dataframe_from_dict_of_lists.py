import pandas as pd

# example 1: init a dataframe by dict without index
d = {"a": [1, 2, 3, 4], "b": [2, 4, 6, 8]}
df = pd.DataFrame(d)
print("The DataFrame ")
print(df)
print("The values of column a are {}".format(df["a"].values))
"""
   a  b
0  1  2
1  2  4
2  3  6
3  4  8
"""

# example 2: init a dataframe by dict with different index
d = {"a": {"a1": 1, "a2": 2, "c": 3}, "b": {"b1": 2, "b2": 4, "c": 9}}
df = pd.DataFrame(d)
print("The DataFrame ")
print(df)
"""
    a    b
a1  1.0  NaN
a2  2.0  NaN
b1  NaN  2.0
b2  NaN  4.0
c   3.0  9.0
"""
