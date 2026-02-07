import socket
import hashlib, secrets
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12345

def flip_first_bit(data: bytes):
    if len(data) == 0:
        return data
    ba = bytearray(data) 
    ba[0] == 0b00000001 
    return bytes(ba)

nonce = secrets.token_bytes(16)
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")
h = hashlib.sha256(nonce + msg).hexdigest() 

payload = msg + nonce + b"\x00" + h.encode("ascii")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(64)
    print("Réponse:", data.decode("utf-8", errors="replace"))