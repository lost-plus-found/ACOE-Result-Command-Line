#!/usr/bin/python3

import PyPDF2, os
import subprocess
import re
import csv

in_path = './curriculam/'
out_path = './pdftohtml/'
htmlFiles = []
for filename in os.listdir(in_path):
    if filename.endswith('.pdf'):
        in_file = in_path + filename
        out_file = out_path + str(len(htmlFiles) + 1)
        htmlFiles.append(out_file)
        subprocess.call("pdftohtml "+ in_file + ' ' + out_file + " >/dev/null", shell=True)

pattern = re.compile('[A-Z]{2}[0-9]{4}')
with open('Subject_list.csv', 'wb') as f:
    fieldnames = ['subject_code', 'credits']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for filename in os.listdir(out_path):
        if filename.endswith('s.html'):
            htmlObj = open(out_path+filename, 'rb')
            text = htmlObj.read()
            l = text.find('name=9')
            q = pattern.findall(text,0,l)
            text2 = text[0:l]
            text2 = text2.split('\n')
            j=0
            credits=[]
            for i,j in zip(text2,text2[5:]):
                i = i.strip('<br/>')
                j = j.strip('<br/>')
                if pattern.search(i) is not None:
                    credits.append(j)
                    writer.writerow({'subject_code': q[len(credits)-1], 'credits' : j })
            htmlObj.close()
            print len(credits)

    f.close()
