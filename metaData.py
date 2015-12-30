import csv
import re
import json
import random

#format ="Symbol","Name","LastSale","MarketCap","IPOyear","Sector","industry","Summary Quote",

fi=open("index.json","w")
fn=open("new.json","w")
fd=open("delete.json","w")
fc=open("change.json","w")
first_list=open("first.list","w")
update_list=open("update.list","w")

count=1
#### NASDAQ DATA ####
with open('./nasdaq.csv','rb') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      rand1 = random.random()
      if re.search('B$',row[3]):
        if rand1<0.9:
          fi.write('{ "create" : { "_index" : "finance2", "_type" : "stock", "_id" : "%s" } }\n' % count)
          fi.write('{ "id": "%s", "symbol" : "%s", "name":"%s" , "marketCap":"%s", "ipo":"%s","sector":"%s","industry":"%s" }\n' % (count,row[0],row[1],row[3],row[4],row[5],row[6]))
	  first_list.write('%d\n' % count)
	  rand2= random.random()
	  if rand2<0.05:
            fd.write('{ "delete" : { "_index" : "finance2", "_type" : "stock", "_id" : "%s" } }\n' % count)
	  elif rand2>0.95:
	    fc.write( '{ "update" : {"_id" : "%s", "_type" : "stock", "_index" : "finance2"} }\n'% count  )
	    fc.write('{"doc": {"marketCap":"%s+%.3fB"}}\n' % (row[3],rand2))
	    update_list.write('%d\n' % count)
	  else: 
	    update_list.write('%d\n' % count)
        else:
          fn.write('{ "create" : { "_index" : "finance2", "_type" : "stock", "_id" : "%s" } }\n' % count)
          fn.write('{ "id": "%s", "symbol" : "%s", "name":"%s" , "marketCap":"%s", "ipo":"%s","sector":"%s","industry":"%s" }\n' % (count,row[0],row[1],row[3],row[4],row[5],row[6]))
	  update_list.write('%d\n' % count)
	count+=1

#### NYSE DATA ####
with open('./nyse.csv','rb') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      rand1 = random.random()
      if re.search('B$',row[3]):
        if rand1<0.9:
          fi.write('{ "create" : { "_index" : "finance2", "_type" : "stock", "_id" : "%s" } }\n' % count)
          fi.write('{ "id": "%s", "symbol" : "%s", "name":"%s" , "marketCap":"%s", "ipo":"%s","sector":"%s","industry":"%s" }\n' % (count,row[0],row[1],row[3],row[4],row[5],row[6]))
	  rand2= random.random()
	  first_list.write('%d\n' % count)
	  if rand2<0.05:
            fd.write('{ "delete" : { "_index" : "finance2", "_type" : "stock", "_id" : "%s" } }\n' % count)
	  elif rand2>0.95:
	    fc.write( '{ "update" : {"_id" : "%s", "_type" : "stock", "_index" : "finance2"} }\n'% count  )
	    fc.write('{"doc": {"marketCap":"%s+%.3fB"}}\n' % (row[3],rand2))
	    update_list.write('%d\n' % count)
	  else:
	    update_list.write('%d\n' % count)
        else:
          fn.write('{ "create" : { "_index" : "finance2", "_type" : "stock", "_id" : "%s" } }\n' % count)
          fn.write('{ "id": "%s", "symbol" : "%s", "name":"%s" , "marketCap":"%s", "ipo":"%s","sector":"%s","industry":"%s" }\n' % (count,row[0],row[1],row[3],row[4],row[5],row[6]))
	  update_list.write('%d\n' % count)
	count+=1


fi.close()
fn.close()
fd.close()
fc.close()
first_list.close()
update_list.close()
