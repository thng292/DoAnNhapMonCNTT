import csv
import copy

variant = csv.reader(open("catalog_products.csv", mode="r", encoding="UTF-8"))
next(variant)
next(variant)

varfield = []

for i in variant :
    varfield.append(copy.deepcopy(i))

data = csv.reader(open("FinalDataWix.csv", mode="r", encoding="UTF-8"))

outp = []
outp.append(next(data))
for index, row in enumerate(data) :
    for i in row:
        i.strip()
    outp.append(row)
    tmp = copy.deepcopy(varfield)
    for i in tmp :
        i[0] = f"product_{index+1}"
        outp.append(i)

with open("ok.csv", "w", encoding="utf-8", newline="") as outf:
    writer = csv.writer(outf)
    writer.writerows(outp)
