# Import stop_words and inappropriateـwords
from .stop_word.stop_words import stop_words_fa, stop_words_en 
from .inappropriateـwords.inappropriateـwords_en import Inappropriateـwords_en
from .inappropriateـwords.inappropriateـwords_fa import Inappropriateـwords_fa

def check_comment(body):
    # All words in body to lower
    body = body.lower()
    
    # body changed to dictionary
    body = body.split()
    
    # Remove all stop_words_en and stop_words_fa
    for stop_word in stop_words_fa :
        for word in stop_word :
            if word in body :
                body.remove(word)
    for word in stop_words_en :
        if word in body:
            body.remove(word)
            
    # Check comment to contain  Inappropriateـwords_en or Inappropriateـwords_fa
    for word in Inappropriateـwords_en :
        if word in body :
            return False
        for w in body :
            if w.find(word)!=-1 :
                return False
    
    for word in Inappropriateـwords_fa :
        if word in body :
            return False
        for w in body :
            if w.find(word)!=-1 :
                return False
    return True


