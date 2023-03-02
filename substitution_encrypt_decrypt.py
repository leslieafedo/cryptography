import re
from string import digits

def encrypt(msg,n) :
    msg = preprocess(msg)
    msg1 = ""
    for x in msg:
        msg1 += chr(((ord(x) - ord("A") + n)%26) + ord("A"))
    return msg1
def decrypt(msg,n) :
    msg = preprocess(msg)
    msg1 = ""
    for x in msg:
        msg1 += chr(((ord(x) - ord("A") - n)%26) + ord("A"))
    return msg1
def preprocess(msg):
    s = re.sub(r'\W+', '', msg)
    remove_digits = str.maketrans('', '', digits)
    res = s.translate(remove_digits)
    res= res.upper()
    return res