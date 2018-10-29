"""
    In this program, we want python to writ a letter. We gives some basics words and then use the random module to make
    letter for us. Basically then there is few 2 possibilities of construction of sentence.

"""

import random

articles = ['a', 'the', 'an']
subjects = ['me', 'him', 'her', 'it', 'car', 'dog']
verbs = ['do', 'speak', 'look','wave']
adverbs =['fastly', 'well', 'badly','slowly']


for _ in [0,1,2,3,4]:
    a_= random.choice(articles)
    s_= random.choice(subjects)
    v_= random.choice(verbs)
    b_= random.choice(adverbs)
    i = random.randint(0,1)
    if i:
        print(a_ + " " + s_ + " " + v_ + " " +b_)
    else:
        print(a_ + " " + s_ + " " + v_)