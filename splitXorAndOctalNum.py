from pwn import *

# Connect to server
io = remote('103.191.240.170', 9998)

it = 0

while it<1:
    value = io.recv().decode()
    print('value', value)
    Number = value.split(': ')
    # print('Number', Number)
    s = Number[1]
    print(len(s))
    if(len(s) == 6):
        print('len(s)', len(s))
        l = int(len(s)/2)
        l = l-1
    else:
       l = int(len(s)/2)
    print(l)
    v,c = s[:l],s[l:]
    it = 0

    print(v, c)

    decnum= (int(v) ^ int(c))

    print(decnum)

    octal = 0
    ctr = 0
    temp = decnum  #copying number
    
    #computing octal using while loop
    while(temp > 0):
        octal += ((temp%8)*(10**ctr))  #Stacking remainders
        temp = int(temp/8)             #updating dividend
        ctr += 1
    io.sendline(str(octal).encode())

io.close()