import json

data = {}

#with open("exp.json") as f:
#	print "Hi"
#	print f.read()
#	s = f.read()
#	print s
#	s = s.replace(";",",")
#	print s
#	f.close()

#with open("exp.json") as f:
#	data = json.load(f)
#	f.close()
str1='''{
	  "4.40" : "00",
	  "4.41" : "20",
	  "4.42" : "P2PE ENC FAIL: SUPPORT P2PE DISABLED",
	  "1.1" : "100000022840",
	  "1.2" : "112131",
	  "1.3" : "36383847",
	  "2.1" : "283080215",
	  "2.2" : "000B4FDDD253",
	  "2.3" : "10.20.10.166",
	  "3.1" : "15",
	  "3.2" : "Mx915",
	  "3.3" : "Reg2",
	  "3.4" : "00",
	  "3.5" : "8.807",
	  "3.6" : "1.8",
	  "3.7" : "RFS00190",
	  "3.8" : "1",
	  "4.1" : "221",
	  "4.2" : "000206",
	  "4.3" : "2",
	  "4.4" : "374245001751006%3D241220117111234500000",
	  #"4.4" : "9999999800002773%3D20121015432112345678",
	  "4.5" : "40.00",
	  "4.6" : "0.00",
	  "4.7" : "0.00",
	  "4.8" : "0.00",
	  "4.9" : "1.00",
	  "4.10" : "0.00",
	  "4.11" : "41.00",
	  "4.13" : "127001",
	  "4.15" : "7",
	  "4.16" : "4DF4D1CA6B231009",
	  "4.17" : "00000E01AE60011B",
	  #"4.16" : "D2DA5C31FA353E3C",
	  #"4.17" : "00000E004AE00ADE",
	  "4.18" : "05072018",
	  "4.19" : "181515",
	  "4.20" : "840",
	  "4.21" : "840",
	  "4.22" : "0",
	  "4.23" : "",
	  "4.24" : "",
	  "4.25" : "0001",
	  "4.26" : "1",
	  "4.27" : "",
	  "4.28" : "",
	  "4.29" : "",
	  "4.30" : "",
	  "4.31" : "",
	  "4.32" : "1",
	  "4.34" : "",
	  "4.39" : "",
	  "4.79" : "0",
	  "5.1" : "",
	  "5.2" : "",
	  "5.3" : "",
	  "5.4" : "111",
	  "5.5" : "",
	  "5.6" : "",
	  "5.7" : "",
	  "5.8" : "",
	  "6.1" : "",
	  "6.2" : "",
	  "6.3" : "",
	  "6.4" : "",
	  "6.5" : "",
	  "6.6" : "",
	  "6.7" : "",
	  "6.8" : "",
	  "6.9" : "",
	  "6.10" : "",
	  "6.11" : "",
	  "6.17" : "",
	  "6.18" : "",
	  "6.19" : "",
	  "6.20" : "",
	  "6.21" : "",
	  "6.22" : "",
	  "6.23" : "",
	  "6.24" : "",
	  "6.25" : "",
	  "6.26" : "",
	  "6.27" : "",
	  "7.1" : "10.00",
	  "7.2" : "10.00",
	  "7.3" : "1.00",
	  "7.4" : "000",
	  "7.5" : "",
	  "8.1" : "",
	  "14.13" : "2"
}'''
print str1.replace(';',',').replace('\n','').replace('=',':')
j=json.dumps(str1.replace(';',',').replace('\n','').replace('=',':'))
print type(j)
