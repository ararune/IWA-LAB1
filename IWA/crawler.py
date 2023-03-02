import socket, time

def connect_to_server(homepage, port, retry = 5):
    s = socket.socket()
    try:
        s.connect((homepage, port))
    except Exception as e:
        print (e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(homepage, port, retry)       
    
    return s

def strip_url(url):
    return url.strip("http://").strip("https://").strip("/")

def get_source(s, homepage, endpoint):

    CRLF = '\r\n'
    get = 'GET /' + endpoint + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += homepage
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    return response

def get_all_hrefs(response, homepage):
    links = []
    while True:
        start = response.find("<a ")
        if start == -1:
            break
        end = response.find(">", start)
        href = response[start:end].split("href=")[-1].split()[0].strip("\"'")

        if href not in links:
            if href.startswith("http") or href.startswith("https"):
                href = strip_url(href)
                links.append(href)
            else:
                href = homepage + href
                links.append(href)
                
        response = response[end:]

    return links

homepage = 'https://crawler-test.com/'
port = 80
endpoint = ''

homepage = strip_url(homepage)
s = connect_to_server(homepage, port)
response = get_source(s, homepage, endpoint)

links = get_all_hrefs(response, homepage)
links.pop(0)
print(len(links))

counter = 0
while counter < 10:
    new_links = []
    for link in links:
        try:
            response = get_source(s, homepage, endpoint)
            if "200 OK" in response:
                counter += 1
                new_links.extend(get_all_hrefs(response, link))
        except Exception as e:
            print(f"Error visiting link {link}: {e}")
        if counter >= 10:
            break
    links.extend(new_links)

print(links)
print(len(links))

