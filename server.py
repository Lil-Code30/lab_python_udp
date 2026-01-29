import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(64)
        print(f"Reçu {len(data)} octets de {addr}")
        print(f"message : {data}") # affichage du message Reçu
        s.sendto(b"OK", addr)