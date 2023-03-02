import math, numpy as np, re

# Encryption
def encrypt(msg, key):
    # convert plaintext to uppercase 
    msg = msg.upper()
    # strip all non-alphanumeric charatcer and whitespaces 
    msg = re.sub('[\W\_]','',msg)
    cipher = ""
    msg_len = len(msg)
    # create message and key lists 
    msg_lst = list(msg)
    key_lst = list(key)
    
    # create a numpy list so that it can be sorted later 
    np_key_lst = np.array(key_lst)

    # create indices array to be used to create final cipher from matrix    
    sorted_key_indices = list(np_key_lst.argsort())

    # determine column length
    col_len = len(key)

    # determine row length
    row_len = int(math.ceil(msg_len / col_len))

    # add the padding character '*'
    fill_null = int((row_len * col_len) - msg_len)
    msg_lst.extend('*' * fill_null)

    # create matrix
    matrix = [msg_lst[i: i + col_len]
            for i in range(0, len(msg_lst), col_len)]

    # read matrix by column
    for i in range(col_len):
        curr_index = sorted_key_indices[i]
        cipher += ''.join([row_len[curr_index]
                        for row_len in matrix])
    return cipher   

def main ():
    return True

# If transposition_encrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()