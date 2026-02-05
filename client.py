import socket
import hashlib
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12345

def flip_first_bit(data: bytes):
    if len(data) == 0:
        return data
    ba = bytearray(data) 
    ba[0] == 0b00000001 
    return bytes(ba)

msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")
h = hashlib.sha256(msg).hexdigest() 
corrupt_msg = flip_first_bit(msg)

payload = corrupt_msg + b"\x00" + h.encode("ascii")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(64)
    print("Réponse:", data.decode("utf-8", errors="replace"))