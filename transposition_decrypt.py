import math 
import numpy as np


# Decryption
def decrypt(cipher_text, key):
    plaintext = ""

    # track key indices
    key_index = 0

    # track msg indices
    msg_index = 0
    msg_len = float(len(cipher_text))
    msg_list = list(cipher_text)

    # calculate column of the matrix
    col_len = len(key)

    # calculate maximum row_len of the matrix
    row_len = int(math.ceil(msg_len / col_len))

    # convert key into list and sort
    # key_list = sorted(list(key))
    key_lst = list(key)

    # create a numpy list so that it can be sorted later 
    np_key_lst = np.array(key_lst)
    # create indices array to be used to create final cipher from matrix    
    sorted_key_indices = list(np_key_lst.argsort())
   
    # create an empty matrix 
    dec_cipher = []
    for _ in range(row_len):
        dec_cipher += [[None] * col_len]

# fill matrix with ciphered text 
    for i in range(col_len):
        curr_index = sorted_key_indices[i]

        for j in range(row_len):
            dec_cipher[j][curr_index] = msg_list[msg_index]
            msg_index += 1
        key_index += 1

    # convert decrypted matrix into a string
    try:
        plaintext = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("error")

    # count number of padding characters
    null_count = plaintext.count('*')

    # return deciphered text without padding characters
    if null_count > 0:
        return plaintext[: -null_count]

    return plaintext 



def main ():
    return True



# If transposition_decrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()