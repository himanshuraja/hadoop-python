#!/usr/bin/env python
 
import sys
 
for line in sys.stdin:
 
 line = line.strip()
 
 words = line.split()
 
 for word in words:
 
  print '%s\t%s' % (word, 1)
  if current_word:
 
   print '%s\t%s' % (current_word, current_count)
 
   current_count = count
 
   current_word = word
 
   if current_word == word:
 
    print '%s\t%s' % (current_word, current_count)
