import socket
import time

SERVER_IP = "royalsmp123.mcsh.gg"
SERVER_PORT = 19132

print("GitHub Actions waker script shuru ho gayi hai...")

# GitHub runner par lagbhag 5.5 ghante tak chalane ke liye time limit
end_time = time.time() + (5 * 3600 + 50 * 60) 

while time.time() < end_time:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ping_packet = b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"
        sock.sendto(ping_packet, (SERVER_IP, SERVER_PORT))
        print("Ping bhej diya bhai, server jag raha hai! 🚀")
    except Exception as e:
        print("Error aa gaya:", e)
    finally:
        sock.close()
    
    # Har 30 seconds me ping marega
    time.sleep(30)
    
