import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('libgen.is', 80))
cmd = 'GET https://libgen.is/search.php?req=python+programming&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
