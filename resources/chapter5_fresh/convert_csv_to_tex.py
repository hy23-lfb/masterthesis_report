import csv
from tabulate import tabulate

# Open the CSV file and read in the data
with open(r'D:\04.GitRepository\masterthesis_report\resources\chapter5_fresh\stats_per_scan.csv', 'r') as f:
  data = list(csv.reader(f))

'''
# Make the first row and first column bold
for i in range(len(data)):
    for j in range(len(data[i])):
        if i == 0 or j == 0:
            data[i][j] = "{" + data[i][j] + '}'
'''

# Generate the LaTeX table
table = tabulate(data, tablefmt='latex')

# Open the LaTeX file for writing
with open(r'D:\04.GitRepository\masterthesis_report\resources\chapter5_fresh\stats_per_scan.tex', 'w') as f:
    f.write(table)
