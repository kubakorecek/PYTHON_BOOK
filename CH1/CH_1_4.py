"""
    In this program, we want python to writ a letter. We gives some basics words and then use the random module to make
    letter for us. Basically then there is few 2 possibilities of construction of sentence. We need to add feature
    that defualt is five lines , but user can put argument in command line to 1 - 10 to change flow.

"""

import random

articles = ['a', 'the', 'an']
subjects = ['me', 'him', 'her', 'it', 'car', 'dog']
verbs = ['do', 'speak', 'look','wave']
adverbs =['fastly', 'well', 'badly','slowly']

try:
    import sys
    lines = int(sys.argv[1])
    if 1<=lines<=10:
        pass
    else:
        raise UnboundLocalError("Integer should be between 1 - 10")
except IndexError:
    print("please call name.py <#lines> between 1-10")
    lines = 0
except TypeError:
    print("please call name.py <#lines>, as INTEGER! bewtween 1-10")
    lines = 0

while lines:
    a_= random.choice(articles)
    s_= random.choice(subjects)
    v_= random.choice(verbs)
    b_= random.choice(adverbs)
    i = random.randint(0,1)
    if i:
        print(a_ + " " + s_ + " " + v_ + " " +b_)
    else:
        print(a_ + " " + s_ + " " + v_)
    lines -=1