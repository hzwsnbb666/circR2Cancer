import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\circR2Cancer\Table\circRNA-info.xlsx")
sheet = book.sheet_by_name("Sheet1")
#建立一个MySQL连接
conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='cirrna',
        port=3306,
        charset='utf8'
        )
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
query = 'insert into cirrnainfo_circrna_info(circRNA,method_of_circRNA_direction,expression_pattern,Chromosome,Region,Strand,Gene_Symbol,host_gene,tissue_or_cell_line,Transcription_interval,Sequence) values (%s, %s, %s, %s,%s,%s,%s, %s,%s,%s,%s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
    circRNA=sheet.cell(r,0).value.rstrip()
    method_of_circRNA_direction=sheet.cell(r,1).value
    expression_pattern=sheet.cell(r,2).value
    Chromosome=sheet.cell(r,3).value
    Region=sheet.cell(r,4).value
    Strand=sheet.cell(r,5).value
    Gene_Symbol=sheet.cell(r,6).value
    host_gene = sheet.cell(r,7).value
    tissue_or_cell_line = sheet.cell(r,8).value
    Transcription_interval = sheet.cell(r,9).value
    Sequence = sheet.cell(r,10).value
    values=(circRNA,method_of_circRNA_direction,expression_pattern,Chromosome,Region,Strand,Gene_Symbol,host_gene,tissue_or_cell_line,Transcription_interval,Sequence)
    # 执行sql语句
    cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")
