from itertools import combinations

def load_wordlist():
    wordlist_file = open('english_wordlist.txt')
    wordlist = {}
    for i in wordlist_file.read().split('\n'):
        wordlist[i] = None
    wordlist_file.close()
    return wordlist

# load the wordlist into a dictionary 
WORDLIST = load_wordlist()

def count(msg):
    wordcount = 0
    # Get all substrings of msg using itertools.combinations() to create a list of possible_words
    possible_words = [msg[x:y] for x, y in combinations(
            range(len(msg) + 1), r = 2)]
    # for each possible word, find if it is in the english_wordlist.txt
    for word in possible_words:
        if word in WORDLIST:
            # count number of found words
            wordcount += 1
    return wordcount


def main ():
    msg = 'SITSMISHYNITITGARMTOYETBANHNOTBUGILTROTSXKXWXZYYZ*Z'
    count(msg)

# If detect_word.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()