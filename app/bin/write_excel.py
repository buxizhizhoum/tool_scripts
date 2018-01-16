#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
function to write pandas DataFrame data to excel.
"""
import openpyxl
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows


def write_to_excel(data, filename, sheet_name, index=True):
    wb = openpyxl.Workbook()  # create workbook
    ws = wb.create_sheet(sheet_name)  # create sheet

    head_flag = True
    for r in dataframe_to_rows(data, index=index, header=head_flag):
        ws.append(r)
        head_flag = False

    wb.save(filename)


if __name__ == "__main__":
    a = range(10)
    test_data = {str(i): i*i for i in a}
    df = pd.DataFrame(test_data, index=a)

    write_to_excel(df, "/tmp/test_01.xlsx", "sheet_01")
