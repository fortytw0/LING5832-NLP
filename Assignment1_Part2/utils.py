import argparse
import string
import nltk



parser = argparse.ArgumentParser()
parser.add_argument('--bert_words_file', type=str, default="BERT-vocab.txt")
parser.add_argument('--unix_words_file', type=str, default = '/usr/share/dict/words')
parser.add_argument('--resultant_csv_file', type=str, default='results.csv')

args = parser.parse_args()

bert_vocab_file = args.bert_words_file
unix_vocab_file = args.unix_words_file
result_vocab_file = args.resultant_csv_file

unix_vocab = open('/usr/share/dict/words').readlines() 
unix_vocab = [word.strip("\n") for word in unix_vocab]


'''
letter_location_map:

In the unix_vocab each alphabetical series starts with 
the respective uppercase alphabet. Use this to get 
start-location of each letter. 

For example : 
letter 'a' starts at index 0, letter 'b' starts at index 42, ....
letter_location_map=[{'a':0}, {'b':42}, ...]
'''
letter_location_map = [{word:i} for i, word in enumerate(unix_vocab) if word in string.ascii_uppercase] 
print(letter_location_map)

'''
lemmatizer: 

Standard nltk.stem.WordNetLemmatizer objet. 
'''
lemmatizer = nltk.stem.WordNetLemmatizer()


def check_regex_pattern(query, pattern) :

    '''
    Check if all the characters in the query satisfy regex pattern. 

    query (str) : Query to check
    pattern (re.pattern) : Pattern from re.compile

    returns (bool) : if query matches pattern
    '''

    if pattern.match(query).span()[1] == len(query)-1 :
        return True
    else : 
        return False



def get_search_limits(query) : 

    '''
    Matching query with entire unix_vocab is cumbersome. 
    
    This function sets start_index and end_index, by ensuring the 
    query-matching is limited to unix_words begininning with the same letter. 

    query (str) : word to be searched
    returns (int, int): (start_index, end_index)
    '''

    start_letter = query[0].upper()

    if start_letter == "Z":  
        return letter_location_map[-1]["Z"], -1 

    for i, dic in enumerate(letter_location_map) : 
    
        try :
            start_index = dic[start_letter]
            end_index = list(letter_location_map[i+1].values())[0]
            return start_index, end_index
            
            
        except: 
            pass

def is_special_case(query, cases=['s', 'ed', 'er', 'ing', 'ey']) : 
    for case in cases : 
        end_i = len(case)
        if query[-end_i:]==case : 
            return True

    return False

def get_base_form(query, cases=['s', 'ed', 'er', 'ing', 'ey']) : 

    for case in cases : 
        end_i = len(case)
        if query[-end_i:]==case : 
            return query[:-end_i]

    return query


def is_proper_noun(query) : 

    '''
    Proper nouns in unix_vocab start with capital letters. 
    Use this to differentiate common words and proper_noun

    query (str) : word to check if proper noun. 
    returns bool : True if query is proper noun. 
    '''
    if query[0].isupper() : 
        return True 
    else : 
        return False

def is_match(query, i) :

    '''
    Checks if query matches with i-th element in unix_vocab. 

    query (str) : word to check. 
    i (int) : index of unix_vocab
    returns bool : True if the words match
    
    ''' 
    if query==unix_vocab[i].lower() : 
        return True
    elif get_base_form(query)==unix_vocab[i].lower() : 
        return True
    else :
        return False

def is_lemma(query, lemma) : 

    '''
    Checks if query and lemma form is same, i.e. if the query is a lemma. 

    query (str) : word to check
    lemma (str) : lemma for of word
    returns (bool) : True if query is in lemma form
    '''
    if query == lemma : 
        return True
    else : 
        return False



def search_unix_vocab(query) : 

    '''
    Lemmatizes query and searches the unix_vocab. The limits of the search are set by get_search_limits().
    Also checks if query is a lemma or proper noun. 

    query (str): word to be searched
    returns (bool, bool, bool) : (True if query is found, True if query is lemma, True if query is proper noun)

    '''

    i, end_index = get_search_limits(query)

    lemma = lemmatizer.lemmatize(query)

    while i<=end_index : 

        if is_match(query, i) : # lemma is present in unix_vocab
            if is_lemma(query, lemma) : 
                if is_proper_noun(unix_vocab[i]) : 
                    return True, False, True
                else : 
                    return True, True, False
            else : 
                return True, False, False
        
        i += 1

    return False, False, False


def log_progress(cnt, tot, interval=100) : 
    if cnt%interval == 0 :
        print("Completed : {}/{}".format(cnt, tot), end="\r", flush=True)












