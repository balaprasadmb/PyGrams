'''
Created on Dec 6, 2022

@author: bborade
'''



s = "5<US>2000000000002615~411111XXXXXX1111~1225~Bpd Msh Brd~VIC~N~<US>2000000000000102~545454XXXXXX5454~1225~Bpd Msh Brd~MCC~N~<US>2000000000000029~353011XXXXXX0000~1225~Bpd Msh Brd~JBC~N~<US>1000000000000108~601100XXXXXX1111~1225~Bpd Msh Brd~NVC~N~<US>1000000000000109~341111XXXXX2000~1225~Bpd Msh Brd~AXC~N~<US>"

l = s.split(sep="<US>")

print(l)
print(len(l))
