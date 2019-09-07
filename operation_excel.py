# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: operation_excel.py
# @Time: 2019-08-25 18:31
import os

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

import get_path_info

path = get_path_info.get_path()


class Operation_excel:


    def __init__(self,xls_name=None, sheet_name=None):
        if xls_name:
            self.xls_name = xls_name
            self.sheet_name = sheet_name
        else:
            self.xls_name = os.path.join(path, 'testFile', 'case', 'userCase.xlsx')
            print(self.xls_name)
            self.sheet_name = 'login'
            print(self.sheet_name)
        self.data = self.get_data()






    def get_xls(self):
        cls = []
        xlsPath = os.path.join(path, 'testFile', 'case', self.xls_name)  # 获取用例文件的路径
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(self.sheet_name)
        nrows = sheet.nrows  # 获取sheet的行数
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != u'case_name':  # 如果Excel的Sheet的第i行的第一列不等于case_name，那么把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls


    def get_data(self):
        xlsPath = os.path.join(path, 'testFile', 'case',self.xls_name)  # 获取用例文件的路径
        book = xlrd.open_workbook(xlsPath)
        # sheet = book.sheets()[sheet_name]
        sheet = book.sheet_by_name(self.sheet_name)
        return sheet


    # 获取单元格的行数
    def get_lines(self):
        num = self.data
        return num.nrows


    # 获取单元格列数
    def get_ncols(self):
        num = self.data
        return num.ncols


    # 获取单元格中的内容
    def get_cell_value(self,row,nrows):
        data = self.data
        return data.cell_value(row,nrows)


    # # 写入数据
    # def write_value(self, xls_name,row, nrows, value):
    #     '''
    #     写入excel数据
    #     row,col,value
    #     '''
    #     read_data = xlrd.open_workbook(xls_name)
    #     write_data = copy(read_data)
    #     sheet_data = write_data.get_sheet(0)
    #     sheet_data.write(row, nrows, value)
    #     write_data.save(xls_name)



    # 获取某一列的数据
    def get_col_values(self,col_id=None):
        values = None
        sheet = self.data
        if col_id != None:
            values = sheet.col_values(col_id)
        else:
            values = sheet.col_values(0)
        return values


    # 获取某一行的数据
    def get_row_values(self,row_id):
        values = None
        sheet = self.data
        if row_id != None:
            values = sheet.row_values(row_id)
        else:
            values = sheet.row_values(0)
        return values


    # 根据case_id找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        ncols_value = self.get_col_values()
        for col_data in ncols_value:
            if case_id in col_data:
                return num
            num = num+1


    # 根据case_id找到对应行的内容
    def get_rows_values(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_values = self.get_row_values(row_num)
        return rows_values







if __name__ == '__main__':


    opers = Operation_excel()
    print(opers.get_xls()) # 获取sheet中的全部数据

    print(opers.get_data()) # 获取sheet中的全部数据

    print(opers.get_lines()) # 获取行数

    print(opers.get_ncols()) # 获取列数

    print(opers.get_col_values(0)) # 获取列值

    print(opers.get_row_values(0)) # 获取行值

    print(opers.get_row_num('login2')) # 获取case_id对应的行号

    print('获取单元格中的数据：',opers.get_cell_value(1,3))


    print(opers.get_xls()[0]) #获取第1列第1行的单元格内容

    print(opers.get_xls()[0][1]) #获取第1列第1行的单元格内容

    print(opers.get_xls()[1][2]) #获取第2列第3行的单元格内容