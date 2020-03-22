# coding=utf-8
from urllib import parse

import matplotlib.pyplot as plt
import networkx as nx
import pymysql
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import cancer_info_test, circrna_info_test,circRNA_cancer_test,circRNA_cancer, cancer_info, circRNA_miRNA, miRNA_cancer, miRNA_info, \
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

# 预测
def predicting(request):
    return render(request,'predicting.html',{})

