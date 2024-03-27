'''
Created on 25-Oct-2023

@author: bborade
'''
import  socket

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ms.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

ms.send(cmd)

while True:
    d = ms.recv(512)
    if len(d) < 1:
        break
    print(d.decode(), end=' ')
ms.close()

