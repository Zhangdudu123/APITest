# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: readExcel.py
# @Time: 2019-08-19 14:11

import os
import get_path_info
from xlrd import open_workbook

#拿到该项目所在的绝对路径
path = get_path_info.get_path()

class readExcel():

    def get_xls(self,xls_name,sheet_name):
        cls = []
        xlsPath = os.path.join(path,'testFile','case',xls_name) #获取用例文件的路径
        file = open_workbook(xlsPath) #打开用例Excel
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows #获取sheet的行数
        for i in range(nrows): #根据行数做循环
            if sheet.row_values(i)[0] != u'case_name': #如果Excel的Sheet的第i行的第一列不等于case_name，那么把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls










if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx','login'))
    print(readExcel().get_xls('userCase.xlsx','login')[0][1]) #获取第1列第1行的单元格内容
    print(readExcel().get_xls('userCase.xlsx','login')[1][2]) #获取第2列第3行的单元格内容
