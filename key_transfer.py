import transposition_encrypt
import transposition_decrypt
import substitution_encrypt_decrypt
import vignere_encrypt_decrypt


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

def alice_encrypt (bob_public_key):
    txt_msg = 'This is a string'
    # alice's private key
    alice_private_key = 69420
    # calculate shared private key
    shared_private_key = calculate (alice_private_key, bob_public_key)
    print('Shared secret key, s = ', shared_private_key)

    # encrypt message
    key_string = str(shared_private_key)
    # encrypt using Substitution cipher
    substitution_cipher = substitution_encrypt_decrypt.encrypt(txt_msg, shared_private_key)
    # encrypt using transposition cipher
    transposition_cipher = transposition_encrypt.encrypt(txt_msg, key_string)
    # encrypt using transposition cipher
    vignere_cipher = vignere_encrypt_decrypt.encrypt(txt_msg, key_string)


    cipher_lst = [substitution_cipher, transposition_cipher, vignere_cipher]
    # vignere_cipher = 
    print('This is the original text:', txt_msg)
    print('This is the encrypted text (Substitution):', substitution_cipher)
    print('This is the encrypted text (Transposition):', transposition_cipher)
    print('This is the encrypted text (Vignere):', vignere_cipher)

    return cipher_lst


# bob, receiving from alice
def bob ():
    # bob's private key
    bob_private_key = 15056
    print ('Bob private key, b = ',bob_private_key)

    # calculate bob's public key
    bob_public_key = calculate(bob_private_key, GEN)
    print ('Bob public key, B = ',bob_public_key)

    return bob_public_key
   

def bob_decrypt (alice_public_key, cipher_lst):
    # bob's private key
    bob_private_key = 15056
    print ('Bob private key, b = ',bob_private_key)
    # calculate shared private key
    shared_private_key = calculate(bob_private_key, alice_public_key)
    print('Shared secret key, s = ', shared_private_key)
    
    # decrypt message
    key_string = str(shared_private_key)
    substitution_decipher = substitution_encrypt_decrypt.decrypt(cipher_lst[0], shared_private_key)
    transposition_decipher = transposition_decrypt.decrypt(cipher_lst[1], key_string)
    vignere_decipher = vignere_encrypt_decrypt.decrypt(cipher_lst[2], key_string)

    decipher_lst = [substitution_decipher, transposition_decipher, vignere_decipher]

    print('This is the ciphered text (Substitution):', cipher_lst[0])
    print('This is the ciphered text (Transposition):', cipher_lst[1])
    print('This is the ciphered text (Vignere):', cipher_lst[2])
    print('This is the deciphered text (Substitution):', decipher_lst[0])
    print('This is the deciphered text (Transposition):', decipher_lst[1])
    print('This is the deciphered text (Vignere):', decipher_lst[2])
    return decipher_lst



def main():
    # txt_msg = 'This is a string'
 
    # get public keys
    print('ALICE: ')
    alice_public_key = alice()
    print('BOB: ')
    bob_public_key = bob()


    cipher_lst = alice_encrypt(bob_public_key)
    decipher_lst = bob_decrypt(alice_public_key, cipher_lst)

    
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