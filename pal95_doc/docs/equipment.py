# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pandas as pd
from pathlib_mate import PathCls as Path
from ..dataframe_to_ltable import df_to_lt


p = Path(__file__).change(new_basename="equipment.tsv")
df = pd.read_csv(p.abspath, sep="\t", encoding="utf8")

def intify(v):
    try:
        return int(v)
    except:
        return v

integer_columns = "排序,武術,防禦,身法,吉運,靈力".split(",")
for c in integer_columns:
    df[c] = df[c].apply(intify)

df.fillna("", inplace=True)

lt_equipment = df_to_lt(df)

if __name__ == "__main__":
    print(df)