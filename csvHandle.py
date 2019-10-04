import csv

headers=['ID','UserName']
rows=[(1001,"wbq"),
      (1002,"wn")
]

with open('csvFile.csv','w') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)