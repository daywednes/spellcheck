'''
Created on Jul 2, 2012

@author: mdoan
'''
import sys
import re
from collections import defaultdict
import random
import time

def reduce_word(word):
  return re.sub(r'[aouie]+', r'_', re.sub(r'([a-z])\1+', r'\1', word.lower()))

def make_word(w):
  w = re.sub(r'[aouie]', vowels_list[random.randint(0, 4)], w)
  wlist = []
  for ch in w:
    if ch != '\'':
      if random.randint(0, 4) == 0:
        for _ in range(random.randint(1,4)): wlist.append(ch)
      else: wlist.append(ch)
    else: wlist.append(ch)
  for i in range(len(wlist)):
    if random.randint(0, 5) == 0: wlist[i] = wlist[i].upper()
  return ''.join(wlist)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    if not(len(sys.argv) > 2 and sys.argv[1] == '-g'):
      print('Syntax error\npython spellcheck.py\npython spellcheck.py -g 1000 [1000 words to be generated]')
      sys.exit(0)

  ''' init '''
  DICT = map(lambda x: x.lower(), open('/usr/share/dict/words').read().split())
  dict_set = set(DICT)
  inverted_dict = defaultdict(list)
  for word in DICT: inverted_dict[reduce_word(word)].append(word)
  vowels = set(['a', 'e', 'i', 'o', 'u'])
  vowels_list = ['a', 'e', 'i', 'o', 'u']

  if len(sys.argv) > 2 and sys.argv[1] == '-g':
    num = int(sys.argv[2])
    random.seed(int(time.time()))
    dict_len = len(DICT)
    for _ in range(num):
      w = DICT[random.randint(0, dict_len-1)]
      print(make_word(w))
  else:
    try:
      while 1:
        word = raw_input('>')
        if word == "" or word == "\n": break
        if word in dict_set:
          print(word + ' -> '+ word)
          continue
        mlist = inverted_dict[reduce_word(word)]
        arr0 = map(lambda x: len(x), re.split(r'[^aoieu]+', word.lower()))
        found = False
        for item in mlist:
          arr1 = map(lambda x: len(x), re.split(r'[^aoieu]+', item))
          if len(arr1) == len(arr0) and arr1 <= arr0:
            print(word + ' -> ' + item)
            found = True
            break
        if not found:
          print(word + ' -> NO SUGGESTION')
    except Exception:
      pass
