import csv, sys

grades = {'S':10.0, 'A':9.0, 'B':8.0, 'C':7.0, 'D':6.0, 'E':5.0, 'U':0.0, 'W':0.0}
credits = {}

def credit_set():
        credits_file  = 'credits.csv'
        with open(credits_file) as credits_obj:
            reader = csv.reader(credits_obj, delimiter=',')
            for row in reader:
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
