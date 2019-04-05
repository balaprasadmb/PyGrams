import cx_Oracle

uat = "192.168.70.120"

oc = "172.168.70.116"

# connection = cx_Oracle.connect("AURUSPAY", "AURUSPAY", "172.30.30.70/auruspay")

con = cx_Oracle.connect("AURUSPAY", "AURUSPAY", "172.168.70.116:1521/live")

cur = con.cursor()

cur_dir = ['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'arraysize', 'arrayvar', 'bindarraysize', 'bindnames', 'bindvars',
'callfunc', 'callproc', 'close', 'connection', 'description', 'execute', 'executemany', 'executemanyprepared', 'fetchall', 'fetchmany', 'fetchone', 'fetchraw',
'fetchvars', 'getarraydmlrowcounts', 'getbatcherrors', 'getimplicitresults', 'inputtypehandler', 'next', 'outputtypehandler', 'parse', 'prepare', 'rowcount',
'rowfactory', 'scroll', 'scrollable', 'setinputsizes', 'setoutputsize', 'statement', 'var']

res = cur.execute("select * from auruspay.transactions")

for r in res.fetchone():
    print r