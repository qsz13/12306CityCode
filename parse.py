
# -*- coding: utf-8 -*

import json
fileHandle = open('/Users/danielqiu/Desktop/CityCode/rawCityCode.txt','r')

rawCode = fileHandle.readline()
outfile = open('/Users/danielqiu/Desktop/CityCode/output.txt','a+')
print >> outfile,"{"


output = []
codelist=rawCode.split('@')
cityname = ""
citycode = ""
for code in codelist:
	namelist = code.split('|')
	i = 0

	for name in namelist:

		if i==1:
			print "城市: "+name
			cityname = name
		if i==2:
			print "代码: "+name
			citycode = name
		i+=1
	print >> outfile,'"'+cityname+'":"'+citycode+'",'

print >> outfile,"}"




