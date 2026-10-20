import os
import socket

port = int(os.environ.get("PORT", 10000))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", port))
server.listen(5)
print(f"[*] Cloud Server listening on port {port}...")

while True:
  client_socket, addr = server.accept()
  print(f"[+] Connection received from IP: {addr[0]}")
  client_socket.send(b"Hello from Lab Server!\n")
  client_socket.close()
