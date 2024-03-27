
fname = r'C:\Workspace\AuruspayRobot\auruspay\smoke\schnucks.robot'

f = open(fname, 'r')

print(dir(f))

contents = f.read()

print(contents)

#contents = contents.encode()

contents = str(contents).replace('\r\n', '\n')

print(contents)

f = open(fname, 'w')
f.seek(0)
f.write(contents)#.encode('utf-8')))
f.close()
