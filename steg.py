import socket
from PIL import Image
from blowfish import encrypt
from DES import Encrypt
import time
def HEX(m):
    result=""
    d={'0000':'0',
       '0001':'1',
       '0010':'2',
       '0011':'3',
       '0100':'4',
       '0101':'5',
       '0110':'6',
       '0111':'7',
       '1000':'8',
       '1001':'9',
       '1010':'A',
       '1011':'B',
       '1100':'C',
       '1101':'D',
       '1110':'E',
       '1111':'F'
        }
    for i in range(0,len(m),4):
        it=m[i:i+4]
        result+=d[it]
    return result
def dectobin(n):
    result=""
    while(n!=0):
        if(n%2==1):
            result='1'+result
        else:
            result='0'+result
        n=n//2
    if(len(result)%4!=0):
        result='0'*(4-len(result)%4)+result
    return result


def send_image(s, filename):
    with open(filename, 'rb') as f:
        image_data = f.read()
        s.sendall(image_data)
        print("Image sent successfully.")
        
def message_to_binary(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message

def binary_to_message(binary):
    message = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message += chr(int(byte, 2))
    return message

def hide_message(image_path, message):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    width, height = img.size
    binary_message = message_to_binary(message) + '1111111111111110'  # Adding the end of message marker

    if len(binary_message) > width * height * 3:
        raise ValueError("Message too long to hide in the image")

    pixels = img.load()
    index = 0
    for y in range(height):
        for x in range(width):
            if index + 2 < len(binary_message):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r & ~1 | int(binary_message[index]), g & ~1 | int(binary_message[index + 1]), b & ~1 | int(binary_message[index + 2]))
                index += 3
            else:
                img.save(f"{image_path}")
                return
'''
server_address = '127.0.0.1'  
server_port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_address, server_port))
print("Server:", s.recv(1024).decode())
'''

def perform(img_addr, msg, key1, key2):


    # Example usage
    m= msg #input("Enter the text(8 characters): ")
    #m="ElephantElepha"
    if(len(m)%8!=0):
        m=m+" "*(8-(len(m)%8))
    #print(m)
    #start_time = time.time() 
    L=[]
    for i in m:
        L.append(ord(i))
    #print(L)
    '''
    for i in L:
        print(dectobin(i))
    '''
    nm=""
    for i in L:
        nm+=HEX(dectobin(i))
    #Dkey="0F1571C947D9E859"
    Dkey=key1 #input("Enter the key for round 1:")
    Dkey=Dkey.upper()
    CT=Encrypt(nm,Dkey)
    CT=CT.lower()
    bk=key2  #input("Enter key for blowfish:")
    #bk="aabb09182736ccdd"
    bk=bk.lower()
    CT=encrypt(CT,bk)
    #print("....Sending Cipher Text to Server....")
    #print(CT)
    hide_message(f"{img_addr}", CT)  # Ensure the image path is correct
    #send_image(s, 'encrypted_image.png')
    #end_time = time.time()
    #execution_time = end_time - start_time
    #print("The execution time is",execution_time)
    print("Message hidden successfully.")
