from PIL import Image
import socket
from blowfish import decrypt
from DES import Decrypt
import time


def receive_image(conn):
    with open('revealed_image.png', 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
'''
# Create a socket
s = socket.socket()

# Specify the server address and port
port = 12345

# Bind the socket to the server address and port
s.bind(('', port))
print("Socket binded to %s" % port)

# Listen for incoming connections
s.listen(5)
print("Socket is listening")
'''

def reveal_message(image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    binary_message = ''
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)
            if binary_message[-16:] == '1111111111111110':
                return binary_to_message(binary_message[:-16])
    return "No Message Found"

def binary_to_message(binary):
    message = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message += chr(int(byte, 2))
    return message
def Decimal(num):
        dec=0
        two=1
        for i in range(len(num)-1,-1,-1):
            if num[i]=='1':
                dec+=two
            two=two*2
        return dec
    
def binary(w):
        d={
            '0':'0000',
            '1':'0001',
            '2':'0010',
            '3':'0011',
            '4':'0100',
            '5':'0101',
            '6':'0110',
            '7':'0111',
            '8':'1000',
            '9':'1001',
            'A':'1010',
            'B':'1011',
            'C':'1100',
            'D':'1101',
            'E':'1110',
            'F':'1111',
            'O':'0000'}
        res=''
        for i in w:
            res+=d[i]
        return res


def deform(img, key1, key2):
    rv=reveal_message(f"{img}")
    rv1=""
    for g in rv:
        if((ord(g)>=48 and ord(g)<=57) or (ord(g)>=97 and ord(g)<=122)):
            rv1+=g
        else:
            break
    rv=rv1
    bk=key2
    bk=bk.lower()
    rv=decrypt(rv,bk).upper()

    Dkey=key1
    PT=Decrypt(rv,Dkey)
    msg=""
    for i in range(0,len(PT),2):
        k1=binary(PT[i])
        k2=binary(PT[i+1])
        k1+=k2
        k3=Decimal(k1)
        msg+=chr(k3)
    return msg


'''
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    
    c.send('Thank you for connecting'.encode())
    
    # Receive the image from the client
    start_time = time.time() 
    receive_image(c)
    print('Image received successfully!')
    rv=reveal_message("C:/Users/gokul.000/Desktop/steg_try/revealed_image.png")
    #print(rv)
    #print("Revealed message:", rv)
    #print("length",len(rv))
    rv1=""
    for g in rv:
        if((ord(g)>=48 and ord(g)<=57) or (ord(g)>=97 and ord(g)<=122)):
            rv1+=g
        else:
            break
    rv=rv1
    #print("Revealed message:", rv)
    #print("length",len(rv))
    bk=input("Enter key for blowfish: ")
    bk=bk.lower()
    #bk="aabb09182736ccdd"
    rv=decrypt(rv,bk).upper()
    #Dkey="0F1571C947D9E859"
    Dkey=input("Enter key for DES: ")
    PT=Decrypt(rv,Dkey)
    end_time = time.time()
    execution_time = end_time - start_time
    print("The execution time is",execution_time)
    msg=""
    for i in range(0,len(PT),2):
        k1=binary(PT[i])
        k2=binary(PT[i+1])
        k1+=k2
        k3=Decimal(k1)
        msg+=chr(k3)
    print("the message is ",msg)
    c.close()
    break
'''