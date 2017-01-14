import xlwt
from datetime import datetime

# 创建workbook（其实就是excel，后来保存一下就行）
workbook = xlwt.Workbook()
# 创建表
worksheet = workbook.add_sheet('Test Sheet')

# 创建样式
style0 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

# 写数据
worksheet.write(0, 0, 123456, style0)
worksheet.write(1, 0, datetime.now(), style1)
worksheet.write(2, 0, 88888)
worksheet.write(2, 1, 99999)
worksheet.write(2, 2, xlwt.Formula("A3+B3"))

# 保存表格
workbook.save('test.xls')