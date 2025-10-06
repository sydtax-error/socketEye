# socketEye
A lightweight Python script that scans predefined ports on a host and retrieves banner information using sockets.
Port Scanner

##Installation

Use the package manager pip
 to install any missing dependencies (e.g., socket is built-in, so no need to install it separately).

'''pip install python'''

##Usage
'''import socket

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
        server.close()'''

##Example Output
'''port 80 is open
Banner Info port 80:
 HTTP/1.1 200 OK
 Content-Type: text/html
 ...

port 23 is closed'''

##How It Works

The script attempts to connect to each port in the list.

If a connection is successful, it sends a simple HTTP request and prints the server’s response (banner).

If the connection fails or times out, it reports the port as closed.



port 23 is closed
