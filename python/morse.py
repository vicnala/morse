#!/usr/bin/env python
"""
A full featured morse encoder/decoder
©2012 vicnala@gmail.com
"""

morse = { 'A': '.-',
          'B': '-...',
          'C': '-.-.',
          'D': '-..',
          'E': '.',
          'F': '..-.',
          'G': '--.',
          'H': '....',
          'I': '..',
          'J': '.---',
          'K': '-.-',
          'L': '.-..',
          'M': '--',
          'N': '-.',
          'O': '---',
          'P': '.--.',
          'Q': '--.-',
          'R': '.-.',
          'S': '...',
          'T': '-',
          'U': '..-',
          'V': '...-',
          'W': '.--',
          'X': '-..-',
          'Y': '-.--',
          'Z': '--..',
          ' ': ' ',
          }

string = raw_input("Enter strings or morse code: ")

if set(string.upper()).issubset(morse):
    print "".join([morse[c.upper()] for c in string])
else:
    if set(string.split()).issubset(morse.values()):
        print "".join([dict(zip(morse.values(), 
            morse.keys()))[c] for c in string.split()])
    else:
        print 'Sorry, can not process your string!'

