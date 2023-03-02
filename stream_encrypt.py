import random
import sys

def generate_keystream(key, size):
    random.seed(key)
    key_stream = ''
    for i in range (size):
        random_char = random.randint(0,1)
        key_stream += ''.join(str(random_char))
    return key_stream

def encrypt(msg, key):
    cipher = ''
    size = len(msg)
    keystream = generate_keystream(key, size)
    for x in range (len(msg)):
        y = (int(msg[x]) ^ int(keystream[x]))
        cipher += ''.join(str(y))
    print (cipher)

def main ():
    msg = 'leslie'
    key = 1

    # encrypt (msg, key)

    bytearr = ''
    f1 = open( "stream_input.txt", "r")
    bytearr = map (ord, f1.read () )
    for i in range(len(bytearr)):
        byt = (bytearr[i] + random.randint(0, 255)) % 256

    print(byt)



if __name__ == '__main__':
    main()