from bs4 import BeautifulSoup
import csv, sys, urllib2

grades = {'S':10.0, 'A':9.0, 'B':8.0, 'C':7.0, 'D':6.0, 'E':5.0, 'U':0.0, 'W':0.0}
credits = {}

def credit_set():
    #url = urllib2.urlopen('https://gist.githubusercontent.com/prabhakaran9397/3f100b326c96aa4a60187ee82fc10e06/raw/9f01a3f5af9e436b3780b830c5204d543d5209f1/credits.txt')
    url = urllib2.urlopen('http://localhost:4000/credits.txt')
    content = url.read()
    credits_file  = BeautifulSoup(content, 'html.parser').string
    credits_bundle = map(str, credits_file.split('\n'))
    for i in  credits_bundle:
        if len(i) > 0:
            row = map(str, i.split())
            credits.setdefault(row[0], row[1])

if __name__ == '__main__':
    credit_set()
    total_credits = 0.0
    total_acc = 0.0
    for line in table:
        total_credits += credits[line[0]]
        total_acc += credits[line[0]]*grades[line[2]]
    gpa = total_acc/total_credits
    print gpa
