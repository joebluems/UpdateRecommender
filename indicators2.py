import csv
import json

ids=[]
with open('update.list','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    for row in csv_reader:
	ids.append(row[0])

### read the output from MAHOUT and collect into hash ###
indicators={}
with open('output2/part-r-00000','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    for row in csv_reader:
      ##### indicators ###
      if float(row[2])>0.90:
        if int(row[0])<10000:
          if row[0] not in indicators: indicators[row[0]]=[]
	  indicators[row[0]].append(row[1])
        if int(row[1])<10000:
          if row[1] not in indicators: indicators[row[1]]=[]
	  indicators[row[1]].append(row[0])
 
### print out the array of recs for each film ### 
for a in ids:
   if a not in indicators:
      indicators[a]=[]
   print '{ "update" : {"_id" : "%s", "_type" : "stock", "_index" : "finance2"} }'% a  
   print('{"doc": {"indicators":%s}}') % json.dumps(indicators[a])
