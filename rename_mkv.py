#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def rename_mkv(string1):
        # its not an mkv file or does not need renaming
    if string1[-4:] != ".mkv" or (string1[-5] != '1' and\
        string1[-6] != '-'): 
        return None
    out = string1.lower()
    out2 = []
    arr = list(out)
    for n, i in enumerate(arr):
        if n == 0: 
            out2.append(i.upper())
            continue

        if arr[n] == '-' and arr[n+1] == '1': break 
        
        elif arr[n-1] == '_' or arr[n-1] == ' ':
            out2.append(i.upper())
            continue
        if i == '_':
            out2.append(' ')
            continue
        out2.append(i)
    out2.append(".mkv")
    out = "".join(out2)
    
    articles = out.split(' ')
    out2 = []
    for n, i in enumerate(articles):
        if (i == "A" or\
            i == "An" or\
            i == "The" or\
            i == "It" or\
            i == "Its" or\
            i == "In" or\
            i == "To" or\
            i == "With" or\
            i == "And" or\
            i == "Of") and n != 0:
            out2.append(i.lower())
            continue
        out2.append(i)
    
    
    out = " ".join(out2)
            
    return out
    
for root, dirs, files in os.walk(".", topdown=False):
    
    for f in files:
        rnm = rename_mkv(f)
        if rnm == None: 
            print "Skipping %s..." % f
            continue
        print "Renaming %s to %s..." % (f, rnm),
        os.rename(f, rnm)
        print "Done."
    
    
#print rename_mkv(string_t)
#os.rename(string_t, rename_mkv(string_t))
#print "Done."
