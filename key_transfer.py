import transposition_encrypt
import transposition_decrypt

PRIME = 841000001
GEN = 45678

def calculate(key, gen):
    return (gen ** key) % PRIME

# alice
def alice ():
    # alice's private key
    alice_private_key = 69420
    print ('Alice private key, a = ',alice_private_key)
    # calculate alice's public key
    alice_public_key = calculate (alice_private_key, GEN)
    print ('Alice public key, A = ',alice_public_key)
    return alice_public_key

def alice_transposition_encrypt (bob_public_key):
    # alice's private key
    alice_private_key = 69420
    # calculate shared private key
    shared_private_key = calculate (alice_private_key, bob_public_key)
    print('Shared secret key, s = ', shared_private_key)

    # encrypt message
    txt_msg = 'This is a string'
    key_string = str(shared_private_key)
    cipher = transposition_encrypt.encrypt(txt_msg, key_string)
    print('This is the original text:', txt_msg)
    print('This is the ciphered text:', cipher)

    return cipher


# bob, receiving from alice
def bob ():
    # bob's private key
    bob_private_key = 15056
    print ('Bob private key, b = ',bob_private_key)

    # calculate bob's public key
    bob_public_key = calculate(bob_private_key, GEN)
    print ('Bob public key, B = ',bob_public_key)

    return bob_public_key
   

def bob_transposition_decrypt (alice_public_key, cipher):
    # bob's private key
    bob_private_key = 15056
    print ('Bob private key, b = ',bob_private_key)
    # calculate shared private key
    shared_private_key = calculate(bob_private_key, alice_public_key)
    print('Shared secret key, s = ', shared_private_key)
    
    # decrypt message
    key_string = str(shared_private_key)
    decipher = transposition_decrypt.decrypt(cipher, key_string)

    print('This is the ciphered text:', cipher)
    print('This is the original text:', decipher)
    return decipher



def main():
    # txt_msg = 'This is a string'
 
    # get public keys
    print('ALICE: ')
    alice_public_key = alice()
    print('BOB: ')
    bob_public_key = bob()


    cipher = alice_transposition_encrypt(bob_public_key)
    decipher = bob_transposition_decrypt(alice_public_key, cipher)

    
    # key_string = str(secret_key)
    # cipher = encrypt(txt_msg, key_string)
    # print('Shared secret key, s = ', secret_key)

    # print('BOB: ')
    # decipher = decrypt(cipher, key_string)
    # print ('This is the deciphered text:', decipher)



# If key_transfer.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()