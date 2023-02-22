import itertools, time, numpy as np
from transposition_decrypt import decrypt
import detect_word

# Brute force code breaker 
def code_break (cipher_text, key_length):
    start_time = time.time()
    broken_text = []
    word_count = []

    # assume key length is known 
    # create a list of ints from 0 to key_length
    lst = [i for i in range(key_length)]
    # iterate through all possible combinations of n numbers 
    key_lst = [list(l) for l in itertools.permutations(lst)]

    # for each combination, run the decryption function 
    for i in range (len(key_lst)):
        deciphered_msg = decrypt(cipher_text, key_lst[i])

        # if deciphered message has any padding characters, ignore it
        if '*' not in deciphered_msg:
            # add deciphered message without padding to a new list 
            broken_text.append(deciphered_msg)
            # find the number of words in each deciphered message
            word_count.append(detect_word.count(deciphered_msg))
 
    # create a np list of the wordcount list
    np_word_count_lst = np.array(word_count)
    # sort the indices of the np_word_count_lst from most to least
    sorted_word_count_lst = list(np_word_count_lst.argsort())[::-1]


    print ('Possible keys and deciphered text: ')
    # print the top 10 from the list of deciphered messages with the most words found 
    for i in sorted_word_count_lst[:10]:
        print (key_lst[i], ' => ',broken_text[i])
        print ('Number of english words found: ', word_count[i])
        print ('')


    end_time = time.time() - start_time
    print ('')
    print('Total code break runtime: ', end_time, 's')


def main ():
    msg = 'NNPTSEROFCSHGSORSTEITYVENFTMLSAOOFIHEIOUETYATAIONHHEADIDREEEDTOHTVSNSCSERPWDNOWCHHEFEOHSV*'
    code_break(msg, 3)


# If transposition_code_break.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()