import socket

plist = [80, 443, 5000, 23, 20, 8080]
host = '127.0.0.1'

for ports in plist:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(5)
    try:
        server.connect((host, int(ports)))
        request = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
        server.send(request.encode())
        banner = server.recv(1024)
        bannerStr = banner.decode()
        print(f"port {ports} is open")
        print(f"Banner Info port {ports}: \n {bannerStr}")
    except:
        print(f"port {ports} is closed")
    finally:
        server.close()
