import re

def generatingeKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)):    
      key.append(key[i % len(key)]) #APPEND A ALPHABET IN THE END
  return("" . join(key)) 
  
def remove_special_characters(text):
    """
    This function removes all special characters from the given text.
    """
    return ''.join(filter(str.isalnum, text))



def encrypt(string, key): # ENCRYPTIN THE TEXT USING THE INPUT STRING AND KEY GENERATED
  encrypt_text = [] 

  

  string = re.sub('[\W\_]','',string).upper()
  key= re.sub('[\W\_]','',key).upper()
  key = generatingeKey(string,key)
  for i in range(len(string)): #USING FOR LOOP FOR ITERATION
    x = (ord(string[i]) +ord(key[i])) % 26   # ENCRYPTING THE GIVEN TEXT WITH KEY 
    x += ord('A') 
    encrypt_text.append(chr(x)) 

   
  return("" . join(encrypt_text)) 

def decrypt(encrypt_text, key): 
  
  key = generatingeKey(encrypt_text,key)
  orig_text = [] 
  for i in range(len(encrypt_text)): #USING FOR LOOP FOR ITERATION
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26  #DECRYPTING THE GIVEN CIPHER TEXT WITH THE KEY
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text))