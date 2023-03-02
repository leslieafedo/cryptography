from transposition_encrypt import encrypt
from transposition_decrypt import decrypt
from transposition_code_break import code_break

def main ():

    # txt_msg = 'And, on top of this, the version of success they grasp toward is not one which they have defined for themselves.'
    f = open('txt_msg.txt', 'r')
    txt_msg = f.read()
    key = 'keys'
    print('\nOriginal message:')
    print (txt_msg)    
    print('\nKey:')
    print (key)
    cipher = encrypt(txt_msg, key)
    print ('\nCipher:')
    print(cipher)
    print ('\nDecipher with known key:')
    print(decrypt(cipher, key))
    print ('\nCode-break')
    code_break(cipher, len(key))
    f.close()

def test():
    import random 
    f = open('txt_msg.txt', 'r')
    txt_msg = f.read() # txt_msg = txt_msg+txt_msg+txt_msg+txt_msg+txt_msg
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = ''
    for i in range (0, 9):
        key += ''.join (random.choice(alphabet))
        print('\nOriginal message:')
        print (txt_msg)    
        print('\nKey:')
        print (key)
        cipher = encrypt(txt_msg, key)
        print ('\nCipher:')
        print(cipher)
        print ('\nDecipher with known key:')
        print(decrypt(cipher, key))
        print ('\nCode-break')
        code_break(cipher, len(key))
    f.close()


# If transposition_main.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    test()