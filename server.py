import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8001  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Listing at {HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = conn.recv(1024)
    http_req = data.decode().split("\r\n")
    req_method, path, http_version = http_req[0].split(" ")

    print(req_method, path, http_req)

    to_serve = "index.html" if path == '/' else path[1:]

    with open(f"./super_cool_website/{to_serve}") as f:
        to_serve = f.read()

    response = f"HTTP/1.1 200\r\nContent-Length: {len(to_serve)}\r\n\r\n{to_serve}".encode()
    print(response)
    conn.send(response)
    conn.close()