from pwn import *

# Connect to server
io = remote('103.191.240.170', 9999)

# Get The Value 
value = io.recv().decode()

#Split The Value by next line
Number = value.split('\n')

# Convert the value into integer
a = int(Number[1])

while True:
    Reverse = 0 
    # Reverse The Number
    while(a > 0):  
        Reminder = a %10    
        Reverse = (Reverse *10) + Reminder    
        a = a //10
    print('Reverse', Reverse) 
    # Send the Reverse Value   
    io.sendline(str(Reverse).encode())
    # Receive The Ouput
    value = io.recv().decode()
    Number = value.split('\n')
    try:
        a = int(Number[0])
    except:
        print('Flag ->', Number[0])
        io.close()

print(io.recv().decode())        
io.close()