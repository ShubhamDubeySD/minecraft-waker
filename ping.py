import socket
import time

SERVER_IP = "royalsmp123.mcsh.gg"
SERVER_PORT = 19132

print("Server waker script start ho gayi hai...")

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ping_packet = b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"
        sock.sendto(ping_packet, (SERVER_IP, SERVER_PORT))
        print("Ping bhej diya bhai, server jag raha hai! 🚀")
    except Exception as e:
        print("Error aa gaya:", e)
    finally:
        sock.close()

    time.sleep(30)
  
