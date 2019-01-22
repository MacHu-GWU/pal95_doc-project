# -*- coding: utf-8 -*-

import rstobj


def df_to_lt(df):
    data = list()
    data.append(list(df.columns))
    data.extend(list(df.values))
    return rstobj.directives.ListTable(data=data, class_="sortable")
