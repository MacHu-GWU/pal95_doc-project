# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pandas as pd
from pathlib_mate import PathCls as Path
from ..dataframe_to_ltable import df_to_lt


p = Path(__file__).change(new_basename="monster.tsv")
df = pd.read_csv(p.abspath, sep="\t", encoding="utf8")
df.fillna("", inplace=True)

lt_monster = df_to_lt(df)
