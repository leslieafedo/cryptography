from transposition_ecrypt import encrypt
from transposition_decrypt import decrypt
from transposition_code_break import code_break

def main ():

    msg = 'And, on top of this, the version of success they grasp toward is not one which they have defined for themselves.'
    key = 'key'
    print(msg)
    print ('')
    cipher = encrypt(msg, key)
    print ('')
    print(cipher)
    print ('')
    print(decrypt(cipher, key))
    print ('')
    print ('Possible plaintext:')
    code_break(cipher, len(key))
    print ('')


# If transposition_main.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()