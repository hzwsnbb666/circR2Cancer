import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\circR2Cancer\Table\MiRNA信息.xlsx")
sheet = book.sheet_by_name("miRNA-info")
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
query = 'insert into cirrnainfo_mirna_info(miRNA,Accession,symbol,description,gene_family,Genome_context,Clustered_miRNAs,database_links) values (%s, %s, %s, %s,%s,%s,%s,%s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
    miRNA=sheet.cell(r,0).value.rstrip()
    Accession=sheet.cell(r,1).value
    symbol=sheet.cell(r,2).value
    description=sheet.cell(r,3).value
    gene_family=sheet.cell(r,4).value
    Genome_context=sheet.cell(r,5).value
    Clustered_miRNAs=sheet.cell(r,6).value
    database_links=sheet.cell(r,7).value
    values=(miRNA,Accession,symbol,description,gene_family,Genome_context,Clustered_miRNAs,database_links)
    # 执行sql语句
    cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")
