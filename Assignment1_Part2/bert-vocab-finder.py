import nltk
import re
import pandas as pd
import argparse
import string 
import random
import utils
import pprint


'''
1. Cleaning with regular expressions

This section takes the bert vocab file and checks if the words is a valid and comprised of english alphabets. 

The word has to pass the regex test to be deemed "legal"

Assumptions:
1. All the characters are in lower case
2. Words derived from compounding will be ignored (that contain spaces or hyphens) 
3. Digits will be ignored
4. Emojis are not words

'''


bert_vocab = open(utils.bert_vocab_file, 'r').readlines()

allowed_patterns = r"[a-z]*" # expects regex
pattern = re.compile(allowed_patterns)
num_legal_words = 0
num_illegal_words = 0
legal_words = []
illegal_words = []


for word in bert_vocab: 
    
    if utils.check_regex_pattern(word, pattern) : 
        num_legal_words += 1
        legal_words.append(word.replace("\n", ""))
        
    else : 
        
        num_illegal_words += 1 
        illegal_words.append(word.replace("\n", ""))
        
print("Regex found: \n\t{} legal words\n\t{} illegal words.".format(num_legal_words, num_illegal_words))

assert num_legal_words+num_illegal_words==len(bert_vocab) # test that every word in bert vocab is accounted for


'''
2. Check if it is a meaningful word

The Unix Words File is a curated list of words that is used for OS services like inbuilt spell checking. 

Assumptions for Unix Words File (UWF):
    i. Not exhaustive, absence of word from UWF does not indicate illegitamacy 
    ii. In lemma form
    iii. Don't account for all the derived morphs
    iv. Capitalize Proper Nouns

If the word appears on UWF, it is very likely legal. 

If the words is not on this UWF - 
    i. it may be a valid word that was derived from the lemma
    ii. it may be a proper noun
    iii. it may be an illegal word
    
'''

results = []
grammatically_correct = []
lemmas = []
proper_nouns = []
uncategorised = []

for cnt, word in enumerate(legal_words) : 

    utils.log_progress(cnt, len(legal_words))

    result = {'word':word}
    result['is_legal'], result['is_lemma'], result['is_proper_noun'] = utils.search_unix_vocab(word) 

    if result['is_legal'] : 
        grammatically_correct.append(word)
    else : 
        uncategorised.append(word)

    if result['is_lemma'] : lemmas.append(word)
    if result['is_proper_noun'] : proper_nouns.append(word)

    results.append(result)

'''
3. Display results to understand

i. Save the legal words into a user specified file 
ii. Display a subset of each set for primitive analysis

'''

pd.DataFrame(results).to_csv(utils.result_vocab_file)

print("Grammatical words : ", len(grammatically_correct))
pprint.pprint(random.sample(grammatically_correct, 20))
print("Lemmas : ", len(lemmas))
pprint.pprint(random.sample(lemmas, 20))
print("Proper nouns : ", len(proper_nouns))
pprint.pprint(random.sample(proper_nouns, 20))
print("Uncategorised : ", len(uncategorised))
pprint.pprint(random.sample(uncategorised, 20))












    