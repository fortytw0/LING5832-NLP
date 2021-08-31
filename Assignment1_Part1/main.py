import pandas as pd
import numpy as np
import random
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sharpness", default=6, type=int)
parser.add_argument("--output_file", default='results.csv', type=str)

args = parser.parse_args()

lemma_df = pd.read_excel('lemmas_60k.xlsx')
lemma_df = lemma_df.sort_values(by='rank', axis=0, ascending=False)


word_list = lemma_df['lemma']
result = []

exponent = args.sharpness
output_file = args.output_file

'''
Part of this logic was adapted from an answer on StackOverflow : 
https://stackoverflow.com/questions/32348974/logarithmic-sampling
'''

min = 1.0
max = 6200.0


i = 0 
sum = 0
start_sample = 0
num_known_words = 0


while (i<=1.0) and (sum<=max) : 
    bucket_size = round((i**exponent) * (max-min) + min)
    sum += bucket_size
    i += 0.005
    
    end_sample = start_sample+bucket_size
    
    
    if end_sample <= max : 
        sample = word_list[start_sample:start_sample+bucket_size]
    else : 
        break
    
    random_word = random.sample(list(sample), 1)[0]
    known = input('Do you know the meaning of the word : {} Enter 1 if yes or 0 if not -->  '.format(random_word))
    
    if known == '1' : 
        
        result.append({'sample_word':random_word, 
                      'known':True, 
                      'bucket_size':bucket_size})
        
        num_known_words += bucket_size
        
    else: 
        
        result.append({'sample_word':random_word, 
                      'known':False, 
                      'bucket_size':bucket_size})
    
        
        
    
    
    
    start_sample = end_sample
    
result_df = pd.DataFrame(result)
result_df.to_csv(output_file, index=False)

num_all_words = result_df['bucket_size'].sum()
ratio_known_words = num_known_words/num_all_words
total_num_known_words = ratio_known_words*max*10

print("You knew {} words.".format(num_known_words))
print("There are a total of {} words.".format(num_all_words))
print("You know {}% of the words in this vocabulary or : {} words".format(ratio_known_words,total_num_known_words ))


    
    
