import csv
import hashlib
import string
from pwn import *

p = remote('127.0.0.1', 9999)

print(p.recv())

hashed_flag = []
for i in range(-39,1):
    p.sendline('2'.encode())
    s = p.recv().decode()
    p.sendline(str(i).encode())
    s = p.recv().decode().split('\n')
    hashed_flag.append(s[0])

print(hashed_flag)

characters = string.printable
store=""
a = []

for i in hashed_flag:
    k = list()
    k.append(i)
    a.append(k)
hashed_flag = a 
for row in hashed_flag:
    print(row)
    for ch in characters:
        ch = chr(ord(ch)+13)
        flag = store
        flag = ch+flag
        if len(flag) < 40:
            flag = flag + "#"*(40-len(flag))
        hashed_flag = hashlib.sha256(flag.encode("utf-8")).hexdigest()
        if hashed_flag == row[0]:
            store = ch + store
            print(store)
            break
            
ans=[]    
for i in range(len(store)):
    ans.append(chr(ord(store[i])-13))

print("".join(ans)) 
