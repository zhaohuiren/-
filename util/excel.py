from xlrd import open_workbook
from xlutils.copy import copy
import os
import random
def receivables(code):
    rb=open_workbook(r'E:\a_测试文件\催收记录导入模板.xls')
    rs=rb.sheet_by_index(0)
    wb=copy(rb)
    ws = wb.get_sheet(0)
    ws.write(1,0,code)
    wb.save(r'E:\a_测试文件\催收记录导入模板程序.xls')

def projects():
    rb=open_workbook(r'E:\a_测试文件\委案\一条.xlsx')
    rs=rb.sheet_by_index(0)
    wb=copy(rb)
    ws = wb.get_sheet(0)
    ws.write(2,6,random.randint(0,100))
    wb.save(r'E:\a_测试文件\委案导入模板程序.xls')


projects()

