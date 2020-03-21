# coding=utf-8
from urllib import parse

import matplotlib.pyplot as plt
import networkx as nx
import pymysql
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import disease, cirrna, relationship, circRNA_cancer, cancer_info, circRNA_miRNA, miRNA_cancer, miRNA_info, \
    circrna_info


# 主页
def index(request):
    return render(request, 'index.html', {})


# 浏览
def browse(request):
    Cir1 = circRNA_cancer.objects.all()
    Cir2 = circRNA_miRNA.objects.all()
    Cir3 = cancer_info.objects.all()
    Cir4 = miRNA_info.objects.all()
    Cir5 = miRNA_cancer.objects.all()
    Cir6 = circrna_info.objects.all()
    return render(request, 'browse/circRNA_Cancer.html',
                  {"Cir1": Cir1, "Cir2": Cir2, "Cir3": Cir3, "Cir4": Cir4, "Cir5": Cir5, "Cir6": Cir6})

def browse2(request):
    Cir1 = circRNA_cancer.objects.all()
    Cir2 = circRNA_miRNA.objects.all()
    Cir3 = cancer_info.objects.all()
    Cir4 = miRNA_info.objects.all()
    Cir5 = miRNA_cancer.objects.all()
    Cir6 = circrna_info.objects.all()
    return render(request, 'browse/circRNA_miRNA.html',
                  {"Cir1": Cir1, "Cir2": Cir2, "Cir3": Cir3, "Cir4": Cir4, "Cir5": Cir5, "Cir6": Cir6})

def browse3(request):
    Cir1 = circRNA_cancer.objects.all()
    Cir2 = circRNA_miRNA.objects.all()
    Cir3 = cancer_info.objects.all()
    Cir4 = miRNA_info.objects.all()
    Cir5 = miRNA_cancer.objects.all()
    Cir6 = circrna_info.objects.all()
    return render(request, 'browse/miRNA_Cancer.html',
                  {"Cir1": Cir1, "Cir2": Cir2, "Cir3": Cir3, "Cir4": Cir4, "Cir5": Cir5, "Cir6": Cir6})



def detail(request):
    url = request.get_full_path()
    url = parse.unquote(url)
    url.replace('<', '\<')
    i = 0
    while (i < len(url)):
        if (url[i] == "="):
            break
        i += 1
    url = url[i + 1:]
    List = url.split('&')
    lens = len(List)
    List[1] = List[1].rstrip()
    List[2] = List[2].rstrip()
    for k in range(1, lens):
        if (List[k] == "" or List[k] == None):
            List[k] = "N/A"
    db = pymysql.connect("localhost", "root", "123456", "cirrna")
    cursor = db.cursor()
    if (List[0] == '1'):
        dict1 = {}
        circrna_cancer = []
        dict1['circRNA'] = List[1]
        dict1['disease'] = List[2]
        dict1['pmid'] = List[3]
        dict1['functional_describution'] = List[4]
        circrna_cancer.append(dict1)
        ###########################################
        cursor.execute("select * from cirrnainfo_circrna_info where circRNA = '" + List[1] + "';")
        data2 = cursor.fetchone()
        dict2 = {}
        if (data2 is None):
            dict2['circRNA'] = List[1]
            dict2['method_of_circRNA_direction'] = "N/A"
            dict2['expression_pattern'] = "N/A"
            dict2['Chromosome'] = "N/A"
            dict2['Region'] = "N/A"
            dict2['Strand'] = "N/A"
            dict2['Gene_Symbol'] = "N/A"
            dict2['host_gene'] = "N/A"
            dict2['tissue_or_cell_line'] = "N/A"
            dict2['Transcription_interval'] = "N/A"
            dict2['Sequence'] = "N/A"
            circrna = []
            circrna.append(dict2)
        else:
            dict2['circRNA'] = data2[1]
            dict2['method_of_circRNA_direction'] = data2[2]
            dict2['expression_pattern'] = data2[3]
            dict2['Chromosome'] = data2[4]
            dict2['Region'] = data2[5]
            dict2['Strand'] = data2[6]
            dict2['Gene_Symbol'] = data2[7]
            dict2['host_gene'] = data2[8]
            dict2['tissue_or_cell_line'] = data2[9]
            dict2['Transcription_interval'] = data2[10]
            dict2['Sequence'] = data2[11]
            circrna = []
            circrna.append(dict2)
        ############################################
        cursor.execute("select * from cirrnainfo_cancer_info where disease = '" + List[2] + "';")
        data3 = cursor.fetchone()
        dict3 = {}
        if (data3 is None):
            dict3['disease'] = "N/A"
            dict3['DOID'] = "N/A"
            dict3['Definition'] = "N/A"
            dict3['Xrefs'] = "N/A"
            dict3['Subsets'] = "N/A"
            dict3['Synonyms'] = "N/A"
            dict3['Relationships'] = "N/A"
            cancer = []
            cancer.append(dict3)
        else:
            dict3['disease'] = data3[1]
            dict3['DOID'] = data3[2]
            dict3['Definition'] = data3[3]
            dict3['Xrefs'] = data3[4]
            dict3['Subsets'] = data3[5]
            dict3['Synonyms'] = data3[6]
            dict3['Relationships'] = data3[7]
            cancer = []
            cancer.append(dict3)
        flag = List[0]
        return render(request, 'detail.html',
                      {"circrna_cancer": circrna_cancer, "circrna": circrna, "cancer": cancer, "flag": flag})
    elif (List[0] == '2'):
        dict1 = {}
        circrna_mirna = []
        dict1['circRNA'] = List[1]
        dict1['miRNA'] = List[2]
        circrna_mirna.append(dict1)
        ###########################################
        cursor.execute("select * from cirrnainfo_circrna_info where circRNA = '" + List[1] + "';")
        data2 = cursor.fetchone()
        dict2 = {}
        if (data2 is None):
            dict2['circRNA'] = List[1]
            dict2['method_of_circRNA_direction'] = "N/A"
            dict2['expression_pattern'] = "N/A"
            dict2['Chromosome'] = "N/A"
            dict2['Region'] = "N/A"
            dict2['Strand'] = "N/A"
            dict2['Gene_Symbol'] = "N/A"
            dict2['host_gene'] = "N/A"
            dict2['tissue_or_cell_line'] = "N/A"
            dict2['Transcription_interval'] = "N/A"
            dict2['Sequence'] = "N/A"
            circrna = []
            circrna.append(dict2)
        else:
            dict2['circRNA'] = data2[1]
            dict2['method_of_circRNA_direction'] = data2[2]
            dict2['expression_pattern'] = data2[3]
            dict2['Chromosome'] = data2[4]
            dict2['Region'] = data2[5]
            dict2['Strand'] = data2[6]
            dict2['Gene_Symbol'] = data2[7]
            dict2['host_gene'] = data2[8]
            dict2['tissue_or_cell_line'] = data2[9]
            dict2['Transcription_interval'] = data2[10]
            dict2['Sequence'] = data2[11]
            circrna = []
            circrna.append(dict2)
        ################################
        cursor.execute("select * from cirrnainfo_mirna_info where miRNA = '" + List[2] + "';")
        data3 = cursor.fetchone()
        dict3 = {}
        if (data3 is None):
            dict3['miRNA'] = List[2]
            dict3['Accession'] = "N/A"
            dict3['symbol'] = "N/A"
            dict3['description'] = "N/A"
            dict3['gene_family'] = "N/A"
            dict3['Genome_context'] = "N/A"
            dict3['Clustered_miRNAs'] = "N/A"
            dict3['database_links'] = "N/A"
            mirna = []
            mirna.append(dict3)
        else:
            dict3['miRNA'] = data3[1]
            dict3['Accession'] = data3[2]
            dict3['symbol'] = data3[3]
            dict3['description'] = data3[4]
            dict3['gene_family'] = data3[5]
            dict3['Genome_context'] = data3[6]
            dict3['Clustered_miRNAs'] = data3[7]
            dict3['database_links'] = data3[8]
            mirna = []
            mirna.append(dict3)
        flag = List[0]
        return render(request, 'detail.html',
                      {"circrna_mirna": circrna_mirna, "circrna": circrna, "mirna": mirna, "flag": flag})
    elif (List[0] == '3'):
        dict1 = {}
        mirna_cancer = []
        dict1['miRNA'] = List[1]
        dict1['disease'] = List[2]
        dict1['pmid'] = List[3]
        dict1['description'] = List[4]
        mirna_cancer.append(dict1)
        ######################################
        cursor.execute("select * from cirrnainfo_mirna_info where miRNA = '" + List[1] + "';")
        data2 = cursor.fetchone()
        dict2 = {}
        if (data2 is None):
            dict2['miRNA'] = List[1]
            dict2['Accession'] = "N/A"
            dict2['symbol'] = "N/A"
            dict2['description'] = "N/A"
            dict2['gene_family'] = "N/A"
            dict2['Genome_context'] = "N/A"
            dict2['Clustered_miRNAs'] = "N/A"
            dict2['database_links'] = "N/A"
            mirna = []
            mirna.append(dict2)
        else:
            dict2['miRNA'] = data2[1]
            dict2['Accession'] = data2[2]
            dict2['symbol'] = data2[3]
            dict2['description'] = data2[4]
            dict2['gene_family'] = data2[5]
            dict2['Genome_context'] = data2[6]
            dict2['Clustered_miRNAs'] = data2[7]
            dict2['database_links'] = data2[8]
            mirna = []
            mirna.append(dict2)
        #####################################################
        cursor.execute("select * from cirrnainfo_cancer_info where disease = '" + List[2] + "';")
        data3 = cursor.fetchone()
        dict3 = {}
        if (data3 is None):
            dict3['disease'] = "N/A"
            dict3['DOID'] = "N/A"
            dict3['Definition'] = "N/A"
            dict3['Xrefs'] = "N/A"
            dict3['Subsets'] = "N/A"
            dict3['Synonyms'] = "N/A"
            dict3['Relationships'] = "N/A"
            cancer = []
            cancer.append(dict3)
        else:
            dict3['disease'] = data3[1]
            dict3['DOID'] = data3[2]
            dict3['Definition'] = data3[3]
            dict3['Xrefs'] = data3[4]
            dict3['Subsets'] = data3[5]
            dict3['Synonyms'] = data3[6]
            dict3['Relationships'] = data3[7]
            cancer = []
            cancer.append(dict3)
        flag = List[0]
        return render(request, 'detail.html',
                      {"mirna_cancer": mirna_cancer, "mirna": mirna, "cancer": cancer, "flag": flag})
    else:

        return render(request, 'detail.html', {})


def all(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('rows'))
        pageNumber = int(request.GET.get('page'))

    total = circRNA_cancer.objects.all().count()
    circrna_cancers = circRNA_cancer.objects.order_by('id')[(pageNumber - 1) * pageSize:(pageNumber) * pageSize]
    rows = []
    data = {"total": total, "rows": rows}
    for circrna_cancer in circrna_cancers:
        rows.append({'circRNA': circrna_cancer.circRNA, 'disease': circrna_cancer.disease,
                     'detail': '<a style="color: #5bc0de;" target="_blank" href="http://www.biobdlab.cn:8000/detail?value=1&' + circrna_cancer.circRNA + '&' + circrna_cancer.disease + '&' + circrna_cancer.pmid + '&' + circrna_cancer.functional_describution + '">detail</a>'})

    return HttpResponse(json.dumps(data), content_type="application/json")


def all2(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('rows'))
        pageNumber = int(request.GET.get('page'))

    total = circRNA_miRNA.objects.all().count()
    circrna_mirnas = circRNA_miRNA.objects.order_by('id')[(pageNumber - 1) * pageSize:(pageNumber) * pageSize]
    rows = []
    data = {"total": total, "rows": rows}
    for circrna_mirna in circrna_mirnas:
        rows.append({'circRNA': circrna_mirna.circRNA, 'miRNA': circrna_mirna.miRNA,
                     'detail': '<a style="color: #5bc0de;" target="_blank" href="http://www.biobdlab.cn:8000/detail?value=2&' + circrna_mirna.circRNA + '&' + circrna_mirna.miRNA + '">detail</a>'})

    return HttpResponse(json.dumps(data), content_type="application/json")

def all3(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('rows'))
        pageNumber = int(request.GET.get('page'))

    total = miRNA_cancer.objects.all().count()
    mirna_cancers = miRNA_cancer.objects.order_by('id')[(pageNumber - 1) * pageSize:(pageNumber) * pageSize]
    rows = []
    data = {"total": total, "rows": rows}
    for mirna_cancer in mirna_cancers:
        rows.append({'miRNA': mirna_cancer.miRNA, 'Cancer': mirna_cancer.disease,
                     'detail': '<a style="color: #5bc0de;" target="_blank" href="http://www.biobdlab.cn:8000/detail?value=3&' + mirna_cancer.miRNA + '&' + mirna_cancer.disease +'&'+mirna_cancer.pmid+ '&'+mirna_cancer.description+'&'+'">detail</a>'})

    return HttpResponse(json.dumps(data), content_type="application/json")

# 下载
def download(request):
    return render(request, 'download.html', {})


# 搜索
def search(request):
    dict1 = {}
    dict2 = {}
    dict3 = {}

    circrna_cancer = []
    circrna_mirna = []
    mirna_cancer = []
    cir1 = "database-content2"
    cir2 = "database-content2"
    cir3 = "database-content2"
    picFlag = "database-content2"
    search_type = request.GET.get("search-type")

    search_content = request.GET.get("search-content")

    nodes  = []
    links = []
    db = pymysql.connect("localhost", "root", "123456", "cirrna")
    cursor = db.cursor()
    flag = 0
    if search_content != None:
        search_content = search_content.strip()
        picFlag = 'database-content1'
        for item in search_content:
            if item != ' ' and item != '\t':
                flag = 1
                break
        if search_content == '' or flag == 0:
            return render(request, 'search.html',
                          {'flag1': 'no', 'circrna_cancer': circrna_cancer, 'circrna_mirna': circrna_mirna,
                           'mirna_cancer': mirna_cancer,
                           'Cir1': cir1, 'Cir2': cir2, 'Cir3': cir3, 'search_content': search_content,
                           'search_type': search_type})
        elif "$" in search_content or "'" in search_content or "%" in search_content or '"' in search_content or "@" in search_content or "+" in search_content or not search_content[0].isalpha():
            return render(request, 'search.html',
                          {'flag1': 'err', 'circrna_cancer': circrna_cancer, 'circrna_mirna': circrna_mirna,
                           'mirna_cancer': mirna_cancer,
                           'Cir1': cir1, 'Cir2': cir2, 'Cir3': cir3, 'search_content': search_content,
                           'search_type': search_type})
    if search_type == "circRNA":
        cir1 = "database-content1"
        cir2 = "database-content1"
        cir3 = "database-content2"
        cursor.execute("select * from cirrnainfo_circrna_cancer where circRNA='" + search_content + "';")
        data1 = cursor.fetchall()
        for item in data1:
            dict1 = {}
            dict1['circRNA'] = item[1]
            dict1['disease'] = item[2]
            dict1['pmid'] = item[13]
            dict1['functional_describution'] = item[4]
            circrna_cancer.append(dict1)

        cursor.execute("select * from cirrnainfo_circrna_mirna where circRNA='" + search_content + "';")
        data1 = cursor.fetchall()
        for item in data1:
            dict2 = {}
            dict2['circRNA'] = item[1]
            dict2['miRNA'] = item[2]
            circrna_mirna.append(dict2)

    elif search_type == "miRNA":
        cir1 = "database-content2"
        cir2 = "database-content1"
        cir3 = "database-content1"
        cursor.execute("select * from cirrnainfo_circrna_mirna where miRNA='" + search_content + "';")
        data1 = cursor.fetchall()
        for item in data1:
            dict2 = {}
            dict2['circRNA'] = item[1]
            dict2['miRNA'] = item[2]
            circrna_mirna.append(dict2)
        cursor.execute("select * from cirrnainfo_mirna_cancer where miRNA='" + search_content + "';")
        data1 = cursor.fetchall()
        for item in data1:
            dict3 = {}
            dict3['miRNA'] = item[1]
            dict3['disease'] = item[2]
            dict3['pmid'] = item[3]
            dict3['description'] = item[4]
            mirna_cancer.append(dict3)

    elif search_type == "Cancer":
        cir1 = "database-content1"
        cir2 = "database-content2"
        cir3 = "database-content1"
        cursor.execute("select * from cirrnainfo_circrna_cancer where disease='" + search_content + "';")
        data1 = cursor.fetchall()
        for item in data1:
            dict1 = {}
            dict1['circRNA'] = item[1]
            dict1['disease'] = item[2]
            dict1['pmid'] = item[13]
            dict1['functional_describution'] = item[4]
            circrna_cancer.append(dict1)
        cursor.execute("select * from cirrnainfo_mirna_cancer where disease='" + search_content + "';")
        data1 = cursor.fetchall()
        for item in data1:
            dict3 = {}
            dict3['miRNA'] = item[1]
            dict3['disease'] = item[2]
            dict3['pmid'] = item[3]
            dict3['description'] = item[4]
            mirna_cancer.append(dict3)
    return render(request, 'search.html',
                  {'flag1': 'ok', 'circrna_cancer': circrna_cancer, 'circrna_mirna': circrna_mirna,
                   'mirna_cancer': mirna_cancer,
                   'Cir1': cir1, 'Cir2': cir2, 'Cir3': cir3, 'search_content': search_content,
                   'search_type': search_type,'picFlag':picFlag})


# 关于
def about(request):
    return render(request, 'about.html', {})


def getdisease(request, diseaseid):
    try:
        mydisease = disease.objects.get(id=diseaseid)

        strs = '''
        
        <p>name_in_cirrna --> ''' + str(mydisease.name_incirrna).replace("<>", ";<br />") + '''<br /><br />

        name --> ''' + str(mydisease.name).replace("<>", ";<br />") + '''<br /><br />

        DOID --> ''' + str(mydisease.DOID).replace("<>", "<br />") + '''<br /><br />

        Definition -->  ''' + str(mydisease.Definition).replace("<>", "<br />") + '''<br /><br />

        Xrefs -->  ''' + str(mydisease.Xrefs).replace("<>", "<br />") + '''<br /><br />

        Alternateids  -->  ''' + str(mydisease.Alternateids).replace("<>", "<br />") + '''<br /><br />

        Subsets   -->  ''' + str(mydisease.Subsets).replace("<>", "<br />") + '''<br /><br />

        Synonyms  -->  ''' + str(mydisease.Synonyms).replace("<>", "<br />") + '''<br /><br />

        Relationships  -->  ''' + str(mydisease.Relationships).replace("<>", "<br />") + '''<br /><br />
        </p>'''

        """
        '''     
        <table border="1" width="800px">
           <tr>
            <th>name_in_cirrna</th>
            <th>name</th>
            <th>DOID</th>
            <th>Definition</th>
            <th>Xrefs</th>
            <th>Alternateids</th>
            <th>Subsets</th>
            <th>Synonyms</th>
            <th>Relationships</th>
          </tr>
          <tr>
            <td> '''+str(mydisease.name_incirrna).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.name).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.DOID).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.Definition).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.Xrefs).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.Alternateids).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.Subsets).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.Synonyms).replace("<>",";<br />")+'''</td>
            <td> '''+str(mydisease.Relationships).replace("<>",";<br />")+'''</td>

          </tr> 
         </table>'''
      """

    except disease.DoesNotExist:
        raise Http404

    print(strs)
    return HttpResponse(strs)


def getcirrna(request, cirrnaid):
    try:
        mycirrna = cirrna.objects.get(id=cirrnaid)

        strs = '''
        
        <p>name_cirrna --> ''' + str(mycirrna.name_cirrna) + '''<br /><br />

        chrom --> ''' + str(mycirrna.chrom) + '''<br /><br />

        start --> ''' + str(mycirrna.start) + '''<br /><br />

        end -->  ''' + str(mycirrna.end) + '''<br /><br />

        strand -->  ''' + str(mycirrna.strand) + '''<br /><br />

        circRNA_ID  -->  ''' + str(mycirrna.circRNA_ID) + '''<br /><br />

        genomic_length   -->  ''' + str(mycirrna.genomic_length) + '''<br /><br />

        spliced_seq_length  -->  ''' + str(mycirrna.spliced_seq_length) + '''<br /><br />

        samples  -->  ''' + str(mycirrna.samples) + '''<br /><br />



        repeats -->  ''' + str(mycirrna.repeats) + '''<br /><br />

        annotation  -->  ''' + str(mycirrna.annotation) + '''<br /><br />

        best_transcript   -->  ''' + str(mycirrna.best_transcript) + '''<br /><br />

        gene_symbol  -->  ''' + str(mycirrna.gene_symbol) + '''<br /><br />

        circRNA_study  -->  ''' + str(mycirrna.circRNA_study) + '''<br /><br />


        </p>'''


    except disease.DoesNotExist:
        raise Http404

    print(strs)
    return HttpResponse(strs)


def displayiframe(request):
    return render(request, 'iframe.html')


def displaydisease(request, name):
    re = relationship.objects.filter(disease_name=name)

    dise = disease.objects.filter(name_incirrna=name)

    dd = []

    ss = ";___\n"

    for i in dise:
        ll = {}
        ll['name_incirrna'] = str(i.name_incirrna).replace("<>", ss)

        ll['name'] = str(i.name).replace("<>", ss)
        ll['DOID'] = str(i.DOID).replace("<>", ss)
        ll['Definition'] = str(i.Definition).replace("<>", ss)
        ll['Xrefs'] = str(i.Xrefs).replace("<>", ss)
        ll['Alternateids'] = str(i.Alternateids).replace("<>", ss)
        ll['Subsets'] = str(i.Subsets).replace("<>", ss)
        ll['Relationships'] = str(i.Relationships).replace("<>", ss)
        dd.append(ll)

    lists = {
        'rela': re,
        'dise': dd,
        'nn': name,
    }

    print(lists['dise'])
    return render(request, 'diseaseiframe.html', lists)


def displaycirrna(request, name):
    re = relationship.objects.filter(displaycir_id=name)

    cir = cirrna.objects.filter(name_cirrna=name)

    lists = {
        'rela': re,
        'cir': cir,
        'nn': name,
    }
    print(lists)
    return render(request, 'ciriframe.html', lists)


def searchcirrna(request, name):
    # cir = cirrna.objects.get(name_cirrna__contains=name)
    cir = []
    cir = relationship.objects.filter(displaycir_id__contains=name)
    flag = False
    num = 0
    strs = '''<table cellpadding="0" cellspacing="1" class="cxtable" id="angel">
    <tr bgcolor="#e4eff8">
        <th width="20px">number</th>
        <th width="80px">name</th>
    </tr>'''

    for i in cir:
        num = num + 1
        flag = True
        strs += '''    <tr bgcolor="#f4f5f6" ><td align="center">''' + str(num) + '''</td>
        <td align="center"><a onclick='openwinc("''' + str(i.displaycir_id) + '''")' \

        href="javascript:void(0)"/">''' + str(i.displaycir_id) + '''</a></td>

         </tr>'''

    if flag:
        strs = '''<h4 class="if2dqwz"> ''' + str(num) + ''' results</h4>''' + strs + '''</table>'''

        return HttpResponse(strs)

    else:
        return HttpResponse('''<h4 class="if2dqwz"> 0 results</h4>''')


def searchdisease(request, name):
    # cir = cirrna.objects.get(name_cirrna__contains=name)
    cir = []
    cir = relationship.objects.filter(disease_name__contains=name)
    flag = False
    num = 0
    strs = '''<table cellpadding="0" cellspacing="1" class="cxtable" id="angel">
    <tr bgcolor="#e4eff8">
        <th width="20px">number</th>
        <th width="80px">name</th>
    </tr>'''

    for i in cir:
        num = num + 1
        flag = True
        strs += '''    <tr bgcolor="#f4f5f6" ><td align="center">''' + str(num) + '''</td>
        <td align="center"><a onclick='openwind("''' + str(i.disease_name) + '''")' \

        href="javascript:void(0)"/">''' + str(i.disease_name) + '''</a></td>

         </tr>'''

    if flag:
        strs = '''<h4 class="if2dqwz"> ''' + str(num) + ''' results</h4>''' + strs + '''</table>'''

        return HttpResponse(strs)

    else:
        return HttpResponse('''<h4 class="if2dqwz"> 0 results</h4>''')


def drawfigure(request):
    # conn = pymysql.connect("localhost","root","zhy0791","cirrna")

    # 游标设置为字典类型
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # r = cursor.execute("call p1()")

    # result = cursor.fetchone()

    # conn.commit()
    # cursor.close()
    # conn.close()
    if request.method == "POST":
        t1 = request.POST.get("inputcirrna", None)
        t2 = request.POST.get("inputmrna", None)
        t3 = request.POST.get("inputdesease", None)
        t1.rstrip()
        t2.rstrip()
        t3.rstrip()
        conn = pymysql.connect("localhost", "root", "123456", "cirrna")
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor3 = conn.cursor()
        G = nx.Graph()
        if t1 != "" and t2 != "" and t3 != "":
            G.add_node(t1)
            G.add_node(t3)
            G.add_node(t2)

            cursor1.execute(
                "select * from cirrnainfo_circrna_cancer where circRNA='" + t1 + "' AND disease='" + t3 + "';")
            cursor2.execute("select * from cirrnainfo_mirna_cancer where miRNA='" + t2 + "' AND disease='" + t3 + "';")
            cursor3.execute("select * from cirrnainfo_circrna_mirna where circRNA='" + t1 + "' AND miRNA='" + t2 + "';")
            if cursor1.fetchone() is not None:
                G.add_edge(t1, t3, color='red')
            elif cursor2.fetchone() is not None:
                G.add_edge(t2, t3, color='red')
            elif cursor3.fetchone() is not None:
                G.add_edge(t1, t2, color='red')
        elif t1 == "" and t2 != "" and t3 != "":
            G.add_node(t2)
            G.add_node(t3)
            cursor1.execute(
                "select miRNA,disease from cirrnainfo_mirna_cancer where miRNA='" + t2 + "' AND disease='" + t3 + "';")
            cursor2.execute("select circRNA from cirrnainfo_circrna_mirna where miRNA='" + t2 + "';")
            cursor3.execute("select circRNA from cirrnainfo_circrna_cancer where disease='" + t3 + "';")
            if cursor1.fetchone() is not None:
                G.add_edge(t2, t3, color='red')
            i = cursor2.fetchall()
            print(i)
            for j in i:
                G.add_node(j[0])
                G.add_edge(j[0], t2, color='red')

            i = cursor3.fetchall()
            print(i)
            for j in i:
                G.add_node(j[0])
                G.add_edge(j[0], t3, color='red')


        elif t1 != "" and t2 == "" and t3 != "":
            G.add_node(t1)
            G.add_node(t3)
            cursor1.execute(
                "select circRNA,disease from cirrnainfo_circrna_cancer where circRNA='" + t1 + "' AND disease='" + t3 + "'")
            cursor2.execute("select miRNA from cirrnainfo_circrna_mirna where circRNA='" + t1 + "'")
            cursor3.execute("select miRNA from cirrnainfo_mirna_cancer where disease='" + t3 + "'")

            if cursor1.fetchone() is not None:
                G.add_edge(t1, t3, color='red')

            i = cursor2.fetchall()
            for j in i:
                G.add_node(j[0])
                G.add_edge(j[0], t2, color='red')

            i = cursor3.fetchall()
            for j in i:
                G.add_node(j[0])
                G.add_edge(j[0], t3, color='red')



        elif t1 != "" and t2 != "" and t3 == "":
            G.add_node(t1)
            G.add_node(t2)
            cursor1.execute(
                "select circRNA,miRNA from cirrnainfo_circrna_mirna where circRNA='" + t1 + "' AND miRNA='" + t2 + "'")
            cursor2.execute("select disease from cirrnainfo_circrna_cancer where circRNA='" + t1 + "'")
            cursor3.execute("select disease from cirrnainfo_mirna_cancer where miRNA='" + t2 + "'")

            if cursor1.fetchone() is not None:
                G.add_edge(t1, t2, color='red')
            i = cursor2.fetchall()
            for j in i:
                G.add_node(j[0])
                G.add_edge(j[0], t1, color='red')

            i = cursor3.fetchall()
            for j in i:
                G.add_node(j[0])
                G.add_edge(j[0], t2, color='red')


        elif t1 != "" and t2 == "" and t3 == "":
            cursor1.execute("select miRNA from cirrnainfo_circrna_mirna where circRNA='" + t1 + "'")
            cursor2.execute("select disease from cirrnainfo_circrna_cancer where circRNA='" + t1 + "'")

            i = cursor1.fetchall()
            print(i)
            j = cursor2.fetchall()
            print(j)
            for m in i:
                G.add_node(m[0])
                G.add_edge(m[0], t1, color='red')
                for n in j:
                    G.add_node(n[0])
                    G.add_edge(n[0], t1, color='red')
                    if cursor3.execute(
                            "select * from cirrnainfo_mirna_cancer where miRNA='" + m[0] + "' and disease='" + n[
                                0] + "'") is not None:
                        G.add_edge(n[0], m[0], color='red')


        elif t1 == "" and t2 != "" and t3 == "":
            cursor1.execute("select circRNA from cirrnainfo_circrna_mirna where miRNA='" + t2 + "'")
            cursor2.execute("select disease from cirrnainfo_mirna_cancer where miRNA='" + t2 + "'")

            i = cursor1.fetchall()
            print(i)
            j = cursor2.fetchall()
            print(j)
            for m in i:
                G.add_node(m[0])
                G.add_edge(m[0], t2, color='red')
                for n in j:
                    G.add_node(n[0])
                    G.add_edge(n[0], t2, color='red')
                    if cursor3.execute(
                            "select * from cirrnainfo_circrna_cancer where circRNA='" + m[0] + "' and disease='" + n[
                                0] + "'") is not None:
                        G.add_edge(n[0], m[0], color='red')


        elif t1 == "" and t2 == "" and t3 != "":
            cursor1.execute("select circRNA from cirrnainfo_circrna_cancer where disease='" + t3 + "'")
            cursor2.execute("select miRNA from cirrnainfo_mirna_cancer where disease='" + t3 + "'")

            i = cursor1.fetchall()
            j = cursor2.fetchall()
            for m in i:
                G.add_node(m[0])
                G.add_edge(m[0], t3, color='red')
                for n in j:
                    G.add_node(n[0])
                    G.add_edge(n[0], t3, color='red')
                    if cursor3.execute(
                            "select * from cirrnainfo_circrna_mirna where circRNA='" + m[0] + "' and miRNA='" + n[
                                0] + "'") is not None:
                        G.add_edge(n[0], m[0], color='red')

        nx.draw(G, with_labels=True)
        plt.savefig('E:/Me/myfile/project/cirRNA/cirRNAInfo/static/img/1.png')
        # plt.show()

    return render(request, "drawfigure.html")
