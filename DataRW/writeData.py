import xlwt
import xlrd
data = xlrd.open_workbook(r'I:\data.xlsx')
# data = xlwt.open_workbook(r'I:\data.xlsx')

table = data.sheet_by_name(u'Sheet1')
for i in range(table.ncols):
    name = table.cell(0, i).value
    print(name)
