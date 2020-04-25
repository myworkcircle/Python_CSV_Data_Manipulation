import csv

file = "Input/main.csv"

fields = []
field2 = ["SKU","FIRST_MINIMUM_PRICE","SECOND_MINIMUM_PRICE"]
output_file = "output/LowestPrice.csv"
mp = {}
ans = []
with open(file,'r') as excel:
    csvreader = csv.reader(excel)
    fields = next(csvreader)
    for rows in csvreader:
        if("USA" in rows[8]):
            if( rows[0] not in mp):
                mp[rows[0]] = []
                try:
                    mp[rows[0]].append(float(rows[5][1:]))
                except:
                    pass
            else:
                if len(mp[rows[0]])<2:
                    try:
                        mp[rows[0]].append(float(rows[5][1:]))
                        mp[rows[0]].sort()
                    except:
                        pass
                else:
                    try:
                        mp[rows[0]].append(float(rows[5][1:]))
                        mp[rows[0]].sort()
                        mp[rows[0]].pop()
                    except:
                        pass

with open(output_file,'w') as final:
    csvwriter = csv.writer(final)
    csvwriter.writerow(field2)
    for key in mp:
        new_row = [key]
        new_row.extend(mp[key])
        csvwriter.writerow(new_row)
    # for key in mp:
    #     print(mp[key])
