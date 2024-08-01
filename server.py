import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting for connections")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr)



    c.send(bytes('welcome kira', 'utf-8'))

    c.close()
