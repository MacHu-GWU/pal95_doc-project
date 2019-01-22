# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pandas as pd
from pathlib_mate import PathCls as Path
from ..dataframe_to_ltable import df_to_lt


p = Path(__file__).change(new_basename="spell.tsv")
df = pd.read_csv(p.abspath, sep="\t", encoding="utf8")

def intify(v):
    try:
        return int(v)
    except:
        return v

integer_columns = "真​氣​消​耗,基礎攻擊力".split(",")
for c in integer_columns:
    df[c] = df[c].apply(intify)

df.fillna("", inplace=True)

lt_spell_lxy = df_to_lt(df[df["人物"] == "李逍遙"])
lt_spell_zle = df_to_lt(df[df["人物"] == "趙靈兒"])
lt_spell_lyr = df_to_lt(df[df["人物"] == "林月如"])
lt_spell_an = df_to_lt(df[df["人物"] == "阿奴"])

if __name__ == "__main__":
    print(df)