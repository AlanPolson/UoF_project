#Converted to csv first
#See csv_parser_row_wise notebook for how this code was created
import csv
import pandas as pd

with open("../Data/Dallas_UOF_2015_CSV.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        #adding Exception for first Row:
        if row[0]=='ID':
            with open ("../Data/Dallas_UOF_2015_Editted_CSV.csv",'w') as newf:
                writer = csv.writer(newf)
                writer.writerow(row+['Lat','Long'])
                continue
        item = row[-1] #taking last item on the row
        start_bracket = end_bracket = comma = lat = lon = None
        #getting the character positions of '(' ',' and ')':
        for j in range(0,len(item)):
            char = item[j]
            if char == '(':
                start_bracket = j
            elif char == ')':
                end_bracket = j
            elif char > start_bracket and char == ',':
                comma = j
        if start_bracket:#added this because if no brackets are present, but address is, address commas confuse
            lat = item[start_bracket+1:comma]
            lon = item[comma+1:end_bracket]
        with open ("../Data/Dallas_UOF_2015_Editted_CSV.csv",'a') as newf:
            writer = csv.writer(newf)
            writer.writerow(row+[lat,lon])
#We delete the old 'Geolocation column because its newline characters confuse excel
data = pd.read_csv("../Data/Dallas_UOF_2015_Editted_CSV.csv")
del data['GeoLocation']
data.to_csv("../Data/Dallas_UOF_2015_Editted_CSV.csv")