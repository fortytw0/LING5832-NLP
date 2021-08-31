# How many words do you know in your native language?

## Introduction

____

### ‘My Native Language’

This is probably a section that you may not receive from most of my colleagues. I need to explain “what my native language is” because it is a little confounding - even to me. 

**The language that we speak at home is English.** 

Professor Martin does go over native language like so in the first lecture - 

>  In your native language like do you know 30,000 words you know 5000 words you know 300,000 words so that that's that's sort of where we'll go next…

… And unfortunately, he does not go into specifying what a native language is.

My family traces their heritage from a state in India called *Tamil Nadu* (literally, *“Tamil State”*), and they speak the langauge *“Tamil”*. I was born and spent my early years in the city of *Bangalore*, where they speak the langauge *“Kannada”*. My entire childhood and teenage years were spent in *Maharashtra* where they speak the language *“Marathi”*. My social group predominantly spoke *“Hindi”*. 

I cannot read  these languages *well*, but I can understand them if they are spoken. 

The language that I am most comfortable with is English, because that is the language I was brought up speaking. It is the language that I speak to myself in, and more importantly - the primay language my parents spoke to me in as a child.

____

### ‘How many’ 

A given word can have the multiple forms and meanings. For instance:

| Meanings for the word Bat                                  |   Forms of the word Bat    |
| ---------------------------------------------------------- | :------------------------: |
| A nocturnal, arial mammal                                  |     Bats - Plural Noun     |
| An implement, usually made of wood that is used to hit     | Bats - Simple Present Verb |
| A verb that implies weilding abovementioned implement      | Batting - Continuous Verb  |
| A verb indiacting championing/advocating for a cause       | Batted - Simple Past Verb  |
| A verb associated with opening and closing eyelids rapidly |  Batting - Gerund of Verb  |
|                                                            |                            |

For the sake of this assignment, I will be assuming that this is all one word - **“bat”**. I will be picking the lemma of any word, so I have a consistent paradigm. The rationale behind this is:

1. Ιt cuts down the complexity to give a tangible idea of my vocabulary. Words such as bat may take  countless forms - I probably understand all of them, but it is hard to put a number on it. 
2. Using just the lemma inherently disambiguates the word sense - for instance **“batter”** - could refer to “the weilder of a bat” or “what pancakes are made of”. By assuming the lemma, I could capture  the difference between *“batter”*-> *“bat”* and *“batter”* -> *“batter”*.  

____

### ‘Words’

Lexicons and vocabularies are always getting updated with new words - due to changing cultures and phenomena around the world. Not all new words are the same however : 

**Words included in this study:** 

1. Words describing scientific phenomena and new cultural processes. These are well defined terms that describe tangible effects around the world, and are often imbibed into established vocabs like OED immediately. 
2. New words that are so commonplace in our modern lives that it has fused into our vocabs. Think “vlog” and “firewall”. These words likely find a place in OED as well. 

**Words excluded from this study:**

1. Creole, Pidgins and fused languages that come from mixing of two languages. It is especially common to hear *“Hinglish”* in India - a mixture of Hindi and English. Words from such repos are ommitted as they can be arbitrarily formed and vary vastly from place to place. 
2. New age slang, that erupts from new social phenomena - for instance the word *“sus”*, which became very famous due to the popular online game “Among Us”. Most of these words could be viewed as fads, and it is unclear whether it will remain in our lexicon in the near future. 

____

### ‘Know’

This would have been a straightforward description, “knowing” the meaning of a word is to understand what it information it conveys in all contexts of its usage. Unfortunately, this does not fix the scope on meaning - and a word could be thought of as meaning much more than the cursory recollection. 

For example, Douglas Adams in the Hitchhiker’s Guide to the Galaxy describes flying as - 

> The art of throwing yourself at the ground and missing.

While this meaning may be true, it is unfortunately not useful for our purpose as this kind of metaphorical meanings can be posited for every word there is. Each individual will interpret it differently, and therefore lead to an unbounded number of meanings. 

By convention I will be using Google as a dictionary - This dictionary has been chosen over other competitors because they certain words in my chosen dataset may not appear in established dictionaries such OED or Merriam-Webster.  

I will claim I know a word if I am able to correctly verify that I recognise at least one meaning of a word that is specified in the dictionary. 

____

## Experiment

### Abstract and Proposal

- I managed to find a repository of English’s most frequent words. It is called [Word Frequency Data](https://www.wordfrequency.info/samples.asp), and identifies the most commonly occurring words in a plethora of corpora. 

- The dataset is interesting as it provides a free version that samples every tenth entry. The words are ranked in descending order of frequency, i.e. more common words appear at the start. 

- I will be sampling random words from this dataset, and verifying its meaning. The ratio of known words in my sample - will be extrapolated to the ~60,000 words in the dataset.  

### Approach and Intuitions

- Sampling words that occur very often is likely going to overstate my knowledge of English vocab. Similarly, oversampling words  that rarely occur will understate the my grasp of the lexicon. 
- Hence, I propose to sample log-linearly - fewer samples for frequent words and higher samples for rare words. 
- I will calculate the ratio of sampled words I knew in each log-linearly bin, and then multiply the ratio with the total size of the parent dataset. This estimates how many words I know in the parent dataset.  

### Methodology

For the purpose of brevity, I request you to refer to the code on the GitHub link for the method. 

### Results

After using varying bin sizes, these are my results : 

| Run ID | Number of words known | Ratio of known words | Extrapolating | Sharpness of Log curve |
| ------ | --------------------- | -------------------- | ------------- | ---------------------- |
| 1      | 5180                  | 0.83751011           | 51925.6265    | 6                      |
| 2      | 5218                  | 0.88726407           | 55010.3724    | 7                      |
| 3      | 5469                  | 0.92163802           | 57141.5571    | 4                      |
| 4      | 5131                  | 0.8681895            | 53827.7749    | 1                      |
|        |                       |                      |               |                        |

I am willing to say that I know around 54000 words in the modern English language, with all the caveats mentioned in the introduction. 





## References and other notes

<span style="background-color:aquamarine">`Please note: I can read the Hindi and Marathi script, but with difficulty. I can decipher Tamil characters, but can understand only colloquial language (not in written form).` </span>

**[This question on StackOverflow helped me shape the logic for making log-linear bins](https://stackoverflow.com/questions/32348974/logarithmic-sampling)**

[Word Frequency Dataset](https://www.wordfrequency.info/samples.asp)



 







