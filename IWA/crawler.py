import socket
import time
import re

def connect_to_server(url):
    url = url.strip("http://").strip("https://").strip("/")
    ip = socket.gethostbyname(url)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 80))
    return s

def get_source(s, url):
    CRLF = "\r\n"
    get = f"GET / HTTP/1.1{CRLF}"
    get += f"Host: {url}{CRLF}"
    get += f"Connection: close{CRLF}"
    get += CRLF

    s.send(get.encode("utf-8"))
    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
    return response.decode("utf-8")

def get_links(response):
    links = []
    while True:
        start = response.find("<a ")
        if start == -1:
            break
        end = response.find(">", start)
        href = response[start:end].split("href=")[-1].split()[0].strip("\"'")

        if href not in links:
            links.append(href)

        response = response[end:]
    return links

if __name__ == "__main__":
    url = "https://crawler-test.com/"
    s = connect_to_server(url)
    response = get_source(s, url)
    links = get_links(response)
    print(links)
    s.close()
