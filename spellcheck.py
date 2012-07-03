'''
Created on Jul 2, 2012

@author: mdoan
'''
import sys
import re
from collections import defaultdict
import random
import time


if len(sys.argv) > 1 and sys.argv[1] != '-r' and sys.argv[1] != '-g':
    print('Syntax error\npython spellcheck.py -r [input pipe]\nor python spellcheck.py\npython spellcheck.py -g 1000 [1000 words to be generated]')
    sys.exit(0)

''' init '''
DICT = list(open('/usr/share/dict/words').read().split())
inverted_dict = defaultdict(list)
vowels = set(['a', 'e', 'i', 'o', 'u'])
vowels_list = ['a', 'e', 'i', 'o', 'u']
for word in DICT:
    another_word = re.sub(r'[aouie]+', r'_', re.sub(r'([a-z])\1+', r'\1', word))
    inverted_dict[another_word].append(word)


def make_word(w):
    w = re.sub(r'[aouie]', vowels_list[random.randint(0, 4)], w)
    wlist = []
    for ch in w:
        if random.randint(0, 5) == 0:
            for _ in range(random.randint(0,4)): wlist.append(ch)
        elif random.randint(0, 5) == 0:
            wlist.append(ch.upper())
        else: wlist.append(ch)
    return ''.join(wlist)
    


if len(sys.argv) > 1 and sys.argv[1] == '-r':
    words = sys.stdin.read().splitlines(False)
    for word in words:
        another_word = re.sub(r'[aouie]+', r'_', re.sub(r'([a-z])\1+', r'\1', word.lower()))
        mlist = inverted_dict[another_word]
        if len(mlist):
            print(word + ' -> ' + mlist[0])
        else: 
            print(word + ' -> NO SUGGESTION')
elif len(sys.argv) > 2 and sys.argv[1] == '-g':
    num = int(sys.argv[2])
    random.seed(int(time.time()))
    dict_len = len(DICT)
    for _ in range(num):
        while 1:
            w = DICT[random.randint(0, dict_len-1)]
            if not '\'' in w: break
#        print(w + ' -> ' + make_word(w))
        print(make_word(w))
else:
    try:
        while 1: 
            word = raw_input()
            if word == "" or word == "\n": break
            another_word = re.sub(r'[aouie]', r'_', re.sub(r'([a-z])\1+', r'\1', word.lower()))
            mlist = inverted_dict[another_word]
            if len(mlist):
                print(word + ' -> ' + mlist[0])
            else: 
                print(word + ' -> NO SUGGESTION')
    except Exception:
        pass
            